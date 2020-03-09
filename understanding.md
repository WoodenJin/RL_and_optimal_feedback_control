# RL and Optimal Feedback Control

系统方程：
$$
\dot{x}(t)=f(x(t))+g(x(t))u(t)
$$
代价函数：
$$
J(t_0,x_0,u(\cdot))=\int^{\infty}_{t_0}r(x(\tau;t_0,x_0,u(\cdot)),u(\tau))d\tau
$$
将$r$设置为仿射二次型：
$$
r(x,u)\equiv Q(x)+u^TRu
$$
value function 为：
$$
V^*(x)\equiv \inf_{u[t,\infty]}{J(t,x,u(\cdot))}
$$
控制律(状态反馈控制)：
$$
u^*(x)=-\frac{1}{2}R^{-1}g^T(x)(\bigtriangledown V^*(x))^T
$$
为什么设置的最优控制与系统的动力学部分不相关$f(x)$？为什么没有引入进去？$g(x)$是关于系统驱动器和响应的关系。

如果引入约束：

