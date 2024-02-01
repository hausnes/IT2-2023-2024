import matplotlib.pyplot as plt

# Lager lister med land og produksjon
land = ["China", "Japan", "Germany", "USA", "South Korea", "India", "Spain", "Mexico", "Brazil", "UK"]
produksjon = [24420744, 7873886, 5746808, 3934357, 3859991, 3677605, 2354117, 1993168, 1778464, 1722698]

# Lager en figur
# plt.figure(figsize=(10, 5))

# Lager et søylediagram
plt.bar(land, produksjon)

# Setter tittel og aksetitler
plt.title("Bilproduksjon i 2019")
plt.xlabel("Land")
plt.ylabel("Produksjon")

# Roterer x-aksen etikettene 90 grader
plt.xticks(rotation=90)

# Justerer bunnen av plottet for å gi plass til etikettene for x-aksen
plt.subplots_adjust(bottom=0.25)

# Viser søylene
plt.show()