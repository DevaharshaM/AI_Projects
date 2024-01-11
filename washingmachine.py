# import library
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# define membership functions of all linguistic values
xDirtness = np.arange(0,100,1)
xLoad = np.arange(0,100,1)
xTime = np.arange(0,60,1)

member_dirtness_small = fuzz.trimf(xDirtness, [0, 0, 50])
member_dirtness_med = fuzz.trimf(xDirtness, [0, 50, 100])
member_dirtness_large = fuzz.trimf(xDirtness, [50, 100, 100])
member_load_small = fuzz.trimf(xLoad, [0, 0, 50])
member_load_med = fuzz.trimf(xLoad, [0, 50, 100])
member_load_large = fuzz.trimf(xLoad, [50, 100, 100])

member_time_veryshort = fuzz.trimf(xTime, [0, 0, 15])
member_time_short = fuzz.trimf(xTime, [0, 15, 30])
member_time_medium = fuzz.trimf(xTime, [15, 30, 45])
member_time_long = fuzz.trimf(xTime, [30, 45, 60])
member_time_verylong = fuzz.trimf(xTime, [45, 60, 60])

# plotting membership functions
fig, ax = plt.subplots(1,3, figsize=(14, 3))

ax[0].plot(xDirtness, member_dirtness_small, 'blue', linewidth=1.5, label='small')
ax[0].plot(xDirtness, member_dirtness_med, 'orange', linewidth=1.5, label='medium')
ax[0].plot(xDirtness, member_dirtness_large, 'green', linewidth=1.5, label='large')
ax[0].set(xlim=(0, 100), ylim=(0, 1))
ax[0].legend()

ax[1].plot(xLoad, member_load_small, 'blue', linewidth=1.5, label='small')
ax[1].plot(xLoad, member_load_med, 'orange', linewidth=1.5, label='medium')
ax[1].plot(xLoad, member_load_large, 'green', linewidth=1.5, label='large')
ax[1].set(xlim=(0, 100), ylim=(0, 1))
ax[1].legend()

ax[2].plot(xTime, member_time_veryshort, 'blue', linewidth=1.5, label='low')
ax[2].plot(xTime, member_time_short, 'orange', linewidth=1.5, label='medium')
ax[2].plot(xTime, member_time_medium, 'green', linewidth=1.5, label='high')
ax[2].plot(xTime, member_time_long, 'magenta', linewidth=1.5, label='medium')
ax[2].plot(xTime, member_time_verylong, 'purple', linewidth=1.5, label='high')
ax[2].set(xlim=(0, 60), ylim=(0, 1))
ax[2].legend()

dirtness_small = fuzz.interp_membership(xDirtness, member_dirtness_small, 60)
dirtness_med = fuzz.interp_membership(xDirtness, member_dirtness_med, 60)
dirtness_large = fuzz.interp_membership(xDirtness, member_dirtness_large, 60)

load_small = fuzz.interp_membership(xLoad, member_load_small, 70)
load_med = fuzz.interp_membership(xLoad, member_load_med, 70)
load_large = fuzz.interp_membership(xLoad, member_load_large, 70)

# Define the rules
rule1 = np.fmin(dirtness_small, load_small)
rule2 = np.fmin(dirtness_med, load_small)
subrule1 = np.fmin(dirtness_small, load_med)
subrule2 = np.fmin(dirtness_med, load_med)
subrule3 = np.fmin(dirtness_large, load_small)
subrule4 = np.fmax(subrule1, subrule2)
rule3 = np.fmax(subrule3, subrule4)
subrule5 = np.fmin(dirtness_small, load_large)
subrule6 = np.fmin(dirtness_med, load_large)
subrule7 = np.fmin(dirtness_large, load_med)
subrule8 = np.fmax(subrule5, subrule6)
rule4 = np.fmax(subrule7, subrule8)
rule5 = np.fmin(dirtness_large, load_large)

# consequent correlation: min (clipping)
time_veryshort = np.fmin(member_time_veryshort, rule1)
time_short = np.fmin(member_time_short, rule2)
time_medium = np.fmin(member_time_medium, rule3)
time_long = np.fmin(member_time_long, rule4)
time_verylong = np.fmin(member_time_verylong, rule5)
time0 = np.zeros_like(xTime)

# aggregating
subaggr1 = np.fmax(time_veryshort, time_short)
subaggr2 = np.fmax(time_medium, time_long)
subaggr3 = np.fmax(subaggr1, time_verylong)
aggregate = np.fmax(subaggr2, subaggr3)

# defuzzifing using centroid of maxima
time_defuzz_x = fuzz.defuzz(xTime, aggregate, 'mom')
time_defuzz_y = fuzz.interp_membership(xTime, aggregate, time_defuzz_x)

# plotting the output
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(xTime, member_time_veryshort, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(xTime, member_time_short, 'orange', linewidth=0.5, linestyle='--')
ax0.plot(xTime, member_time_medium, 'g', linewidth=0.5, linestyle='--')
ax0.plot(xTime, member_time_long, 'm', linewidth=0.5, linestyle='--')
ax0.plot(xTime, member_time_verylong, 'purple', linewidth=0.5, linestyle='--')
ax0.fill_between(xTime, time0, aggregate, facecolor='brown', alpha=0.7)
ax0.plot([time_defuzz_x, time_defuzz_x], [0, time_defuzz_y], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')
ax0.set(xlim=(0, 60), ylim=(0, 1))

print(f'Washing time: {time_defuzz_x}')
