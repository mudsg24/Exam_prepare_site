import json
import os
import shutil

# Paths
PUBLIC_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public"
ASSETS_DIR = os.path.join(PUBLIC_DIR, "server-data/assets")
TUTORIALS_DIR = os.path.join(PUBLIC_DIR, "server-data/tutorials")
SERVER_DATA_DIR = os.path.join(PUBLIC_DIR, "server-data")
BRAIN_DIR = "/Users/yuan/.gemini/antigravity/brain/815ea66c-b7a3-4292-902f-8a49832464e9"

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(TUTORIALS_DIR, exist_ok=True)

# 1. Copy generated AI illustrations
images_map = {
    "ren_tx_imm_signal_1785524220542.jpg": "ren_tx_imm_signal.png",
    "ren_tx_crossmatch_1785524237147.jpg": "ren_tx_crossmatch.png",
    "ren_tx_tcmr_path_1785524252703.jpg": "ren_tx_tcmr_path.png",
    "ren_tx_abmr_c4d_1785524270183.jpg": "ren_tx_abmr_c4d.png",
    "ren_tx_diff_dx_1785524285166.jpg": "ren_tx_diff_dx.png"
}

for src_name, dst_name in images_map.items():
    src_path = os.path.join(BRAIN_DIR, src_name)
    dst_path = os.path.join(ASSETS_DIR, dst_name)
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copied {src_name} to {dst_path}")
    else:
        print(f"Warning: {src_path} not found")

