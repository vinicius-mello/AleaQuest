from MoodleXML import MoodleXML
from sympy import *
from sympy.printing.latex import print_latex
from sympy.matrices import randMatrix
import random

prng = random.Random(1)
category = 'Sistema4x4'

def Sistema4x4(i):
  A = randMatrix(4, 4, -5, 5, prng = prng)
  P,L,D,U = A.LUdecompositionFF()
  text = fr'''
  Calcule o determinante da matriz \[ {latex(A)} .\]
  '''
  answer = int(det(A))
  return { 'answer' : answer, 'text' : text}

f = open(category+'.xml', 'w')
f.write(MoodleXML(category, Det4x4))
f.close()