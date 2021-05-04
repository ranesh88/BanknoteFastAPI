# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:09:39 2021

@author: Ranesh
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float