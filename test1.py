import matplotlib.pyplot as plt
import numpy as np

# Utworzenie wykresu
fig, ax = plt.subplots(figsize=(10, 8))

# Parametry przykładowe
I = 1.0  # prąd (amplituda)
U_R = 3.0  # napięcie na rezystorze
U_L = 4.0  # napięcie na cewce
U_C = 2.0  # napięcie na kondensatorze

# Pozycje fazorow (kąty w radianach)
# Prąd jako referencja (0°)
angle_I = 0

# Napięcia
angle_U_R = 0  # w fazie z prądem
angle_U_L = np.pi/2  # +90°
angle_U_C = -np.pi/2  # -90°

# Napięcie wypadkowe
U_L_net = U_L - U_C  # różnica napięć reaktancyjnych
U = np.sqrt(U_R**2 + U_L_net**2)  # napięcie całkowite
angle_U = np.arctan2(U_L_net, U_R)  # kąt fazowy

# Rysowanie fazorow
arrow_props = dict(arrowstyle='->', lw=2.5)

# Prąd I (czerwony, grubszy)
ax.annotate('', xy=(I*np.cos(angle_I), I*np.sin(angle_I)), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=3, color='red'))
ax.text(I*np.cos(angle_I)+0.15, I*np.sin(angle_I), 'I', fontsize=16, 
        fontweight='bold', color='red')

# Napięcie U_R (niebieski)
ax.annotate('', xy=(U_R*np.cos(angle_U_R), U_R*np.sin(angle_U_R)), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=2.5, color='blue'))
ax.text(U_R*np.cos(angle_U_R)-0.3, U_R*np.sin(angle_U_R)-0.3, '$U_R$', 
        fontsize=14, color='blue')

# Napięcie U_L (zielony)
ax.annotate('', xy=(U_L*np.cos(angle_U_L), U_L*np.sin(angle_U_L)), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=2.5, color='green'))
ax.text(U_L*np.cos(angle_U_L)+0.2, U_L*np.sin(angle_U_L), '$U_L$', 
        fontsize=14, color='green')

# Napięcie U_C (fioletowy)
ax.annotate('', xy=(U_C*np.cos(angle_U_C), U_C*np.sin(angle_U_C)), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=2.5, color='purple'))
ax.text(U_C*np.cos(angle_U_C)+0.2, U_C*np.sin(angle_U_C), '$U_C$', 
        fontsize=14, color='purple')

# Napięcie całkowite U (pomarańczowy, grubsze)
ax.annotate('', xy=(U*np.cos(angle_U), U*np.sin(angle_U)), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=3.5, color='orange'))
ax.text(U*np.cos(angle_U)+0.2, U*np.sin(angle_U)+0.2, '$U$', 
        fontsize=16, fontweight='bold', color='orange')

# Kąt fazowy φ
angle_arc = np.linspace(0, angle_U, 50)
arc_radius = 1.0
ax.plot(arc_radius*np.cos(angle_arc), arc_radius*np.sin(angle_arc), 
        'k--', lw=1.5)
ax.text(0.7, 0.5, f'φ = {np.degrees(angle_U):.1f}°', fontsize=12)

# Linie pomocnicze (przerywane)
ax.plot([0, U_R], [0, U_L_net], 'k--', lw=1, alpha=0.3)
ax.plot([U_R, U_R], [0, U_L_net], 'k--', lw=1, alpha=0.3)

# Osie współrzędnych
ax.axhline(y=0, color='k', linestyle='-', lw=0.5, alpha=0.5)
ax.axvline(x=0, color='k', linestyle='-', lw=0.5, alpha=0.5)

# Ustawienia wykresu
ax.set_xlim(-1, 5)
ax.set_ylim(-3, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_xlabel('Oś rzeczywista (Re)', fontsize=12)
ax.set_ylabel('Oś urojona (Im)', fontsize=12)
ax.set_title('Diagram fazorowy dla obwodu szeregowego RLC\n(Fazory obracają się przeciwnie do ruchu wskazówek zegara)', 
             fontsize=14, fontweight='bold')

# Legenda
legend_elements = [
    plt.Line2D([0], [0], color='red', lw=3, label='Prąd I (referencja)'),
    plt.Line2D([0], [0], color='blue', lw=2.5, label='$U_R$ (w fazie z I)'),
    plt.Line2D([0], [0], color='green', lw=2.5, label='$U_L$ (wyprzedza I o 90°)'),
    plt.Line2D([0], [0], color='purple', lw=2.5, label='$U_C$ (opóźnia I o 90°)'),
    plt.Line2D([0], [0], color='orange', lw=3.5, label='$U$ (napięcie całkowite)')
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

# Adnotacje
textstr = f'Parametry:\n$U_R$ = {U_R} V\n$U_L$ = {U_L} V\n$U_C$ = {U_C} V\n$U_{{L}} - U_{{C}}$ = {U_L_net} V\n$|U|$ = {U:.2f} V'
ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()

print("Diagram fazorowy został zapisany!")