## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file factoringSpecialForms-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_127 = Integer(127); _sage_const_5 = Integer(5); _sage_const_109 = Integer(109); _sage_const_101 = Integer(101); _sage_const_9 = Integer(9); _sage_const_4 = Integer(4); _sage_const_79 = Integer(79); _sage_const_119 = Integer(119); _sage_const_95 = Integer(95); _sage_const_145 = Integer(145); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_137 = Integer(137); _sage_const_8 = Integer(8); _sage_const_6 = Integer(6)## This file (factoringSpecialForms-Practice1.sagetex.sage) was *autogenerated* from factoringSpecialForms-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('factoringSpecialForms-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_1 
_st_.blockbegin()
try:
 
 ######  Define a function to convert a sage number into a saved counter number.
 
 #####Define default Sage variables.
 #Default function variables
 var('x,y,z,X,Y,Z')
 #Default function names
 var('f,g,h,dx,dy,dz,dh,df')
 #Default Wild cards
 w0 = SR.wild(_sage_const_0 )
 
 def DispSign(b):
     """ Returns the string of the 'signed' version of `b`, e.g. 3 -> "+3", -3 -> "-3", 0 -> "".
     """
     if b == _sage_const_0 :
         return ""
     elif b > _sage_const_0 :
         return "+" + str(b)
     elif b < _sage_const_0 :
         return str(b)
     else:
         # If we're here, then something has gone wrong.
         raise ValueError
 
 def ISP(b):
     return DispSign(b)
 
 def NoEval(f, c):
     # TODO
     """ Returns a non-evaluted version of the result f(c).
     """
     cStr = str(c)
     # fLatex = latex(f)
     fString = latex(f)
     fStrList = list(fString)
     length = len(fStrList)
     fStrList2 = range(length)
     for i in range(_sage_const_0 , length):
         if fStrList[i] == "x":
             fStrList2[i] = "("+cstr+")"
         else:
             fStrList2[i] = fStrList[i]
     f2 = join(fStrList2,"")
     return LatexExpr(f2)
 
 def HyperSimp(f):
     """ Returns the expression `f` without hyperbolic expressions.
     """
     subsDict = {
         sinh(w0) : (exp(w0) - exp(-w0))/_sage_const_2 ,
         cosh(w0) : (exp(w0) + exp(-w0))/_sage_const_2 ,
         tanh(w0) : (exp(w0) - exp(-w0))/(exp(w0) + exp(-w0)),
         sech(w0) : _sage_const_2 /(exp(w0) + exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         csch(w0) : _sage_const_2 /(exp(w0) - exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         coth(w0) : (exp(w0) + exp(-w0))/(exp(w0) - exp(-w0)),   # This seems to work, but Nowell said it didn't at one point.
         arcsinh(w0) :       ln( w0 + sqrt((w0)**_sage_const_2  + _sage_const_1 ) ),
         arccosh(w0) :       ln( w0 + sqrt((w0)**_sage_const_2  - _sage_const_1 ) ),
         arctanh(w0) : _sage_const_1 /_sage_const_2  * ln( (_sage_const_1  + w0) / (_sage_const_1  - w0) ),
         arccsch(w0) :       ln( (_sage_const_1  + sqrt((w0)**_sage_const_2  + _sage_const_1 ))/w0 ),
         arcsech(w0) :       ln( (_sage_const_1  + sqrt(_sage_const_1  - (w0)**_sage_const_2 ))/w0 ),
         arccoth(w0) : _sage_const_1 /_sage_const_2  * ln( (_sage_const_1  + w0) / (w0 - _sage_const_1 ) )
     }
     g = f.substitute(subsDict)
     return simplify(g)
 
 def RandInt(a,b):
     """ Returns a random integer in [`a`,`b`]. Note that `a` and `b` should be integers themselves to avoid unexpected behavior.
     """
     return QQ(randint(int(a),int(b)))
     # return choice(range(a,b+1))
 
 def NonZeroInt(b,c, avoid = [_sage_const_0 ]):
     """ Returns a random integer in [`b`,`c`] which is not in `av`.
         If `av` is not specified, defaults to a non-zero integer.
     """
     while True:
         a = RandInt(b,c)
         if a not in avoid:
             return a
 
 def RandVector(b, c, avoid=[], rep=_sage_const_1 ):
     """ Returns essentially a multiset permutation of ([b,c]-av) * rep.
         That is, a vector which contains each integer in [`b`,`c`] which is not in `av` a total of `rep` number of times.
         Example:
         sage: RandVector(1,3, [2], 2)
         [3, 1, 1, 3]
     """
     oneVec = [val for val in range(b,c+_sage_const_1 ) if val not in avoid]
     vec = oneVec * rep
     shuffle(vec)
     return vec
 
 
except:
 _st_.goboom(_sage_const_95 )
_st_.blockend()
_st_.current_tex_line = _sage_const_9 
_st_.blockbegin()
try:
 ###### Problem p1
 p1c1 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1c2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p1pwr1 = RandInt(_sage_const_1 ,_sage_const_3 )
 
 p1f1 = (p1c2*x**p1pwr1)**_sage_const_2  - p1c1**_sage_const_2 
 p1f2 = (p1c2*x**p1pwr1)**_sage_const_3  - p1c1**_sage_const_3 
 p1tog = RandInt(_sage_const_0 ,_sage_const_1 )
 p1f3 = p1f1**p1tog*p1f2**(_sage_const_1 -p1tog)
 
 p1f4 = expand(p1f3)
 
 
 ###### Problem p2
 p2c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p2pwr1 = RandInt(_sage_const_1 ,_sage_const_3 )
 p2pwr2 = RandInt(_sage_const_2 ,_sage_const_3 )
 p2f1 = (p2c1*x**p2pwr1 - p2c2)**p2pwr2
 
 p2f2 = expand(p2f1)
 
 
 ###### Problem p3
 p3c1 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3c2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3pwr1 = RandInt(_sage_const_1 ,_sage_const_3 )
 
 p3f1 = (p3c2*x**p3pwr1)**_sage_const_2  - p3c1**_sage_const_2 
 p3f2 = (p3c2*x**p3pwr1)**_sage_const_3  - p3c1**_sage_const_3 
 p3tog = RandInt(_sage_const_0 ,_sage_const_1 )
 p3f3 = p3f1**p3tog*p3f2**(_sage_const_1 -p3tog)
 
 p3f4 = expand(p3f3)
 
 
 ###### Problem p4
 p4c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p4c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p4pwr1 = RandInt(_sage_const_1 ,_sage_const_3 )
 p4pwr2 = RandInt(_sage_const_2 ,_sage_const_3 )
 p4f1 = (p4c1*x**p4pwr1 - p4c2)**p4pwr2
 
 p4f2 = expand(p4f1)
 
 
 ###### Problem p5
 p5c1 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p5c2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p5pwr1 = RandInt(_sage_const_1 ,_sage_const_3 )
 
 p5f1 = (p5c2*x**p5pwr1)**_sage_const_2  - p5c1**_sage_const_2 
 p5f2 = (p5c2*x**p5pwr1)**_sage_const_3  - p5c1**_sage_const_3 
 p5tog = RandInt(_sage_const_0 ,_sage_const_1 )
 p5f3 = p5f1**p5tog*p5f2**(_sage_const_1 -p5tog)
 
 p5f4 = expand(p5f3)
 
 
 ###### Problem p6
 p6c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p6c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p6pwr1 = RandInt(_sage_const_1 ,_sage_const_3 )
 p6pwr2 = RandInt(_sage_const_2 ,_sage_const_3 )
 p6f1 = (p6c1*x**p6pwr1 - p6c2)**p6pwr2
 
 p6f2 = expand(p6f1)
 
 
except:
 _st_.goboom(_sage_const_79 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_0 , latex(p1f4))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_1 , latex(p1f3))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_2 , latex(p2f2))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_3 , latex(p2f1))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_119 
 _st_.inline(_sage_const_4 , latex(p3f4))
except:
 _st_.goboom(_sage_const_119 )
try:
 _st_.current_tex_line = _sage_const_119 
 _st_.inline(_sage_const_5 , latex(p3f3))
except:
 _st_.goboom(_sage_const_119 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_6 , latex(p4f2))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_7 , latex(p4f1))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_137 
 _st_.inline(_sage_const_8 , latex(p5f4))
except:
 _st_.goboom(_sage_const_137 )
try:
 _st_.current_tex_line = _sage_const_137 
 _st_.inline(_sage_const_9 , latex(p5f3))
except:
 _st_.goboom(_sage_const_137 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_10 , latex(p6f2))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_11 , latex(p6f1))
except:
 _st_.goboom(_sage_const_145 )
_st_.endofdoc()

