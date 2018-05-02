% script for calculating lagrange points
grav = 6.67408e-11; m_sun = 1.98855e30; r_se = 149600000e3;
m_earth = 5.97219e24;
v_earth = sqrt(grav*m_sun/r_se);
w_earth = v_earth/r_se;

syms r
r_lagr = vpa(solve(m_sun/(r_se - r)^2 == m_earth/r^2 + m_sun/r_se^2 - r*(m_sun + m_earth)/r_se^3, r));
r_lagr = r_se*nthroot(m_earth/(3*m_sun),3);
v_lagr = w_earth*(r_se - r_lagr(1))
r_se - r_lagr(1)
