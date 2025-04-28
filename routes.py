departure_date = "2025-04-23"
return_flight_date = "2025-04-30"

routes = [
    ["CAI", "SVO", departure_date, return_flight_date],  # Cairo → Moscow
    ["CAI", "LAX", departure_date, return_flight_date],  # Cairo → Los Angeles
    ["CAI", "MNL", departure_date, return_flight_date],  # Cairo → Manila
    ["CAI", "SGN", departure_date, return_flight_date],  # Cairo → Ho Chi Minh
    ["CAI", "SZX", departure_date, return_flight_date],  # Cairo → Shenzhen
    ["CAI", "TPE", departure_date, return_flight_date],  # Cairo → Taipei
    ["CAI", "YVR", departure_date, return_flight_date],  # Cairo → Vancouver
    ["CAI", "LIM", departure_date, return_flight_date],  # Cairo → Lima
    ["CAI", "BOG", departure_date, return_flight_date],  # Cairo → Bogotá
    ["CAI", "UIO", departure_date, return_flight_date],  # Cairo → Quito
    ["CAI", "KTM", departure_date, return_flight_date],  # Cairo → Kathmandu
    ["CAI", "DAC", departure_date, return_flight_date],  # Cairo → Dhaka
    ["CAI", "LAD", departure_date, return_flight_date],  # Cairo → Luanda
    ["CAI", "NBO", departure_date, return_flight_date],  # Cairo → Nairobi
    ["CAI", "ABV", departure_date, return_flight_date],  # Cairo → Abuja
    ["CAI", "DAR", departure_date, return_flight_date],  # Cairo → Dar es Salaam
    ["CAI", "ACC", departure_date, return_flight_date],  # Cairo → Accra
    ["CAI", "SGN", departure_date, return_flight_date],  # Cairo → Saigon
    ["CAI", "EVN", departure_date, return_flight_date],  # Cairo → Yerevan
    ["CAI", "TBS", departure_date, return_flight_date],  # Cairo → Tbilisi
    ["CAI", "BAH", departure_date, return_flight_date],  # Cairo → Bahrain
    ["CAI", "MCT", departure_date, return_flight_date],  # Cairo → Muscat
    ["CAI", "RUH", departure_date, return_flight_date],  # Cairo → Riyadh
    ["CAI", "AMM", departure_date, return_flight_date],  # Cairo → Amman
    ["CAI", "BEY", departure_date, return_flight_date],  # Cairo → Beirut
    ["HBE", "HKG", departure_date, return_flight_date],  # Alexandria → Hong Kong
    ["HBE", "LON", departure_date, return_flight_date],  # Alexandria → London
    ["HBE", "YTO", departure_date, return_flight_date],  # Alexandria → Toronto
    ["HBE", "DXB", departure_date, return_flight_date],  # Alexandria → Dubai
    ["HBE", "NYC", departure_date, return_flight_date],  # Alexandria → New York City
    ["HBE", "PAR", departure_date, return_flight_date],  # Alexandria → Paris
    ["HBE", "IST", departure_date, return_flight_date],  # Alexandria → Istanbul
    ["HBE", "BER", departure_date, return_flight_date],  # Alexandria → Berlin
    ["HBE", "AMS", departure_date, return_flight_date],  # Alexandria → Amsterdam
    ["HBE", "MAD", departure_date, return_flight_date],  # Alexandria → Madrid
    ["HBE", "ROM", departure_date, return_flight_date],  # Alexandria → Rome
    ["HBE", "TYO", departure_date, return_flight_date],  # Alexandria → Tokyo
    ["HBE", "SYD", departure_date, return_flight_date],  # Alexandria → Sydney
    ["HBE", "BKK", departure_date, return_flight_date],  # Alexandria → Bangkok
    ["HBE", "SIN", departure_date, return_flight_date],  # Alexandria → Singapore
    ["HBE", "KUL", departure_date, return_flight_date],  # Alexandria → Kuala Lumpur
    ["HBE", "CAI", departure_date, return_flight_date],  # Alexandria → Cairo
    ["HBE", "JED", departure_date, return_flight_date],  # Alexandria → Jeddah
    ["HBE", "DOH", departure_date, return_flight_date],  # Alexandria → Doha
    ["HBE", "LOS", departure_date, return_flight_date],  # Alexandria → Lagos
    ["HBE", "SFO", departure_date, return_flight_date],  # Alexandria → San Francisco
    ["HBE", "ORD", departure_date, return_flight_date],  # Alexandria → Chicago
    ["HBE", "BOM", departure_date, return_flight_date],  # Alexandria → Mumbai
    ["HBE", "DEL", departure_date, return_flight_date],  # Alexandria → Delhi
    ["HBE", "MEX", departure_date, return_flight_date],  # Alexandria → Mexico City
    ["HBE", "GRU", departure_date, return_flight_date],  # Alexandria → São Paulo
    ["HBE", "BCN", departure_date, return_flight_date],  # Alexandria → Barcelona
    ["HBE", "CPH", departure_date, return_flight_date],  # Alexandria → Copenhagen
    ["HBE", "OSL", departure_date, return_flight_date],  # Alexandria → Oslo
    ["HBE", "STO", departure_date, return_flight_date],  # Alexandria → Stockholm
    ["HBE", "HEL", departure_date, return_flight_date],  # Alexandria → Helsinki
    ["HBE", "WAW", departure_date, return_flight_date],  # Alexandria → Warsaw
    ["HBE", "ATH", departure_date, return_flight_date],  # Alexandria → Athens
    ["HBE", "ZRH", departure_date, return_flight_date],  # Alexandria → Zurich
    ["HBE", "VIE", departure_date, return_flight_date],  # Alexandria → Vienna
    ["HBE", "PRG", departure_date, return_flight_date],  # Alexandria → Prague
    ["HBE", "BRU", departure_date, return_flight_date],  # Alexandria → Brussels
    ["HBE", "LIS", departure_date, return_flight_date],  # Alexandria → Lisbon
    ["HBE", "DUB", departure_date, return_flight_date],  # Alexandria → Dublin
    ["HBE", "MLA", departure_date, return_flight_date],  # Alexandria → Malta
    ["HBE", "TUN", departure_date, return_flight_date],  # Alexandria → Tunis
    ["HBE", "CMN", departure_date, return_flight_date],  # Alexandria → Casablanca
    ["HBE", "ALG", departure_date, return_flight_date],  # Alexandria → Algiers
    ["HBE", "KRT", departure_date, return_flight_date],  # Alexandria → Khartoum
    ["HBE", "JNB", departure_date, return_flight_date],  # Alexandria → Johannesburg
    ["HBE", "ICN", departure_date, return_flight_date],  # Alexandria → Seoul
    ["HBE", "HNL", departure_date, return_flight_date],  # Alexandria → Honolulu
    ["HBE", "SCL", departure_date, return_flight_date],  # Alexandria → Santiago
    ["HBE", "CPT", departure_date, return_flight_date],  # Alexandria → Cape Town
    ["HBE", "BNE", departure_date, return_flight_date],  # Alexandria → Brisbane
    ["HBE", "MEL", departure_date, return_flight_date],  # Alexandria → Melbourne
    ["JFK", "SVO", departure_date, return_flight_date],  # New York → Moscow
    ["JFK", "BUD", departure_date, return_flight_date],  # New York → Budapest
    ["JFK", "TPE", departure_date, return_flight_date],  # New York → Taipei
    ["LAX", "ICN", departure_date, return_flight_date],  # LA → Seoul
    ["LAX", "HND", departure_date, return_flight_date],  # LA → Tokyo Haneda
    ["LAX", "MNL", departure_date, return_flight_date],  # LA → Manila
    ["DXB", "SGN", departure_date, return_flight_date],  # Dubai → Ho Chi Minh
    ["DXB", "LIS", departure_date, return_flight_date],  # Dubai → Lisbon
    ["DXB", "BNE", departure_date, return_flight_date],  # Dubai → Brisbane
    ["SIN", "CPT", departure_date, return_flight_date],  # Singapore → Cape Town
    ["SIN", "AKL", departure_date, return_flight_date],  # Singapore → Auckland
    ["SIN", "LIM", departure_date, return_flight_date],  # Singapore → Lima
    ["CDG", "EZE", departure_date, return_flight_date],  # Paris → Buenos Aires
    ["CDG", "BNE", departure_date, return_flight_date],  # Paris → Brisbane
    ["CDG", "KIX", departure_date, return_flight_date],  # Paris → Osaka
    ["FRA", "HAN", departure_date, return_flight_date],  # Frankfurt → Hanoi
    ["FRA", "PER", departure_date, return_flight_date],  # Frankfurt → Perth
    ["FRA", "RUH", departure_date, return_flight_date],  # Frankfurt → Riyadh
    ["MAD", "MEX", departure_date, return_flight_date],  # Madrid → Mexico City
    ["MAD", "GIG", departure_date, return_flight_date],  # Madrid → Rio de Janeiro
    ["MAD", "BOG", departure_date, return_flight_date],  # Madrid → Bogotá
    ["AMS", "DAR", departure_date, return_flight_date],  # Amsterdam → Dar es Salaam
    ["AMS", "ACC", departure_date, return_flight_date],  # Amsterdam → Accra
    ["AMS", "LOS", departure_date, return_flight_date],  # Amsterdam → Lagos
    ["IST", "EVN", departure_date, return_flight_date],  # Istanbul → Yerevan
    ["IST", "TBS", departure_date, return_flight_date],  # Istanbul → Tbilisi
    ["IST", "BGW", departure_date, return_flight_date],  # Istanbul → Baghdad
]