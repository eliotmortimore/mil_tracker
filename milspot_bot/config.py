import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # FlightRadar24 API settings
    FR24_API_KEY = os.getenv("FR24_API_KEY", "")
    
    # WhatsApp API credentials (Twilio)
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
    WHATSAPP_TO_NUMBER = os.getenv("WHATSAPP_TO_NUMBER")

    # Military aircraft identifiers - Enhanced list
    MILITARY_CALLSIGNS = [
        'NATO40', 'NATO41', 'NATO42', 'NATO43', 'NATO44', 'NATO45',
        'RCH', 'REACH', 'SAM', 'SPAR', 'VENUS', 'JEDI', 'HAVOC',
        'RRR', 'ASCOT', 'COBRA', 'VIPER', 'TARTAN',
        'RSD', 'RSD1', 'RSD2', 'RSD3', 'RSD4', 'RSD5',
        'FORTE', 'DRAGON', 'HAWK', 'EAGLE', 'FALCON', 'PHANTOM',
        'THUNDER', 'LIGHTNING', 'STORM', 'TEMPEST', 'HURRICANE',
        'WARRIOR', 'KNIGHT', 'PALADIN', 'SENTINEL', 'GUARDIAN',
        'SHADOW', 'GHOST', 'SPECTRE', 'PHANTOM', 'WRAITH',
        'BLACK', 'RED', 'BLUE', 'GREEN', 'GOLD', 'SILVER',
        'ALPHA', 'BETA', 'GAMMA', 'DELTA', 'ECHO', 'FOXTROT',
        'GOLF', 'HOTEL', 'INDIA', 'JULIET', 'KILO', 'LIMA',
        'MIKE', 'NOVEMBER', 'OSCAR', 'PAPA', 'QUEBEC', 'ROMEO',
        'SIERRA', 'TANGO', 'UNIFORM', 'VICTOR', 'WHISKEY', 'XRAY',
        'YANKEE', 'ZULU'
    ]

    MILITARY_AIRCRAFT_TYPES = [
        'B1', 'B2', 'B52', 'TU95', 'TU160', 'TU22M',
        'RC135', 'U2', 'P8', 'E3TF', 'E4B', 'E6B', 'E8C', 'RC12', 'U28', 'MC12',
        'F15', 'F16', 'F18', 'F22', 'F35', 'SU27', 'SU30', 'SU35', 'MIG29', 'MIG31',
        'C130', 'C17', 'C5', 'A400M', 'IL76', 'AN124', 'KC135', 'KC10',
        'E3', 'E4', 'E6', 'E8', 'P3', 'P8', 'U2', 'RC135',
        'A10', 'AV8', 'EA18', 'EA6', 'EF18', 'F15E', 'F16C', 'F16D'
    ]

    MILITARY_OPERATORS = [
        'USAF', 'US AIR FORCE', 'UNITED STATES AIR FORCE',
        'RAF', 'ROYAL AIR FORCE',
        'RUSSIAN AIR FORCE', 'VKS',
        'LUFTWAFFE', 'GERMAN AIR FORCE',
        'FRENCH AIR FORCE', 'ARMEE DE L\'AIR',
        'NATO', 'NORTH ATLANTIC TREATY ORGANIZATION',
        'IDF', 'ISRAELI AIR FORCE',
        'JASDF', 'JAPAN AIR SELF DEFENSE FORCE',
        'CAF', 'CANADIAN AIR FORCE',
        'RCAF', 'ROYAL CANADIAN AIR FORCE',
        'RDAF', 'ROYAL DANISH AIR FORCE',
        'RNLAF', 'ROYAL NETHERLANDS AIR FORCE',
        'RSAF', 'ROYAL SAUDI AIR FORCE',
        'IAF', 'INDIAN AIR FORCE',
        'PLAAF', 'PEOPLE\'S LIBERATION ARMY AIR FORCE',
        'ROKAF', 'REPUBLIC OF KOREA AIR FORCE',
        'TURKISH AIR FORCE', 'TURAF',
        'UAE AIR FORCE', 'UAEAF',
        'AUSTRALIAN AIR FORCE', 'RAAF',
        'SPAF', 'SPANISH AIR FORCE',
        'SWEDISH AIR FORCE', 'SWAF',
        'FINNISH AIR FORCE', 'FAF',
        'NORWEGIAN AIR FORCE', 'RNoAF',
        'PORTUGUESE AIR FORCE', 'PRTAF',
        'POLISH AIR FORCE', 'PLAF',
        'CZECH AIR FORCE', 'CZAF',
        'SLOVAK AIR FORCE', 'SVKAF',
        'HUNGARIAN AIR FORCE', 'HUAF',
        'ROMANIAN AIR FORCE', 'ROAF',
        'BULGARIAN AIR FORCE', 'BGR AF',
        'GREEK AIR FORCE', 'HAF',
        'CROATIAN AIR FORCE', 'HRZ',
        'SERBIAN AIR FORCE', 'SRB AF',
        'SLOVENIAN AIR FORCE', 'SVN AF',
        'SWISS AIR FORCE', 'SWISS AF',
        'BELGIAN AIR FORCE', 'BAF',
        'AUSTRIAN AIR FORCE', 'AAF',
        'IRISH AIR CORPS', 'IAC',
        'LUXEMBOURG AIR FORCE', 'LUX AF',
        'ESTONIAN AIR FORCE', 'EST AF',
        'LATVIAN AIR FORCE', 'LVA AF',
        'LITHUANIAN AIR FORCE', 'LTU AF',
        'MALTESE AIR FORCE', 'MLT AF',
        'CYPRUS AIR FORCE', 'CYP AF',
        'GEORGIAN AIR FORCE', 'GEO AF',
        'UKRAINIAN AIR FORCE', 'UKR AF',
        'MOLDOVAN AIR FORCE', 'MDA AF',
        'BELARUSIAN AIR FORCE', 'BLR AF',
        'ARMENIAN AIR FORCE', 'ARM AF',
        'AZERBAIJANI AIR FORCE', 'AZE AF',
        'KAZAKH AIR FORCE', 'KAZ AF',
        'UZBEK AIR FORCE', 'UZB AF',
        'KYRGYZ AIR FORCE', 'KGZ AF',
        'TAJIK AIR FORCE', 'TJK AF',
        'TURKMEN AIR FORCE', 'TKM AF',
        'AFGHAN AIR FORCE', 'AFG AF',
        'PAKISTAN AIR FORCE', 'PAF',
        'BANGLADESH AIR FORCE', 'BAF',
        'SRI LANKA AIR FORCE', 'SLAF',
        'MYANMAR AIR FORCE', 'MAF',
        'THAI AIR FORCE', 'RTAF',
        'VIETNAM AIR FORCE', 'VPAF',
        'MALAYSIAN AIR FORCE', 'RMAF',
        'SINGAPORE AIR FORCE', 'RSAF',
        'INDONESIAN AIR FORCE', 'TNI-AU',
        'PHILIPPINE AIR FORCE', 'PAF',
        'TAIWAN AIR FORCE', 'ROCAF',
        'MONGOLIAN AIR FORCE', 'MAF',
        'NORTH KOREAN AIR FORCE', 'KPAF',
        'SOUTH KOREAN AIR FORCE', 'ROKAF',
        'AUSTRALIAN AIR FORCE', 'RAAF',
        'NEW ZEALAND AIR FORCE', 'RNZAF',
        'FIJI AIR FORCE', 'FAF',
        'PAPUA NEW GUINEA AIR FORCE', 'PNG AF',
        'SOLOMON ISLANDS AIR FORCE', 'SIAF',
        'TONGA AIR FORCE', 'TAF',
        'SAMOA AIR FORCE', 'SAF',
        'VANUATU AIR FORCE', 'VAF',
        'FRANCE', 'GERMANY', 'ITALY', 'SPAIN', 'TURKEY', 'GREECE', 'POLAND', 'ROMANIA', 'NETHERLANDS', 'BELGIUM', 'CZECH', 'SLOVAK', 'HUNGARY', 'BULGARIA', 'CROATIA', 'SLOVENIA', 'ESTONIA', 'LATVIA', 'LITHUANIA', 'LUXEMBOURG', 'MALTA', 'CYPRUS', 'GEORGIA', 'UKRAINE', 'MOLDOVA', 'BELARUS', 'ARMENIA', 'AZERBAIJAN', 'KAZAKHSTAN', 'UZBEKISTAN', 'KYRGYZSTAN', 'TAJIKISTAN', 'TURKMENISTAN', 'AFGHANISTAN', 'PAKISTAN', 'BANGLADESH', 'SRI LANKA', 'MYANMAR', 'THAILAND', 'VIETNAM', 'MALAYSIA', 'SINGAPORE', 'INDONESIA', 'PHILIPPINES', 'TAIWAN', 'MONGOLIA', 'NORTH KOREA', 'SOUTH KOREA', 'AUSTRALIA', 'NEW ZEALAND', 'FIJI', 'PAPUA NEW GUINEA', 'SOLOMON ISLANDS', 'TONGA', 'SAMOA', 'VANUATU'
    ]
    
    MILITARY_REG_PREFIXES = [
        'ZZ', '43C', '44C', '45C', '46C', '47C', '48C', '49C', '4AC', '4BC', '4CC', '4DC', '4EC', '4FC', '50C', '51C', '52C', '53C', '54C', '55C', '56C', '57C', '58C', '59C', '5AC', '5BC', '5CC', '5DC', '5EC', '5FC', '60C', '61C', '62C', '63C', '64C', '65C', '66C', '67C', '68C', '69C', '6AC', '6BC', '6CC', '6DC', '6EC', '6FC', '70C', '71C', '72C', '73C', '74C', '75C', '76C', '77C', '78C', '79C', '7AC', '7BC', '7CC', '7DC', '7EC', '7FC', '80C', '81C', '82C', '83C', '84C', '85C', '86C', '87C', '88C', '89C', '8AC', '8BC', '8CC', '8DC', '8EC', '8FC', '90C', '91C', '92C', '93C', '94C', '95C', '96C', '97C', '98C', '99C', '9AC', '9BC', '9CC', '9DC', '9EC', '9FC'
    ]

    # Geopolitical hotspots - TEMPORARILY REMOVED ALL GEOFENCES
    HOTSPOTS = {}  # Empty dictionary - no regional restrictions
    
    # Score weights for different factors
    SCORE_WEIGHTS = {
        'military_callsign': 10,
        'military_aircraft': 8,
        'military_operator': 6,
        'hotspot_location': 0,  # Temporarily disabled
        'loitering_pattern': 3,
        'unknown_destination': 2,
        'altitude_anomaly': 1,
        'squawk_anomaly': 1
    } 