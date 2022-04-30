from solver import *


def cauchy_euler(params,Func):
    # Initial Condition
    t0 = params['t0']
    t_akhir = params['t_akhir']
    h = params['h']
    y0 = params['y0']
    dy0 = params['dy0']

    res_euler = []
    t = []
    step = int((t_akhir - t0) / h)

    for i in range(step):
        tm = (i + 1) * h
        (y_next, dy_next) = euler(tm, h, y0, dy0, Func)
        res_euler.append(y_next)
        t.append(tm)
        y0 = y_next
        dy0 = dy_next

    return (t,res_euler)

def cauchy_eulercromer(params,Func):
    # Initial Condition
    t0 = params['t0']
    t_akhir = params['t_akhir']
    h = params['h']
    y0 = params['y0']
    dy0 = params['dy0']

    res_euler_cromer = []
    t = []
    step = int((t_akhir - t0) / h)

    for i in range(step):
        tm = (i + 1) * h
        (y_next, dy_next) = euler_cromer(tm, h, y0, dy0, Func)
        res_euler_cromer.append(y_next)
        t.append(tm)
        y0 = y_next
        dy0 = dy_next
    return (t, res_euler_cromer)

for i in range(step):
    tm = (i + 1) * h
    (u_next, du_next) = euler_cromer(tm, h, u0, du0, Func)
    res_eulercromer.append(u_next)
    t.append(tm)
    u0 = u_next
    du0 = du_next


plt.title('Non Linear Pendulum h =0.01')
plt.plot(t,res_euler,color='r', label = 'Euler')
plt.plot(t,res_eulercromer,color='g', label = 'Euler Cromer')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.legend()

plt.show()

