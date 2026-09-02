""" 
seed car inventory database
date: 2026-07/30
1. name of the car
2. description of the car
3. year of the car
4. model of the car
5. price of the car
6. list of colors options
7. availability of the car
8. imagefile of the car image
"""

Luxury_cars = [
    {
        "car_id": 1322,
        "car_name": "Mercedes-Benz S-Class",
        "car_description": (
        "The Mercedes-Benz S 580 4MATIC pairs handcrafted luxury with "
        "effortless V8 performance, all-wheel drive, and flagship technology."
        ),
        "year": 2024,
        "model": "S 580 4MATIC",
        "price": 128150,
        "availability": True,
        "imagefile": "img/mercedes-benz-s-class.png"
    }, 
    {
        "car_id": 2124,
        "car_name": "BMW M4",
        "car_description": (
            "The BMW M4 Competition xDrive combines twin-turbo performance, "
            "all-wheel-drive traction, and focused G82 coupe styling."
        ),
        "year": 2025,
        "model": "M4 Competition xDrive (G82)",
        "price": 96995,
        "availability": True,
        "imagefile": "img/bmw-m4-G80.png"
    },
    {
        "car_id": 3212,
        "car_name": "Audi RS 7",
        "car_description": (
            "The Audi RS 7 Performance blends twin-turbo V8 power, quattro "
            "all-wheel drive, and everyday luxury in a dramatic Sportback design."
        ),
        "year": 2024,
        "model": "RS 7 Performance",
        "price": 114000,
        "availability": False,
        "imagefile": "img/audi-rs7.png"
    },
    {
        "car_id": 1224,
        "car_name": "Porsche 911 Turbo S",
        "car_description": (
            "The Porsche 911 Turbo S delivers blistering all-wheel-drive "
            "performance while preserving the iconic 911 shape and everyday usability."
        ),
        "year": 2025,
        "model": "911 Turbo S",
        "price": 224000,
   
        "availability": True,
        "imagefile": "img/porsche-911-turbo-s.png"
    }, 
    {
        "car_id": 5432,
        "car_name": "Lexus LC 500",
        "car_description": (
            "The Lexus LC 500 pairs a naturally aspirated V8 and rear-wheel drive "
            "with a handcrafted interior and dramatic grand-touring design."
        ),
        "year": 2026,
        "model": "LC 500",
        "price": 101000,
        "availability": True,  
        "imagefile": "img/lexus-lc500.png"
    },
    {
        "car_id": 6321,
        "car_name": "Land Rover Range Rover",
        "car_description": (
            "The Range Rover combines serene luxury, confident all-terrain "
            "capability, and advanced technology in a commanding full-size SUV."
        ),
        "year": 2026,
        "model": "Range Rover",
        "price": 104000,
        "availability": True,
        "imagefile": "img/land-rover-range-rover.png"
    },
    {
        "car_id": 7432,
        "car_name": "Aston Martin DB11",
        "car_description": (
            "The Aston Martin DB11 pairs twin-turbo V8 performance and rear-wheel "
            "drive with a handcrafted cabin and timeless grand-touring design."
        ),
        "year": 2023,
        "model": "DB11 V8 Coupe",
        "price": 205000,
        "availability": True,
        "imagefile": "img/aston-martin-db11.png"
    }
]


superCars = [
    {
        "car_id": 8543,
        "car_name": "Ferrari SF90 Stradale",
        "car_description": (
            "The Ferrari SF90 Stradale combines a twin-turbo V8 and three electric "
            "motors with all-wheel drive, a custom wide-body kit, and carbon-fiber aero."
        ),
        "year": 2023,
        "model": "SF90 Stradale",
        "price": 625000,
        "availability": True,
        "imagefile": "img/ferrari-sf90-stradale-blue-widebody.png"
    },
    {
        "car_id": 9654,
        "car_name": "Lamborghini Aventador SVJ",
        "car_description": (
            "The Lamborghini Aventador SVJ pairs a naturally aspirated V12 with "
            "all-wheel drive and active aerodynamics for uncompromising performance."
        ),
        "year": 2021,
        "model": "Aventador SVJ",
        "price": 517770,
        "availability": True,
        "imagefile": "img/lamborghini-aventador-svj.png"
    },
    {
        "car_id": 1076,
        "car_name": "McLaren 720S",
        "car_description": (
            "The McLaren 720S combines a lightweight carbon-fiber structure, "
            "twin-turbo V8 power, and advanced aerodynamics with a focused cockpit."
        ),
        "year": 2023,
        "model": "720S",
        "price": 299000,
        "availability": True,
        "imagefile": "img/mclaren-720s.png"
    },
    {
        "car_id": 1187,
        "car_name": "Bugatti Chiron",
        "car_description": (
            "The Bugatti Chiron pairs quad-turbocharged W16 power with all-wheel "
            "drive, exceptional craftsmanship, and extraordinary high-speed capability."
        ),
        "year": 2024,
        "model": "Chiron",
        "price": 3000000,
        "availability": True,
        "imagefile": "img/bugatti-chiron.png"
    },
    {
        "car_id": 1298,
        "car_name": "Koenigsegg Jesko",
        "car_description": (
            "The Koenigsegg Jesko Attack combines twin-turbo V8 power, a rapid-shifting "
            "Light Speed Transmission, and extreme high-downforce aerodynamics."
        ),
        "year": 2025,
        "model": "Jesko Attack",
        "price": 3000000,
        "availability": True,
        "imagefile": "img/koenigsegg-jesko.png"
    },
    {
        "car_id": 1309,
        "car_name": "Pagani Huayra",
        "car_description": (
            "The Pagani Huayra is a hypercar that combines a twin-turbo V12 engine, "
            "handcrafted carbon fiber construction, and exquisite Italian design."
        ),
        "year": 2024,
        "model": "Huayra",
        "price": 3000000,
        "availability": True,
        "imagefile": "img/pagani-huayra.png"
    },
    {
        "car_id": 1410,
        "car_name": "Aston Martin Valkyrie",
        "car_description": (
            "The Aston Martin Valkyrie is a hypercar that combines a naturally aspirated "
            "V12 engine, Formula 1-inspired aerodynamics, and extreme performance."
        ),
        "year": 2025,
        "model": "Valkyrie",
        "price": 3000000,
        "availability": True,
        "imagefile": "img/aston-martin-valkyrie.png"
    }
]


