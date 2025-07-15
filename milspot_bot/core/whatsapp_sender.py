"""
WhatsApp Sender using Twilio API
Sends formatted messages to WhatsApp via Twilio
"""

import os
import logging
from twilio.rest import Client
from config import Config

class WhatsAppSender:
    def __init__(self):
        self.config = Config()
        self.client = None
        self._initialize_twilio()
    
    def _initialize_twilio(self):
        """Initialize Twilio client with credentials from config"""
        try:
            account_sid = self.config.TWILIO_ACCOUNT_SID
            auth_token = self.config.TWILIO_AUTH_TOKEN
            from_number = self.config.TWILIO_WHATSAPP_NUMBER
            to_number = self.config.WHATSAPP_TO_NUMBER
            
            if not all([account_sid, auth_token, from_number, to_number]):
                logging.warning("⚠️ Missing Twilio credentials. WhatsApp notifications will be disabled.")
                return
            
            self.client = Client(account_sid, auth_token)
            self.from_number = from_number
            self.to_number = to_number
            
            logging.info("✅ Twilio WhatsApp client initialized successfully")
            
        except Exception as e:
            logging.error(f"❌ Failed to initialize Twilio client: {e}")
            self.client = None
    
    def send_message(self, message: str) -> bool:
        """
        Send a WhatsApp message via Twilio
        
        Args:
            message: The message to send
            
        Returns:
            bool: True if message sent successfully, False otherwise
        """
        if not self.client:
            logging.warning("⚠️ Twilio client not initialized. Cannot send WhatsApp message.")
            return False
        
        try:
            if not self.to_number:
                logging.error("❌ No destination number configured")
                return False
                
            twilio_message = self.client.messages.create(
                from_=self.from_number,
                body=message,
                to=self.to_number
            )
            
            logging.info(f"✅ WhatsApp message sent successfully (SID: {twilio_message.sid})")
            return True
            
        except Exception as e:
            logging.error(f"❌ Failed to send WhatsApp message: {e}")
            return False
    
    def send_flight_notification(self, flight_data: dict, fr24_url: str, intelligence_summary: str = "") -> bool:
        """
        Send a formatted military flight notification with intelligence analysis
        
        Args:
            flight_data: Dictionary containing flight information
            fr24_url: FlightRadar24 tracking URL
            intelligence_summary: Detailed intelligence analysis
            
        Returns:
            bool: True if message sent successfully, False otherwise
        """
        callsign = flight_data.get('callsign', 'Unknown')
        aircraft_type = flight_data.get('aircraft_code', 'Unknown')
        registration = flight_data.get('registration', 'Unknown')
        altitude = flight_data.get('altitude', 0)
        speed = flight_data.get('ground_speed', 0)
        
        message = f"""🚁 MILITARY FLIGHT DETECTED

Aircraft: {aircraft_type}
Callsign: {callsign}
Registration: {registration}
Altitude: {altitude} ft
Speed: {speed} kts

Live tracking: {fr24_url}

{intelligence_summary}

Detected via Military Flight Tracker Bot"""

        return self.send_message(message) 