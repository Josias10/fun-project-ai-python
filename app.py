import streamlit as st
import altair as alt
import pandas as pd

st.title("Test Profesi : Manager, Analyst, Frontliner")
st.write("Test ini merupakan suatu assessment bagi kamu untuk mengetahui apakah kamu cocok menjadi seorang Manager, Analyst, atau Frontliner")

name = st.text_input("Masukkan Namamu : ")
st.markdown("Jawab pertanyaan di bawah untuk mengetahui Kecocokan Profesimu")

score = {
    "Manager" : 0,
    "Analyst" : 0,
    "Frontliner" : 0
}
#Pertanyaan 1
qna1 = st.radio("1. Apakah kamu sukai dari opsi berikut ini : ",
        ["Menganalisis masalah kompleks",
         "Memimpin dan memberikan instruksi orang lain",
         "Bertemu dan berinteraksi dengan orang lain"])
if qna1 == "Menganalisis masalah kompleks":
    score["Analyst"] += 1
elif qna1 == "Memimpin dan memberikan instruksi orang lain":
    score["Manager"] += 1
else:
    score["Frontliner"] +=1

#Pertanyaan 2
qna2 = st.radio("2. Bagaimana caranya kamu mengambil suatu keputusan? ",
        ["Dengan mempertimbangkan bersama anggota tim",
         "Berdasarkan Data dan logika",
         "Cepat dan tanggap terhadap situasi"])
if qna2 == "Berdasarkan Data dan logika":
    score["Analyst"] += 1
elif qna2 == "Dengan mempertimbangkan bersama anggota tim":
    score["Manager"] += 1
else:
    score["Frontliner"] +=1

#Pertanyaan 3
qna3 = st.radio("3. Apa bentuk kekuatan utamamu? ",
        ["Analitik dan penalaran logika",
         "Kemampuan mengkoordinasi tim",
         "Komunikasi"])
if qna3 == "Analitik dan penalaran logika":
    score["Analyst"] += 1
elif qna3 == "Kemampuan mengkoordinasi tim":
    score["Manager"] += 1
else:
    score["Frontliner"] +=1

if st.button("Lihat Hasil"):
    
    st.write("-"*50)
    if len(set(score.values())) == 1:
        st.subheader (f"Wah {name}, kamu orang yang Multitalent! Cocok di berbagai Peran")

    else:
        recommended = max(score, key=score.get)
        st.subheader (f"{name}, Kamu cocok sebagai {recommended}!")
        if recommended == "Analyst" : 
            st.write("Kamu adalah seseorang yang menyukai data, logika, dan mencari pola tersembunyi.")
        elif recommended == "Manager":
            st.write("Kamu adalah seorang pemimpin yang mampu mengatur tim dan mengambil keputusan besar.")
        else : 
            st.write("Kamu adalah sosok yang ramah, cepat tanggap, dan senang berinteraksi langsung dengan orang lain.")

    
    #Grafik
    st.markdown("Berikut merupakan Skor kamu dalam Grafik : ")
    df_chart = pd.DataFrame(list(score.items()), columns=['Profesi', 'Skor'])
    chart = alt.Chart(df_chart).mark_bar().encode(
        x =alt.X('Profesi', axis=alt.Axis(labelAngle=0)),
        y = 'Skor',
        color = 'Profesi'
    ).properties(
        width = 500,
        height = 300
    )
    st.altair_chart(chart)

    #TABEL
    df_score = pd.DataFrame.from_dict(score, orient='index', columns=['Skor']).reset_index()
    df_score.columns = ["Profesi", "Skor"]
    st.table(df_score)
