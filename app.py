import streamlit as st
import base64

# ==================== KONFIGURASI HALAMAN ====================
st.set_page_config(
    page_title="Kalkulator Digital - Politeknik AKA Bogor",
    page_icon="🏫",
    layout="wide"
)

# ==================== FUNGSI UNTUK LOAD GAMBAR ====================
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Coba load gambar logo (jika ada)
try:
    img_base64 = get_img_as_base64("logo-politeknik-aka-bogor.png")
    logo_css = f"""
    .stApp {{
        background: linear-gradient(
            rgba(15, 23, 42, 0.85),
            rgba(15, 23, 42, 0.85)
        ), url('data:image/png;base64,{img_base64}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    """
except FileNotFoundError:
    logo_css = """
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
    }
    """

# ==================== CUSTOM CSS ====================
st.markdown(f"""
    <style>
    {logo_css}
    
    .main > div {{
        background: rgba(15, 23, 42, 0.6);
        border-radius: 20px;
        padding: 20px;
        backdrop-filter: blur(3px);
    }}
    
    [data-testid="stSidebar"] {{
        background: rgba(15, 23, 42, 0.85) !important;
        backdrop-filter: blur(5px);
    }}
    
    .stButton button {{
        background: linear-gradient(90deg, #3b82f6, #2563eb);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }}
    
    .stButton button:hover {{
        transform: scale(1.02);
    }}
    
    .stNumberInput input {{
        background-color: #1f2937;
        color: white;
        border-radius: 10px;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background-color: #1f2937;
        border-radius: 10px;
        padding: 10px 20px;
        color: white;
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: #3b82f6;
        color: white;
    }}
    
    .custom-header {{
        text-align: center;
        padding: 2rem;
        background: linear-gradient(90deg, #1d4ed8, #0f4c81);
        border-radius: 20px;
        margin-bottom: 2rem;
    }}
    
    .custom-footer {{
        text-align: center;
        padding: 1rem;
        margin-top: 2rem;
        color: #94a3b8;
        font-size: 14px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.markdown("""
    <div class="custom-header">
        <h1 style="color: white; margin: 0;">🏫 KALKULATOR DIGITAL</h1>
        <p style="color: white; font-size: 18px; margin-top: 10px;">Kalkulator Pembuatan & Pengenceran Larutan</p>
        <p style="color: #93c5fd; font-size: 14px; margin-top: 10px;">Politeknik AKA Bogor</p>
    </div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h2 style="color: #60a5fa;">📋 Menu</h2>
    </div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "",
    ["💧 Pembuatan Larutan", "🧪 Pengenceran", "📁 Riwayat", "📊 Tabel Periodik"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Politeknik AKA Bogor")
st.sidebar.caption("Program Studi Pengolahan Limbah Industri")
st.sidebar.caption("© 2026 | Versi 2.0")

# ==================== SESSION STATE ====================
if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

def tambah_riwayat(data):
    st.session_state.riwayat.insert(0, data)
    if len(st.session_state.riwayat) > 20:
        st.session_state.riwayat.pop()

# ==================== UNSUR ====================
unsur = {
    "H": {"nomor": 1, "massa": 1.008}, "He": {"nomor": 2, "massa": 4.0026},
    "Li": {"nomor": 3, "massa": 6.94}, "Be": {"nomor": 4, "massa": 9.012},
    "B": {"nomor": 5, "massa": 10.81}, "C": {"nomor": 6, "massa": 12.011},
    "N": {"nomor": 7, "massa": 14.007}, "O": {"nomor": 8, "massa": 15.999},
    "F": {"nomor": 9, "massa": 18.998}, "Ne": {"nomor": 10, "massa": 20.18},
    "Na": {"nomor": 11, "massa": 22.99}, "Mg": {"nomor": 12, "massa": 24.305},
    "Al": {"nomor": 13, "massa": 26.982}, "Si": {"nomor": 14, "massa": 28.085},
    "P": {"nomor": 15, "massa": 30.974}, "S": {"nomor": 16, "massa": 32.06},
    "Cl": {"nomor": 17, "massa": 35.45}, "Ar": {"nomor": 18, "massa": 39.948},
    "K": {"nomor": 19, "massa": 39.098}, "Ca": {"nomor": 20, "massa": 40.078},
    "Sc": {"nomor": 21, "massa": 44.956}, "Ti": {"nomor": 22, "massa": 47.867},
    "V": {"nomor": 23, "massa": 50.942}, "Cr": {"nomor": 24, "massa": 51.996},
    "Mn": {"nomor": 25, "massa": 54.938}, "Fe": {"nomor": 26, "massa": 55.845},
    "Co": {"nomor": 27, "massa": 58.933}, "Ni": {"nomor": 28, "massa": 58.693},
    "Cu": {"nomor": 29, "massa": 63.546}, "Zn": {"nomor": 30, "massa": 65.38},
    "Ga": {"nomor": 31, "massa": 69.723}, "Ge": {"nomor": 32, "massa": 72.63},
    "As": {"nomor": 33, "massa": 74.922}, "Se": {"nomor": 34, "massa": 78.971},
    "Br": {"nomor": 35, "massa": 79.904}, "Kr": {"nomor": 36, "massa": 83.798},
    "Rb": {"nomor": 37, "massa": 85.468}, "Sr": {"nomor": 38, "massa": 87.62},
    "Y": {"nomor": 39, "massa": 88.906}, "Zr": {"nomor": 40, "massa": 91.224},
    "Nb": {"nomor": 41, "massa": 92.906}, "Mo": {"nomor": 42, "massa": 95.95},
    "Tc": {"nomor": 43, "massa": 98}, "Ru": {"nomor": 44, "massa": 101.07},
    "Rh": {"nomor": 45, "massa": 102.91}, "Pd": {"nomor": 46, "massa": 106.42},
    "Ag": {"nomor": 47, "massa": 107.87}, "Cd": {"nomor": 48, "massa": 112.41},
    "In": {"nomor": 49, "massa": 114.82}, "Sn": {"nomor": 50, "massa": 118.71},
    "Sb": {"nomor": 51, "massa": 121.76}, "Te": {"nomor": 52, "massa": 127.6},
    "I": {"nomor": 53, "massa": 126.9}, "Xe": {"nomor": 54, "massa": 131.29},
    "Cs": {"nomor": 55, "massa": 132.91}, "Ba": {"nomor": 56, "massa": 137.33},
    "La": {"nomor": 57, "massa": 138.91}, "Ce": {"nomor": 58, "massa": 140.12},
    "Pr": {"nomor": 59, "massa": 140.91}, "Nd": {"nomor": 60, "massa": 144.24},
    "Pm": {"nomor": 61, "massa": 145}, "Sm": {"nomor": 62, "massa": 150.36},
    "Eu": {"nomor": 63, "massa": 151.96}, "Gd": {"nomor": 64, "massa": 157.25},
    "Tb": {"nomor": 65, "massa": 158.93}, "Dy": {"nomor": 66, "massa": 162.5},
    "Ho": {"nomor": 67, "massa": 164.93}, "Er": {"nomor": 68, "massa": 167.26},
    "Tm": {"nomor": 69, "massa": 168.93}, "Yb": {"nomor": 70, "massa": 173.05},
    "Lu": {"nomor": 71, "massa": 174.97}, "Hf": {"nomor": 72, "massa": 178.49},
    "Ta": {"nomor": 73, "massa": 180.95}, "W": {"nomor": 74, "massa": 183.84},
    "Re": {"nomor": 75, "massa": 186.21}, "Os": {"nomor": 76, "massa": 190.23},
    "Ir": {"nomor": 77, "massa": 192.22}, "Pt": {"nomor": 78, "massa": 195.08},
    "Au": {"nomor": 79, "massa": 196.97}, "Hg": {"nomor": 80, "massa": 200.59},
    "Tl": {"nomor": 81, "massa": 204.38}, "Pb": {"nomor": 82, "massa": 207.2},
    "Bi": {"nomor": 83, "massa": 208.98}, "Po": {"nomor": 84, "massa": 209},
    "At": {"nomor": 85, "massa": 210}, "Rn": {"nomor": 86, "massa": 222},
    "Fr": {"nomor": 87, "massa": 223}, "Ra": {"nomor": 88, "massa": 226},
    "Ac": {"nomor": 89, "massa": 227}, "Th": {"nomor": 90, "massa": 232.04},
    "Pa": {"nomor": 91, "massa": 231.04}, "U": {"nomor": 92, "massa": 238.03},
    "Np": {"nomor": 93, "massa": 237}, "Pu": {"nomor": 94, "massa": 244},
    "Am": {"nomor": 95, "massa": 243}, "Cm": {"nomor": 96, "massa": 247},
    "Bk": {"nomor": 97, "massa": 247}, "Cf": {"nomor": 98, "massa": 251},
    "Es": {"nomor": 99, "massa": 252}, "Fm": {"nomor": 100, "massa": 257},
    "Md": {"nomor": 101, "massa": 258}, "No": {"nomor": 102, "massa": 259},
    "Lr": {"nomor": 103, "massa": 266}, "Rf": {"nomor": 104, "massa": 267},
    "Db": {"nomor": 105, "massa": 268}, "Sg": {"nomor": 106, "massa": 269},
    "Bh": {"nomor": 107, "massa": 270}, "Hs": {"nomor": 108, "massa": 277},
    "Mt": {"nomor": 109, "massa": 278}, "Ds": {"nomor": 110, "massa": 281},
    "Rg": {"nomor": 111, "massa": 282}, "Cn": {"nomor": 112, "massa": 285},
    "Nh": {"nomor": 113, "massa": 286}, "Fl": {"nomor": 114, "massa": 289},
    "Mc": {"nomor": 115, "massa": 290}, "Lv": {"nomor": 116, "massa": 293},
    "Ts": {"nomor": 117, "massa": 294}, "Og": {"nomor": 118, "massa": 294}
}

# ==================== MENU PEMBUATAN LARUTAN ====================
if menu == "💧 Pembuatan Larutan":
    st.subheader("💧 Pembuatan Larutan")
    col1, col2 = st.columns(2)
    with col1:
        mr = st.number_input("Massa Molar (Mr) g/mol", min_value=0.0, step=0.1, format="%.4f")
        volume = st.number_input("Volume Larutan (mL)", min_value=0.0, step=10.0)
    with col2:
        molaritas = st.number_input("Konsentrasi (M)", min_value=0.0, step=0.1)
    if st.button("🔬 Hitung Massa Zat", type="primary"):
        if mr > 0 and volume > 0 and molaritas > 0:
            massa = molaritas * (volume / 1000) * mr
            hasil = f"Massa yang dibutuhkan: **{massa:.4f} gram**"
            st.success(hasil)
            tambah_riwayat(f"Larutan → {hasil}")

# ==================== MENU PENGENCERAN ====================
elif menu == "🧪 Pengenceran":
    st.subheader("🧪 Pengenceran Larutan")
    tab1, tab2 = st.tabs(["📏 Hitung V₂ (Volume Akhir)", "📐 Hitung V₁ (Volume Awal)"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            m1 = st.number_input("M₁ (Molaritas Awal)", min_value=0.0, step=0.1, key="m1")
            v1 = st.number_input("V₁ (Volume Awal) mL", min_value=0.0, step=10.0, key="v1")
        with col2:
            m2 = st.number_input("M₂ (Molaritas Akhir)", min_value=0.0, step=0.1, key="m2")
        if st.button("Hitung V₂", key="btn_v2", type="primary"):
            if m1 > 0 and v1 > 0 and m2 > 0:
                v2 = (m1 * v1) / m2
                hasil = f"Volume Akhir (V₂) = **{v2:.2f} mL**"
                st.success(hasil)
                tambah_riwayat(f"Pengenceran → {hasil}")
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            m1a = st.number_input("M₁ (Molaritas Awal)", min_value=0.0, step=0.1, key="m1a")
            m2a = st.number_input("M₂ (Molaritas Akhir)", min_value=0.0, step=0.1, key="m2a")
        with col2:
            v2a = st.number_input("V₂ (Volume Akhir) mL", min_value=0.0, step=10.0, key="v2a")
        if st.button("Hitung V₁", key="btn_v1", type="primary"):
            if m1a > 0 and m2a > 0 and v2a > 0:
                v1a = (m2a * v2a) / m1a
                hasil = f"Volume Awal (V₁) = **{v1a:.2f} mL**"
                st.success(hasil)
                tambah_riwayat(f"Pengenceran → {hasil}")

# ==================== MENU RIWAYAT ====================
elif menu == "📁 Riwayat":
    st.subheader("📁 Riwayat Perhitungan")
    if len(st.session_state.riwayat) == 0:
        st.info("Belum ada riwayat perhitungan.")
    else:
        for i, item in enumerate(st.session_state.riwayat):
            st.markdown(f"{i+1}. {item}")
    if st.button("🗑️ Hapus Semua Riwayat", type="secondary"):
        st.session_state.riwayat = []
        st.rerun()

# ==================== MENU TABEL PERIODIK (DIPERBAIKI) ====================
elif menu == "📊 Tabel Periodik":
    st.subheader("📊 Tabel Periodik Unsur")
    st.markdown("Klik unsur untuk melihat detail nomor atom dan massa atom.")
    
    cari = st.text_input("🔍 Cari unsur (simbol)", placeholder="Contoh: H, He, Na, Cl")
    
    # PERBAIKAN: case insensitive dan ignore spasi
    cari_bersih = cari.strip().capitalize() if cari else ""
    
    cols = st.columns(6)
    col_idx = 0
    
    for simbol, data in unsur.items():
        # Jika ada kata kunci, cek apakah simbol mengandung kata kunci (case insensitive)
        if cari_bersih:
            if cari_bersih.lower() not in simbol.lower():
                continue
        
        with cols[col_idx % 6]:
            with st.popover(f"🔬 {simbol}"):
                st.markdown(f"### {simbol}")
                st.markdown(f"**Nomor Atom:** {data['nomor']}")
                st.markdown(f"**Massa Atom:** {data['massa']} g/mol")
        col_idx += 1
    
    if col_idx == 0 and cari_bersih:
        st.warning(f"Tidak ditemukan unsur dengan kata kunci '{cari}'")

# ==================== FOOTER ====================
st.markdown("""
    <div class="custom-footer">
        Politeknik AKA Bogor | Program Studi Pengolahan Limbah Industri
    </div>
""", unsafe_allow_html=True)
