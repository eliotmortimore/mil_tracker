#!/usr/bin/env python3
"""
Military Flight Tracker Bot Runner
Scans FlightRadar24 for military flights and sends WhatsApp notifications
"""

import logging
import sys
import os
from datetime import datetime
from core.scanner import FlightScanner
from core.scoring import FlightScorer
from core.flight_analyzer import FlightAnalyzer
from config import Config

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def main():
    """Main bot runner function"""
    logging.info("🚀 Starting Military Flight Tracker Bot")
    
    try:
        # Initialize components
        config = Config()
        scanner = FlightScanner()
        scorer = FlightScorer()
        analyzer = FlightAnalyzer()
        
        # Get military flights
        logging.info("🔍 Scanning for military flights...")
        military_flights = scanner.get_military_flights()
        
        if not military_flights:
            logging.info("❌ No military flights found")
            return
        
        # Score and select the most interesting flight
        best_flight = None
        best_score = 0
        
        for flight in military_flights:
            score = scorer.score_flight(flight)
            if score > best_score:
                best_score = score
                best_flight = flight
        
        if best_flight:
            logging.info(f"🎯 Selected flight: {best_flight.get('callsign', 'Unknown')} (Score: {best_score})")
            
            # Create FlightRadar24 URL
            lat = best_flight.get('latitude', 0)
            lon = best_flight.get('longitude', 0)
            callsign = best_flight.get('callsign', 'Unknown')
            
            fr24_url = f"https://www.flightradar24.com/{callsign}"
            
            # Generate intelligence analysis
            intelligence_summary = analyzer.generate_intelligence_summary(best_flight, best_score)
            
            # Send WhatsApp notification
            try:
                from core.whatsapp_sender import WhatsAppSender
                sender = WhatsAppSender()
                
                sender.send_flight_notification(best_flight, fr24_url, intelligence_summary)
                logging.info("✅ WhatsApp notification with intelligence analysis sent successfully")
                
            except Exception as e:
                logging.error(f"❌ Failed to send WhatsApp notification: {e}")
        else:
            logging.info("❌ No suitable military flights found")
            
    except Exception as e:
        logging.error(f"❌ Bot error: {e}")
        raise

if __name__ == "__main__":
    main() 