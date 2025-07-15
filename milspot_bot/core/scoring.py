from typing import Dict
from config import Config

class FlightScorer:
    def __init__(self):
        self.config = Config()
    
    def is_in_hotspot(self, lat: float, lon: float) -> bool:
        """Check if coordinates are in any geopolitical hotspot"""
        for hotspot_name, (lat_min, lon_min, lat_max, lon_max) in self.config.HOTSPOTS.items():
            if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
                return True
        return False
    
    def detect_loitering_pattern(self, flight: Dict) -> bool:
        """Detect potential loitering behavior"""
        altitude = flight.get('alt', 0)
        speed = flight.get('gspeed', 0)
        
        # Low altitude and slow speed suggests loitering
        if altitude < 15000 and speed < 250:
            return True
        
        return False
    
    def get_aircraft_interest_score(self, aircraft_code: str) -> int:
        """Score aircraft type based on intelligence value"""
        if not aircraft_code:
            return 0
        
        aircraft_code = aircraft_code.upper()
        
        # Bomber aircraft (highest priority)
        if any(code in aircraft_code for code in ['B1', 'B2', 'B52', 'TU95', 'TU160', 'TU22M']):
            return self.config.SCORE_WEIGHTS['bomber_aircraft']
        
        # High-value reconnaissance aircraft
        if any(code in aircraft_code for code in ['RC135', 'U2', 'P8', 'E3TF', 'E4B', 'E6B', 'E8C', 'RC12', 'U28', 'MC12', 'P3', 'P8A', 'EP3', 'RC26']):
            return self.config.SCORE_WEIGHTS['recon_aircraft']
        
        # Fighter aircraft
        if any(code in aircraft_code for code in ['F15', 'F16', 'F18', 'F22', 'F35', 'F14', 'F4', 'MIG29', 'MIG31', 'SU27', 'SU30', 'SU35', 'J10', 'J11', 'J20']):
            return self.config.SCORE_WEIGHTS['fighter_aircraft']
        
        # Tanker aircraft
        if any(code in aircraft_code for code in ['KC135', 'KC10', 'KC46', 'KC130', 'KC767', 'A330MRTT']):
            return self.config.SCORE_WEIGHTS['tanker_aircraft']
        
        # Transport aircraft
        if any(code in aircraft_code for code in ['C17', 'C130', 'C5M', 'C30J', 'C27J', 'C295', 'A400M', 'IL76', 'AN124', 'AN225', 'Y20', 'Y9']):
            return self.config.SCORE_WEIGHTS['transport_aircraft']
        
        # Special mission aircraft
        if any(code in aircraft_code for code in ['AC130', 'MC130', 'EC130', 'WC130', 'HC130']):
            return self.config.SCORE_WEIGHTS['rare_aircraft']
        
        # Helicopters
        if any(code in aircraft_code for code in ['AH64', 'UH60', 'CH47', 'AH1', 'MI8', 'MI24', 'KA52']):
            return self.config.SCORE_WEIGHTS['rare_aircraft']
        
        # UAV/UAS
        if any(code in aircraft_code for code in ['MQ1', 'MQ9', 'RQ4', 'RQ170', 'RQ180', 'MQ4', 'MQ8']):
            return self.config.SCORE_WEIGHTS['rare_aircraft']
        
        # Other military aircraft
        if any(code in aircraft_code for code in ['A10', 'AV8', 'EA18', 'EA6', 'EF18', 'F15E', 'F16C', 'F16D']):
            return self.config.SCORE_WEIGHTS['fighter_aircraft']
        
        return 0
    
    def get_callsign_score(self, callsign: str) -> int:
        """Score callsign based on military patterns"""
        if not callsign:
            return 0
        
        callsign = callsign.upper()
        
        for military_prefix in self.config.MILITARY_CALLSIGNS:
            if callsign.startswith(military_prefix):
                return self.config.SCORE_WEIGHTS['military_callsign']
        
        return 0
    
    def get_operator_score(self, flight: Dict) -> int:
        """Score based on known military operators"""
        painted_as = flight.get('painted_as', '').upper()
        operating_as = flight.get('operating_as', '').upper()
        
        military_operators = [
            'USAF', 'USN', 'USMC', 'USARMY', 'NATO', 'RAF', 'LUFTWAFFE',
            'ARMEE', 'AERONAUTICA', 'EJERCITO', 'FUERZA', 'FORCA', 'SILA',
            'VOENNO', 'VOZDUSHNO', 'KONGSBERG', 'KONGSBERG', 'KONGSBERG'
        ]
        
        if painted_as in military_operators or operating_as in military_operators:
            return self.config.SCORE_WEIGHTS['military_operator']
        
        return 0
    
    def get_squawk_score(self, flight: Dict) -> int:
        """Score based on unusual squawk codes"""
        squawk = flight.get('squawk', '')
        
        # Military squawk codes (7500, 7600, 7700 are emergency codes)
        military_squawks = ['7500', '7600', '7700', '7777', '0000', '1200']
        
        if squawk in military_squawks:
            return self.config.SCORE_WEIGHTS['squawk_anomaly']
        
        return 0
    
    def is_military(self, flight: Dict) -> bool:
        callsign = (flight.get('callsign') or '').upper()
        aircraft_type = (flight.get('type') or '').upper()
        operator = (flight.get('operating_as') or '').upper()
        painted_as = (flight.get('painted_as') or '').upper()
        reg = (flight.get('reg') or '').upper()
        # Check callsign
        for pattern in self.config.MILITARY_CALLSIGNS:
            if callsign.startswith(pattern):
                return True
        # Check aircraft type
        for mtype in self.config.MILITARY_AIRCRAFT_TYPES:
            if mtype in aircraft_type:
                return True
        # Check operator
        for op in self.config.MILITARY_OPERATORS:
            if op in operator or op in painted_as:
                return True
        # Check registration prefix (optional, e.g. "ZZ" for RAF)
        for prefix in self.config.MILITARY_REG_PREFIXES:
            if reg.startswith(prefix):
                return True
        return False

    def score_flight(self, flight: Dict) -> int:
        if not self.is_military(flight):
            return 0
        # If military, apply further scoring (e.g. loitering, hotspot, etc.)
        score = 5  # base score for being military
        lat = flight.get('lat')
        lon = flight.get('lon')
        if lat and lon and self.is_in_hotspot(lat, lon):
            score += 2
        if self.detect_loitering_pattern(flight):
            score += 3
        return score 