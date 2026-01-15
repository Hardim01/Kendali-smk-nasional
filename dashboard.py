import streamlit as st

# 1. Konfigurasi Akun & Jabatan
users = {
    "kepsek": {"password": "123", "role": "Kepala Sekolah"},
    "kurikulum": {"password": "kur", "role": "Waka Kurikulum"},
    "kesiswaan": {"password": "kes", "role": "Waka Kesiswaan"},
    "sarpras": {"password": "sar", "role": "Waka Sarpras"},
    "hubin": {"password": "hub", "role": "Waka Hubin"},
    "ktu": {"password": "ktu", "role": "Kepala TU (KTU)"},
    "bendahara": {"password": "bos", "role": "Bendahara BOS"},
    "keuangan": {"password": "adm", "role": "Admin Keuangan"},
    "bk": {"password": "bk1", "role": "Guru BK"},
    "laboran": {"password": "lab", "role": "Laboran"},
    "osis": {"password": "osi", "role": "Pembina OSIS"},
    "media": {"password": "med", "role": "Tim Media"},
    "tertib": {"password": "ter", "role": "Tim Ketertiban"}
}

def login():
    st.markdown("<h2 style='text-align: center;'>🔐 LOGIN SISTEM KENDALI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>SMK NASIONAL - RUAS STUDIO</p>", unsafe_allow_html=True)
    
    username = st.text_input("Username Jabatan")
    password = st.text_input("Password", type="password")
    if st.button("Masuk ke Sistem", use_container_width=True):
        if username in users and users[username]["password"] == password:
            st.session_state["auth"] = True
            st.session_state["role"] = users[username]["role"]
            st.session_state["user"] = username
            st.rerun()
        else:
            st.error("Username atau Password salah!")

if "auth" not in st.session_state:
    st.session_state["auth"] = False

if not st.session_state["auth"]:
    login()
else:
    role = st.session_state["role"]
    st.sidebar.title(f"👤 {st.session_state['user'].upper()}")
    st.sidebar.info(f"Jabatan: **{role}**")
    if st.sidebar.button("Keluar Sistem"):
        st.session_state["auth"] = False
        st.rerun()

    st.title(f"🛡️ Panel Kendali: {role}")
    
    # Dashboard Pimpinan
    if role in ["Kepala Sekolah", "Kepala TU (KTU)"]:
        st.subheader("📊 Ringkasan Seluruh Unit")
        c1, c2, c3 = st.columns(3)
        c1.metric("Saldo Kas", "Rp 123.500.000", "+2.4%")
        c2.metric("Absensi Guru", "98%", "-1%")
        c3.metric("Laporan OSIS", "3 Masuk")
        
        st.info("💡 **Instruksi Kepsek:** Segera selesaikan laporan BOS tahap 1.")

    # Menu Keuangan
    elif role in ["Bendahara BOS", "Admin Keuangan"]:
        st.subheader("💰 Input Transaksi Baru")
        st.number_input("Jumlah (Rp)")
        st.text_input("Keterangan")
        st.file_uploader("Upload Bukti")
        st.button("Simpan Transaksi")

    else:
        st.subheader("📝 Laporan Kerja Mingguan")
        st.text_area("Tulis kegiatan hari ini...")
        st.button("Kirim Laporan")

    st.divider()
    st.caption("RUAS STUDIO © 2026 - Aplikasi Kendali Internal")