sportsCars = [
    {
        "car_id": 1235,
        "car_name": "Chevrolet Corvette C8",
        "car_description": (
            "The Chevrolet Corvette C8 combines a mid-mounted, naturally aspirated "
            "V8 with sharp handling and everyday usability in an exotic-looking package."
        ),
        "year": 2024,
        "model": "Corvette C8",
        "price": 65000,
        "availability": True,
        "imagefile": "img/chevrolet-corvette-c8.png"
    },
    {
        "car_id": 1236,
        "car_name": "Porsche 911",
        "car_description": (
            "The Porsche 911 is a rear-engine sports car that combines timeless design, "
            "precise handling, and exhilarating performance."
        ),
        "year": 2024,
        "model": "911 Carrera",
        "price": 120000,
        "availability": True,
        "imagefile": "img/porsche-911.png"
    },
    {
        "car_id": 1237,
        "car_name": "Nissan GT-R",
        "car_description": (
            "The Nissan GT-R combines twin-turbo V6 power, advanced all-wheel drive, "
            "and relentless acceleration in an unmistakably muscular coupe."
        ),
        "year": 2024,
        "model": "GT-R Premium",
        "price": 115000,
        "availability": True,
        "imagefile": "img/nissan-gt-r.png"
    },
    {
        "car_id": 1238,
        "car_name": "Ford Mustang",
        "car_description": (
            "The Ford Mustang is an iconic American sports car that combines powerful engines, "
            "aggressive styling, and thrilling performance."
        ),
        "year": 2024,
        "model": "Mustang GT Fastback",
        "price": 55000,
        "availability": True,
        "imagefile": "img/ford-mustang.png"
    }
]


sedanCars = [
    {
        "car_id": 1301,
        "car_name": "Toyota Camry",
        "car_description": (
            "The Toyota Camry is a reliable and comfortable sedan that combines fuel efficiency, "
            "modern technology, and a smooth driving experience."
        ),
        "year": 2024,
        "model": "Camry XSE",
        "price": 30000,
        "availability": True,
        "imagefile": "img/toyota-camry.png"
    },
    {
        "car_id": 1302,
        "car_name": "Honda Accord",
        "car_description": (
            "The Honda Accord is a stylish and efficient sedan that offers a comfortable ride, "
            "advanced safety features, and a well-designed interior."
        ),
        "year": 2024,
        "model": "Accord Touring Hybrid",
        "price": 32000,
        "availability": True,
        "imagefile": "img/honda-accord.png"
    }
]


electricCars = [
    {
        "car_id": 1421,
        "car_name": "Tesla Model S",
        "car_description": (
            "The Tesla Model S is a fully electric luxury sedan that offers impressive range, "
            "cutting-edge technology, and exhilarating performance."
        ),
        "year": 2024,
        "model": "Model S Dual Motor AWD",
        "price": 90000,
        "availability": True,
        "imagefile": "img/tesla-model-s.png"
    }
]

hybridCars = [
    {
        "car_id": 1501,
        "car_name": "Toyota Prius",
        "car_description": (
            "The Toyota Prius is a pioneering hybrid car that combines fuel efficiency, "
            "eco-friendly technology, and a comfortable driving experience."
        ),
        "year": 2024,
        "model": "Prius XLE",
        "price": 28000,
        "availability": True,
        "imagefile": "img/toyota-prius.png"
    },
    {
        "car_id": 1502,
        "car_name": "Honda Insight",
        "car_description": (
            "The Honda Insight is a stylish hybrid sedan that offers excellent fuel economy, "
            "advanced safety features, and a comfortable interior."
        ),
        "year": 2022,
        "model": "Insight Touring",
        "price": 29000,
        "availability": True,
        "imagefile": "img/honda-insight.png"
    },
    {
        "car_id": 1702,
        "car_name": "Hyundai Ioniq 5",
        "car_description": (
            "The Hyundai Ioniq 5 is a fully electric crossover that combines futuristic design,"
            " fast charging capabilities, and a spacious interior."
        ),
        "year": 2024,
        "model": "Ioniq 5 Limited AWD",
        "price": 48000,
        "availability": True,
        "imagefile": "img/hyundai-ioniq-5.png"
    },
    {
    "car_id": 1829,
    "car_name": "kia EV6",
    "car_description": (
        "The Kia EV6 is a fully electric crossover that combines sleek design, "
        "impressive range, and advanced technology for an exhilarating driving experience."
    ),
    "year": 2024,
    "model": "EV6 GT-Line",
    "price": 45000,
    "availability": True,
    "imagefile": "img/kia-ev6.png"
    }
]