# 2. Build Tutorial JSON
tutorial_data = {
    "paperId": "2026_Renal_transplant_rejection_(主題備考)",
    "title": "2026 Renal Transplant Rejection (腎臟移植排斥) 移植免疫、Banff 病理分型、TCMR/ABMR 診斷與臨床處置",
    "sourceCategory": "2026 年主題練習",
    "sections": [
        {
            "id": "sec_1",
            "title": "Section 1: Immunobiology of Allorecognition & T-Cell Activation Signals",
            "content": """### Topology Mapping Matrix

| Allorecognition Pathway | Antigen Presenting Cell (APC) | Target / MHC Interaction | Clinical Role & Timing |
| :--- | :--- | :--- | :--- |
| **Direct Pathway** | Donor APCs (Passenger Leukocytes) | Intact donor MHC I / II recognized by recipient CD8+ / CD4+ T-cells | Dominates early acute rejection (TCMR) |
| **Indirect Pathway** | Recipient APCs | Processed donor HLA peptides presented on recipient MHC II | Drives late TCMR, chronic allograft injury, and de novo DSA generation |
| **Semi-Direct Pathway** | Recipient APCs | Intact donor MHC transferred via extracellular vesicles (exosomes) | Facilitates CD4-CD8 cross-talk |

### T-Cell Three-Signal Model & Immunosuppressive Targets

1. **Signal 1 (TCR / CD3 Antigen Recognition)**:
   - Recipient T-Cell Receptor (TCR) binds peptide-MHC complex.
   - Triggers intracellular intracellular calcium release, activating Calcineurin.
   - Calcineurin dephosphorylates Nuclear Factor of Activated T-Cells (NFAT), allowing NFAT nuclear translocation and Interleukin-2 (IL-2) transcription.
   - **Pharmacologic Blockade**: Calcineurin Inhibitors (Tacrolimus, Cyclosporine). Corticosteroids also inhibit NF-kB and cytokine transcription.

2. **Signal 2 (Costimulation Pathway)**:
   - CD28 on T-cells engages B7-1 (CD80) and B7-2 (CD86) on APCs. Essential for T-cell proliferation and survival.
   - **Coinhibitory Gate**: CTLA-4 binds B7 with higher affinity than CD28, transmitting off-signals.
   - **Pharmacologic Blockade**: Belatacept (CTLA4-Ig fusion protein) selectively blocks CD28-B7 costimulation.

3. **Signal 3 (Cytokine Proliferation Pathway)**:
   - IL-2 binds IL-2 Receptor (CD25 / IL-2Ra), activating mammalian Target of Rapamycin (mTOR) and driving cell cycle entry from G1 to S phase.
   - **Pharmacologic Blockade**: Basiliximab (anti-CD25 mAb), mTOR inhibitors (Sirolimus, Everolimus), and antimetabolites (Mycophenolate Mofetil / MMF, Azathioprine).

### High-Yield Differential Comparison Table

| Target Signal | Drug Class / Representative Agent | Key Mechanism of Action | Major Adverse Effects |
| :--- | :--- | :--- | :--- |
| **Signal 1** | Tacrolimus / Cyclosporine | Calcineurin inhibition -> blocks NFAT activation | Acute/Chronic Nephrotoxicity, New-Onset Diabetes After Transplantation (NODAT), Tremor |
| **Signal 2** | Belatacept | Recombinant CTLA4-Ig -> blocks CD28/B7 interaction | Post-Transplant Lymphoproliferative Disorder (PTLD) in EBV-seronegative recipients |
| **Signal 3** | Basiliximab / Sirolimus | Anti-CD25 mAb (induction) / mTOR inhibitor (maintenance) | Proteinuria, impaired wound healing, interstitial pneumonitis, hyperlipidemia |
| **Nucleotide Synthesis** | Mycophenolate Mofetil (MMF) | Inosine Monophosphate Dehydrogenase (IMPDH) inhibition | Bone marrow suppression (leukopenia), Gastrointestinal distress, CMV reactivation |

### Pathophysiological Decision Tree

```
[Donor Allograft Ingestion / Graft Vascular Anastomosis]
        │
        ├── Direct Presentation: Donor APCs ──> Recipient CD4+/CD8+ T-cell Activation ──> Early Acute TCMR
        │
        └── Indirect Presentation: Recipient APCs process Donor HLA ──> CD4+ T-cell & B-cell Help
                │
                ├── Signal 1 (TCR/CD3) ──> Calcineurin ──> NFAT ──> IL-2 Transcription (Blocked by Tacrolimus/Cyclosporine)
                ├── Signal 2 (CD28/B7) ──> Costimulatory Cascade (Blocked by Belatacept)
                └── Signal 3 (IL-2/IL-2R) ──> mTOR Pathway ──> Cell Cycle Entry (Blocked by Basiliximab/Sirolimus)
                        │
                        └── Germinal Center Activation ──> Plasmablasts ──> Donor-Specific Antibodies (DSA) ──> ABMR
```

### Conceptual Trap Analysis

> [!WARNING]
> **Belatacept & PTLD Risk Warning**: Belatacept is strictly contraindicated in EBV-seronegative kidney transplant recipients due to a markedly increased risk of central nervous system PTLD.
> 
> **Direct vs Indirect Pathway Shift**: Direct presentation decreases over time as donor passenger leukocytes die out. Indirect presentation persists indefinitely and is the primary driver of chronic active ABMR and transplant glomerulopathy.
""",
            "diagrams": [
                {
                    "id": "diag_sec1_1",
                    "imagePath": "/server-data/assets/ren_tx_imm_signal.png",
                    "relPath": "/server-data/assets/ren_tx_imm_signal.png",
                    "caption": "Figure 1.1: T-Cell Activation Signals (Signal 1, 2, 3) & Immunosuppressive Drug Target Sites in Renal Transplantation.",
                    "sourceBook": "Gemini Medical Concept Illustration",
                    "type": "ai_illustration"
                },
                {
                    "id": "diag_sec1_2",
                    "imagePath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Fig_1.png",
                    "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Fig_1.png",
                    "caption": "Figure 1.2: Brenner 11e Fig 69.2 / KDIGO Transplant: Cosignaling Interactions in T Cells (CD28/B7 Costimulation vs CTLA-4 Coinhibition).",
                    "sourceBook": "Brenner 11e Ch 69",
                    "type": "micrograph"
                }
            ]
        },
        {
            "id": "sec_2",
            "title": "Section 2: Pre-Transplant Histocompatibility Testing & Crossmatching",
            "content": """### Pre-Transplant Immunological Risk Assessment

1. **Calculated Panel Reactive Antibody (cPRA)**:
   - Measures the percentage of deceased donors in a representative donor pool with whom the candidate's anti-HLA antibodies would react.
   - High cPRA (> 20% or > 80%) indicates high sensitization, increased risk of positive crossmatch, prolonged waitlist time, and higher risk of early ABMR.

2. **Crossmatch Testing Modalities**:
   - **Complement-Dependent Cytotoxicity (CDC) Crossmatch**: Mixes recipient serum with donor lymphocytes plus rabbit complement. Cell lysis indicates presence of high-titer complement-binding anti-HLA antibodies. A positive CDC crossmatch is a strict contraindication to transplantation (causes hyperacute rejection).
   - **Antihuman Globulin (AHG)-Enhanced CDC Crossmatch**: Adds secondary anti-human globulin to enhance sensitivity for lower-titer IgG antibodies.
   - **Flow Cytometry Crossmatch (FCXM)**: Fluorescently-labeled anti-human IgG detects low-density donor-specific antibody binding to T-cells (HLA Class I) or B-cells (HLA Class I & II). Highly sensitive; positive FCXM correlates with increased risk of acute and subclinical ABMR.
   - **Virtual Crossmatch (VXM)**: Compares high-resolution donor HLA typing with recipient Single Antigen Bead (SAB) Luminex antibody profile to predict crossmatch results electronically.

### High-Yield Differential Comparison Table

| Testing Method | Target Analyte | Sensitivity | Clinical Outcome Correlation |
| :--- | :--- | :--- | :--- |
| **CDC Crossmatch** | High-titer complement-activating anti-HLA IgG/IgM | Standard / Low | Positive CDC predicts Hyperacute Rejection (Contraindication) |
| **AHG-CDC Crossmatch** | Moderate-titer anti-HLA IgG | Intermediate | Positive AHG-CDC predicts early accelerated ABMR |
| **Flow Cytometry (FCXM)** | Low-titer donor-specific anti-HLA IgG (T & B cells) | High | Positive FCXM predicts acute ABMR & subclinical rejection |
| **Virtual Crossmatch (VXM)** | Computerized HLA epitope & Luminex SAB profile | High | Enables rapid organ allocation and risk stratification |

### Single Antigen Bead (SAB) Assays & Technical Caveats

> [!NOTE]
> **Luminex SAB Analytical Caveats**:
> - **Mean Fluorescence Intensity (MFI)** is non-linear and semi-quantitative.
> - **Prozone Effect**: High-titer complement-fixing antibodies (C1q) or IgM can cause steric hindrance and produce falsely low MFI readings. Dilution of serum unmasks true antibody strength.
> - **Shared Epitopes / Eplets**: Multiple beads sharing identical amino acid eplets can dilute antibody binding, underestimating MFI.

### Pathophysiological Decision Tree

```
[Pre-Transplant Recipient HLA Antibody Screening (Luminex SAB)]
        │
        ├── High cPRA (> 80%) ──> High Sensitization Risk ──> Consider Desensitization / Paired Kidney Exchange
        │
        └── Donor Organ Offered ──> Perform Virtual Crossmatch (VXM) & Physical Crossmatch
                │
                ├── CDC Crossmatch Positive ──> High-Titer DSA ──> CONTRAINDICATED (Hyperacute Rejection Risk)
                ├── Flow Cytometry Positive (CDC Negative) ──> Low-Titer DSA ──> Augment Immunosuppression / High Risk ABMR
                └── Crossmatch Negative (VXM Negative) ──> Standard Risk ──> Proceed to Kidney Transplantation
```

### Conceptual Trap Analysis

> [!WARNING]
> **T-Cell vs B-Cell Crossmatch Binding**: T-cells express HLA Class I only. B-cells express BOTH HLA Class I and HLA Class II. A positive B-cell crossmatch with a negative T-cell crossmatch suggests donor-specific antibodies directed against HLA Class II (DR, DQ, DP).
""",
            "diagrams": [
                {
                    "id": "diag_sec2_1",
                    "imagePath": "/server-data/assets/ren_tx_crossmatch.png",
                    "relPath": "/server-data/assets/ren_tx_crossmatch.png",
                    "caption": "Figure 2.1: Pre-Transplant Crossmatch Methods (CDC, AHG-CDC, Flow Cytometry Crossmatch).",
                    "sourceBook": "Gemini Medical Concept Illustration",
                    "type": "ai_illustration"
                },
                {
                    "id": "diag_sec2_2",
                    "imagePath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_1.png",
                    "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_1.png",
                    "caption": "Figure 2.2: KDIGO 2009 / Brenner 11e Table 69.4: Clinical Histocompatibility Testing & Risk Assessment Menu.",
                    "sourceBook": "Brenner 11e Ch 69",
                    "type": "micrograph"
                }
            ]
        },
        {
            "id": "sec_3",
            "title": "Section 3: Acute T-Cell Mediated Rejection (TCMR) & Banff Grading",
            "content": """### Clinical Presentation & Pathophysiology of TCMR

- **Clinical Features**: Serum creatinine elevation, oliguria, graft tenderness, low-grade fever, hypertension, and fluid retention occurring typically > 5 days post-transplant.
- **Biopsy Findings**: T-cell infiltration into cortical interstitium and tubular epithelium.
- **Biomarker Status**: Peritubular capillary C4d staining is **negative**; circulating DSA is typically absent.

### Banff Histopathological Scoring for TCMR

1. **Interstitial Inflammation (`i`)**: Mononuclear cell infiltration in uninjured parenchyma (`i0` < 10%, `i1` 10-25%, `i2` 26-50%, `i3` > 50%).
2. **Tubulitis (`t`)**: Mononuclear cell invasion into tubular basement membrane (`t0` 0, `t1` 1-4 lymphocytes/tubule, `t2` 5-10 lymphocytes/tubule, `t3` > 10 lymphocytes/tubule).
3. **Intimal Arteritis / Endothelialitis (`v`)**: Lymphocytic infiltration beneath arterial endothelial cells (`v0` 0, `v1` mild intimal arteritis < 25% luminal occlusion, `v2` severe intimal arteritis > 25% luminal occlusion, `v3` transmural arteritis or fibrinoid necrosis).

### Banff Diagnostic Categories for TCMR

- **Borderline TCMR**: `i1` (10-25% inflammation) with `t1`, or `i2/i3` with `t1`, without arteritis (`v = 0`).
- **Grade IA TCMR**: `i2` or `i3` (> 25% inflammation) with moderate tubulitis `t2` (> 5 mononuclear cells/tubule).
- **Grade IB TCMR**: `i2` or `i3` with severe tubulitis `t3` (> 10 mononuclear cells/tubule).
- **Grade IIA TCMR**: Mild to moderate intimal arteritis `v1`.
- **Grade IIB TCMR**: Severe intimal arteritis `v2`.
- **Grade III TCMR**: Transmural arteritis and/or arterial fibrinoid necrosis `v3`.

### High-Yield Differential Comparison Table

| Banff TCMR Grade | Histological Criteria | Primary Treatment Strategy | Expected Clinical Response |
| :--- | :--- | :--- | :--- |
| **Borderline / Grade IA** | `i1-i3`, `t1-t2`, `v0` | High-dose Methylprednisolone pulse (250-500 mg IV x 3 days) | Excellent (> 90% resolution) |
| **Grade IB** | `i2-i3`, `t3`, `v0` | High-dose Methylprednisolone pulse | Good response |
| **Grade IIA / IIB** | Intimal arteritis (`v1` or `v2`) | Methylprednisolone pulse + Antithymocyte Globulin (ATG) | Requires close monitoring |
| **Grade III** | Transmural arteritis (`v3`) / necrosis | Antithymocyte Globulin (ATG) + Methylprednisolone pulse | High risk of graft loss |
| **Steroid-Resistant TCMR** | Persistent GFR decline post-steroid pulse | Lymphocyte-depleting antibody (ATG / Thymoglobulin) | Rescues allograft function |

### Pathophysiological Decision Tree

```
[Elevated Creatinine > 5 Days Post-Transplant]
        │
        └── Renal Allograft Biopsy ──> Assess Banff Scores (i, t, v)
                │
                ├── Grade IA / IB (i2/i3, t2/t3, v0) ──> Methylprednisolone Pulse (500mg IV x 3 days)
                │       │
                │       ├── Response (Creatinine Drops) ──> Return to Maintenance Immunosuppression
                │       └── Steroid Resistant ──> Initiate Antithymocyte Globulin (ATG) Therapy
                │
                └── Grade II / III (v1, v2, v3 Intimal/Transmural Arteritis)
                        │
                        └── Initiate ATG (Thymoglobulin) + Steroid Pulse + Adjust CNI Trough Levels
```

### Conceptual Trap Analysis

> [!WARNING]
> **Arteritis (`v` Score) Significance**: The presence of even mild intimal arteritis (`v1`) elevates the diagnosis to Banff Grade II TCMR, automatically signaling a higher risk of treatment failure with steroids alone and requiring consideration of ATG therapy.
""",
            "diagrams": [
                {
                    "id": "diag_sec3_1",
                    "imagePath": "/server-data/assets/ren_tx_tcmr_path.png",
                    "relPath": "/server-data/assets/ren_tx_tcmr_path.png",
                    "caption": "Figure 3.1: Acute T-Cell Mediated Rejection (TCMR) Histopathological Features (Tubulitis, Interstitial Inflammation, Intimal Arteritis).",
                    "sourceBook": "Gemini Medical Concept Illustration",
                    "type": "ai_illustration"
                },
                {
                    "id": "diag_sec3_2",
                    "imagePath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_2.png",
                    "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_2.png",
                    "caption": "Figure 3.2: Brenner 11e Table 70.8: Banff Histopathology Lesion Scores & Rejection Grading.",
                    "sourceBook": "Brenner 11e Ch 70",
                    "type": "micrograph"
                }
            ]
        },
        {
            "id": "sec_4",
            "title": "Section 4: Active & Chronic Antibody-Mediated Rejection (ABMR)",
            "content": """### Pathophysiology & Banff Diagnostic Triad for Active ABMR

Active Antibody-Mediated Rejection (ABMR) requires all 3 criteria of the **Banff Diagnostic Triad**:
1. **Histological Evidence of Acute Tissue Injury**: Microvascular inflammation (Glomerulitis `g > 0`, Peritubular Capillaritis `ptc > 0`), acute tubular necrosis, or acute microvascular thombi.
2. **Evidence of Current / Recent Antibody Interaction with Endothelium**:
   - Linear **C4d deposition** in peritubular capillaries (`c4d` >= 2 by IF, or `c4d` >= 1 by IHC).
   - *OR* in C4d-negative cases: Moderate microvascular inflammation (`g + ptc >= 2`) or validated endothelial gene expression transcripts.
3. **Serological Evidence of Circulating Donor-Specific Antibodies (DSA)**: Positive Luminex Single Antigen Bead (SAB) assay against donor HLA Class I, HLA Class II, or non-HLA antigens (e.g. anti-MICA, anti-AT1R).

### Chronic Active ABMR & Histopathological Landmarks

- **Transplant Glomerulopathy (`cg`)**: Duplication / double contours of the glomerular basement membrane (GBM) seen on silver stain or electron microscopy.
- **Peritubular Capillary Basement Membrane Multilayering (`ptcbm`)**: Seen on electron microscopy.
- **Fibrointimal Thickening of Arteries (`cv`)**: Severe vascular remodeling causing irreversible ischemia.

### Multimodal Therapeutic Strategy for Active ABMR

> [!IMPORTANT]
> **Active ABMR Multimodal Combination Protocol**:
> 1. **Therapeutic Plasma Exchange (TPE / Plasmapheresis)**: Physical removal of circulating DSA and complement factors (5-10 sessions).
> 2. **Intravenous Immunoglobulin (IVIG)**: High-dose IVIG (1-2 g/kg) post-TPE to neutralize residual antibodies, inhibit complement C3/C5, and downregulate Fc receptors.
> 3. **Corticosteroids**: Methylprednisolone pulse therapy to suppress endothelial inflammation.
> 4. **B-Cell & Plasma Cell Targeted Therapies**:
>    - **Rituximab** (anti-CD20 mAb): Depletes precursor B-cells in secondary lymphoid organs.
>    - **Bortezomib** (Proteasome Inhibitor): Induces apoptosis in long-lived plasma cells.
>    - **Tocilizumab** (anti-IL-6R mAb): Blocks IL-6 signaling for plasma cell survival.
>    - **Eculizumab** (anti-C5 mAb): Blocks terminal membrane attack complex (C5b-C9) formation in severe complement-mediated TMA.

### High-Yield Differential Comparison Table

| Feature | Acute TCMR | Active ABMR |
| :--- | :--- | :--- |
| **Primary Target Tissue** | Tubular Epithelium (`t`) & Interstitium (`i`) | Vascular Endothelium (`g`, `ptc`, microvasculature) |
| **Banff Microvascular Lesions** | `g = 0`, `ptc = 0` | Glomerulitis (`g > 0`) & Capillaritis (`ptc > 0`) |
| **C4d Staining (PTC)** | **Negative** | **Positive** (Linear deposition along peritubular capillaries) |
| **Serum DSA Status** | Usually Negative | **Positive** (Donor-Specific Anti-HLA Antibodies) |
| **First-Line Treatment** | Methylprednisolone Pulse +/- ATG | **Plasmapheresis + IVIG + Pulse Steroids** +/- Rituximab |

### Pathophysiological Decision Tree

```
[Circulating DSA Positive + Elevated Serum Creatinine]
        │
        └── Renal Biopsy: Glomerulitis (g) + Capillaritis (ptc) + C4d Staining
                │
                └── Active ABMR Confirmed (Banff Category 2)
                        │
                        ├── Step 1: Therapeutic Plasma Exchange (TPE) x 5-7 Sessions (Remove DSA)
                        ├── Step 2: High-Dose IVIG (2 g/kg) + Methylprednisolone Pulse (Suppress Inflammation)
                        ├── Step 3: Add Rituximab (Anti-CD20) or Bortezomib (Proteasome Inhibitor)
                        └── Refractory / Severe TMA ──> Eculizumab (Terminal C5 Complement Blockade)
```

### Conceptual Trap Analysis

> [!WARNING]
> **Steroid-Alone Trap in ABMR**: Pulse corticosteroids alone are effective for TCMR, but completely inadequate for active ABMR. Pulse steroids cannot eliminate preformed circulating DSA or prevent complement-mediated endothelial destruction. Plasmapheresis and IVIG are mandatory.
""",
            "diagrams": [
                {
                    "id": "diag_sec4_1",
                    "imagePath": "/server-data/assets/ren_tx_abmr_c4d.png",
                    "relPath": "/server-data/assets/ren_tx_abmr_c4d.png",
                    "caption": "Figure 4.1: Antibody-Mediated Rejection (ABMR) Features: Linear C4d Deposition along Peritubular Capillaries & Microvascular Inflammation.",
                    "sourceBook": "Gemini Medical Concept Illustration",
                    "type": "ai_illustration"
                },
                {
                    "id": "diag_sec4_2",
                    "imagePath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_3.png",
                    "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_3.png",
                    "caption": "Figure 4.2: Brenner 11e Table 70.7: Differences Between Pure Forms of Acute TCMR and Active ABMR.",
                    "sourceBook": "Brenner 11e Ch 70",
                    "type": "micrograph"
                }
            ]
        },
        {
            "id": "sec_5",
            "title": "Section 5: Differential Diagnosis & Clinical Management Algorithms",
            "content": """### Clinical Management of Allograft Dysfunction

Post-transplant renal allograft dysfunction (elevated serum creatinine or oliguria) requires systematic differentiation between:
1. **Acute TCMR**: Tubulitis (`t`), interstitial inflammation (`i`), `C4d-`, `DSA-`. Treatment: Pulse steroids / ATG.
2. **Active ABMR**: Glomerulitis (`g`), capillaritis (`ptc`), `C4d+`, `DSA+`. Treatment: Plasmapheresis + IVIG + steroids + Rituximab.
3. **Calcineurin Inhibitor (CNI) Toxicity**:
   - *Acute*: Reversible afferent arteriolar vasoconstriction due to high CNI trough level (Tacrolimus > 12-15 ng/mL). Biopsy shows **isometric tubular vacuolization**. Treatment: CNI dose reduction.
   - *Chronic*: Irreversible **striped interstitial fibrosis** and **nodular arteriolar hyalinosis**. Treatment: CNI reduction or conversion to Belatacept/mTORi.
4. **BK Virus Nephropathy (BKVN)**:
   - Polyomavirus reactivation causing tubulointerstitial nephritis. Biopsy shows intranuclear viral inclusions, positive **SV40 immunohistochemistry**. Blood BK PCR > 10,000 copies/mL.
   - **Critical Treatment Paradox**: Requires **REDUCTION of immunosuppression** (discontinue MMF, lower CNI target). Increasing immunosuppression will destroy the graft!
5. **Delayed Graft Function (DGF)**:
   - Defined as requirement for dialysis within the first 7 days post-transplant due to ischemia-reperfusion injury / acute tubular necrosis (ATN).
   - Requires protocol renal biopsy at days 7-10 to rule out occult superimposed acute rejection.

### High-Yield Differential Comparison Table

| Diagnostic Entity | Primary Biopsy Landmark | C4d / Viral Marker | CNI Trough Level | Core Therapeutic Action |
| :--- | :--- | :--- | :--- | :--- |
| **Acute TCMR** | Tubulitis (`t`), Interstitial inflammation (`i`) | `C4d-`, `DSA-`, `SV40-` | Therapeutic / Subtherapeutic | **Methylprednisolone Pulse / ATG** |
| **Active ABMR** | Glomerulitis (`g`), Capillaritis (`ptc`) | **`C4d+`**, **`DSA+`** | Therapeutic / Subtherapeutic | **Plasmapheresis + IVIG + Pulse Steroids** |
| **CNI Toxicity** | Isometric tubular vacuolization, Striped fibrosis | `C4d-`, `DSA-`, `SV40-` | **Supratherapeutic** | **Reduce CNI Dose** |
| **BK Virus Nephropathy** | Intranuclear inclusions, Interstitial nephritis | **`SV40 IHC Positive`** | Therapeutic / High | **REDUCE Immunosuppression (Stop MMF)** |

### Pathophysiological Decision Tree

```
[Post-Transplant Renal Allograft Dysfunction (Elevated Creatinine)]
        │
        ├── Step 1: Rule out prerenal hypovolemia, urinary leak/obstruction (Ultrasound), & CNI Overdose
        │
        └── Step 2: Perform Urgent Renal Allograft Biopsy & Check Serum DSA + BK Viral Load
                │
                ├── Biopsy: Tubulitis (t) + Interstitial Inflammation (i) ──> Acute TCMR ──> Steroid Pulse / ATG
                ├── Biopsy: Glomerulitis (g) + Capillaritis (ptc) + C4d+ ──> Active ABMR ──> TPE + IVIG + Steroids
                ├── Biopsy: SV40 Positive + High BK Viral Load ──> BKVN ──> REDUCE Immunosuppression (Stop MMF)
                └── Biopsy: Isometric Vacuolization + High CNI Trough ──> CNI Toxicity ──> Reduce CNI Dose
```

### Conceptual Trap Analysis

> [!WARNING]
> **BKVN vs Rejection Treatment Trap**: Misdiagnosing BK Virus Nephropathy as Acute TCMR and administering pulse steroids will cause explosive viral replication and rapid, irreversible graft destruction. Always check SV40 IHC staining on biopsy before pulsing steroids for tubulitis!
""",
            "diagrams": [
                {
                    "id": "diag_sec5_1",
                    "imagePath": "/server-data/assets/ren_tx_diff_dx.png",
                    "relPath": "/server-data/assets/ren_tx_diff_dx.png",
                    "caption": "Figure 5.1: Clinical Decision Tree for Post-Kidney Transplant Allograft Dysfunction (TCMR, ABMR, CNI Toxicity, BKVN).",
                    "sourceBook": "Gemini Medical Concept Illustration",
                    "type": "ai_illustration"
                },
                {
                    "id": "diag_sec5_2",
                    "imagePath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_10.png",
                    "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_10.png",
                    "caption": "Figure 5.2: Brenner 11e Fig 70.4 / KDIGO Transplant: Management Algorithm for Persistent Delayed Graft Function & Allograft Dysfunction.",
                    "sourceBook": "Brenner 11e Ch 70",
                    "type": "micrograph"
                }
            ]
        }
    ]
}

