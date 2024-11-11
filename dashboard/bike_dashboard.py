import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

hour_df = pd.read_csv('hour.csv')

st.header("BIKE SHARING")

st.subheader('Cuaca Paling Banyak Meraih Pengguna')

fig, ax = plt.subplots(figsize=(10, 5))
hour_df['weather_cut'] = pd.cut(hour_df.weathersit, bins=4, 
                                labels=['Cerah, Sedikit Berawan, Sebagian Berawan', 
                                        'Kabut + Berawan, Kabut + Awan Pecah, Kabut + Beberapa Awan', 
                                        'Salju Ringan, Hujan Ringan + Badai Petir + Awan Tersebar, Hujan Ringan + Awan Tersebar', 
                                        'Hujan Lebat + Hujan Es + Badai Petir + Kabut, Salju + Kabut'])

banyak_user_weather = hour_df.groupby(by=["weather_cut"]).cnt.sum().sort_values(ascending=True).reset_index()
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="weather_cut",
    x="cnt",
    data=banyak_user_weather,
    palette=colors,
    ax=ax
)

ax.set_ylabel("Jumlah User", fontsize=15)
ax.set_xlabel("Cuaca", fontsize=15)
ax.set_title("Jumlah User Pada Setiap Cuaca", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=10)

st.pyplot(fig)


st.subheader('Cuaca dan Jam Paling Banyak Meraih Pengguna')
fig, ax = plt.subplots(figsize=(10, 5))
hour_df['hr_cut']=pd.cut(hour_df.hr, bins=24, right=False,
                           labels = ['00:00', '01.00','02:00',
                                     '03:00', '04.00','05:00',
                                     '06:00', '07.00','08:00',
                                     '09:00', '10.00','11:00',
                                     '12:00', '13.00','14:00',
                                     '15:00', '16.00','17:00',
                                     '18:00', '19.00','20:00',
                                     '21:00', '22.00','23:00',])

banyak_user_jam_weather = hour_df.groupby(by=["hr_cut", "weathersit"]).cnt.sum().reset_index()

sns.scatterplot(
    data=banyak_user_jam_weather,
    x="hr_cut",
    y="cnt",
    hue="weathersit",
)
ax.set_ylabel("Jumlah User", fontsize=15)
ax.set_xlabel("Jam", fontsize=15)
ax.set_title("Jam yang paling banyak dikunjungi berdasarkan kondisi cuacanya", loc="center", fontsize=20)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)




                   
                   
