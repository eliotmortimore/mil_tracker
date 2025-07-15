# Military Flight Tracker

A real-time military aircraft tracking system that monitors global flight data and sends WhatsApp notifications for detected military flights.

## 🚀 Features

- **🌍 Worldwide Scanning**: Monitors global flight data for military aircraft
- **🎯 Strict Military Filtering**: Only detects and reports actual military flights
- **📱 WhatsApp Integration**: Sends real-time notifications via Twilio WhatsApp
- **🔍 Enhanced Detection**: Comprehensive military aircraft type and callsign detection
- **📊 Live Flight Data**: Real-time FlightRadar24 API integration
- **🛡️ Security**: Proper credential management with .env protection

## 🛩️ Military Aircraft Detection

### Aircraft Types Detected:

- **Bomber Aircraft**: B1, B2, B52, TU95, TU160, TU22M
- **Reconnaissance**: RC135, U2, P8, E3TF, E4B, E6B, E8C, RC12, U28, MC12
- **Fighter Aircraft**: F15, F16, F18, F22, F35, SU27, SU30, SU35, MIG29, MIG31
- **Transport**: C130, C17, C5, A400M, IL76, AN124, KC135, KC10
- **Special Mission**: E3, E4, E6, E8, P3, P8, U2, RC135

### Military Callsigns Detected:

- **NATO**: NATO40, NATO41, NATO42, NATO43, NATO44, NATO45
- **US Military**: RCH, REACH, SAM, SPAR, VENUS, JEDI, HAVOC
- **UK Military**: RRR, ASCOT, COBRA, VIPER, TARTAN
- **Russian**: RSD, RSD1, RSD2, RSD3, RSD4, RSD5

## 📋 Requirements

- Python 3.8+
- Twilio Account (for WhatsApp notifications)
- FlightRadar24 API Key

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/eliotmortimore/mil_tracker.git
   cd mil_tracker
   ```

2. **Install dependencies:**

   ```bash
   cd milspot_bot
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the `milspot_bot/` directory:
   ```env
   FR24_API_KEY=your_flightradar24_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
   WHATSAPP_TO_NUMBER=whatsapp:+your_phone_number
   ```

## 🔧 Usage

### Run the Bot:

```bash
python3 main.py
```

### Test WhatsApp Integration:

```bash
python3 send_example.py
```

## 📱 WhatsApp Setup

1. **Get Twilio Credentials:**

   - Sign up at [Twilio](https://www.twilio.com/)
   - Get your Account SID and Auth Token
   - Set up WhatsApp Business API

2. **Join Twilio WhatsApp Sandbox:**
   - Send the provided code to `+14155238886` on WhatsApp
   - Follow the setup instructions in your Twilio console

## 🎯 How It Works

1. **Flight Scanning**: Continuously monitors global flight data
2. **Military Detection**: Filters flights using comprehensive military criteria
3. **Scoring System**: Ranks flights by military significance
4. **Notification**: Sends formatted WhatsApp messages with live FlightRadar24 URLs

## 📊 Example Output

```
🎯 Selected flight: NATO40 (Score: 15)
📱 WhatsApp message sent successfully

Flight Details:
- Aircraft: E-3A Sentry (AWACS)
- Callsign: NATO40
- Location: Central Europe
- Live URL: https://www.flightradar24.com/NATO40
```

## 🔒 Security

- `.env` file is in `.gitignore` to protect credentials
- No sensitive data is committed to the repository
- Secure API key management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is for educational and research purposes only.

## ⚠️ Disclaimer

This tool is designed for legitimate OSINT research and military aviation enthusiasts. Please ensure compliance with all applicable laws and regulations in your jurisdiction.
