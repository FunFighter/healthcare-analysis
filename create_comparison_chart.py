"""
Create comprehensive comparison chart for Current vs Singapore Model
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Data
metrics = [
    'Administrative Costs',
    'Potential Savings',
    'Per Capita Savings',
    'Households That Save',
    'Jobs Displaced',
    'Workforce Transferability',
    'Transition Cost',
    'R&D Spending'
]

current = [
    '13.8%',
    '$0',
    '$0',
    'N/A',
    '0',
    '8.1/10',
    '$0',
    '$275B'
]

singapore = [
    '3.5% (model)',
    '$508B (calc)',
    '$1,515 (calc)',
    '96.1% (model)',
    '1,109,950 (proj)',
    '8.1/10 (assess)',
    '$36.1B (calc)',
    '$275B (proj)'
]

# Create figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')

# Title
fig.suptitle('Healthcare System Comparison', fontsize=20, fontweight='bold', y=0.98)
ax.text(0.5, 0.95, 'Current System vs Singapore Hybrid Model', 
        ha='center', fontsize=14, style='italic', transform=ax.transAxes)

# Table parameters
n_rows = len(metrics)
cell_height = 0.08
table_top = 0.88
col_widths = [0.35, 0.30, 0.30]
col_positions = [0.05, 0.40, 0.70]

# Colors
header_color = '#2c3e50'
current_color = '#e74c3c'
singapore_color = '#2ecc71'
row_colors = ['#ecf0f1', '#ffffff']

# Draw headers
headers = ['Metric', 'Current System', 'Singapore Model']
header_colors = [header_color, current_color, singapore_color]

for i, (header, pos, width, color) in enumerate(zip(headers, col_positions, col_widths, header_colors)):
    # Header box
    rect = FancyBboxPatch((pos, table_top), width, cell_height,
                          boxstyle="round,pad=0.01", 
                          facecolor=color, edgecolor='white', linewidth=2,
                          transform=ax.transAxes, zorder=2)
    ax.add_patch(rect)
    
    # Header text
    ax.text(pos + width/2, table_top + cell_height/2, header,
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='white', transform=ax.transAxes, zorder=3)

# Draw data rows
for i, (metric, curr, sing) in enumerate(zip(metrics, current, singapore)):
    y_pos = table_top - (i + 1) * cell_height
    
    # Alternating row colors
    row_color = row_colors[i % 2]
    
    # Metric cell (left column)
    rect = FancyBboxPatch((col_positions[0], y_pos), col_widths[0], cell_height,
                          boxstyle="round,pad=0.005",
                          facecolor=row_color, edgecolor='#bdc3c7', linewidth=1,
                          transform=ax.transAxes, zorder=1)
    ax.add_patch(rect)
    ax.text(col_positions[0] + 0.01, y_pos + cell_height/2, metric,
            ha='left', va='center', fontsize=11, fontweight='bold',
            transform=ax.transAxes, zorder=2)
    
    # Current value cell
    rect = FancyBboxPatch((col_positions[1], y_pos), col_widths[1], cell_height,
                          boxstyle="round,pad=0.005",
                          facecolor=row_color, edgecolor='#bdc3c7', linewidth=1,
                          transform=ax.transAxes, zorder=1)
    ax.add_patch(rect)
    ax.text(col_positions[1] + col_widths[1]/2, y_pos + cell_height/2, curr,
            ha='center', va='center', fontsize=10,
            transform=ax.transAxes, zorder=2)
    
    # Singapore value cell
    rect = FancyBboxPatch((col_positions[2], y_pos), col_widths[2], cell_height,
                          boxstyle="round,pad=0.005",
                          facecolor=row_color, edgecolor='#bdc3c7', linewidth=1,
                          transform=ax.transAxes, zorder=1)
    ax.add_patch(rect)
    
    # Highlight improvements in green
    text_color = 'black'
    text_weight = 'normal'
    if metric in ['Potential Savings', 'Per Capita Savings', 'Households That Save']:
        text_color = '#27ae60'
        text_weight = 'bold'
    elif metric == 'Administrative Costs':
        text_color = '#27ae60'
        text_weight = 'bold'
    
    ax.text(col_positions[2] + col_widths[2]/2, y_pos + cell_height/2, sing,
            ha='center', va='center', fontsize=10, color=text_color, weight=text_weight,
            transform=ax.transAxes, zorder=2)

# Add legend for labels
legend_y = table_top - (n_rows + 1) * cell_height - 0.05
ax.text(0.05, legend_y, 'Legend:', fontsize=10, fontweight='bold', transform=ax.transAxes)
ax.text(0.05, legend_y - 0.03, '(model) = Based on our model assumptions', fontsize=9, transform=ax.transAxes)
ax.text(0.05, legend_y - 0.06, '(calc) = Calculated from our model', fontsize=9, transform=ax.transAxes)
ax.text(0.05, legend_y - 0.09, '(proj) = Our projection', fontsize=9, transform=ax.transAxes)
ax.text(0.05, legend_y - 0.12, '(assess) = Our assessment', fontsize=9, transform=ax.transAxes)

# Add key insights box
insights_y = legend_y - 0.20
insights_box = FancyBboxPatch((0.05, insights_y - 0.15), 0.90, 0.14,
                             boxstyle="round,pad=0.01",
                             facecolor='#e8f8f5', edgecolor='#27ae60', linewidth=2,
                             transform=ax.transAxes, zorder=1)
ax.add_patch(insights_box)

ax.text(0.50, insights_y - 0.02, 'Key Findings from Our Analysis', 
        ha='center', fontsize=11, fontweight='bold', color='#27ae60',
        transform=ax.transAxes, zorder=2)

findings = [
    '• Administrative costs reduced from 13.8% to 3.5% (our model)',
    '• Potential savings: $508B annually ($1,515 per person) (our calculation)',
    '• 96.1% of households save money (our model)',
    '• R&D spending maintained at $275B (our projection)'
]

for i, finding in enumerate(findings):
    ax.text(0.07, insights_y - 0.05 - i*0.025, finding,
            ha='left', fontsize=9, transform=ax.transAxes, zorder=2)

# Add note at bottom
ax.text(0.50, 0.01, 'All figures based on our models and calculations. See notebook for detailed methodology.',
        ha='center', fontsize=8, style='italic', color='#7f8c8d',
        transform=ax.transAxes)

plt.tight_layout()
plt.savefig('comprehensive_comparison_chart.png', dpi=300, bbox_inches='tight', facecolor='white')
print("Chart saved: comprehensive_comparison_chart.png")
plt.show()
