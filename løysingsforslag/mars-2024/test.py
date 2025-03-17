from datetime import datetime

# Dato i formatet "YYYY-MM-DD"
dato = "2020-01-08"

# Konverterer strengen til eit datetime-objekt
dato_objekt = datetime.strptime(dato, "%Y-%m-%d")

# Henter vekenummeret (isocalendar returnerer ein tuple med år [0], uke [1], ukedag [2])
vekenummer = dato_objekt.isocalendar()[1]

print(f"Vekenummeret for {dato} er {vekenummer}.")