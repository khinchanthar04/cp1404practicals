"""
CP1404 Practical 5
Wimbledon displaying, processing and data-reading
"""

FILENAME = "wimbledon.csv"
data = []
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2
with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    header = in_file.readline().strip().split(',')
    for line in in_file:
        row = line.strip().split(',')
        data.append(row)

champion_counts = {}
countries = set()
for row in data:
    countries.add(row[INDEX_COUNTRY])
    try:
        champion_counts[row[INDEX_CHAMPION]] += 1
    except KeyError:
        champion_counts[row[INDEX_CHAMPION]] = 1

print("Wimbledon Champions: ")
for champion, count in champion_counts.items():
    print(f"{champion} {count}")

sorted_countries = sorted(countries)
countries_string = ", ".join(sorted_countries)
print(f"\nThese {len(countries)} countries have won Wimbledon: ")
print(countries_string)

