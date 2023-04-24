"""
https://www.willhaben.at/iad/gebrauchtwagen/auto/gebrauchtwagenboerse?sfId=56810cc8-1128-4387-8ade-04c0d313f092&isNavigation=true&CAR_MODEL/MAKE=1064&CAR_MODEL/MODEL=66&MOTOR_CONDITION=10&MOTOR_CONDITION=50&MOTOR_CONDITION=91&MOTOR_CONDITION=40
https://www.willhaben.at/iad/gebrauchtwagen/auto/gebrauchtwagenboerse?CAR_MODEL/MAKE=1064&sfId=eacebcfa-db2b-47c9-97b5-1582215a9a9e&rows=30&isNavigation=true&MOTOR_CONDITION=20&MOTOR_CONDITION=50&MOTOR_CONDITION=10&MOTOR_CONDITION=93&MOTOR_CONDITION=91&MOTOR_CONDITION=40&ENGINE/FUEL=100004&EQUIPMENT=15&page=1
https://www.willhaben.at/iad/gebrauchtwagen/auto/gebrauchtwagenboerse?CAR_MODEL/MAKE=1054&sfId=eacebcfa-db2b-47c9-97b5-1582215a9a9e&rows=30&isNavigation=true&EQUIPMENT=15&MOTOR_CONDITION=20&MOTOR_CONDITION=50&MOTOR_CONDITION=10&MOTOR_CONDITION=91&MOTOR_CONDITION=40&sort=3&ENGINE/FUEL=100003&ENGINE/FUEL=100004&page=1
"""

brand = {'Alfa Romeo': 1000, 'AMC': 1001,'Aston Martin':  1002, 'Audi':  1003,
         'Bentley':  1004, 'BMW':  1005, 'Buick':  1006, 'Cadillac':  1007, 'Chevrolet':  1008, 'Chrysler':  1009,
         'Citroen':  1010, 'Axiam':  1011, 'Daewoo':  1012, 'Daiahatsu':  1013,
         'Doge':  1014, 'Ferrari':  1015, 'Fiat':  1016, 'Ford':  1017, 'Honda':  1018, 'Hummer':  1019,
         'Hyundai':  1020, 'Isuzu':  1021, 'Iveco':  1022, 'Jaguar':  1023, 'Jeep':  1024, 'Kia':  1025,
         'Lada':  1026, 'Lamborghini':  1027, 'Lancia':  1028, 'Land Rover':  1029, 'Lexus':  1030, 'Lincoln':  1031,
         'Lotus':  1032, 'Maserati':  1033, 'Maybach':  1034, 'Mazda':  1035, 'Mercedes-Benz':  1036,
         'Mercury':  1037, 'MG':  1038, 'Mini':  1039, 'Mitsubishi':  1040, 'Morgan':  1042, 'Nissan':  1042,
         'Opel':  1043, 'Pagani':  1044, 'Peugeot':  1045, 'nothing':  1046, 'Pontiac':  1047, 'Porsche':  1048,
         'Puch':  1049, 'Qvale':  1050, 'Renault':  1051, 'Rolls-Royce':  1052, 'Rover':  1053, 'Saab':  1054,
         'Sauber':  1055, 'Seat':  1056, 'Skoda':  1057, 'Smart':  1058, 'SsangYong':  1059, 'Subaru':  1060,
         'Suzuki':  1061, 'Toyota':  1062, 'TVR':  1063, 'Volvo' : 1064, 'VW': 1065, 'Wiesmann': 1066}

fuel = {'Benzin': 100001, 'Diesel': 100003, 'Elektro': 100004, 'Hybrid/Benzin': 100013, 'Hybrid/Diesel':100022}
