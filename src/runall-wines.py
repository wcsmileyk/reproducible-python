import importlib
import sys

import recipy

subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

data_file = sys.argv[1]

interim_file = subset.process_data_GBP(data_file)
print(f'Created Interim Data file: {interim_file}')
country = sys.argv[2]

plotwines.create_plots(interim_file)

print(f'Subsetting {interim_file}')
print(f'Country Searched: {country}')
print(country_sub.get_country(interim_file, country))
