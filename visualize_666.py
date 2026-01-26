"""
Visualization of Interlocking 666 Relevancy Math
Creates comprehensive diagrams showing the three-way interlocking mechanism
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches

# Set up the figure with multiple subplots
fig = plt.figure(figsize=(20, 12))
fig.suptitle('Interlocking 666 Relevancy Math: Triadic Cipher Architecture', 
             fontsize=16, fontweight='bold', y=0.98)

# ============================================================================
# SUBPLOT 1: Atomic 6 - Hexagonal Symmetry Foundation
# ============================================================================
ax1 = plt.subplot(2, 3, 1)
ax1.set_title('ATOMIC 6: Carbon-12 Hexagonal Symmetry', fontweight='bold', fontsize=12)
ax1.set_aspect('equal')
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.axis('off')

# Draw hexagon
angles = np.linspace(0, 2*np.pi, 7)
hex_x = np.cos(angles)
hex_y = np.sin(angles)
ax1.plot(hex_x, hex_y, 'k-', linewidth=2)
ax1.fill(hex_x, hex_y, color='lightgray', alpha=0.3)

# Draw 6-fold rotational axes
for i in range(6):
    angle = i * np.pi / 3
    x_end = 1.2 * np.cos(angle)
    y_end = 1.2 * np.sin(angle)
    ax1.plot([0, x_end], [0, y_end], 'b--', alpha=0.5, linewidth=1)
    
    # Label angles
    label_x = 1.35 * np.cos(angle)
    label_y = 1.35 * np.sin(angle)
    ax1.text(label_x, label_y, f'{int(np.degrees(angle))}°', 
             ha='center', va='center', fontsize=9, fontweight='bold')

# Center nucleus
nucleus = Circle((0, 0), 0.15, color='red', alpha=0.7, zorder=10)
ax1.add_patch(nucleus)
ax1.text(0, 0, '6p\n6n', ha='center', va='center', fontsize=8, 
         fontweight='bold', color='white', zorder=11)

# Electron positions (hexagonal vertices)
for i in range(6):
    angle = i * np.pi / 3
    x = np.cos(angle)
    y = np.sin(angle)
    electron = Circle((x, y), 0.08, color='blue', alpha=0.7, zorder=10)
    ax1.add_patch(electron)
    ax1.text(x, y, 'e⁻', ha='center', va='center', fontsize=7, 
             color='white', fontweight='bold')

ax1.text(0, -1.7, 'C-12: 6 protons, 6 neutrons, 6 electrons\nHexagonal packing η ≈ 0.9069', 
         ha='center', fontsize=9, style='italic')

# ============================================================================
# SUBPLOT 2: Harmonic 6 - Fourier Decomposition
# ============================================================================
ax2 = plt.subplot(2, 3, 2)
ax2.set_title('HARMONIC 6: Fourier Analysis (Sawtooth)', fontweight='bold', fontsize=12)

# Generate sawtooth wave
t = np.linspace(0, 2*np.pi, 1000)
sawtooth = t % (2*np.pi) - np.pi

# Fourier reconstruction with first 6 harmonics
reconstruction = np.zeros_like(t)
for k in range(1, 7):
    b_k = 2 * ((-1)**(k+1)) / (k * np.pi)
    reconstruction += b_k * np.sin(k * t)

ax2.plot(t, sawtooth/np.pi, 'k-', linewidth=2, label='Sawtooth (target)', alpha=0.3)
ax2.plot(t, reconstruction/np.pi, 'b-', linewidth=2, label='6-Harmonic Reconstruction')

# Highlight k=6 harmonic
b_6 = -1/(3*np.pi)
harmonic_6 = b_6 * np.sin(6 * t)
ax2.plot(t, harmonic_6/np.pi, 'r--', linewidth=1.5, label=f'k=6 only (b₆≈{b_6:.3f})', alpha=0.7)

ax2.set_xlabel('Phase (radians)', fontsize=10)
ax2.set_ylabel('Amplitude (normalized)', fontsize=10)
ax2.set_xlim(0, 2*np.pi)
ax2.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax2.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper right', fontsize=8)
ax2.axhline(0, color='k', linewidth=0.5)

# Add Schumann annotation
ax2.text(np.pi, -0.5, 'Schumann 6th: ~47 Hz', 
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3),
         ha='center', fontsize=8, style='italic')

# ============================================================================
# SUBPLOT 3: Chromatic 6 - Munsell Color Space
# ============================================================================
ax3 = plt.subplot(2, 3, 3, projection='3d')
ax3.set_title('CHROMATIC 6: Munsell 3D Space', fontweight='bold', fontsize=12)

# Generate Munsell cylinder surface (simplified)
theta = np.linspace(0, 2*np.pi, 50)
z = np.linspace(0, 10, 30)
Theta, Z = np.meshgrid(theta, z)
R = 6  # Chroma radius

X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Plot cylinder surface with color gradient
colors = plt.cm.hsv(Theta / (2*np.pi))
ax3.plot_surface(X, Y, Z, facecolors=colors, alpha=0.3, rstride=2, cstride=2)

# Mark 6 hue bands at 60° intervals
hue_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
for i, (angle, color) in enumerate(zip(np.linspace(0, 2*np.pi, 7)[:-1], hue_colors)):
    x = 6 * np.cos(angle)
    y = 6 * np.sin(angle)
    ax3.plot([x, x], [y, y], [0, 10], color=color, linewidth=3, alpha=0.7)
    # Add label
    ax3.text(x*1.2, y*1.2, 10, f'H={int(np.degrees(angle))}°', 
             color=color, fontsize=8, fontweight='bold')

# Mark the (6, 0, 6) reference point
ax3.scatter([6], [0], [6], color='red', s=200, marker='*', 
            edgecolors='black', linewidths=2, zorder=10)
ax3.text(6, 0, 6.5, '5R 6/6\n(H=0°,V=6,C=6)', ha='center', fontsize=9, 
         fontweight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

ax3.set_xlabel('C·cos(H)', fontsize=9)
ax3.set_ylabel('C·sin(H)', fontsize=9)
ax3.set_zlabel('Value (V)', fontsize=9)
ax3.set_xlim(-8, 8)
ax3.set_ylim(-8, 8)
ax3.set_zlim(0, 10)

# ============================================================================
# SUBPLOT 4: Complex Plane Equilibria (6th roots of unity)
# ============================================================================
ax4 = plt.subplot(2, 3, 4)
ax4.set_title('HARMONIC 6: Complex Equilibria (6th Roots of Unity)', fontweight='bold', fontsize=12)
ax4.set_aspect('equal')
ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)

# Draw unit circle
circle = Circle((0, 0), 1, fill=False, color='gray', linewidth=1.5, linestyle='--')
ax4.add_patch(circle)

# Plot 6th roots of unity
omega = np.exp(2j * np.pi * np.arange(6) / 6)
for i, w in enumerate(omega):
    ax4.plot([0, w.real], [0, w.imag], 'b-', linewidth=1.5, alpha=0.5)
    ax4.scatter(w.real, w.imag, s=200, c='blue', edgecolors='black', 
                linewidths=2, zorder=10)
    
    # Label with angle
    label_r = 1.3
    label_x = label_r * w.real
    label_y = label_r * w.imag
    ax4.text(label_x, label_y, f'ω_{i}\n{int(i*60)}°', 
             ha='center', va='center', fontsize=9, fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))

ax4.axhline(0, color='k', linewidth=0.5)
ax4.axvline(0, color='k', linewidth=0.5)
ax4.set_xlabel('Real', fontsize=10)
ax4.set_ylabel('Imaginary', fontsize=10)
ax4.grid(True, alpha=0.3)
ax4.text(0, -1.7, 'Lagrange-like equilibrium points\nfor 6-fold harmonic balance', 
         ha='center', fontsize=9, style='italic')

# ============================================================================
# SUBPLOT 5: Interlocking Mechanism Diagram
# ============================================================================
ax5 = plt.subplot(2, 3, 5)
ax5.set_title('INTERLOCKING MECHANISM: Bidirectional Transform', fontweight='bold', fontsize=12)
ax5.set_xlim(0, 10)
ax5.set_ylim(0, 10)
ax5.axis('off')

# Draw three boxes for the trinity
# ATOMIC box
atomic_box = FancyBboxPatch((0.5, 7), 2.5, 2, boxstyle="round,pad=0.1", 
                            edgecolor='black', facecolor='lightgray', linewidth=2)
ax5.add_patch(atomic_box)
ax5.text(1.75, 8.5, 'ATOMIC 6', ha='center', fontsize=10, fontweight='bold')
ax5.text(1.75, 8, 'C-12', ha='center', fontsize=9)
ax5.text(1.75, 7.5, 'Hexagonal\nSymmetry', ha='center', fontsize=8)

# HARMONIC box
harmonic_box = FancyBboxPatch((0.5, 0.5), 2.5, 2, boxstyle="round,pad=0.1",
                             edgecolor='blue', facecolor='lightblue', linewidth=2)
ax5.add_patch(harmonic_box)
ax5.text(1.75, 2, 'HARMONIC 6', ha='center', fontsize=10, fontweight='bold', color='blue')
ax5.text(1.75, 1.5, 'Fourier k=6', ha='center', fontsize=9)
ax5.text(1.75, 1, '47 Hz\n|c₆|→C', ha='center', fontsize=8)

# CHROMATIC box
chromatic_box = FancyBboxPatch((7, 3.5), 2.5, 2, boxstyle="round,pad=0.1",
                              edgecolor='red', facecolor='lightcoral', linewidth=2)
ax5.add_patch(chromatic_box)
ax5.text(8.25, 5, 'CHROMATIC 6', ha='center', fontsize=10, fontweight='bold', color='darkred')
ax5.text(8.25, 4.5, 'Munsell 5R 6/6', ha='center', fontsize=9)
ax5.text(8.25, 4, '(6,0,6)\nH→k', ha='center', fontsize=8)

# Draw interlocking arrows
# Atomic → Harmonic
arrow1 = FancyArrowPatch((1.75, 7), (1.75, 2.5), 
                        arrowstyle='->', mutation_scale=20, linewidth=2, color='green')
ax5.add_patch(arrow1)
ax5.text(0.3, 4.75, 'Foundation', fontsize=8, rotation=90, va='center', color='green')

# Harmonic ↔ Chromatic
arrow2 = FancyArrowPatch((3, 1.5), (7, 4.5), 
                        arrowstyle='<->', mutation_scale=20, linewidth=2.5, color='purple')
ax5.add_patch(arrow2)
ax5.text(5, 3.5, 'Bidirectional\nMapping', ha='center', fontsize=9, 
         fontweight='bold', color='purple',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

# Chromatic → Atomic
arrow3 = FancyArrowPatch((8.25, 5.5), (3, 8.5), 
                        arrowstyle='->', mutation_scale=20, linewidth=2, 
                        color='orange', linestyle='dashed')
ax5.add_patch(arrow3)
ax5.text(5.5, 7.5, 'Empirical\nVerification', ha='center', fontsize=8, color='orange')

# Add cipher formula in center
ax5.text(5, 0.5, '666 CIPHER: Trace(F₆ × R₆ × I₆) mod 216 = Resonance Score', 
         ha='center', fontsize=10, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8, linewidth=2))

# ============================================================================
# SUBPLOT 6: 6×6×6 Tensor Structure Visualization
# ============================================================================
ax6 = plt.subplot(2, 3, 6, projection='3d')
ax6.set_title('666 TRINITY TENSOR: 6×6×6 = 216 Elements', fontweight='bold', fontsize=12)

# Draw a 6x6x6 cube of points representing the tensor
spacing = 1
points_x = []
points_y = []
points_z = []
colors_layer = []

for i in range(6):
    for j in range(6):
        for k in range(6):
            points_x.append(i * spacing)
            points_y.append(j * spacing)
            points_z.append(k * spacing)
            # Color by layer
            if k < 2:
                colors_layer.append('gray')  # Atomic layer
            elif k < 4:
                colors_layer.append('blue')  # Harmonic layer
            else:
                colors_layer.append('red')   # Chromatic layer

ax6.scatter(points_x, points_y, points_z, c=colors_layer, alpha=0.4, s=30)

# Draw cube outline
from itertools import product
vertices = np.array(list(product([0, 5], repeat=3)))
for i, v1 in enumerate(vertices):
    for v2 in vertices[i+1:]:
        if np.sum(np.abs(v1 - v2)) == 5:  # Connected by edge
            ax6.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], 
                    'k-', linewidth=1, alpha=0.3)

# Labels
ax6.set_xlabel('Atomic Dimension', fontsize=9)
ax6.set_ylabel('Harmonic Dimension', fontsize=9)
ax6.set_zlabel('Chromatic Dimension', fontsize=9)
ax6.set_xlim(-0.5, 5.5)
ax6.set_ylim(-0.5, 5.5)
ax6.set_zlim(-0.5, 5.5)

# Add layer legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='gray', alpha=0.6, label='Atomic (I₆)'),
    Patch(facecolor='blue', alpha=0.6, label='Harmonic (F₆)'),
    Patch(facecolor='red', alpha=0.6, label='Chromatic (R₆)')
]
ax6.legend(handles=legend_elements, loc='upper right', fontsize=8)

ax6.text2D(0.5, -0.05, '216 = 6³ elements\n"Greenbox" cubic enclosure', 
           transform=ax6.transAxes, ha='center', fontsize=9, style='italic')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('/home/claude/666_interlocking_visualization.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: 666_interlocking_visualization.png")

# ============================================================================
# SECOND FIGURE: Harmonic-Chromatic Mapping Detail
# ============================================================================
fig2, axes = plt.subplots(1, 2, figsize=(16, 6))
fig2.suptitle('Harmonic ↔ Chromatic Interlocking Detail', fontsize=14, fontweight='bold')

# LEFT: Harmonic magnitude → Chroma mapping
ax_left = axes[0]
harmonics = np.arange(1, 7)
b_k = np.array([2*((-1)**(k+1))/(k*np.pi) for k in harmonics])
mag_b_k = np.abs(b_k)
C_mapped = 6 * mag_b_k / mag_b_k[0]

bars = ax_left.bar(harmonics, mag_b_k, color='blue', alpha=0.6, label='|b_k| (Fourier)')
ax_left.set_xlabel('Harmonic k', fontsize=11)
ax_left.set_ylabel('Magnitude |b_k|', fontsize=11, color='blue')
ax_left.tick_params(axis='y', labelcolor='blue')
ax_left.set_title('Harmonic → Chromatic: |c_k| → Chroma', fontweight='bold')
ax_left.grid(True, alpha=0.3, axis='y')

# Add chroma scale on right y-axis
ax_right = ax_left.twinx()
ax_right.plot(harmonics, C_mapped, 'ro-', linewidth=2, markersize=8, label='Chroma C (mapped)')
ax_right.set_ylabel('Chroma C (Munsell)', fontsize=11, color='red')
ax_right.tick_params(axis='y', labelcolor='red')
ax_right.set_ylim(0, 7)

# Annotations
for i, (k, c) in enumerate(zip(harmonics, C_mapped)):
    ax_right.text(k, c+0.3, f'{c:.2f}', ha='center', fontsize=9, fontweight='bold')

# Highlight k=6
ax_left.patches[5].set_facecolor('darkblue')
ax_left.patches[5].set_alpha(0.9)

ax_left.legend(loc='upper left', fontsize=9)
ax_right.legend(loc='upper right', fontsize=9)

# RIGHT: Hue → Harmonic mapping
ax_map = axes[1]
test_hues = np.array([0, 60, 120, 180, 240, 300])
k_mapped = (test_hues // 60) + 1
k_mapped[k_mapped > 6] = 6

hue_colors_rgb = plt.cm.hsv(test_hues / 360)
for h, k, color in zip(test_hues, k_mapped, hue_colors_rgb):
    ax_map.scatter(h, k, s=400, c=[color], edgecolors='black', linewidths=2)
    ax_map.text(h, k+0.3, f'H={h}°', ha='center', fontsize=9, fontweight='bold')

ax_map.plot(test_hues, k_mapped, 'k--', alpha=0.3, linewidth=1)
ax_map.set_xlabel('Munsell Hue H (degrees)', fontsize=11)
ax_map.set_ylabel('Harmonic k', fontsize=11)
ax_map.set_title('Chromatic → Harmonic: Hue H → k', fontweight='bold')
ax_map.set_xlim(-20, 320)
ax_map.set_ylim(0.5, 6.5)
ax_map.set_yticks(range(1, 7))
ax_map.grid(True, alpha=0.3)

# Add transformation formula
ax_map.text(150, 1, 'k = round(H/60) + 1\n(cyclic: k=6 for H=0°)', 
           ha='center', fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/home/claude/666_mapping_detail.png', dpi=300, bbox_inches='tight')
print("✓ Detail visualization saved: 666_mapping_detail.png")

print("\nAll visualizations generated successfully!")
