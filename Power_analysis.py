
# https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/ For sample size
# https://machinelearningmastery.com/effect-size-measures-in-python/ For effect size - use R
# https://www.geeksforgeeks.org/introduction-to-power-analysis-in-python/ For power size

from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.power import TTestPower



##################################### T1 ##################################################

# Regressing SIQ_T1
# parameters for power analysis
effect = 0.658 # R (not squared) R is the coefficient of correlation (Pearson correlation), while R2 is the coefficiant of determination
alpha = 0.05
power = 0.8

# perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print('Sample Size: %.3f' % result)
# sample size needed is 37,4

power = TTestPower()
n_test = power.solve_power(nobs=41, effect_size = 0.658,
                           power = None, alpha = 0.05)
print('Power: {:.3f}'.format(n_test))
# Power: 0,984



# Regressing BSL_T1
effect = 0.91
alpha = 0.05
power = 0.8

# perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print('Sample Size: %.3f' % result)
# Sample size needed 19,9

power = TTestPower()
n_test = power.solve_power(nobs=41, effect_size = 0.91,
                           power = None, alpha = 0.05)
print('Power: {:.3f}'.format(n_test))
# Power: 1,0




# Regressing ISAS_T1
effect = 0.726
alpha = 0.05
power = 0.8

# perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print('Sample Size: %.3f' % result)
# Sample size needed 30,7

power = TTestPower()
n_test = power.solve_power(nobs=41, effect_size = 0.726,
                           power = None, alpha = 0.05)
print('Power: {:.3f}'.format(n_test))
# Power: 0,995



#################################### T3 #############################################################



# Regressing SIQ_T3
# parameters for power analysis
effect = 0.820 # R (not squared) R is the coefficient of correlation (Pearson correlation), while R2 is the coefficiant of determination
alpha = 0.05
power = 0.8

# perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print('Sample Size: %.3f' % result)
# sample size needed is 24,3

power = TTestPower()
n_test = power.solve_power(nobs=41, effect_size = 0.820,
                           power = None, alpha = 0.05)
print('Power: {:.3f}'.format(n_test))
# Power: 0,999



# Regressing BSL_T3
effect = 0.938
alpha = 0.05
power = 0.8

# perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print('Sample Size: %.3f' % result)
# Sample size needed 18,8

power = TTestPower()
n_test = power.solve_power(nobs=41, effect_size = 0.938,
                           power = None, alpha = 0.05)
print('Power: {:.3f}'.format(n_test))
# Power: 1,0




# Regressing ISAS_T1
effect = 0.65
alpha = 0.05
power = 0.8

# perform power analysis
analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print('Sample Size: %.3f' % result)
# Sample size needed 38,1

power = TTestPower()
n_test = power.solve_power(nobs=41, effect_size = 0.65,
                           power = None, alpha = 0.05)
print('Power: {:.3f}'.format(n_test))
# Power: 0,982







