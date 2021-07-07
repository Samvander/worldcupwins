import pandas as pd
import geopandas
import folium


world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))


url = "https://en.wikipedia.org/wiki/National_team_appearances_in_the_FIFA_World_Cup"
tables = pd.read_html(url)
table = tables[3]

pd.set_option('display.max_rows', 200)

# print(table)

newTable = world.merge(table, how='left', left_on=['name'], right_on=['Team'])

my_map = folium.Map()
folium.Choropleth(
    geo_data=newTable,
    name='chloropleth',
    data=table,
    columns=['Team','W'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='FIFA World Cup Wins by Country'
).add_to(my_map)
my_map.save('fifawc.html')
