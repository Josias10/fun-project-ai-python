import streamlit as st
import altair as alt
import pandas as pd

st.title("👩‍💼👨‍💼 Test Profesi : Manager, Analyst, Frontliner")
st.write("💼Test ini merupakan suatu assessment bagi kamu untuk mengetahui apakah kamu cocok menjadi seorang Manager, Analyst, atau Frontliner 💼")

#Input Nama
name = st.text_input("✍️Masukkan Namamu : ")
if name : 
    st.markdown("Jawab pertanyaan di bawah untuk mengetahui Kecocokan Profesimu")
else :
    st.warning("Mohon masukkan nama terlebih dahulu untuk memulai kuis.")

#Penentuan Skor    
score = {
    "Manager" : 0,
    "Analyst" : 0,
    "Frontliner" : 0
}

#Fungsi Memberikan pertanyaan, jawaban, dan point
def quest(pertanyaan, jawaban, map):
    jawaban = st.radio(pertanyaan, jawaban, key=pertanyaan)
    score[map[jawaban]] += 1

#Pertanyaan 1
if name:
    quest(
        "1. Apa yang paling kamu sukai dari pilihan berikut ini?",
        ["Menganalisis masalah kompleks", "Memimpin dan memberikan instruksi orang lain", "Bertemu dan berinteraksi dengan orang lain"],
        {
            "Menganalisis masalah kompleks": "Analyst",
            "Memimpin dan memberikan instruksi orang lain": "Manager",
            "Bertemu dan berinteraksi dengan orang lain": "Frontliner"
        }
    )

    quest(
        "2. Bagaimana cara kamu mengambil keputusan?",
        ["Dengan mempertimbangkan bersama anggota tim", "Berdasarkan Data dan logika", "Cepat dan tanggap terhadap situasi"],
        {
            "Dengan mempertimbangkan bersama anggota tim": "Manager",
            "Berdasarkan Data dan logika": "Analyst",
            "Cepat dan tanggap terhadap situasi": "Frontliner"
        }
    )

    quest(
        "3. Apa kekuatan utama kamu?",
        ["Analitik dan penalaran logika", "Kemampuan mengkoordinasi tim", "Komunikasi"],
        {
            "Analitik dan penalaran logika": "Analyst",
            "Kemampuan mengkoordinasi tim": "Manager",
            "Komunikasi": "Frontliner"
        }
    )

    if st.button("🔎 Lihat Hasil"):
        st.write("-"*50)
        total_score = sum(score.values())

        if total_score == 0 : 
            st.error("Kamu belum menjawab semua pertanyaan.")
        else : 
            st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGZ5bDRnZjJtMnQ5cWdzZjJ1YTF3bXB4MTg1dHU0MW1oaDRsZWZ3ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Js7cqIkpxFy0bILFFA/giphy.gif")
            with st.expander("📢 Klik di sini untuk melihat hasil kuismu"):
                if len(set(score.values())) == 1:
                    st.subheader(f"Wah {name}, kamu orang yang Multitalent! ✨✨ Cocok di berbagai peran!🌟")
                else:
                    recommended = max(score, key=score.get)
                    st.subheader (f"{name}, Kamu cocok sebagai {recommended}!")
                    if recommended == "Analyst" : 
                        st.write("📊 Kamu adalah seseorang yang menyukai data, logika, dan mencari pola tersembunyi.")
                    elif recommended == "Manager":
                        st.write("👩‍💼 Kamu adalah seorang pemimpin yang mampu mengatur tim dan mengambil keputusan besar.")
                    else : 
                        st.write("🤝Kamu adalah sosok yang ramah, cepat tanggap, dan senang berinteraksi langsung dengan orang lain.")

                
                #Grafik
                st.markdown("📊 Presentase Kecocokan Profesimu")
                df_chart = pd.DataFrame({
                    "Profesi": list(score.keys()),
                    "Skor": list(score.values()),
                    "Persentase": [round((v / total_score) * 100, 1) for v in score.values()]
                })
                chart = alt.Chart(df_chart).mark_bar().encode(
                    x=alt.X('Profesi', axis=alt.Axis(labelAngle=0)),
                    y=alt.Y('Persentase', title="Persentase (%)"),
                    color='Profesi',
                    tooltip=['Profesi', 'Skor', 'Persentase']
                ).properties(
                    width = 500,
                    height = 300
                )
                st.altair_chart(chart)

                #Tabel
                st.markdown("📋 Detail Skor dan Persentase")
                st.table(df_chart)

                 # Penutup
                st.markdown("---")
                st.markdown("🎉 Terima Kasih Sudah Mengikuti Quiz!")
                st.write("Semoga hasil ini membantumu lebih mengenal potensi dan arah kariermu ke depan ya! 🚀")
                st.write("Tetap semangat, terus belajar 💪")

                # Tombol Mulai Ulang
                st.markdown("### 🔁 Ingin Coba Lagi?")
                if st.button("Mulai Ulang"):
                    st.experimental_rerun()