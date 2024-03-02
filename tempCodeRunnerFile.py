import folium

m = folium.Map(location=(23.880756,90.267220), tiles="Cartodb dark_matter",
               attr="https://www.openstreetmap.org/copyright",zoom_start = 15)


tooltip = folium.GeoJsonTooltip(fields=["Name"],
                                    aliases=["Name"],
    localize=True,
    sticky=False,
    labels=True,
    style="""
        background-color: #F0EFEF;
        border: 2px solid black;
        border-radius: 3px;
        box-shadow: 3px;
    """,
    max_width=800,
)

geoJSON_file = 'E:\\Web GIS Work\\Folium\\ju_structure.geojson'

folium.GeoJson(geoJSON_file, name="ju_structure", popup=folium.features.GeoJsonPopup(fields=["Name"]),
               tooltip=tooltip).add_to(m)

road_file = 'E:\\Web GIS Work\\Folium\\varisty_road.geojson'

road_style = {'color':'#ffd700'}

folium.GeoJson(road_file, style_function=lambda x:road_style).add_to(m)
folium.LayerControl().add_to(m)


m.save("JU_Map.html")
