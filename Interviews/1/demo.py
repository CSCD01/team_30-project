import matplotlib.pyplot as plt
import csv, sys

countries = sys.argv[1:]

reader = csv.DictReader(open('factbook.csv'), delimiter=";")

labels = []
country_gdp = []

for row in reader:
    if (row['Country'] in countries):
        labels.append(row['Country'])
        country_gdp.append(float(row['GDP']))

plt.bar(labels, country_gdp, bottom=0)
plt.xlabel('Country', fontsize=16)
plt.ylabel('GDP (Trillion \$)', fontsize=16)
plt.title('GDP of countries in (2011)', fontsize=16)
plt.show()
