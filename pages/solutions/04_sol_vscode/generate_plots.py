import numpy as np
import matplotlib.pyplot as plt

v0 = 12.0          
alpha_deg = 45.0   
g = 9.81
m = 1.0
b = 0.15

alpha = np.radians(alpha_deg)
v0x = v0 * np.cos(alpha)
v0y = v0 * np.sin(alpha)

t_flight = (2 * v0y) / g
t_no_drag = np.linspace(0, t_flight, 300)
x_no_drag = v0x * t_no_drag
y_no_drag = v0y * t_no_drag - 0.5 * g * t_no_drag**2

dt = 0.005
x_drag, y_drag, t_drag = [0.0], [0.0], [0.0]
vx, vy = v0x, v0y
t_curr = 0.0

while y_drag[-1] >= 0 and t_curr < 10:
    ax = -(b/m) * vx
    ay = -g - (b/m) * vy
    vx += ax * dt
    vy += ay * dt
    x_drag.append(x_drag[-1] + vx * dt)
    y_drag.append(y_drag[-1] + vy * dt)
    t_curr += dt
    t_drag.append(t_curr)

plt.figure(figsize=(8, 5))
plt.plot(x_no_drag, y_no_drag, 'b-', label='Bez oporu powietrza')
plt.plot(x_drag, y_drag, 'r--', label='Z oporem powietrza')
plt.title(f'Trajektoria rzutu ukośnego ($v_0 = {v0}$ m/s, $\\alpha = {alpha_deg}^\\circ$)')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.ylim(bottom=0)
plt.grid(True)
plt.legend()
plt.savefig('pages/solutions/04_sol_vscode/trajektoria.png', dpi=150, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(t_no_drag, y_no_drag, 'b-', label='Bez oporu powietrza')
plt.plot(t_drag, y_drag, 'r--', label='Z oporem powietrza')
plt.title('Wysokość w zależności od czasu $y(t)$')
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.ylim(bottom=0)
plt.grid(True)
plt.legend()
plt.savefig('pages/solutions/04_sol_vscode/wysokosc_czas.png', dpi=150, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(t_no_drag, x_no_drag, 'b-', label='Bez oporu powietrza')
plt.plot(t_drag, x_drag, 'r--', label='Z oporem powietrza')
plt.title('Zasięg w zależności od czasu $x(t)$')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.grid(True)
plt.legend()
plt.savefig('pages/solutions/04_sol_vscode/zasieg_czas.png', dpi=150, bbox_inches='tight')
plt.close()

print("Wygenerowano pliki graficzne!")
