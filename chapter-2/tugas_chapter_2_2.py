# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:24:39 2021

@author: LENOVO
"""
def ganjil(n):
    x = n % 2
    if x != 0:
        y = True
    else:
        y = False
    return y
    
def genap(m):
    a = m % 2
    if a != 0:
        b = False
    else:
        b = True
    return b

def ikan(jenis):
    print(f'Salah satu jenis ikan adalah {jenis}')
    

class Kelulusan():
 
    def __init__(self, masukan_nama):
        self.nama = masukan_nama
 
    def nilai(self, nilai):
        if nilai >= 70:
            print(self.nama,'Selamat anda lulus dengan nilai',nilai)
        else:
            print(self.nama,'Maaf anda tidak lulus dengan nilai',nilai)
