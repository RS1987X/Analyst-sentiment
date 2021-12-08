# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:05:30 2021

@author: Richard
"""

import pandas as pd
xl = pd.read_excel('Analyst rating changes.xlsx')
#
#
#n_upgrades = pd.DataFrame(columns=['Name','Upgrades'])
#n_upgrades.set_axis(['Name', 'Upgrades'],axis=1)
#for x in xl:
#    if x["Rating changes (steps)"] == 1 && x["Rating"] == "Buy":
#        n_upgrades = 