tutorial_filename = "tutorials/2026_Renal_transplant_rejection_(主題備考)_tutorial.json"
tutorial_path = os.path.join(SERVER_DATA_DIR, tutorial_filename)
with open(tutorial_path, "w", encoding="utf-8") as f:
    json.dump(tutorial_data, f, ensure_ascii=False, indent=2)
print(f"Wrote tutorial JSON to {tutorial_path}")

# 3. Build Question Bank JSON (20 High-Yield Pure English MCQs)
# Options distribution: 5 A, 5 B, 5 C, 5 D
questions = [
    # Q1: Direct vs Indirect Pathway (Ans: A)
    {
        "id": "q1",
        "number": 1,
        "stem": "Which of the following statements best describes the immunobiology of antigen presentation in renal allograft rejection?",
        "options": [
            {"id": "A", "text": "The direct pathway involves recipient T-cells recognizing intact donor MHC Class I and II molecules displayed directly on donor antigen-presenting cells (passenger leukocytes)."},
            {"id": "B", "text": "The indirect pathway is primary responsible for hyperacute rejection occurring within minutes of vascular anastomosis."},
            {"id": "C", "text": "Direct antigen presentation persists indefinitely and is the primary driver of chronic active antibody-mediated rejection years after transplantation."},
            {"id": "D", "text": "Recipient CD4+ T-cells cannot recognize donor antigens processed and presented by recipient antigen-presenting cells."}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Direct antigen presentation occurs when recipient T-cells recognize intact donor MHC molecules on donor APCs (passenger leukocytes), dominating early acute T-cell mediated rejection (TCMR). The indirect pathway involves recipient APCs processing donor HLA peptides, driving late TCMR, de novo DSA formation, and chronic active ABMR.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Fig_1.png",
                "caption": "Brenner 11e Fig 69.2: Cosignaling Interactions in T Cells."
            }
        ]
    },
    # Q2: T-Cell Activation Signal 2 & Belatacept (Ans: B)
    {
        "id": "q2",
        "number": 2,
        "stem": "A 52-year-old male kidney transplant recipient is prescribed Belatacept as part of a CNI-sparing maintenance immunosuppressive regimen. What is the precise mechanism of action of Belatacept?",
        "options": [
            {"id": "A", "text": "Inhibition of calcineurin phosphatase activity, blocking NFAT nuclear translocation."},
            {"id": "B", "text": "Selective binding to B7-1 (CD80) and B7-2 (CD86) on antigen-presenting cells, blocking CD28 costimulatory Signal 2."},
            {"id": "C", "text": "Competitive antagonism of the Interleukin-2 receptor alpha subunit (CD25)."},
            {"id": "D", "text": "Inhibition of inosine monophosphate dehydrogenase (IMPDH), impairing de novo purine synthesis."}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Belatacept is a recombinant soluble fusion protein consisting of the extracellular domain of human CTLA-4 linked to an Fc fragment. It binds to CD80 (B7-1) and CD86 (B7-2) on APCs, blocking interaction with CD28 on T-cells and inhibiting costimulatory Signal 2.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_imm_signal.png",
                "caption": "T-Cell Activation Signals & Immunosuppressive Drug Targets."
            }
        ]
    },
    # Q3: Pre-Transplant CDC Crossmatch (Ans: C)
    {
        "id": "q3",
        "number": 3,
        "stem": "A candidate undergoing evaluation for kidney transplantation has a pre-transplant Complement-Dependent Cytotoxicity (CDC) crossmatch result of 90% cell lysis with donor T-lymphocytes. What is the clinical implication of this result?",
        "options": [
            {"id": "A", "text": "The patient is eligible for immediate transplantation with standard CNI triple therapy."},
            {"id": "B", "text": "The positive crossmatch is caused by low-titer non-HLA antibodies and carries no prognostic significance."},
            {"id": "C", "text": "Transplantation is strictly contraindicated due to a very high risk of immediate hyperacute rejection."},
            {"id": "D", "text": "The patient requires post-operative single-agent corticosteroid pulse therapy to prevent subclinical rejection."}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "A positive CDC crossmatch indicates high-titer circulating donor-specific complement-fixing antibodies. Proceeding with renal transplantation in the setting of a positive CDC crossmatch leads to immediate hyperacute rejection and total graft necrosis; therefore, transplantation is strictly contraindicated.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_crossmatch.png",
                "caption": "Pre-Transplant Crossmatch Methods & Interpretations."
            }
        ]
    },
    # Q4: Luminex SAB MFI & Prozone Effect (Ans: D)
    {
        "id": "q4",
        "number": 4,
        "stem": "During serum HLA antibody identification using Luminex Single Antigen Bead (SAB) assay, a highly sensitized patient displays an unexpectedly low Mean Fluorescence Intensity (MFI) for HLA-DR4, despite a prior strong cytotoxic antibody history. Serial dilution of the patient serum unmasks a dramatically high MFI (> 15,000). What technical phenomenon accounts for this finding?",
        "options": [
            {"id": "A", "text": "Eplet mismatch saturation."},
            {"id": "B", "text": "Nonspecific bead adsorption."},
            {"id": "C", "text": "HLA Class I allele denaturation."},
            {"id": "D", "text": "The Prozone effect due to high-titer complement C1q binding or steric hindrance."}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "The Prozone effect (or complement interference) occurs when extremely high titers of HLA antibody fix complement components (C1q) or aggregate on Luminex beads, sterically blocking secondary detection antibodies and falsely suppressing MFI readings. Serum dilution abrogates complement interference and reveals true high-titer antibody presence.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_1.png",
                "caption": "Brenner 11e Fig 69.9: MFI Analytical Limitations and Prozone Effect."
            }
        ]
    },
    # Q5: Acute TCMR Histopathology & Banff Grading (Ans: A)
    {
        "id": "q5",
        "number": 5,
        "stem": "A kidney allograft biopsy obtained 3 weeks post-transplant demonstrates diffuse interstitial mononuclear cell infiltration involving 40% of uninjured cortex (i2), severe tubulitis with 12 lymphocytes per tubular cross-section (t3), and mild intimal arteritis with subendothelial mononuclear infiltration causing 15% luminal occlusion (v1). What is the Banff 2017 histological classification for this biopsy?",
        "options": [
            {"id": "A", "text": "Banff Grade IIA Acute T-Cell Mediated Rejection (TCMR)."},
            {"id": "B", "text": "Banff Grade IB Acute T-Cell Mediated Rejection (TCMR)."},
            {"id": "C", "text": "Borderline Acute T-Cell Mediated Rejection."},
            {"id": "D", "text": "Active Antibody-Mediated Rejection (ABMR)."}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "According to Banff criteria, the presence of intimal arteritis (v > 0) automatically classifies the lesion as Grade II or III TCMR. Mild to moderate intimal arteritis (v1, < 25% luminal occlusion) defines Banff Grade IIA Acute TCMR.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_tcmr_path.png",
                "caption": "Acute TCMR Histopathological Features & Banff Grading."
            }
        ]
    },
    # Q6: Steroid-Resistant TCMR Therapy (Ans: B)
    {
        "id": "q6",
        "number": 6,
        "stem": "A 40-year-old male recipient diagnosed with Banff Grade IB TCMR receives high-dose intravenous Methylprednisolone pulse therapy (500 mg daily for 3 consecutive days). On post-treatment day 5, his serum creatinine remains elevated at 3.4 mg/dL with persistent oliguria. What is the most appropriate next therapeutic step?",
        "options": [
            {"id": "A", "text": "Immediate surgical graft nephrectomy."},
            {"id": "B", "text": "Initiation of lymphocyte-depleting antibody therapy with Antithymocyte Globulin (ATG)."},
            {"id": "C", "text": "Switching maintenance therapy from Tacrolimus to Belatacept."},
            {"id": "D", "text": "Administration of high-dose oral Cyclophosphamide."}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Steroid-resistant acute TCMR (failure of serum creatinine to decrease after high-dose methylprednisolone pulse therapy) requires T-cell depleting antibody therapy, primarily Antithymocyte Globulin (ATG / Thymoglobulin).",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_2.png",
                "caption": "Management of Acute TCMR & Steroid Resistance."
            }
        ]
    },
    # Q7: Active ABMR Banff Diagnostic Triad (Ans: C)
    {
        "id": "q7",
        "number": 7,
        "stem": "Which combination of pathological and clinical findings satisfies the full Banff diagnostic triad for Active Antibody-Mediated Rejection (ABMR)?",
        "options": [
            {"id": "A", "text": "Tubulitis (t2), interstitial inflammation (i2), negative C4d, and absence of DSA."},
            {"id": "B", "text": "Isometric tubular vacuolization, arteriolar hyalinosis, negative C4d, and high Tacrolimus trough level."},
            {"id": "C", "text": "Microvascular inflammation (glomerulitis g > 0, capillaritis ptc > 0), linear peritubular capillary C4d deposition, and positive circulating donor-specific anti-HLA antibodies (DSA)."},
            {"id": "D", "text": "Intranuclear viral inclusion bodies, positive SV40 immunohistochemistry, and negative C4d."}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "The Banff diagnostic triad for Active ABMR requires: (1) histological acute tissue injury (microvascular inflammation g+ptc), (2) evidence of antibody-endothelium interaction (linear C4d deposition in peritubular capillaries or gene expression classifiers), and (3) serological detection of circulating donor-specific antibodies (DSA).",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_abmr_c4d.png",
                "caption": "Active ABMR Features & C4d Deposition."
            }
        ]
    },
    # Q8: Multimodal Treatment for Active ABMR (Ans: D)
    {
        "id": "q8",
        "number": 8,
        "stem": "A 48-year-old female recipient 2 months post-kidney transplant is diagnosed with biopsy-proven Active ABMR with high-titer anti-HLA Class II DSA. Which of the following therapeutic regimens represents the established core standard of care?",
        "options": [
            {"id": "A", "text": "High-dose Methylprednisolone pulse monotherapy for 7 days."},
            {"id": "B", "text": "Discontinuation of all immunosuppression and starting ganciclovir."},
            {"id": "C", "text": "Increasing oral Tacrolimus trough target to > 20 ng/mL."},
            {"id": "D", "text": "Therapeutic Plasma Exchange (TPE / Plasmapheresis) combined with Intravenous Immunoglobulin (IVIG) and Corticosteroid pulse therapy."}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Active ABMR treatment requires a multimodal approach to clear preformed antibodies, neutralize residual immunoglobulins, and suppress vascular inflammation: Therapeutic Plasma Exchange (TPE) + IVIG + Corticosteroid pulse therapy +/- Rituximab. Pulse steroids alone are insufficient.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_3.png",
                "caption": "Treatment Protocols for Active ABMR."
            }
        ]
    },
    # Q9: C4d Complement Cleavage Product (Ans: A)
    {
        "id": "q9",
        "number": 9,
        "stem": "What is the biological significance of peritubular capillary C4d staining on renal allograft biopsy?",
        "options": [
            {"id": "A", "text": "C4d is a stable, inactive cleavage fragment of complement component C4 covalently bound to vascular endothelium, serving as a footprint of classical complement activation by antibody."},
            {"id": "B", "text": "C4d is a toxic inflammatory cytokine secreted by CD8+ cytotoxic T-cells during direct tubulitis."},
            {"id": "C", "text": "C4d represents intracellular viral capsid protein expressed during active Polyomavirus replication."},
            {"id": "D", "text": "C4d is an extracellular matrix protein formed specifically in response to chronic calcineurin inhibitor vasoconstriction."}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "When donor-specific antibodies bind to HLA antigens on allograft vascular endothelial cells, the classical complement pathway is activated. C4 is cleaved into C4a and C4b; C4b degrades into C4d, which forms a durable covalent bond with endothelial cell membranes and basement membranes, acting as a biomarker for antibody-mediated endothelial injury.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_abmr_c4d.png",
                "caption": "C4d Deposition along Peritubular Capillaries."
            }
        ]
    },
    # Q10: Herb-Drug Interaction & Rejection (Ans: B)
    {
        "id": "q10",
        "number": 10,
        "stem": "A 38-year-old male kidney transplant recipient maintained on Tacrolimus, Mycophenolate Mofetil, and Prednisone begins taking an over-the-counter herbal supplement (St. John's Wort / Hypericum perforatum) for mild depression. Two weeks later, his Tacrolimus trough level drops from 8.2 ng/mL to 1.8 ng/mL, and he develops acute serum creatinine elevation (1.2 to 2.8 mg/dL). Biopsy confirms acute TCMR. What pharmacokinetic mechanism caused this rejection episode?",
        "options": [
            {"id": "A", "text": "Direct chemical chelation of Tacrolimus in the gastrointestinal tract."},
            {"id": "B", "text": "Induction of hepatic and intestinal Cytochrome P-450 3A (CYP3A) enzymes and P-glycoprotein (P-gp) by St. John's Wort."},
            {"id": "C", "text": "Inhibition of renal organic anion transporters (OAT1/OAT3)."},
            {"id": "D", "text": "Competitive binding to FK-binding protein 12 (FKBP-12)."}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "St. John's Wort (Hypericum perforatum) is a potent inducer of hepatic and intestinal CYP3A4/5 isoenzymes and P-glycoprotein (P-gp) efflux pumps. Inducing CYP3A and P-gp significantly increases Tacrolimus metabolism and clearance, causing blood levels to drop to subtherapeutic ranges and precipitating acute allograft rejection.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_diff_dx.png",
                "caption": "Differential Diagnosis of Allograft Dysfunction & Drug Interactions."
            }
        ]
    },
    # Q11: Chronic Active ABMR Histopathology (Ans: C)
    {
        "id": "q11",
        "number": 11,
        "stem": "A renal allograft biopsy performed 4 years post-transplant for insidious decline in GFR and worsening proteinuria displays double contours of the glomerular basement membrane (transplant glomerulopathy, cg > 0) on silver stain and electron microscopy multilayering of peritubular capillary basement membranes. What is the primary underlying etiology?",
        "options": [
            {"id": "A", "text": "Recurrent Focal Segmental Glomerulosclerosis (FSGS)."},
            {"id": "B", "text": "Acute grade IA T-cell mediated rejection."},
            {"id": "C", "text": "Chronic Active Antibody-Mediated Rejection (Chronic ABMR)."},
            {"id": "D", "text": "Acute tubular necrosis secondary to hypovolemia."}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Transplant glomerulopathy (cg score > 0, characterized by GBM double contours / duplication) and peritubular capillary basement membrane multilayering are hallmark ultrastructural and light microscopic features of Chronic Active Antibody-Mediated Rejection (ABMR), driven by low-grade chronic endothelial damage from de novo DSA.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_3.png",
                "caption": "Chronic Active ABMR Histopathology."
            }
        ]
    },
    # Q12: BKVN vs Acute Rejection Treatment Paradox (Ans: D)
    {
        "id": "q12",
        "number": 12,
        "stem": "A 56-year-old kidney recipient 8 months post-transplant presents with serum creatinine rise (1.4 to 2.3 mg/dL). Renal biopsy reveals tubulointerstitial mononuclear cell infiltration and viral cytopathic changes with intranuclear inclusions in tubular epithelial cells. Immunohistochemistry is strongly positive for SV40 large T antigen. Quantitative blood BK PCR shows 85,000 copies/mL. What is the mandatory initial management strategy?",
        "options": [
            {"id": "A", "text": "High-dose Methylprednisolone pulse therapy (500 mg IV daily for 3 days)."},
            {"id": "B", "text": "Initiation of Therapeutic Plasma Exchange (TPE) and IVIG."},
            {"id": "C", "text": "Administration of Antithymocyte Globulin (ATG)."},
            {"id": "D", "text": "Reduction of overall immunosuppression (discontinuing or reducing Mycophenolate Mofetil and lowering CNI target levels)."}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "BK Virus Nephropathy (BKVN) presents a major clinical paradox: it pathologically mimics TCMR with interstitial inflammation and tubulitis, but is driven by active polyomavirus replication (SV40 positive). The mandatory first-line therapy is REDUCTION of immunosuppression (stopping/reducing MMF and lowering CNI trough targets). Pulsing steroids or giving ATG for misdiagnosed TCMR will accelerate viral destruction of the graft.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_diff_dx.png",
                "caption": "Differential Diagnosis Flowchart: BKVN vs TCMR."
            }
        ]
    },
    # Q13: Acute CNI Toxicity Histopathology (Ans: A)
    {
        "id": "q13",
        "number": 13,
        "stem": "A recipient taking high-dose Tacrolimus develops acute renal allograft dysfunction with a 12-hour trough concentration of 18.5 ng/mL. A renal biopsy shows clear, isometric, non-membrane-bound vacuolization of proximal tubular epithelial cells without significant tubulitis, glomerulitis, or C4d deposition. What is the diagnosis?",
        "options": [
            {"id": "A", "text": "Acute Calcineurin Inhibitor (CNI) Nephrotoxicity."},
            {"id": "B", "text": "Acute T-Cell Mediated Rejection Grade IA."},
            {"id": "C", "text": "Acute Antibody-Mediated Rejection."},
            {"id": "D", "text": "BK Virus Nephropathy."}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Isometric tubular vacuolization (equal-sized fine lipid-containing vacuoles in proximal tubular cytoplasm) combined with supratherapeutic drug levels (> 15 ng/mL) is the pathognomonic histological hallmark of acute CNI nephrotoxicity, caused by intense afferent arteriolar vasoconstriction.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_2.png",
                "caption": "CNI Toxicity vs Allograft Rejection."
            }
        ]
    },
    # Q14: Delayed Graft Function (DGF) Management (Ans: B)
    {
        "id": "q14",
        "number": 14,
        "stem": "A 60-year-old recipient of a deceased donor kidney with prolonged cold ischemia time (28 hours) remains anuric and requires hemodialysis on post-operative days 2, 5, and 8. Serum Tacrolimus levels are in the therapeutic range (8-10 ng/mL). What is the definition of this condition, and what diagnostic evaluation is recommended by KDIGO guidelines?",
        "options": [
            {"id": "A", "text": "Hyperacute rejection; perform immediate surgical nephrectomy."},
            {"id": "B", "text": "Delayed Graft Function (DGF); perform protocol renal allograft biopsy at days 7–10 to rule out occult superimposed rejection."},
            {"id": "C", "text": "Chronic allograft arteriopathy; start long-term high-dose steroids."},
            {"id": "D", "text": "Calcineurin inhibitor resistance; switch immediately to Sirolimus."}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Delayed Graft Function (DGF) is defined as the requirement for dialysis within the first 7 days post-transplant, usually caused by ischemia-reperfusion ATN. Because serum creatinine cannot be monitored during dialysis dependence, KDIGO guidelines recommend a protocol allograft biopsy at 7-10 days to detect occult superimposed acute rejection.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_10.png",
                "caption": "Brenner 11e Fig 70.4: Management Algorithm for Persistent DGF."
            }
        ]
    },
    # Q15: Post-Transplant Pregnancy Safety Gate (Ans: C)
    {
        "id": "q15",
        "number": 15,
        "stem": "A 31-year-old female kidney transplant recipient asks her nephrologist about pregnancy planning. According to American Society of Transplantation (AST) consensus guidelines, which criteria must be met before safe conception can be advised?",
        "options": [
            {"id": "A", "text": "Minimum 3 months post-transplant, taking Mycophenolate Mofetil 1000 mg twice daily."},
            {"id": "B", "text": "Minimum 6 months post-transplant, despite a recent treated Grade IIA TCMR episode 1 month ago."},
            {"id": "C", "text": "Minimum 1 year post-transplant, stable renal function (Creatinine < 1.5 mg/dL), proteinuria < 500 mg/day, zero acute rejection episodes in the prior 1 year, and cessation of teratogenic agents (MMF/mTORi)."},
            {"id": "D", "text": "Pregnancy is strictly contraindicated in all female kidney transplant recipients regardless of timing."}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "AST pregnancy guidelines require: (1) at least 1 year post-transplant, (2) stable kidney function (Serum Creatinine < 1.5 mg/dL), (3) minimal proteinuria (< 500 mg/day), (4) NO acute rejection episodes in the preceding 12 months, and (5) switching off teratogenic medications (MMF must be stopped at least 6 weeks prior; Sirolimus stopped).",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_diff_dx.png",
                "caption": "Post-Transplant Clinical Management & Pregnancy Safety Criteria."
            }
        ]
    },
    # Q16: Risk Factors for Chronic Rejection (Ans: D)
    {
        "id": "q16",
        "number": 16,
        "stem": "In long-term clinical outcome studies of kidney transplantation, which factor is most strongly correlated with the development of chronic allograft rejection and late graft loss?",
        "options": [
            {"id": "A", "text": "Asymptomatic transient proteinuria during week 1 post-transplant."},
            {"id": "B", "text": "Use of Basiliximab induction instead of Antithymocyte Globulin in low-risk recipients."},
            {"id": "C", "text": "Mild postoperative urinary tract infection successfully treated with oral antibiotics."},
            {"id": "D", "text": "Late timing (> 6 months post-transplant) and increased severity of prior acute rejection episodes."}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Prior acute rejection episodes—especially those occurring late (> 6 months post-transplant), showing high histological severity (intimal arteritis), or suffering incomplete resolution—are the strongest clinical risk factors for developing chronic active rejection, progressive nephron loss, and late graft failure.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_1.png",
                "caption": "Risk Factors for Acute and Chronic Rejection."
            }
        ]
    },
    # Q17: Post-Transplant TMA Management (Ans: A)
    {
        "id": "q17",
        "number": 17,
        "stem": "On post-operative day 14, a kidney recipient develops sudden onset of microangiopathic hemolytic anemia (schistocytes on blood smear, LDH 1,200 U/L, undetectable haptoglobin), severe thrombocytopenia, and rapidly rising serum creatinine (1.3 to 3.5 mg/dL). Biopsy demonstrates extensive fibrin thrombi in renal arterioles and glomeruli with positive DSA. What diagnosis and intervention are indicated?",
        "options": [
            {"id": "A", "text": "ABMR-associated Thrombotic Microangiopathy (TMA); initiate Therapeutic Plasma Exchange (TPE), IVIG, discontinue CNI, and consider Eculizumab."},
            {"id": "B", "text": "Acute pyelonephritis; start IV Ciprofloxacin monotherapy without modifying immunosuppression."},
            {"id": "C", "text": "Prerenal azotemia; administer 3 liters of normal saline bolus."},
            {"id": "D", "text": "Steroid withdrawal syndrome; double oral Prednisone dose."}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Post-transplant TMA with microangiopathic hemolytic anemia, thrombocytopenia, and renal microthrombi in the presence of DSA represents severe complement-mediated microvascular injury secondary to active ABMR or CNI toxicity. Immediate intervention with TPE, IVIG, CNI withdrawal, and complement C5 inhibitor (Eculizumab) is required to salvage the graft.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_abmr_c4d.png",
                "caption": "ABMR-Associated Microvascular Injury & TMA."
            }
        ]
    },
    # Q18: Direct vs Indirect Pathway Complement Fixation (Ans: B)
    {
        "id": "q18",
        "number": 18,
        "stem": "Which antibody isotype and complement activation pathway are primarily responsible for peritubular capillary C4d deposition in hyperacute and active antibody-mediated rejection?",
        "options": [
            {"id": "A", "text": "IgE antibodies activating the alternative complement pathway via Factor B."},
            {"id": "B", "text": "Donor-specific IgG1, IgG3, or IgM antibodies activating the classical complement pathway via C1q engagement."},
            {"id": "C", "text": "IgA antibodies activating the mannose-binding lectin (MBL) pathway via MASP-2."},
            {"id": "D", "text": "IgD antibodies activating properdin-dependent C5 convertase directly."}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Classical complement activation is initiated when donor-specific IgG1, IgG3, or IgM antibodies bind to HLA antigens on endothelial cells, engaging C1q. This cleaves C4 into C4a and C4b; C4b degrades to C4d, which covalently binds to endothelial basement membranes.",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_abmr_c4d.png",
                "caption": "Classical Complement Cascade & C4d Deposition."
            }
        ]
    },
    # Q19: Protocol Biopsy Timing in Stable Patients (Ans: C)
    {
        "id": "q19",
        "number": 19,
        "stem": "What is the primary diagnostic objective of performing a surveillance (protocol) renal allograft biopsy at 3 to 6 months post-transplant in a patient with stable serum creatinine?",
        "options": [
            {"id": "A", "text": "To measure systemic Tacrolimus blood concentrations directly in renal tissue."},
            {"id": "B", "text": "To screen for acute bacterial pyelonephritis before urine culture results."},
            {"id": "C", "text": "To detect subclinical rejection (occult TCMR or subclinical ABMR) and early IFTA before irreversible serum creatinine elevation occurs."},
            {"id": "D", "text": "To confirm complete genetic chimera formation between donor and recipient cells."}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Surveillance (protocol) biopsies allow early detection of subclinical rejection (histological TCMR or C4d+/DSA+ ABMR without overt GFR decline) and early interstitial fibrosis/tubular atrophy (IFTA), enabling therapeutic adjustments before permanent parenchymal loss occurs.",
        "resolvedImages": [
            {
                "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Table_1.png",
                "caption": "Protocol Biopsy Role in Renal Transplantation."
            }
        ]
    },
    # Q20: Banff Lesion Score 'v' vs 't' vs 'g' (Ans: D)
    {
        "id": "q20",
        "number": 20,
        "stem": "Match the Banff histopathological lesion score abbreviation with its correct anatomical lesion definition:",
        "options": [
            {"id": "A", "text": "g = Mononuclear cell infiltration within proximal tubular epithelial cells; t = Duplication of glomerular basement membrane."},
            {"id": "B", "text": "ptc = Subendothelial infiltration of lymphocytes in interlobular arteries; v = C4d staining in peritubular capillaries."},
            {"id": "C", "text": "cg = Tubular atrophy percentage; ci = Glomerular crescent formation."},
            {"id": "D", "text": "t = Tubulitis (lymphocytes invading tubular basement membrane); v = Intimal arteritis (lymphocytes in subendothelial space of arteries); g = Glomerulitis (mononuclear cells in glomerular capillaries)."}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "In the Banff classification: t = Tubulitis (lymphocytes in tubular epithelium), v = Intimal arteritis (endothelialitis in arteries), g = Glomerulitis (inflammatory cells in glomerular capillary loops), ptc = Peritubular capillaritis, and cg = Transplant glomerulopathy (GBM double contours).",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/ren_tx_tcmr_path.png",
                "caption": "Banff Histopathological Scores (t, v, g, ptc, cg)."
            }
        ]
    }
]

