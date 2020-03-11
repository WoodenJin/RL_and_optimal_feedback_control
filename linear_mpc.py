import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-deep")

x0 = (np.random.random(1)[0] - 0.5) * 10

x = []
u = []
temp_u = 0
for i in range(40):
    x.append(x0)
    temp_u = 3 * x0 / 5
    temp_u = -min(max(-1, temp_u), 1)
    u.append(temp_u)
    x0 = x0 + temp_u
    pass

fig = plt.figure(figsize=[8, 6])
ax1 = fig.add_subplot(111)
l1 = ax1.plot(x, lw=3, color='C1', label='trajectory', marker='o')
ax1.set_ylim([-5, 5])
ax1.set_ylabel('x')
ax1.set_xlim(0, len(x))
ax1.yaxis.label.set_color('C1')
ax2 = ax1.twinx()
l2 = ax2.plot(u, lw=3, color='C3', label='actuator', marker='o')
ax2.set_ylim(-1, 1)
ax2.set_ylabel('u')
ax2.yaxis.label.set_color('C3')
# plt.legend(handles=[l1, l2, ], labels=['trajectory', 'actuator'], loc='best')
plt.savefig('./linear_mpc.png')
plt.show()

x = np.linspace(-3, 3, 50)
u = np.zeros(50)
for i in range(50):
    temp_u = 3 * x[i] / 5
    temp_u = -min(max(-1, temp_u), 1)
    u[i] = temp_u
    pass
fig = plt.figure(figsize=[8, 6])
plt.plot(x,u)
plt.show()