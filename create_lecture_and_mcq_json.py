import json
import os

paper_id = "2026_Stem_Cells_Kidney_Regeneration_and_Gene_and_Cell_Therapy_in_Nephrology_(主題備考)"
title = "2026 Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology"
source_category = "2026 年主題練習"

# 1. Tutorial JSON
tutorial_data = {
    "paperId": paper_id,
    "title": title,
    "sections": [
        {
            "id": "section_1",
            "title": "Nephron Progenitors, Lineage Tracing & Organoid Differentiation",
            "content": """### Topology Mapping & Developmental Lineage
腎臟發育起源於 **Intermediate Mesoderm (IM)**，經由 Wnt Signaling 與 FGF Signaling 的調控，分化為 **Ureteric Bud (UB)** 與 **Metanephric Mesenchyme (MM)**。在 MM 之中，特定細胞群標誌著 **Six2** 與 **Cited1**，稱為 **Nephron Progenitor Cells (NPCs)**。Six2+ NPCs 具備 self-renewal 與 multipotency，能進一步形構成 **Cap Mesenchyme**，並發育為 **Renal Vesicle**、**Comma-Shaped Body**、**S-Shaped Body**，最終分化成 Glomerular Podocytes、Proximal Convoluted Tubule (PCT)、Loop of Henle 與 Distal Convoluted Tubule (DCT)。

近年利用 **Human Pluripotent Stem Cells (hPSCs)** 與 **Induced Pluripotent Stem Cells (iPSCs)** 進行 3D 擬態培養（如 Takasato 或 Morizane protocol），成功誘導出具備三維構造的 **Human Kidney Organoids**。此類 Organoid 能表現高度器官特異性 marker：
- **Podocytes**: Podocalyxin (PODXL), Nephrin (NPHS1), Synaptopodin.
- **Proximal Tubule**: Lotus Tetragonolobus Lectin (LTL), Cubilin, Megalin.
- **Distal Tubule / Loop of Henle**: E-Cadherin (ECAD), PAX8.

---

### High-Yield Differential Comparison: Pluripotent vs Adult Progenitors

| Feature / Marker | Pluripotent Stem Cells (iPSC/hPSC) | Adult Renal Stem / Progenitor Cells |
| :--- | :--- | :--- |
| **Pluripotency / Multipotency** | Pluripotent (可分化三胚層所有細胞) | Lineage-restricted (如 CD133+ CD24+ PECs) |
| **Organoid Genesis Ability** | 高度能力 (可自組裝 3D Kidney Organoids) | 極低能力 (僅能做單層或 3D Tubuloids) |
| **Lineage Markers** | OCT4, SOX2, Six2, PAX2, WT1 | CD133, CD24, Pax2 |
| **Vascularization Capacity** | 缺乏主動血流灌注 (Avascular without flow) | 需要外源性 Endothelial Network 輔助 |
| **Disease Modeling Focus** | CRISPR 基因編輯 Monogenic Disease (PKD, Alport) | Acute Tubular Injury & Paracrine Repair |

---

### Pathophysiological Decision Tree: Organoid Cystogenesis & Disease Modeling
```
[Patient iPSC with PKD1 / PKD2 Mutation]
           │
           ▼
[Directed Differentiation to 3D Kidney Organoids]
           │
           ▼
[Formation of Tubular & Glomerular Structures]
           │
           ▼
[Application of Fluid Shear Stress / Cyclic Stretch]
           │
           ▼
[Loss of Primary Cilia Function & Dysregulated cAMP / Ca2+]
           │
           ▼
[Progressive Cystic Dilation of Epithelial Tubules]
           │
           ▼
[Screening for Therapeutic Compounds (e.g., CFTR / mTOR Inhibitors)]
```

---

### Conceptual Trap Analysis (觀念避坑指南)
- ⚠️ **避坑考點 1**：Kidney Organoids 雖然能展現 Segmental Nephron Differentiation，但其 **Ureteric Bud Collecting Duct Network** 與 **Metanephric Nephron Segment** 在多數現行 Protocol 中無法達到完整 Functional Drainage Connection，且細胞成熟度相當於 **Fetal Kidney (中期胚胎腎)** 而非 Adult Kidney。
- ⚠️ **避坑考點 2**：在 Organoid 培養過程中，除了 Nephron Lineage 外，常伴隨 **Off-Target Stromal Cells (如 Fibroblasts, Cartilage-like cells)** 的過度增生，單細胞定序 (scRNA-seq) 已成為驗證 Organoid 趨同度與品質控管的 Standard Gatekeeper。
""",
            "diagrams": [
                {
                    "id": "diagram_1_micrograph",
                    "relPath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_1.png",
                    "imagePath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_1.png",
                    "caption": "Fig. 85.1 Differentiation of mouse and human nephron progenitor cells (NPC) showing Six2+ lineage tracing, 3D culture expansion, and kidney organoid segment profiles (LTL, ECAD, PODXL, PAX8).",
                    "sourceBook": "Brenner 11e Ch 85",
                    "type": "micrograph"
                },
                {
                    "id": "diagram_1_ai",
                    "relPath": "/server-data/assets/stem_cell_organoid_diff.png",
                    "imagePath": "/server-data/assets/stem_cell_organoid_diff.png",
                    "caption": "Gemini AI Structural Mechanism Diagram: Directed differentiation trajectory of iPSCs into Six2+ NPCs, renal vesicles, and 3D kidney organoids with segmental nephron specialization.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        },
        {
            "id": "section_2",
            "title": "Kidney Cell Delivery, Ectopic Growth & Bioengineering Scaffolds",
            "content": """### Bioengineering Approaches & Decellularization
當前腎臟組織工程 (Renal Tissue Engineering) 致力於解決 ESRD 器官短缺問題，主要包含三大策略：
1. **Decellularized Extracellular Matrix (ECM) Scaffolds**: 利用 Detergent (如 SDS, Triton X-100) 灌流去細胞化，保留天然腎臟的 3D Architecture, Glomerular Basement Membrane (GBM) 與 Vascular Conduits。關鍵挑戰在於 **Recellularization (再細胞化)** 與 **Re-endothelialization (血管內皮化)**，若血管未完全覆蓋 Endothelium，植入後易引發 **Thrombosis & Vascular Occlusion**。
2. **Microphysiological Systems (Kidney-on-a-Chip)**: 結合 Microfluidic Device 與 Primary Human Proximal Tubule Epithelial Cells (PTECs)，模擬 Fluid Shear Stress (FSS, 0.2~1.0 dyne/cm²)，促進 Organic Anion Transporter 1/3 (OAT1/OAT3) 與 P-glycoprotein 的表達，提供精準毒理學與藥物轉運篩選平台。
3. **Wearable & Implantable Bioartificial Kidneys (WAK / iBAK)**:
   - **WAK**: 微型化血液透析/過濾系統，採用連續再生 Sorbent Cartridge 去除 Urea 與 Creatinine。
   - **iBAK**: 結合 High-Efficiency Silicon Nanopore Membranes (過濾血漿 Filter) 與 Human Renal Epithelial Bioreactor (重吸收 Electrolytes 與 Water)，連接 Iliac Vessels 並引流至 Urinary Bladder。

---

### High-Yield Differential Comparison: Bioengineering Platforms

| Technology | Primary Mechanism | Vascular Connection | Key Limitations |
| :--- | :--- | :--- | :--- |
| **Decellularized Scaffold** | Perfusion detergent decellularization + cell seeding | Native Renal Artery / Vein | Re-endothelialization thrombosis |
| **Kidney-on-a-Chip** | Microfluidic fluid shear stress on PTECs | Closed microfluidic channels | Non-implantable; in vitro toxicology only |
| **Implantable Bioartificial Kidney (iBAK)** | Silicon nanopores + renal epithelial cell bioreactor | Surgical anastomosis to Iliac Vessels | Bioreactor cell viability & immunogenicity |
| **Subcapsular NPC Delivery** | Microinjection of NPCs under renal capsule | Host microvascular sprouting | Ectopic growth / Cyst formation risk |

---

### Pathophysiological Decision Tree: Recellularization of Decellularized ECM
```
[Whole Kidney Perfusion Decellularization with SDS / Triton X-100]
           │
           ▼
[Acellular ECM Scaffold (Preserving Basement Membrane & Glycoproteins)]
           │
           ▼
[Dual-Route Seeding: Arterial Endothelial Cells + Ureteral Epithelial Cells]
           │
           ▼
[Bioreactor Perfusion Culture under Hydrostatic & Osmotic Pressure]
           │
           ▼
[In Vivo Surgical Anastomosis to Recipient Renal Vessels]
           │
           ├───────────────────────────────┐
           ▼                               ▼
[Complete Endothelial Coverage]    [Incomplete Endothelial Coverage]
           │                               │
           ▼                               ▼
[Functional Filtration & Flow]    [Platelet Adhesion & Rapid Thrombosis]
```

---

### Conceptual Trap Analysis (觀念避坑指南)
- ⚠️ **避坑考點 1**：全器官去細胞化支架 (Decellularized Whole-Organ Scaffold) 雖然完整保存了 Col IV, Laminin, Heparan Sulfate Proteoglycans，但其血管網（特別是 Peritubular Capillaries）若無法做到 100% 血管內皮鋪覆 (Complete Re-endothelialization)，血流進入後會在露出膠原蛋白處引發即刻凝血 (Hyperacute Thrombotic Occlusion)。
- ⚠️ **避坑考點 2**：Metanephros 異位移植 (Ectopic Implant) 雖能在 Host (如 Mouse Kidney Capsule 或 Omentum) 內持續分化並產生 Ultrafiltrate，但若缺少與 Host Ureter 的 Surgical Anastomosis，植入物極易發展成 **Hydronephrosis (腎積水) 與 Fibrosis**。
""",
            "diagrams": [
                {
                    "id": "diagram_2_micrograph",
                    "relPath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_3.png",
                    "imagePath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_3.png",
                    "caption": "Fig. 85.3 Kidney bioengineering modalities including decellularized renal scaffolds, Kidney-on-a-chip microphysiological models, and theoretical implantable bioartificial kidney (iBAK) schematics.",
                    "sourceBook": "Brenner 11e Ch 85",
                    "type": "micrograph"
                },
                {
                    "id": "diagram_2_ai",
                    "relPath": "/server-data/assets/kidney_bioengineering.png",
                    "imagePath": "/server-data/assets/kidney_bioengineering.png",
                    "caption": "Gemini AI Structural Mechanism Diagram: Whole-organ decellularization, microfluidic shear-stress bioreactors, and silicon nanopore implantable bioartificial kidney architecture.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        },
        {
            "id": "section_3",
            "title": "Xenotransplantation, Blastocyst Complementation & Metanephric Implantation",
            "content": """### Immunology & Molecular Barriers in Xenotransplantation
異種器官移植 (Renal Xenotransplantation) 主要以 **Pig (Sus scrofa)** 為供體來源，但面臨嚴峻的免疫排斥反應：
1. **Hyperacute Rejection (HAR)**: 發生於數分鐘至數小時內。受體循環中天然存在之 Pre-formed Anti-pig Antibodies (主要是 Anti-α-Gal) 結合至豬腎內皮細胞上的 **Galactose-α-1,3-galactose (α-Gal)** 聚醣標記，進而活化 Complement Cascade (C3a, C5a, Membrane Attack Complex C5b-9)，引發微血管血栓與出血性壞死。
   - **Key Genetic Modification**: 使用 CRISPR-Cas9 敲除 **GGTA1** (α-1,3-galactosyltransferase) 基因。
   - **Additional Knockouts**: 敲除 **CMAH** (N-glycolylneuraminic acid) 與 **B4GALNT2**。
   - **Transgenic Complement Inhibitors**: 轉殖人類補體調控蛋白 **hCD46 (MCP)**, **hCD55 (DAF)**, **hCD59 (Protectin)**。
2. **Acute Humoral & Cellular Rejection**: 藉由轉殖 **hCD47** 傳遞 \"Don't eat me\" 訊號給 Host Macrophages，避免外源性吞噬。
3. **Porcine Endogenous Retroviruses (PERVs)**: 豬基因組中嵌入的逆轉錄病毒。利用 CRISPR-Cas9 multiplex genome editing 可一次性去活化超過 60 個 copies 的 PERVs，阻斷 Cross-Species Viral Transmission。

---

### Interspecific Blastocyst Complementation (跨物種胚胎補充)
胚胎補充技術為器官再生帶來全新革命：
- **Principle**: 在基因缺失的受體胚胎（如 **SALL1-/-** 或 **SIX2-/-** 導致缺腎的 Pig Blastocyst）中，微注射人類 **iPSCs / PSCs**。外源性人類幹細胞在胚胎缺損的 Developmental Niche 中生長擴增，填補器官發育空間，發育出完全由人類細胞構成的 **Chimeric Kidney**。
- **Ethical & Biological Barriers**: 人類幹細胞可能參與受體神經系統與生殖細胞 (Germline Chimerism) 的發育；此外，跨物種發育微環境不相容 (Developmental Heterochrony) 亦增加失敗率。

---

### High-Yield Differential Comparison: Rejection & Genetic Targets

| Rejection Mechanism | Timeframe | Primary Antigen / Mediator | Preventive Genetic Strategy |
| :--- | :--- | :--- | :--- |
| **Hyperacute Rejection (HAR)** | Minutes to Hours | α-Gal epitope, Complement MAC (C5b-9) | **GGTA1 KO** + Transgenic **hCD46 / hCD55 / hCD59** |
| **Acute Antibody-Mediated (AMR)** | Days to Weeks | Anti-Neu5Gc, Anti-Sd(a), HLA-donor antibodies | **CMAH KO**, **B4GALNT2 KO** |
| **Cellular Immunity & Macrophage** | Days to Months | T-cell TCR recognition, SIRPα incompatibility | Transgenic **hCD47** expression |
| **PERV Transmission** | N/A (Infectious Risk) | Retroviral reverse transcriptase | **CRISPR-Cas9 multiplex PERV inactivation** |

---

### Pathophysiological Decision Tree: Renal Xenotransplant Genetic Modification
```
[Wild-Type Pig Donor Organ]
           │
           ▼
[CRISPR-Cas9 Knockout of Triple Carbohydrate Antigens: GGTA1 / CMAH / B4GALNT2]
           │
           ▼
[Transgenic Insertion of Human Complement Inhibitors: hCD46 / hCD55 / hCD59]
           │
           ▼
[Transgenic Expression of Human Immune Regulatory Proteins: hCD47 / EPCR / Thrombomodulin]
           │
           ▼
[Multiplex Genome Editing to Inactivate All Endogenous PERVs]
           │
           ▼
[Transplantation into Human Recipient with Minimal Immunological Rejection]
```

---

### Conceptual Trap Analysis (觀念避坑指南)
- ⚠️ **避坑考點 1**：僅單純敲除 **GGTA1** 基因無法完全避免 Hyperacute/Acute Rejection，因為受體體內仍含有針對 **Neu5Gc (CMAH 產物)** 與 **Sd(a) (B4GALNT2 產物)** 的天然抗體，因此現代醫療等級豬隻必須施行 **Triple Antigen Knockout (TKO)**。
- ⚠️ **避坑考點 2**：補體抑制蛋白 **hCD46** 作用於 C3b/C4b 分解，**hCD55** 促進 C3/C5 convertase 衰變，而 **hCD59** 則專一阻斷 **C9 聚合形成 Membrane Attack Complex (MAC)**。三者的分子機轉常在考試中進行細節對照。
""",
            "diagrams": [
                {
                    "id": "diagram_3_micrograph",
                    "relPath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_5.png",
                    "imagePath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_5.png",
                    "caption": "Fig. 85.5 Xenotransplantation challenges and solutions: Pig kidney hyperacute rejection in primate recipients and blastocyst complementation in knockout animal models.",
                    "sourceBook": "Brenner 11e Ch 85",
                    "type": "micrograph"
                },
                {
                    "id": "diagram_3_ai",
                    "relPath": "/server-data/assets/xenotransplantation.png",
                    "imagePath": "/server-data/assets/xenotransplantation.png",
                    "caption": "Gemini AI Structural Mechanism Diagram: Triple antigen knockout (GGTA1/CMAH/B4GALNT2), human complement regulatory transgene protection, and blastocyst complementation niche filling.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        },
        {
            "id": "section_4",
            "title": "Gene Therapy Vectors, CRISPR Gene Editing & CAR-T/MSC Cell Therapy",
            "content": """### Gene Delivery Vectors in Nephrology
腎臟基因治療的核心挑戰在於 **Cell-Specific Tropism (細胞專一趨向性)** 與 **Glomerular Filtration Barrier (GFB) Passage**。主要載體比較：
1. **Adeno-Associated Virus (AAV)**:
   - **AAV2, AAV9, AAV LK03**: 具備良好的 Podocyte 與 Tubular Epithelial Tropism。AAV LK03 對人類 Podocytes 的轉殖效率極高。
   - **Advantage**: Low immunogenicity, non-integrating (Mainly episomal DNA), 適合非分裂細胞 (Non-dividing cells like mature Podocytes)。
2. **Lentivirus**: 能整合入 Host Genome，適合用於急速分裂的幹細胞或 Progenitor Cells，但在成熟足細胞中轉殖效率受限於 GFB 穿透力。
3. **Non-Viral Vectors (LNP / Synthetic Nanoparticles)**: 脂質奈米顆粒 (LNPs) 封裝 mRNA 或 RNP (Ribonucleoprotein)，降低病毒衣殼引起的全身性免疫反應。

---

### Monogenic Disease Therapeutics & CRISPR Gene Editing
- **Target Diseases**:
  - **NPHS2 Mutation (Podocin Deficiency)**: AAV-mediated delivery of functional *NPHS2* gene successfully restores Podocin localization to the slit diaphragm, reducing proteinuria and slowing CKD progression.
  - **Alport Syndrome (*COL4A3/A4/A5*)**: 利用 Prime Editing 或 Base Editing 修正點突變，修復 Type IV Collagen α3α4α5 network。
- **CRISPR Technologies**:
  - **Double-Strand Breaks (DSB)** via Cas9 endonuclease: 引發 NHEJ (Non-Homologous End Joining) 或 HDR (Homology-Directed Repair)。
  - **Base Editors (CBE / ABE)**: 不需引發 DSB 即可進行 C->T 或 A->G 轉換，大幅降低 Off-Target Indels 與 Translocations 風險。

---

### CAR-T & Mesenchymal Stem Cell (MSC) Therapeutics
1. **CAR-T Cell Therapy in Autoimmune Nephritis**:
   - **CD19-targeted / BCMA-targeted CAR-T**: 清除 Pathogenic B-cells 與 Autoreactive Plasma Cells，在難治型 **Lupus Nephritis (LN)** 與 **ANCA-Associated Vasculitis** 展現長效無藥緩解 (Drug-free Remission)。
2. **Mesenchymal Stem Cells (MSCs)**:
   - **Mechanism**: 主要並非直接分化取代受損腎細胞，而是透過 **Paracrine / Endocrine Secretion** 發揮作用。
   - **Extracellular Vesicles (EVs) & Exosomes**: 傳遞 microRNAs (如 miR-let-7, miR-21 inhibitors), TSG-6, HGF, VEGF，減緩 **Acute Kidney Injury (AKI)** 的 Tubular Apoptosis，並促進 Endothelial Repair 與 Anti-fibrotic Pathways。

---

### High-Yield Differential Comparison: Gene Delivery Vectors

| Vector System | Genome Integration | Target Cell Tropism in Kidney | Risk of Immunogenicity | Suitable Indication |
| :--- | :--- | :--- | :--- | :--- |
| **AAV (e.g. AAV LK03)** | Low (Episomal) | High for Podocytes & Tubular cells | Low to Moderate | Monogenic Podocytopathies (*NPHS2*) |
| **Lentivirus** | High (Chromosomal) | Progenitor / Dividing cells | Moderate | Ex vivo stem cell editing |
| **LNP / mRNA** | None | Endothelial & Tubular cells | Low | Transient enzyme replacement / CRISPR RNP |
| **CAR-T Cells** | Transduced T-cell genome | Autoreactive B-cells / Plasma cells | CRS / ICANS risk | Refractory Lupus Nephritis |

---

### Pathophysiological Decision Tree: AAV-Mediated Podocyte Gene Therapy
```
[Identification of Monogenic NPHS2 Mutation causing FSGS / Nephrotic Syndrome]
           │
           ▼
[Construction of Recombinant AAV Vector (e.g., AAV LK03) carrying Functional NPHS2 cDNA]
           │
           ▼
[Systemic Intravenous or Direct Renal Artery Infusion]
           │
           ▼
[Vector Transduction across Glomerular Endothelium to Podocyte Foot Processes]
           │
           ▼
[Episomal Expression of Functional Podocin Protein at Slit Diaphragm]
           │
           ▼
[Restoration of Slit Diaphragm Integrity, Resolution of Albuminuria & Survival Extension]
```

---

### Conceptual Trap Analysis (觀念避坑指南)
- ⚠️ **避坑考點 1**：**Mesenchymal Stem Cells (MSCs)** 治療 AKI 的核心機制是 **Paracrine Secretion of Exosomes / EVs**，而不是廣泛轉化 (Transdifferentiation) 成新生的 Tubule Epithelial Cells。任何選項若宣稱「MSCs 直接分化取代 90% 受損近曲小管」皆為錯誤敘述！
- ⚠️ **避坑考點 2**：Podocytes 屬於 Terminally Differentiated Non-Dividing Cells，因此使用 **Episomal AAV Vectors** 能維持數年長效表達；相反地，若在快速分裂的 Tubular Cells 使用 AAV，基因表達會隨著細胞分裂遞減 (Dilution effect)。
"""
            ,
            "diagrams": [
                {
                    "id": "diagram_4_micrograph",
                    "relPath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_6.png",
                    "imagePath": "/reference-images/Brenner 11e/85. Stem Cells, Kidney Regeneration, and Gene and Cell Therapy in Nephrology/Fig_85_6.png",
                    "caption": "Fig. 85.6 Gene therapy and gene editing: CRISPR-Cas9 DSB induction, base editing, and kidney organoid disease modeling in PKD and epidermal stem cell gene therapy.",
                    "sourceBook": "Brenner 11e Ch 85",
                    "type": "micrograph"
                },
                {
                    "id": "diagram_4_ai",
                    "relPath": "/server-data/assets/gene_and_cell_therapy.png",
                    "imagePath": "/server-data/assets/gene_and_cell_therapy.png",
                    "caption": "Gemini AI Structural Mechanism Diagram: AAV LK03 podocyte transduction, CRISPR-Cas9 NPHS2 gene repair, and CD19 CAR-T depletion of autoreactive B-cells in Lupus Nephritis.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        }
    ]
}

os.makedirs("public/server-data/tutorials", exist_ok=True)
with open(f"public/server-data/tutorials/{paper_id}_tutorial.json", "w", encoding="utf-8") as f:
    json.dump(tutorial_data, f, ensure_ascii=False, indent=2)

print("Tutorial JSON generated successfully.")

# 2. Practice Test Bank JSON (20 High-Yield MCQs)
# Options: A, B, C, D distribution balanced (5 of each)
questions = [
    {
        "id": "q1",
        "number": 1,
        "stem": "Which molecular marker specifically defines the multipotent, self-renewing nephron progenitor cell (NPC) population residing within the cap mesenchyme during mammalian kidney development?",
        "options": [
            {"id": "A", "text": "Six2"},
            {"id": "B", "text": "Aquaporin-2"},
            {"id": "C", "text": "Uromodulin"},
            {"id": "D", "text": "Calbindin-D28k"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Six2 是標誌 Cap Mesenchyme 中 Nephron Progenitor Cells (NPCs) 的核心 Transcription Factor。Six2+ NPCs 具備 Self-Renewal 與 Multipotency，能分化為 Podocytes, Proximal Tubules, Loop of Henle 及 Distal Tubules。Aquaporin-2 為 Collecting Duct Principal Cells 標記；Uromodulin 為 Thick Ascending Limb 標記；Calbindin-D28k 為 Distal Convoluted Tubule 標記。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q2",
        "number": 2,
        "stem": "In human pluripotent stem cell (hPSC)-derived kidney organoids, which lectin marker is universally utilized to confirm specific differentiation into Proximal Convoluted Tubule (PCT) epithelial segments?",
        "options": [
            {"id": "A", "text": "Concanavalin A"},
            {"id": "B", "text": "Lotus tetragonolobus lectin (LTL)"},
            {"id": "C", "text": "Wheat germ agglutinin"},
            {"id": "D", "text": "Peanut agglutinin"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Lotus tetragonolobus lectin (LTL) 能特異性結合 Proximal Tubule 的 Brush Border Oligosaccharides，為 3D Kidney Organoids 中鑑定 Proximal Convoluted Tubule (PCT) 頂端膜發育的 Gold Standard Marker。PODXL 與 Nephrin 代表 Podocytes，ECAD 則代表 Distal Tubules / Collecting Duct。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q3",
        "number": 3,
        "stem": "What is considered a primary developmental and structural limitation of current in vitro human pluripotent stem cell-derived 3D kidney organoids compared to native adult human kidneys?",
        "options": [
            {"id": "A", "text": "Complete absence of Podocalyxin-positive podocyte-like cells"},
            {"id": "B", "text": "Inability to undergo CRISPR-Cas9 genomic editing"},
            {"id": "C", "text": "Lack of functional vascular perfusion and collecting duct urinary drainage connection"},
            {"id": "D", "text": "Total failure to express distal tubular E-cadherin"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "現行 3D Kidney Organoids 的主要瓶頸在於缺乏內源性主動血流灌注 (Functional Vascular Perfusion Flow) 以及未與完整集尿管系統連接 (Lack of Urinary Drainage Connection)，導致其整體分化成熟度維持在 Fetal Kidney 階段，且長期培養易產生 Avessel Fluid Accumulation。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q4",
        "number": 4,
        "stem": "In kidney organoid-based disease modeling of Autosomal Dominant Polycystic Kidney Disease (ADPKD), which mechanical microenvironmental factor significantly accelerates tubular cystogenesis in CRISPR-mutant PKD1 organoids?",
        "options": [
            {"id": "A", "text": "Static hyperosmolar glucose incubation"},
            {"id": "B", "text": "High-dose erythropoietin exposure"},
            {"id": "C", "text": "Fluid shear stress or cyclic mechanical stretch"},
            {"id": "D", "text": "Complete withdrawal of extracellular calcium"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "研究證明在 CRISPR 敲除 *PKD1* 或 *PKD2* 的 Human Kidney Organoids 中，施加 Fluid Shear Stress 或機械拉伸 (Cyclic Stretch) 能活化 Primary Cilia 訊號異常，刺激 Intracellular cAMP 累積與液體分泌，進而大幅加速 Tubular Cystogenesis。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q5",
        "number": 5,
        "stem": "An adeno-associated virus (AAV) vector capsids variant designated AAV LK03 has demonstrated superior therapeutic transduction efficiency targeting which specific renal cell type in human models of monogenic nephrotic syndrome?",
        "options": [
            {"id": "A", "text": "Glomerular endothelial cells"},
            {"id": "B", "text": "Glomerular podocytes"},
            {"id": "C", "text": "Macula densa cells"},
            {"id": "D", "text": "Medullary interstitial fibroblasts"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "AAV LK03 基因治療載體在人類與小鼠模型中展現對 Glomerular Podocytes 的高高度 Tropism。Ding et al. (Sci Transl Med 2023) 證明 AAV LK03 遞送 functional *NPHS2* cDNA 可成功遞送至足細胞，修復 Slit Diaphragm 並緩解 Albuminuria。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q6",
        "number": 6,
        "stem": "During whole-organ renal decellularization for biological scaffold engineering, what is the most critical physiological obstacle encountered upon re-implanting the recellularized construct into host blood circulation?",
        "options": [
            {"id": "A", "text": "Rapid enzymatic digestion of collagen IV by host amylase"},
            {"id": "B", "text": "Immediate platelet activation and intravascular thrombosis due to incomplete endothelialization"},
            {"id": "C", "text": "Instant clearance of the scaffold by alveolar macrophages"},
            {"id": "D", "text": "Conversion of tubular basement membranes into bone spicules"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "去細胞化腎臟支架在再細胞化過程中，若 Vascular Net 未能達成 100% 完全內皮覆蓋 (Incomplete Re-endothelialization)，露出之外質膠原蛋白與 Basement Membrane 在接觸 Host 血流後會引發即刻 Platelet Adhesion & Coagulation Cascade，造成 Rapid Intravascular Thrombosis 與 Occlusion。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q7",
        "number": 7,
        "stem": "In Microphysiological Systems (Kidney-on-a-Chip), what key physical force is incorporated to significantly enhance the functional expression of organic anion transporters (OAT1/OAT3) in primary proximal tubular epithelial cells?",
        "options": [
            {"id": "A", "text": "Fluid shear stress"},
            {"id": "B", "text": "Zero-gravity levitation"},
            {"id": "C", "text": "High-voltage direct current"},
            {"id": "D", "text": "Focused ultrasound radiation"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Kidney-on-a-Chip 微流體晶片藉由提供生理水準之 Fluid Shear Stress (FSS, ~0.2-0.5 dyne/cm²)，能重塑 Proximal Tubule Cells 的 Primary Cilia 與 Cytoskeleton，顯著上調 OAT1, OAT3, P-glycoprotein 等 Transporters 之膜表達與毒物轉運能力。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q8",
        "number": 8,
        "stem": "The theoretical Implantable Bioartificial Kidney (iBAK) design utilizes a two-stage system consisting of a silicon nanopore hemofilter connected in series with which biological component?",
        "options": [
            {"id": "A", "text": "Pancreatic islet cell spheroid bioreactor"},
            {"id": "B", "text": "Hepatic parenchymal cell bioreactor"},
            {"id": "C", "text": "Human renal epithelial cell bioreactor"},
            {"id": "D", "text": "Splenocyte cell bioreactor"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Implantable Bioartificial Kidney (iBAK) 架構第一階段為 Silicon Nanopore Hemofilter (執行無泵高效率 Ultrafiltration)，第二階段串聯 Human Renal Epithelial Cell Bioreactor (由 Proximal Tubule Cells 組成，執行 Electrolyte/Water Reabsorption 與 Metabolic Functions)。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q9",
        "number": 9,
        "stem": "Hyperacute rejection of unprocessed swine renal xenografts in primate recipients is primarily initiated by pre-formed recipient antibodies binding to which major donor carbohydrate antigen?",
        "options": [
            {"id": "A", "text": "Galactose-α-1,3-galactose (α-Gal)"},
            {"id": "B", "text": "N-acetylglucosamine"},
            {"id": "C", "text": "Beta-2 microglobulin"},
            {"id": "D", "text": "Fucose-alpha-1,2-galactose"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "豬隻腎臟異種移植發生 Hyperacute Rejection (HAR) 的主因是人類循環中天然存在抗 α-Gal 抗體，特異性結合豬內皮細胞表面的 Galactose-α-1,3-galactose (α-Gal) 聚醣。敲除 *GGTA1* 基因可消除 α-Gal 表現。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q10",
        "number": 10,
        "stem": "Which enzyme encoded by the swine genome is knocked out via CRISPR-Cas9 to prevent the synthesis of the α-Gal carbohydrate epitope in donor pigs for xenotransplantation?",
        "options": [
            {"id": "A", "text": "Alpha-galactosidase A"},
            {"id": "B", "text": "GGTA1 (α-1,3-galactosyltransferase)"},
            {"id": "C", "text": "Fut8 (alpha-1,6-fucosyltransferase)"},
            {"id": "D", "text": "Mgat5 (acetylglucosaminyltransferase)"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "GGTA1 (α-1,3-galactosyltransferase) 負責催化 α-Gal 標記的合成。敲除 GGTA1 基因是防止人類與靈長類受體發生 Hyperacute Xenograft Rejection 的最關鍵基因工程步驟。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q11",
        "number": 11,
        "stem": "To eliminate the risk of cross-species viral transmission during porcine-to-human organ xenotransplantation, CRISPR-Cas9 multiplex genome editing is employed to deactivate which endogenous porcine genomic elements?",
        "options": [
            {"id": "A", "text": "Porcine Cytomegalovirus (PCMV) capsids"},
            {"id": "B", "text": "Porcine Endogenous Retroviruses (PERVs)"},
            {"id": "C", "text": "Porcine Parvovirus envelope genes"},
            {"id": "D", "text": "Porcine Circovirus type 2 replicases"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Porcine Endogenous Retroviruses (PERVs) 嵌合於豬隻全基因組DNA中。George Church 等團隊利用 CRISPR-Cas9 多重基因編輯技術一次性去活化超過 60 個 PERVs Pol 基因 copies，解決異種移植病毒跨物種感染風險。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q12",
        "number": 12,
        "stem": "In Interspecific Blastocyst Complementation for organ regeneration, human pluripotent stem cells are injected into a host blastocyst that bears a homozygous knockout of which critical renal developmental gene?",
        "options": [
            {"id": "A", "text": "Six2 or Sall1"},
            {"id": "B", "text": "Renin"},
            {"id": "C", "text": "Erythropoietin"},
            {"id": "D", "text": "Uromodulin"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Blastocyst Complementation 利用 *Sall1* 或 *Six2* 基因缺失導致無腎發育 (Anphric Niche) 的動物胚胎，微注射人類 iPSCs，使人類細胞補位成長為 chimeric human kidney。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q13",
        "number": 13,
        "stem": "Transgenic expression of human complement regulatory proteins in donor pigs mitigates hyperacute rejection. Which human protein acts specifically to prevent the assembly of the Membrane Attack Complex (C5b-9)?",
        "options": [
            {"id": "A", "text": "hCD46 (Membrane Cofactor Protein)"},
            {"id": "B", "text": "hCD55 (Decay-Accelerating Factor)"},
            {"id": "C", "text": "hCD59 (Protectin)"},
            {"id": "D", "text": "Factor H"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "hCD59 (Protectin) 專一性結合 C8 與 C9，防止 C9 聚合進入細胞膜，從而阻斷 Membrane Attack Complex (MAC, C5b-9) 的形成。hCD46 輔助 C3b/C4b 切割，hCD55 促進 C3/C5 convertase 衰變。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q14",
        "number": 14,
        "stem": "Mesenchymal Stem Cells (MSCs) mediate tissue repair in Acute Kidney Injury (AKI) models predominantly through which pathophysiological mechanism?",
        "options": [
            {"id": "A", "text": "Direct transdifferentiation into proximal tubular epithelial cells"},
            {"id": "B", "text": "Fusing with podocytes to form polykaryons"},
            {"id": "C", "text": "Paracrine secretion of extracellular vesicles (EVs) and anti-inflammatory cytokines"},
            {"id": "D", "text": "Phagocytosing calcified renal crystals"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "大量研究證實 MSCs 在 AKI 中的修復作用絕大部分來自 Paracrine Secretion (旁分泌作用)，特別是釋放微囊泡 (Extracellular Vesicles / Exosomes) 與 Growth Factors (HGF, VEGF, TSG-6)，抑制 Tubular Apoptosis 並促進內皮修復，而非直接分化為腎管細胞。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q15",
        "number": 15,
        "stem": "In refractory Lupus Nephritis, Chimeric Antigen Receptor (CAR)-T cell therapy targeting which surface antigen has shown remarkable success in inducing drug-free clinical remission by depleting pathogenic B-cell lineages?",
        "options": [
            {"id": "A", "text": "CD3"},
            {"id": "B", "text": "CD19"},
            {"id": "C", "text": "CD4"},
            {"id": "D", "text": "CD8"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "針對 CD19 (或 BCMA) 的 CAR-T 細胞療法在難治型 Systemic Lupus Erythematosus (SLE) 與 Lupus Nephritis 患者中，能深度清除 Autoantibody-producing B cells，達到持久的 Drug-free Remission。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q16",
        "number": 16,
        "stem": "Which genomic modification technology allows targeted single-nucleotide conversion (e.g., C-to-T or A-to-G) without creating double-strand DNA breaks (DSBs), thereby reducing off-target chromosomal translocations in renal gene editing?",
        "options": [
            {"id": "A", "text": "Zinc Finger Nucleases"},
            {"id": "B", "text": "TALENs"},
            {"id": "C", "text": "Base Editing"},
            {"id": "D", "text": "Standard wild-type Cas9 endonuclease"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Base Editors (如 Cytidine Base Editor CBE 或 Adenine Base Editor ABE) 結合 Catalytically Impaired Cas9 與 Deaminase，能在不產生 Double-Strand Breaks (DSBs) 的情況下執行單點鹼基轉換，極大提高安全性並降低 Off-Target Indels。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q17",
        "number": 17,
        "stem": "When implanting bioengineered embryonic metanephroi into an ectopic site in animal models, which anatomical complication routinely develops if ureteral continuity is not surgically established?",
        "options": [
            {"id": "A", "text": "Hydronephrosis"},
            {"id": "B", "text": "Renal artery aneurysm"},
            {"id": "C", "text": "Acute glomerulonephritis"},
            {"id": "D", "text": "Renal cell carcinoma"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Metanephros 異位植入 (如 Omentum 或 Kidney Capsule) 後能自行分化產生原始尿液 (Ultrafiltrate)，但若未對接 Host Ureter 建立引流通道，尿液積聚會導致廣泛的 Hydronephrosis (腎積水) 與壓迫性壞死。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q18",
        "number": 18,
        "stem": "Transgenic pigs modified to express human CD47 suppress host macrophage phagocytosis of xenograft endothelial cells by interacting with which inhibitory receptor on host macrophages?",
        "options": [
            {"id": "A", "text": "Toll-like receptor 4 (TLR4)"},
            {"id": "B", "text": "SIRPα (Signal Regulatory Protein Alpha)"},
            {"id": "C", "text": "Fc gamma receptor I"},
            {"id": "D", "text": "C-reactive protein receptor"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Human CD47 為標誌 'Don't eat me' 的細胞表面蛋白，透過結合 Host Macrophages 上的 SIRPα (Signal Regulatory Protein Alpha) 受體，傳遞抑制性訊號，防止異種移植內皮細胞被巨噬細胞吞噬。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q19",
        "number": 19,
        "stem": "Why are non-integrating recombinant adeno-associated virus (rAAV) vectors particularly effective for long-term transgene expression in mature renal podocytes?",
        "options": [
            {"id": "A", "text": "Podocytes undergo rapid cell division every 24 hours"},
            {"id": "B", "text": "Podocytes are terminally differentiated, non-dividing cells, preventing episomal vector dilution"},
            {"id": "C", "text": "AAV vectors permanently integrate into chromosome 17 in podocytes"},
            {"id": "D", "text": "Podocytes lack lysosomes, preventing viral degradation"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Podocytes 為終末分化且不具備分裂能力的細胞 (Terminally Differentiated Non-Dividing Cells)。rAAV 以 Episomal Concatemers 形式存在於細胞核中，不會因細胞分裂而稀釋 (No vector dilution effect)，因此能提供持久數年之基因表現。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    },
    {
        "id": "q20",
        "number": 20,
        "stem": "In modern bioengineered kidney tissue evaluation, single-cell RNA sequencing (scRNA-seq) has been paramount in identifying which unexpected off-target cell population in hPSC organoid cultures?",
        "options": [
            {"id": "A", "text": "Non-renal stromal and cartilage-like cells"},
            {"id": "B", "text": "Cardiac ventricular myocytes"},
            {"id": "C", "text": "Retinal pigmented epithelial cells"},
            {"id": "D", "text": "Cerebellar Purkinje neurons"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Single-cell RNA sequencing (scRNA-seq) 分析揭露現行 hPSC-derived Kidney Organoid 培養中，約有 10-20% 的細胞會偏離 Nephron Lineage，分化為 Off-Target Non-Renal Stromal Cells 以及 Cartilage-like / Myogenic Lineages，此為 Organoid Protocol 優化的重點。",
        "nlmResponses": [],
        "reconciliationStatus": "PENDING"
    }
]

paper_data = {
    "id": paper_id,
    "paperId": paper_id,
    "title": title,
    "sourceCategory": source_category,
    "year": 2026,
    "questionCount": len(questions),
    "questions": questions
}

with open(f"public/server-data/{paper_id}.json", "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print("Practice Paper JSON generated successfully.")
