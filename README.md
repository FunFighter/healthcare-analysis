# Healthcare Analysis - Shareable Notebook

##  Complete Analysis Notebook

This directory contains a comprehensive Jupyter notebook that answers all healthcare research questions using only data-backed claims.

---

##  What's Inside

### healthcare_analysis.ipynb

A complete, self-contained Jupyter notebook that:

 **Answers all 5 research questions**
1. How much goes to treatment vs. insurance processing?
2. How much could Americans save?
3. What is the impact on different income brackets?
4. How would insurance workforce be reallocated?
5. Which model supports US R&D while saving money?

 **Only makes data-backed claims**
- All claims clearly labeled as "from our model" or "our calculation"
- World Bank API data clearly marked as "actual data"
- No unsupported assertions

 **Includes comprehensive visualizations**
- 8+ charts generated in the notebook
- All saved as high-quality PNG files
- Publication-ready graphics

 **Provides complete analysis**
- Data loading and validation
- Statistical analysis
- Comparative modeling
- Summary tables
- Clear conclusions

---

##  Quick Start

```bash
# From the healthcare/share directory
jupyter notebook healthcare_analysis.ipynb
```

Or from the main directory:
```bash
jupyter notebook healthcare/share/healthcare_analysis.ipynb
```

---

##  Notebook Structure

### Part 1: US Healthcare Spending Breakdown
- Question 1: Where does the money go?
- Data: Our model of US healthcare spending
- Visualization: Pie and bar charts

### Part 2: International Healthcare Comparison
- Question 2: How much could we save?
- Data: Our model of international admin costs
- Visualization: Comparative bar charts

### Part 3: Real International Healthcare Data
- Data: World Bank API (actual data)
- Metrics: Spending, life expectancy, outcomes
- Visualization: Multi-panel comparison

### Part 4: Income Bracket Impact Analysis
- Question 3: Who wins and who loses?
- Data: Our modeled scenarios
- Visualization: Savings by bracket

### Part 5: Total National Savings
- Data: Aggregate calculations
- Visualization: Total and per-household savings

### Part 6: Insurance Workforce Transition
- Question 4: What happens to workers?
- Data: Our workforce model
- Visualization: Displacement and transferability

### Part 7: Medical R&D Preservation
- Question 5: Can we preserve innovation?
- Data: Our R&D projections
- Visualization: R&D scenarios

### Summary
- All questions answered
- Data sources clearly labeled
- Limitations acknowledged

---

##  Key Features

### Data Transparency
- **Model data**: Clearly labeled as "our model" or "our calculation"
- **Actual data**: World Bank API data marked as "actual data"
- **Projections**: Clearly labeled as "our projection"
- **Assessments**: Clearly labeled as "our assessment"

### No Unsupported Claims
- Every claim backed by data in the notebook
- No external references without data
- Clear distinction between model and reality

### Reproducible
- All code included in notebook
- Data files referenced from parent directory
- Can be re-run to verify results

---

##  Data Files Used

The notebook loads data from the parent directory:

```
../us_healthcare_breakdown.csv
../us_treatment_vs_overhead.csv
../international_admin_comparison.csv
../potential_admin_savings.csv
../healthcare_merged_data.csv
../current_healthcare_costs_by_bracket.csv
../scenario_singapore_hybrid.csv
../scenario_single_payer_universal.csv
../scenario_multi_payer_universal.csv
../scenario_public_option.csv
../aggregate_savings_comparison.csv
../insurance_workforce_current.csv
../workforce_needs_by_model.csv
../skill_transferability.csv
../workforce_transition_costs.csv
../us_medical_rd_breakdown.csv
../international_rd_comparison.csv
../rd_scenarios_universal_healthcare.csv
../optimal_model_scores.csv
```

---

##  Generated Visualizations

The notebook generates and saves:

1. `healthcare_spending_breakdown.png` - US spending pie and bar charts
2. `international_comparison.png` - Admin costs comparison
3. `world_bank_data.png` - Real international data (4 panels)
4. `income_bracket_analysis.png` - Savings by bracket (4 panels)
5. `aggregate_savings.png` - Total national savings
6. `workforce_analysis.png` - Workforce transition (4 panels)
7. `rd_analysis.png` - R&D preservation (4 panels)

All at 300 DPI, publication-ready quality.

---

##  Summary of Findings

### From Our Models and Calculations:

**Administrative Overhead**
- Our model: 13.8% of spending
- Potential savings: $350-450B/year (our calculation)

**Income Impact**
- 96% of households save money (our model)
- Only top income bracket pays more

**Workforce**
- 1.1M jobs displaced (our projection)
- 8.1/10 average transferability (our assessment)
- $36B transition cost (our calculation)

**R&D**
- Can be maintained at $270-280B (our projection)
- Current: $275B (our model)

### From World Bank API (Actual Data):

**US Healthcare (2023)**
- Spending: 16.5% of GDP
- Per capita: $12,434
- Life expectancy: 78.4 years
- Out-of-pocket: varies by country

---

##  Important Notes

### Data Sources
1. **World Bank API**: Actual international healthcare data
2. **Our Models**: All other data based on our modeling assumptions
3. **Calculations**: Derived from our model data

### Limitations
- Models based on assumptions
- Actual implementation would differ
- Political/regulatory factors not modeled
- Transition complexity simplified

### Transparency
Every claim in the notebook is:
- Backed by data we generated
- Clearly labeled as model/calculation/projection
- Distinguishable from actual data

---

##  Requirements

```python
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyter>=1.0.0
```

Install from parent directory:
```bash
pip install -r ../../requirements.txt
```

---

##  How to Use

### View the Notebook
```bash
jupyter notebook healthcare_analysis.ipynb
```

### Run All Cells
1. Open notebook
2. Click "Kernel"  "Restart & Run All"
3. Wait for all cells to execute
4. Review results and visualizations

### Export Results
- **PDF**: File  Download as  PDF
- **HTML**: File  Download as  HTML
- **Images**: All charts saved as PNG files

---

##  Verification

The notebook has been designed to:
-  Only make claims backed by our data
-  Clearly label all data sources
-  Distinguish model from reality
-  Acknowledge limitations
-  Provide reproducible analysis

---

##  Questions Answered

### Q1: Treatment vs Insurance Processing?
**Answer**: 76.1% treatment, 13.8% admin (from our model)

### Q2: How much could we save?
**Answer**: $350-450B annually (our calculation)

### Q3: Impact on income brackets?
**Answer**: 96% save money (our model)

### Q4: What about insurance workers?
**Answer**: 1.1M displaced, 8.1/10 transferability (our projection/assessment)

### Q5: Can we preserve R&D?
**Answer**: Yes, $270-280B maintained (our projection)

---

##  For Researchers

This notebook is designed for:
- Academic review
- Policy analysis
- Further research
- Methodology validation

All assumptions and calculations are transparent and reproducible.

---

**Created**: November 2025  
**Status**: Complete  
**Data**: Model-based with World Bank API validation  
**Transparency**: All claims clearly labeled and backed by data
