'''
Problem:
    Fuzzy Control system taking care of air conditioner.
    Fuzzy AI controlling should adapt inner temperature based on outdoor tempereature,
    humidity and hour.

Authors:
    Adam Tomporowski, s16740
    Piotr Baczkowski, s16621
'''

#To run this program you need to install and import below modules in same format
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedent/Consequent objects holding universal variables and membership
hour = ctrl.Antecedent(np.arange(0, 24, 1), 'hour')
temperature = ctrl.Antecedent(np.arange(0, 45, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')
aCondit = ctrl.Consequent(np.arange(18, 31, 1), 'aCondit')

"""
Main functions hold objects and universal variables for fuzzy AI

Functions :
    hour : Antecedent function hold universal variables based on real hours
    temperature : Antecedent function hold universal variables based on possible outdoor temperature
    humidity : Antecedent function hold universal variables based on possible outdoor temperature
    ACondit : Consequemt function hold universal variables based on possible indoor temperature 
"""

hour.automf(3)
temperature.automf(3)
humidity.automf(3)

"""Auto-membership function population setted on 3"""

aCondit['Cold'] = fuzz.trimf(aCondit.universe, [18, 21, 24])
aCondit['Comfortable'] = fuzz.trimf(aCondit.universe, [21, 24, 27])
aCondit['Hot'] = fuzz.trimf(aCondit.universe, [24, 27, 30])

"""
Custom membership functions can be built interactively with a familiar
Pythonic API

Functions are designed for the most optimized temperatures for humans.
aCondit:
    Function is using (trimf) triangular membership function genereator,
    All of them are incerased by 3, to model comfortable temperatures,
    based on outdoor conditions
"""

rule1 = ctrl.Rule(hour['poor'] | temperature['poor'] | humidity['poor'], aCondit['Cold'])
rule2 = ctrl.Rule(hour['average'] | temperature['average'] | humidity['average'], aCondit['Comfortable'])
rule3 = ctrl.Rule(hour['good'] | temperature['good'] | humidity['good'], aCondit['Hot'])

"""
Rule functions in a fuzzy system, connecting Antecedents to Consequemt
Three rules providing high-level fot fuzzy system design.  
"""

temp_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

"""Function use Fuzzy Control System based on defined rules"""

temp_setting = ctrl.ControlSystemSimulation(temp_ctrl)

"""Function use calculate system from Fuzzy control system, based on previously defined rules"""

temp_setting.input['hour'] = 8
temp_setting.input['temperature'] = 22
temp_setting.input['humidity'] = 32

temp_setting.compute()

print(temp_setting.output['aCondit'])
aCondit.view(sim=temp_setting)
"""
temp_setting.input : 
    Pass inputs to the ControlSystem using our Antecedent labels with Pythonic API
    Variables should fit between before declared ranges for best result

temp_setting_compute() :
    function analyze and examine numbers to determine the most optimal output variable
"""

plt.show()

"""Function generating plot view"""