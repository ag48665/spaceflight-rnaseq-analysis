# NASA Spaceflight RNA-seq Analysis

## Overview

RNA-seq differential expression analysis of NASA GeneLab spaceflight samples.

This project explores transcriptomic changes associated with spaceflight conditions using exploratory bioinformatics workflows and cloud-deployed visualization tools.

---

## Features

- RNA-seq preprocessing
- Principal Component Analysis (PCA)
- Differential expression analysis
- Volcano plot visualization
- Heatmap visualization
- Interactive Streamlit dashboard
- Dockerized reproducible workflow
- Cloud deployment

---

## Dataset

NASA GeneLab OSD-401 RNA-seq dataset.

Source:
https://osdr.nasa.gov/bio/repo/data/studies/OSD-401

---

## Workflow

Raw RNA-seq counts  
↓  
Log transformation  
↓  
PCA analysis  
↓  
Differential expression analysis  
↓  
Volcano plot generation  
↓  
Heatmap visualization  
↓  
Interactive dashboard deployment

---

## Results

### PCA Analysis

![PCA](figures/pca_plot.png)

PCA analysis revealed transcriptomic variability between experimental sample groups.

---

### Volcano Plot

![Volcano](figures/volcano_plot_colored.png)

Differential expression analysis identified significantly upregulated and downregulated genes.

---

### Heatmap

![Heatmap](figures/heatmap_top_genes.png)

Heatmap visualization demonstrates expression patterns of top differentially expressed genes.

---

## Technologies

- Python
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Docker
- Git/GitHub
- Jupyter Notebook

---

## Run with Docker

```bash
docker build -t nasa-rnaseq-analysis .
docker run -p 8888:8888 nasa-rnaseq-analysis