paper_filename = "2026_Renal_transplant_rejection_(主題備考).json"
paper_data = {
    "id": "2026_Renal_transplant_rejection_(主題備考)",
    "paperId": "2026_Renal_transplant_rejection_(主題備考)",
    "title": "2026 Renal Transplant Rejection (腎臟移植排斥) 臨床發育病理、Banff 分型與免疫抑制藥物處置",
    "sourceCategory": "2026 年主題練習",
    "year": 2026,
    "questionCount": len(questions),
    "questions": questions
}

paper_path = os.path.join(SERVER_DATA_DIR, paper_filename)
with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)
print(f"Wrote Exam Paper JSON to {paper_path}")

# 4. Update exams_manifest.json
manifest_path = os.path.join(SERVER_DATA_DIR, "exams_manifest.json")
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Remove existing entry if any
manifest = [item for item in manifest if item.get("id") != "2026_Renal_transplant_rejection_(主題備考)" and item.get("paperId") != "2026_Renal_transplant_rejection_(主題備考)"]

new_item = {
    "id": "2026_Renal_transplant_rejection_(主題備考)",
    "paperId": "2026_Renal_transplant_rejection_(主題備考)",
    "title": "2026 Renal Transplant Rejection (腎臟移植排斥) 臨床發育病理、Banff 分型與免疫抑制藥物處置",
    "filename": paper_filename,
    "sourceCategory": "2026 年主題練習",
    "year": 2026,
    "questionCount": len(questions),
    "nlmProcessedCount": 0,
    "qcVerifiedCount": 0,
    "hasTutorial": True,
    "tutorialFilename": tutorial_filename,
    "tutorialId": "2026_Renal_transplant_rejection_(主題備考)_tutorial",
    "updatedAt": "2026-08-01T02:58:00.000000+00:00"
}

manifest.append(new_item)

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("Updated exams_manifest.json successfully.")
