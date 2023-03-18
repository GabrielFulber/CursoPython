import  numpy as np

import matplotlib.pyplot as plt

import skfuzzy as fuzzy

from skfuzzy import control

dominio_fila = np.arange(0,21,1)
dominio_ext = np.arange(0,21,1)

f1 = control.Antecedent(dominio_fila, 'f1')
f2 = control.Antecedent(dominio_fila, 'f2')
f3 = control.Antecedent(dominio_fila, 'f3')
f4 = control.Antecedent(dominio_fila, 'f4')

ext = control.Consequent(dominio_ext, 'ext')

f1['pequena'] = fuzzy.trimf(f1.universe, [0, 4, 8])
f1['media'] = fuzzy.trimf(f1.universe, [4, 8, 12])
f1['grande'] = fuzzy.trapmf(f1.universe, [8, 12, 20, 20])

f2['pequena'] = fuzzy.trimf(f2.universe, [0, 4, 8])
f2['media'] = fuzzy.trimf(f2.universe, [4, 8, 12])
f2['grande'] = fuzzy.trapmf(f2.universe, [8, 12, 20, 20])

f3['pequena'] = fuzzy.trimf(f3.universe, [0, 4, 8])
f3['media'] = fuzzy.trimf(f3.universe, [4, 8, 12])
f3['grande'] = fuzzy.trapmf(f3.universe, [8, 12, 20, 20])

f4['pequena'] = fuzzy.trimf(f4.universe, [0, 4, 8])
f4['media'] = fuzzy.trimf(f4.universe, [4, 8, 12])
f4['grande'] = fuzzy.trapmf(f4.universe, [8, 12, 20, 20])

f1.view()

ext['zero'] = fuzzy.trimf(ext.universe, [0, 0, 5])

ext['curta'] = fuzzy.trimf(ext.universe, [0, 5, 10])

ext['media'] = fuzzy.trimf(ext.universe, [5, 10, 15])

ext['longa'] = fuzzy.trapmf(ext.universe, [10, 15, 20, 20])

ext.view()

r1 = control.Rule(f1['grande'] & f2['pequena'], ext['longa'])

r2 = control.Rule(f3['media'] | f4['pequena'], ext['media'])

r3 = control.Rule(f2['media'] & f1['pequena'], ext['zero'])

semaforo_controle = control.ControlSystem([r1, r2, r3])

sA = control.ControlSystemSimulation(semafaro_controle)

sA.input['f1'] = 5

sA.input['f2'] = 10

sA.input['f3'] = 0

sA.input['f4'] = 0

sA.compute()

sA.output

ext.view(sim=sA)