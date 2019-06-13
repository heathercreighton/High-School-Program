"""
title: math_variables_exercises
author: eam3kzn
date: 6/11/18 11:27 AM
"""

import math

# Swallow follow-along
'''
60 / 3 = 20
1450 / (60 / 3)
1450 / 20 = 72.5
'''

# Other fruit
'''
1450 / (60 / 3) = 72.5
128 / (60 / 3) = 6.4
8 / (60 / 3) = 0.4
'''

# Macaws follow-along
carrying_weight_percentage = 1 / 3
coconut_weight = 1450
macaw_weight = 900
macaw_limit = macaw_weight * carrying_weight_percentage
number_macaws = coconut_weight / macaw_limit
print(number_macaws)
print(math.ceil(number_macaws))
