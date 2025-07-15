import requests
import json
from typing import List, Dict, Optional
from config import Config

class FlightScanner:
    def __init__(self):
        self.config = Config()
        self.session = requests.Session()
        # Add browser-like User-Agent header
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        
        self.global_bounds = {
            'lamin': -90.0,  # min latitude
            'lamax': 90.0,   # max latitude
            'lomin': -180.0, # min longitude
            'lomax': 180.0   # max longitude
        }
    
    def set_cookies(self, cookies: Dict[str, str]):
        """Set cookies from browser session"""
        self.session.cookies.update(cookies)
        print(f"Added {len(cookies)} cookies to session")
    
    def get_flightradar24_data(self, bounds: Optional[tuple] = None) -> List[Dict]:
        """
        Fetch flight data from FlightRadar24
        bounds: (lat_min, lon_min, lat_max, lon_max)
        """
        if bounds:
            url = f"https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds={bounds[0]},{bounds[1]},{bounds[2]},{bounds[3]}"
        else:
            url = "https://data-live.flightradar24.com/zones/fcgi/feed.js"
        
        print(f"Fetching data from: {url}")
        
        try:
            response = self.session.get(url, timeout=10)
            print(f"Response status: {response.status_code}")
            data = response.json()
            print(f"Full data: {data}")
            if 'aircraft' in data:
                print(f"Aircraft key content: {data['aircraft']}")
            print(f"Raw data keys: {list(data.keys())[:10]}")  # Show first 10 keys
            
            flights = []
            for flight_id, flight_data in data.items():
                if isinstance(flight_data, list) and len(flight_data) >= 15:
                    flight = {
                        'id': flight_id,
                        'callsign': flight_data[16] or '',
                        'aircraft_code': flight_data[8] or '',
                        'registration': flight_data[9] or '',
                        'latitude': flight_data[1],
                        'longitude': flight_data[2],
                        'altitude': flight_data[4],
                        'ground_speed': flight_data[5],
                        'heading': flight_data[3],
                        'origin_airport': flight_data[11] or '',
                        'destination_airport': flight_data[12] or '',
                        'timestamp': flight_data[10]
                    }
                    flights.append(flight)
            
            print(f"Processed {len(flights)} flights from raw data")
            return flights
        except Exception as e:
            print(f"Error fetching FlightRadar24 data: {e}")
            return []
    
    def get_flightradar24_data_alt(self) -> List[Dict]:
        """
        Alternative method using a different FlightRadar24 endpoint
        """
        url = "https://www.flightradar24.com/data/aircraft.json"
        
        print(f"Trying alternative endpoint: {url}")
        
        try:
            response = self.session.get(url, timeout=10)
            print(f"Alternative response status: {response.status_code}")
            data = response.json()
            print(f"Alternative data keys: {list(data.keys())[:10] if isinstance(data, dict) else 'Not a dict'}")
            
            # Process alternative data format if needed
            flights = []
            if isinstance(data, dict) and 'aircraft' in data:
                for aircraft in data['aircraft']:
                    if isinstance(aircraft, dict):
                        flight = {
                            'callsign': aircraft.get('identification', {}).get('callsign', ''),
                            'aircraft_code': aircraft.get('aircraft', {}).get('model', {}).get('code', ''),
                            'registration': aircraft.get('aircraft', {}).get('registration', ''),
                            'latitude': aircraft.get('trail', [{}])[0].get('lat', 0) if aircraft.get('trail') else 0,
                            'longitude': aircraft.get('trail', [{}])[0].get('lng', 0) if aircraft.get('trail') else 0,
                            'altitude': aircraft.get('state', {}).get('altitude', 0),
                            'ground_speed': aircraft.get('state', {}).get('speed', 0),
                        }
                        flights.append(flight)
            
            print(f"Alternative method processed {len(flights)} flights")
            return flights
        except Exception as e:
            print(f"Error fetching alternative FlightRadar24 data: {e}")
            return []
    

    
    def get_flightradar24_api_data(self, bounds: Optional[str] = None) -> List[Dict]:
        """
        Use the new FlightRadar24 live flight endpoint with authentication
        """
        api_key = self.config.FR24_API_KEY
        if not api_key:
            print("❌ No FlightRadar24 API key provided. Please set FR24_API_KEY in your .env file")
            return []

        url = "https://fr24api.flightradar24.com/api/live/flight-positions/full"
        # Always use global bounds for worldwide scanning
        bounds = f"{self.global_bounds['lamin']},{self.global_bounds['lamax']},{self.global_bounds['lomin']},{self.global_bounds['lomax']}"
        params = {
            'bounds': bounds
        }
        headers = {
            'Accept': 'application/json',
            'Accept-Version': 'v1',
            'Authorization': f'Bearer {api_key}'
        }
        try:
            print(f"Requesting {url} with bounds: {bounds}")
            response = self.session.get(url, headers=headers, params=params, timeout=15)
            if response.status_code == 200:
                data = response.json()
                print(f"API Response keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
                flights = []
                if isinstance(data, dict):
                    print(f"Top-level keys: {list(data.keys())}")
                    if 'data' in data and isinstance(data['data'], list):
                        for aircraft in data['data']:
                            print(f"Aircraft entry: {aircraft}")
                            if isinstance(aircraft, dict):
                                flight = {
                                    'callsign': aircraft.get('callsign', ''),
                                    'aircraft_code': aircraft.get('aircraft_type', ''),
                                    'registration': aircraft.get('registration', ''),
                                    'latitude': aircraft.get('latitude', 0),
                                    'longitude': aircraft.get('longitude', 0),
                                    'altitude': aircraft.get('altitude', 0),
                                    'ground_speed': aircraft.get('ground_speed', 0),
                                }
                                flights.append(flight)
                    else:
                        print(f"No 'data' key with a list value found in API response. Full response: {json.dumps(data)[:500]}")
                print(f"API processed {len(flights)} flights from {url}")
                return flights
            else:
                print(f"Endpoint {url} failed: {response.status_code} - {response.text[:200]}")
                return []
        except Exception as e:
            print(f"Error fetching FlightRadar24 API data: {e}")
            return []
    
    def is_military_flight(self, flight: Dict) -> bool:
        """Determine if a flight is military based on callsign and aircraft type"""
        callsign = flight.get('callsign', '') or ''
        aircraft_code = flight.get('aircraft_code', '') or ''
        
        callsign = callsign.upper()
        aircraft_code = aircraft_code.upper()
        
        # Check callsign patterns
        for military_prefix in self.config.MILITARY_CALLSIGNS:
            if callsign.startswith(military_prefix):
                return True
        
        # Check aircraft type
        for military_type in self.config.MILITARY_AIRCRAFT_TYPES:
            if military_type.upper() in aircraft_code:
                return True
        
        return False
    
    def get_military_flights(self, bounds: Optional[str] = None) -> List[Dict]:
        """Get all military flights from FlightRadar24 using the new API only"""
        all_flights = self.get_flightradar24_api_data(bounds=bounds)
        military_flights = [f for f in all_flights if self.is_military_flight(f)]
        print(f"Found {len(military_flights)} military flights out of {len(all_flights)} total flights")
        return military_flights 