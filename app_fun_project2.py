import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(page_title="Quiz Profesi", layout="centered")

st.title("👩‍💼👨‍💼 Test Profesi: Manager, Analyst, Frontliner")
st.write("Selamat datang di kuis penentuan profesi! 💼 Quiz ini akan menentukan kamu lebih cocok menjadi seorang **Manager**, **Analyst**, atau **Frontliner**? Yuk, cari tahu!")

# Input Nama
name = st.text_input("✍️ Masukkan Namamu:")
if name:
    st.markdown("**Jawab pertanyaan di bawah ini untuk mengetahui kecocokan profesimu!**")
else:
    st.warning("Mohon masukkan nama terlebih dahulu untuk memulai kuis.")

# Inisialisasi skor
score = {
    "Manager": 0,
    "Analyst": 0,
    "Frontliner": 0
}

# Fungsi pertanyaan
def tanya(pertanyaan, opsi, mapping):
    jawaban = st.radio(pertanyaan, opsi, key=pertanyaan)
    score[mapping[jawaban]] += 1

# Pertanyaan-pertanyaan
if name:
    tanya(
        "1. Apa yang paling kamu sukai dari pilihan berikut ini?",
        ["Menganalisis masalah kompleks", "Memimpin dan memberikan instruksi orang lain", "Bertemu dan berinteraksi dengan orang lain"],
        {
            "Menganalisis masalah kompleks": "Analyst",
            "Memimpin dan memberikan instruksi orang lain": "Manager",
            "Bertemu dan berinteraksi dengan orang lain": "Frontliner"
        }
    )

    tanya(
        "2. Bagaimana cara kamu mengambil keputusan?",
        ["Dengan mempertimbangkan bersama anggota tim", "Berdasarkan Data dan logika", "Cepat dan tanggap terhadap situasi"],
        {
            "Dengan mempertimbangkan bersama anggota tim": "Manager",
            "Berdasarkan Data dan logika": "Analyst",
            "Cepat dan tanggap terhadap situasi": "Frontliner"
        }
    )

    tanya(
        "3. Apa kekuatan utama kamu?",
        ["Analitik dan penalaran logika", "Kemampuan mengkoordinasi tim", "Komunikasi"],
        {
            "Analitik dan penalaran logika": "Analyst",
            "Kemampuan mengkoordinasi tim": "Manager",
            "Komunikasi": "Frontliner"
        }
    )

    if st.button("🔎 Lihat Hasil"):
        st.markdown("---")
        total_score = sum(score.values())

        if total_score == 0:
            st.error("Kamu belum menjawab semua pertanyaan.")
        else:
            with st.expander("📢 Klik di sini untuk melihat hasil kuismu"):
                if len(set(score.values())) == 1:
                    st.success(f"Wah {name}, kamu orang yang Multitalent! 🌟 Cocok di berbagai peran!")
                else:
                    recommended = max(score, key=score.get)
                    if recommended == "Analyst":
                        st.info(f"📊 {name}, Kamu cocok sebagai **Analyst**!")
                        st.write("Kamu menyukai data, logika, dan mencari pola tersembunyi.")
                    elif recommended == "Manager":
                        st.success(f"👩‍💼 {name}, Kamu cocok sebagai **Manager**!")
                        st.write("Kamu adalah pemimpin yang mampu mengatur tim dan mengambil keputusan.")
                    else:
                        st.warning(f"🤝 {name}, Kamu cocok sebagai **Frontliner**!")
                        st.write("Kamu ramah, cepat tanggap, dan senang berinteraksi langsung dengan orang lain.")

                # Grafik Persentase
                st.markdown("### 📊 Persentase Kecocokan Profesi")
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
                ).properties(width=500, height=300)
                st.altair_chart(chart)

                # Tabel
                st.markdown("### 📋 Detail Skor dan Persentase")
                st.table(df_chart)

                # Penutup
                st.markdown("---")
                st.markdown("## 🎉 Terima Kasih Sudah Mengikuti Quiz!")
                st.write("Semoga hasil ini membantumu lebih mengenal potensi dan arah kariermu ke depan. 🚀")
                st.write("Tetap semangat, terus belajar, dan jangan takut mencoba hal baru! 💪")

                # Tombol Mulai Ulang
                st.markdown("### 🔁 Ingin Coba Lagi?")
                if st.button("Mulai Ulang"):
                    st.experimental_rerun()