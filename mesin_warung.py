import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Aplikasi Warung",
    page_icon="🏪",
    layout="centered"
)

# --- GANTI NAMA APLIKASI DI BAWAH INI ---
st.title("🏪 KASIR WARUNG IMAFATIH") 
# ---------------------------------------

st.write("Penghitung Laba Bersih Otomatis")

# 2. Input Jumlah Terjual
st.subheader("Input Penjualan:")
col1, col2 = st.columns(2)

with col1:
    qty_a = st.number_input("Jajan A (Rp 1.000)", min_value=0, step=1, value=0)
    qty_c = st.number_input("Jajan C (Rp 3.000)", min_value=0, step=1, value=0)

with col2:
    qty_b = st.number_input("Jajan B (Rp 2.000)", min_value=0, step=1, value=0)
    qty_d = st.number_input("Jajan D (Rp 4.000)", min_value=0, step=1, value=0)

# 3. Tombol Hitung
if st.button("HITUNG LABA BERSIH", use_container_width=True):
    # Logika Modal
    untung_a = (1000 - 800) * qty_a
    untung_b = (2000 - 1600) * qty_b
    untung_c = (3000 - 2400) * qty_c
    untung_d = (4000 - 3200) * qty_d
    
    total_omzet = (qty_a * 1000) + (qty_b * 2000) + (qty_c * 3000) + (qty_d * 4000)
    total_laba = untung_a + untung_b + untung_c + untung_d
    
    st.markdown("---")
    st.metric(label="TOTAL OMZET", value=f"Rp {total_omzet:,.0f}")
    st.metric(label="LABA BERSIH", value=f"Rp {total_laba:,.0f}")
    
    if total_laba > 0:
        st.success(f"Untung bersih hari ini: Rp {total_laba:,.0f}")

# --- GANTI TULISAN DI BAWAH INI (SCROLL PALING BAWAH) ---
st.caption("Dikembangkan oleh Suamitercintahmu - semoga mempermudah")
# -------------------------------------------------------
