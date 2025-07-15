"""
Flight Intelligence Analyzer
Generates detailed descriptions of why military flights are interesting
"""

from typing import Dict, List
from config import Config

class FlightAnalyzer:
    def __init__(self):
        self.config = Config()
        
        # Aircraft type categories for analysis
        self.aircraft_categories = {
            'fighter': ['F15', 'F16', 'F18', 'F22', 'F35', 'F14', 'F4', 'MIG29', 'MIG31', 'SU27', 'SU30', 'SU35', 'J10', 'J11', 'J20'],
            'bomber': ['B1', 'B2', 'B52', 'TU95', 'TU160', 'TU22M'],
            'reconnaissance': ['RC135', 'U2', 'P8', 'E3TF', 'E4B', 'E6B', 'E8C', 'RC12', 'U28', 'MC12', 'P3', 'P8A', 'EP3', 'RC26'],
            'tanker': ['KC135', 'KC10', 'KC46', 'KC130', 'KC767', 'A330MRTT'],
            'transport': ['C17', 'C130', 'C5M', 'C30J', 'C27J', 'C295', 'A400M', 'IL76', 'AN124', 'AN225', 'Y20', 'Y9'],
            'special_mission': ['AC130', 'MC130', 'EC130', 'WC130', 'HC130'],
            'helicopter': ['AH64', 'UH60', 'CH47', 'AH1', 'MI8', 'MI24', 'KA52'],
            'uav': ['MQ1', 'MQ9', 'RQ4', 'RQ170', 'RQ180', 'MQ4', 'MQ8']
        }
        
        # Callsign patterns for analysis
        self.callsign_patterns = {
            'nato': ['NATO40', 'NATO41', 'NATO42', 'NATO43', 'NATO44', 'NATO45'],
            'us_air_force': ['RCH', 'REACH', 'SAM', 'SPAR'],
            'us_navy': ['VENUS', 'JEDI', 'HAVOC'],
            'uk_raf': ['RRR', 'ASCOT', 'COBRA', 'VIPER', 'TARTAN'],
            'russian': ['RSD', 'RSD1', 'RSD2', 'RSD3', 'RSD4', 'RSD5'],
            'special_ops': ['FORTE', 'DRAGON', 'HAWK', 'EAGLE', 'FALCON', 'PHANTOM']
        }
        
        # Geographic regions of interest
        self.regions = {
            'eastern_europe': {'lat_min': 45, 'lat_max': 55, 'lon_min': 15, 'lon_max': 30},
            'baltic_sea': {'lat_min': 55, 'lat_max': 65, 'lon_min': 15, 'lon_max': 30},
            'black_sea': {'lat_min': 40, 'lat_max': 50, 'lon_min': 25, 'lon_max': 40},
            'mediterranean': {'lat_min': 30, 'lat_max': 45, 'lon_min': 5, 'lon_max': 25},
            'middle_east': {'lat_min': 25, 'lat_max': 40, 'lon_min': 30, 'lon_max': 60},
            'north_africa': {'lat_min': 20, 'lat_max': 35, 'lon_min': -10, 'lon_max': 25}
        }
    
    def analyze_aircraft_type(self, aircraft_code: str) -> List[str]:
        """Analyze aircraft type and return intelligence insights"""
        if not aircraft_code:
            return []
        
        aircraft_code = aircraft_code.upper()
        insights = []
        
        for category, types in self.aircraft_categories.items():
            for aircraft_type in types:
                if aircraft_type in aircraft_code:
                    if category == 'fighter':
                        insights.append("🛩️ Fighter aircraft - High-speed air superiority mission")
                    elif category == 'bomber':
                        insights.append("💣 Strategic bomber - Long-range strike capability")
                    elif category == 'reconnaissance':
                        insights.append("🔍 Reconnaissance aircraft - Intelligence gathering mission")
                    elif category == 'tanker':
                        insights.append("⛽ Aerial refueling tanker - Force projection support")
                    elif category == 'transport':
                        insights.append("✈️ Military transport - Troop/cargo movement")
                    elif category == 'special_mission':
                        insights.append("🎯 Special mission aircraft - Specialized operations")
                    elif category == 'helicopter':
                        insights.append("🚁 Military helicopter - Tactical air support")
                    elif category == 'uav':
                        insights.append("🤖 Unmanned aerial vehicle - Remote operations")
                    break
        
        return insights
    
    def analyze_callsign(self, callsign: str) -> List[str]:
        """Analyze callsign patterns and return intelligence insights"""
        if not callsign:
            return []
        
        callsign = callsign.upper()
        insights = []
        
        for pattern_type, patterns in self.callsign_patterns.items():
            for pattern in patterns:
                if callsign.startswith(pattern):
                    if pattern_type == 'nato':
                        insights.append("🇺🇳 NATO mission aircraft - Alliance operations")
                    elif pattern_type == 'us_air_force':
                        insights.append("🇺🇸 US Air Force transport - Strategic airlift")
                    elif pattern_type == 'us_navy':
                        insights.append("🇺🇸 US Navy aircraft - Maritime operations")
                    elif pattern_type == 'uk_raf':
                        insights.append("🇬🇧 UK Royal Air Force - British military operations")
                    elif pattern_type == 'russian':
                        insights.append("🇷🇺 Russian military aircraft - VKS operations")
                    elif pattern_type == 'special_ops':
                        insights.append("⚡ Special operations aircraft - Covert missions")
                    break
        
        return insights
    
    def analyze_location(self, lat: float, lon: float) -> List[str]:
        """Analyze geographic location and return intelligence insights"""
        insights = []
        
        for region_name, bounds in self.regions.items():
            if (bounds['lat_min'] <= lat <= bounds['lat_max'] and 
                bounds['lon_min'] <= lon <= bounds['lon_max']):
                
                if region_name == 'eastern_europe':
                    insights.append("🌍 Eastern Europe - Near NATO eastern flank")
                elif region_name == 'baltic_sea':
                    insights.append("🌊 Baltic Sea region - NATO-Russia border area")
                elif region_name == 'black_sea':
                    insights.append("⚫ Black Sea region - Strategic maritime area")
                elif region_name == 'mediterranean':
                    insights.append("🌊 Mediterranean - Southern NATO operations")
                elif region_name == 'middle_east':
                    insights.append("🕌 Middle East - Regional security operations")
                elif region_name == 'north_africa':
                    insights.append("🏜️ North Africa - Mediterranean security")
                break
        
        return insights
    
    def analyze_flight_characteristics(self, flight_data: Dict) -> List[str]:
        """Analyze flight characteristics for intelligence insights"""
        insights = []
        
        altitude = flight_data.get('altitude', 0)
        speed = flight_data.get('ground_speed', 0)
        squawk = flight_data.get('squawk', '')
        
        # Altitude analysis
        if altitude > 40000:
            insights.append("☁️ High-altitude flight - Strategic reconnaissance or command")
        elif altitude < 15000:
            insights.append("🛬 Low-altitude flight - Tactical operations or approach")
        
        # Speed analysis
        if speed < 250:
            insights.append("🐌 Slow flight - Possible loitering or surveillance")
        elif speed > 500:
            insights.append("⚡ High-speed flight - Rapid response or intercept")
        
        # Squawk analysis
        if squawk in ['7500', '7600', '7700']:
            insights.append("🚨 Emergency squawk - Aircraft in distress")
        elif squawk == '7777':
            insights.append("🎯 Military squawk - Active military operations")
        
        return insights
    
    def analyze_operator(self, flight_data: Dict) -> List[str]:
        """Analyze aircraft operator for intelligence insights"""
        insights = []
        
        painted_as = flight_data.get('painted_as', '').upper()
        operating_as = flight_data.get('operating_as', '').upper()
        
        military_operators = {
            'USAF': '🇺🇸 US Air Force',
            'USN': '🇺🇸 US Navy', 
            'USMC': '🇺🇸 US Marine Corps',
            'RAF': '🇬🇧 Royal Air Force',
            'NATO': '🇺🇳 NATO Alliance',
            'LUFTWAFFE': '🇩🇪 German Air Force',
            'ARMEE': '🇫🇷 French Air Force',
            'AERONAUTICA': '🇮🇹 Italian Air Force',
            'EJERCITO': '🇪🇸 Spanish Air Force'
        }
        
        for operator_code, operator_name in military_operators.items():
            if operator_code in painted_as or operator_code in operating_as:
                insights.append(f"{operator_name} - Official military aircraft")
                break
        
        return insights
    
    def generate_intelligence_summary(self, flight_data: Dict, score: int) -> str:
        """Generate comprehensive intelligence summary for a military flight"""
        
        # Collect all analysis insights
        all_insights = []
        
        # Aircraft type analysis
        aircraft_insights = self.analyze_aircraft_type(flight_data.get('aircraft_code', ''))
        all_insights.extend(aircraft_insights)
        
        # Callsign analysis
        callsign_insights = self.analyze_callsign(flight_data.get('callsign', ''))
        all_insights.extend(callsign_insights)
        
        # Location analysis
        location_insights = self.analyze_location(
            flight_data.get('latitude', 0), 
            flight_data.get('longitude', 0)
        )
        all_insights.extend(location_insights)
        
        # Flight characteristics analysis
        characteristic_insights = self.analyze_flight_characteristics(flight_data)
        all_insights.extend(characteristic_insights)
        
        # Operator analysis
        operator_insights = self.analyze_operator(flight_data)
        all_insights.extend(operator_insights)
        
        # Generate summary
        if all_insights:
            summary = "🔍 INTELLIGENCE ANALYSIS:\n\n"
            for insight in all_insights:
                summary += f"• {insight}\n"
            
            # Add score context
            if score >= 15:
                summary += "\n🎯 HIGH-VALUE TARGET - Significant intelligence interest"
            elif score >= 10:
                summary += "\n⚠️ MODERATE INTEREST - Worth monitoring"
            else:
                summary += "\n📊 STANDARD MILITARY TRAFFIC"
        else:
            summary = "🔍 INTELLIGENCE ANALYSIS:\n\n• Standard military aircraft detected"
        
        return summary 