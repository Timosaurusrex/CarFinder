import matplotlib.pyplot as plt
from math import sqrt

urls = [{'file': 'seat-st'}, {'file': 'golf'}, {'file': 'variant'}, {'file': 'skoda'}]

for num in range(0, len(urls)):
    with open(f"sorted_{urls[num]['file']}.txt", 'w') as f:
       f.write("")
    with open(f"{urls[num]['file']}.txt", 'r') as f:
        lines = f.readlines()

    autos = []
    all_autos = []

    # Iterieren über jede zweite Zeile in der Liste von Zeilen, da jede zweite Zeile ein neues Auto darstellt
    for i in range(0, len(lines)):
        # Aufteilen der Zeile mit Werten in eine Liste
        values = lines[i].strip().split(',')
        # Erstellen eines neuen Auto-Dictionaries mit den Werten
        auto = {
            'marke': values[0],
            'preis': int(values[1]),
            'postleitzahl': values[2],
            'erstzulassung': int(values[3]),
            'kilometerstand': int(values[4]),
            'ps': values[5],
            'url_auto': values[6].strip()
        }
        # Hinzufügen des neuen Autos zur Liste von Autos
        autos.append(auto)
        all_autos.append(auto)

    # Ausgabe der Liste von Autos
    print(autos)

    # Filtern von Autos mit gleicher Erstzulassung
    for erstzulassung in range(2018, 2022):
        autos_filtered = [auto for auto in autos if auto['erstzulassung'] == erstzulassung]
        if len(autos_filtered) == 0:
            break
        print(autos_filtered)
        # Erstellen von x- und y-Listen für das Diagramm
        x_values = [auto['preis'] for auto in autos_filtered]
        y_values = [auto['kilometerstand'] for auto in autos_filtered]

        # Schreiben der Daten in eine Datei nach x*y sortiert
        autos_sorted = sorted(autos_filtered, key=lambda auto: sqrt((auto['preis']/1000)**2+(auto['kilometerstand']/10000)**2))
        with open(f"sorted_{urls[num]['file']}.txt", 'a') as f:
            f.write("Autos von " + str(erstzulassung) + ": \n")
            for auto in autos_sorted:
                f.write(f"Marke: {auto['marke']}, Preis: {auto['preis']}, Kilometerstand: {auto['kilometerstand']}, PS: {auto['ps']}, Postleitzahl: {auto['postleitzahl']}, Url: {auto['url_auto']}\n")
            f.write("\n")
        f.close()


    """
        # Erstellen des Diagramms
        plt.scatter(x_values, y_values)
        plt.title(f'Autos von {erstzulassung}')
        plt.xlabel('Preis')
        plt.ylabel('Kilometerstand')
        plt.show()
    """
    """"""

    # Alle Autos sortiert
    autos_sorted2 = sorted(all_autos, key=lambda auto: sqrt((auto['preis']/1000)**2+(auto['kilometerstand']/10000)**2))
    with open(f"sorted_{urls[num]['file']}.txt", "a") as f:
        f.write("Alle Autos sortiert: \n")
        for auto in autos_sorted2:
            f.write(f"EZ: {auto['erstzulassung']}, Preis: {auto['preis']}, Km: {auto['kilometerstand']}, Marke: {auto['marke']}, PS: {auto['ps']}, Postleitzahl: {auto['postleitzahl']}, Url: {auto['url_auto']}\n")
    f.close()

    # Erstellen von x- und y-Listen für das Diagramm
    x2_values = [auto['preis'] for auto in all_autos]
    y2_values = [auto['kilometerstand'] for auto in all_autos]

    # Erstellen des Diagramms
    plt.scatter(x2_values, y2_values)
    plt.title(f'{urls[num]["file"]} von all Erstzulassungen')
    plt.xlabel('Preis')
    plt.ylabel('Kilometerstand')
    plt.show()