import csv

# Åpne CSV-filen
with open('05994_20240126-145813-csv.csv', 'r', encoding="ISO-8859-1") as fil:
  # Leser innholdet i filen som en liste over rader
  leser = csv.reader(fil)

  # Initialiserer datastrukturer for å lagre aggregerte data
  total_tid_kvinner = 0
  total_tid_menn = 0
  aktivitetsdata = {}

  # Hopper over topptekstlinjen
  next(leser)

  # Itererer over hver rad i filen
  for rad in leser:
    # Del raden i separate elementer basert på semikolon
    elementer = rad[0].split(';')

    # Hent kjønn og tidsbruk fra elementene
    aktivitetsnavn = elementer[0]
    kjønn = elementer[1]
    tid = float(elementer[2])

    # Oppdater total tid for menn og kvinner
    if kjønn == "Kvinner":
      total_tid_kvinner += tid
    elif kjønn == "Menn":
      total_tid_menn += tid

    # Behandle aktivitetsnavn (kan inneholde spesialtegn)
    if aktivitetsnavn in aktivitetsdata:
      aktivitetsdata[aktivitetsnavn] += tid
    else:
      aktivitetsdata[aktivitetsnavn] = tid

# Skriver ut total tid brukt av menn og kvinner
print(f"Total tid brukt av kvinner: {total_tid_kvinner:.2f} timer")
print(f"Total tid brukt av menn: {total_tid_menn:.2f} timer")

# Skriver ut detaljert tidsbruk fordelt på aktivitet og kjønn
for aktivitetsnavn, tid in aktivitetsdata.items():
  print(f"{aktivitetsnavn}: {tid:.2f} timer")