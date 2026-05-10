import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NASA RNA-seq Dashboard",
    layout="wide"
)

st.title("🚀 NASA RNA-seq Bioinformatics Dashboard")
st.markdown("Differential expression analysis of NASA GeneLab RNA-seq samples")

# =========================
# Metrics
# =========================

col1, col2, col3 = st.columns(3)

col1.metric("Samples", 12)
col2.metric("Upregulated Genes", 135)
col3.metric("Downregulated Genes", 670)

st.divider()

# =========================
# PCA
# =========================

st.header("🧬 PCA Analysis")

st.image(
    "figures/pca_plot.png",
    caption="Principal Component Analysis of RNA-seq samples",
    use_container_width=True
)

st.markdown("""
Principal Component Analysis (PCA) shows clustering of transcriptomic profiles
between experimental groups.
""")

# =========================
# Volcano Plot
# =========================

st.header("🌋 Differential Expression Volcano Plot")

st.image(
    "figures/volcano_plot_colored.png",
    caption="Differentially expressed genes",
    use_container_width=True
)

st.markdown("""
- 🔴 Red points = Upregulated genes  
- 🔵 Blue points = Downregulated genes  
- ⚪ Gray points = Not significant
""")

# =========================
# Heatmap
# =========================

st.header("🔥 Heatmap of Top Differentially Expressed Genes")

st.image(
    "figures/heatmap_top_genes.png",
    caption="Expression patterns across samples",
    use_container_width=True
)

# =========================
# Table
# =========================

st.header("📊 Top Differentially Expressed Genes")

top_genes = pd.read_csv("top_genes.csv")

st.dataframe(top_genes.head(20))

# =========================
# Footer
# =========================

st.divider()

st.markdown("""
### 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Docker

### 📡 Bioinformatics Workflow

RNA-seq → normalization → PCA → differential expression → volcano plot → heatmap
""")