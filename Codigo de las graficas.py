import pandas as pd
import plotly.express as px

# Datos de esperanza de vida
esperanza_vida_data = {
    "Fecha": [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005],
    "Esperanza de vida - Mujeres": [758, 751, 754, 767, 774, 774, 770, 765, 762, 761, 761, 761, 762, 759, 759, 756, 754, 750],
    "Esperanza de vida - Hombres": [166, 566, 166, 868, 967, 966, 866, 766, 766, 667, 667, 967, 167, 666, 266, 866, 65, 865],
    "Esperanza de vida": [847, 87, 437, 17, 357, 917, 767, 837, 997, 157, 267, 297, 257, 967, 717, 337, 977, 647]
}

esperanza_df = pd.DataFrame(esperanza_vida_data)

# Gráfico de evolución de la esperanza de vida
fig1 = px.line(
    esperanza_df, 
    x="Fecha", 
    y=["Esperanza de vida - Mujeres", "Esperanza de vida - Hombres", "Esperanza de vida"],
    labels={"value": "Esperanza de Vida (años)", "variable": "Categoría"},
    title="Evolución de la Esperanza de Vida en El Salvador"
)
fig1.update_layout(xaxis_title="Año", yaxis_title="Esperanza de Vida (años)")
fig1.show()

# Datos de homicidios
homicidios_data = {
    "Fecha": [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010],
    "Número de Homicidios": [496, 1085, 1341, 2398, 3346, 3962, 5276, 6656, 3921, 2513, 2594, 4371, 3987]
}

homicidios_df = pd.DataFrame(homicidios_data)

# Gráfico de homicidios anuales
fig2 = px.bar(
    homicidios_df, 
    x="Fecha", 
    y="Número de Homicidios", 
    title="Número de Homicidios en El Salvador por Año",
    labels={"Número de Homicidios": "Cantidad de Homicidios", "Fecha": "Año"},
    color="Número de Homicidios"
)
fig2.update_layout(xaxis_title="Año", yaxis_title="Número de Homicidios", xaxis=dict(tickangle=45))
fig2.show()
