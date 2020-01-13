## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file functionComposition-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_106 = Integer(106); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_119 = Integer(119); _sage_const_88 = Integer(88); _sage_const_84 = Integer(84); _sage_const_112 = Integer(112); _sage_const_86 = Integer(86); _sage_const_110 = Integer(110); _sage_const_80 = Integer(80); _sage_const_82 = Integer(82); _sage_const_114 = Integer(114); _sage_const_99 = Integer(99); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_108 = Integer(108); _sage_const_123 = Integer(123); _sage_const_77 = Integer(77); _sage_const_121 = Integer(121); _sage_const_127 = Integer(127); _sage_const_125 = Integer(125); _sage_const_93 = Integer(93); _sage_const_101 = Integer(101); _sage_const_97 = Integer(97); _sage_const_95 = Integer(95)## This file (functionComposition-Practice1.sagetex.sage) was *autogenerated* from functionComposition-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('functionComposition-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
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
_st_.current_tex_line = _sage_const_6 
_st_.blockbegin()
try:
 p1pwr = RandInt(_sage_const_1 ,_sage_const_3 )
 p1funcvec = [x**p1pwr, e**x, log(abs(x)), sqrt(x)]
 p1c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p1c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p1c3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p1c4 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p1choice1 = RandInt(_sage_const_0 ,_sage_const_3 )
 p1choice2 = NonZeroInt(_sage_const_0 ,_sage_const_3 ,[_sage_const_3 -p1choice1])
 
 p1func1 = p1c1*p1funcvec[p1choice1](x + p1c2)
 p1func2 = p1c3*p1funcvec[p1choice2](x + p1c4)
 
 p1ans1 = p1func1(p1func2(x))
 p1ans2 = p1func2(p1func1(x))
 
 
 p2pwr = RandInt(_sage_const_1 ,_sage_const_3 )
 p2funcvec = [x**p2pwr, e**x, log(abs(x)), sqrt(x)]
 p2c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p2c3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c4 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p2choice1 = RandInt(_sage_const_0 ,_sage_const_3 )
 p2choice2 = NonZeroInt(_sage_const_0 ,_sage_const_3 ,[_sage_const_3 -p2choice1])
 
 p2func1 = p2c1*p2funcvec[p2choice1](x + p2c2)
 p2func2 = p2c3*p2funcvec[p2choice2](x + p2c4)
 
 p2ans1 = p2func1(p2func2(x))
 p2ans2 = p2func2(p2func1(x))
 
 
 p3pwr = RandInt(_sage_const_1 ,_sage_const_3 )
 p3funcvec = [x**p3pwr, e**x, log(abs(x)), sqrt(x)]
 p3c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p3c3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3c4 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p3choice1 = RandInt(_sage_const_0 ,_sage_const_3 )
 p3choice2 = NonZeroInt(_sage_const_0 ,_sage_const_3 ,[_sage_const_3 -p3choice1])
 
 p3func1 = p3c1*p3funcvec[p3choice1](x + p3c2)
 p3func2 = p3c3*p3funcvec[p3choice2](x + p3c4)
 
 p3ans1 = p3func1(p3func2(x))
 p3ans2 = p3func2(p3func1(x))
 
 
 p4pwr = RandInt(_sage_const_1 ,_sage_const_3 )
 p4funcvec = [x**p4pwr, e**x, log(abs(x)), sqrt(x)]
 p4c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p4c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p4c3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p4c4 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p4choice1 = RandInt(_sage_const_0 ,_sage_const_3 )
 p4choice2 = NonZeroInt(_sage_const_0 ,_sage_const_3 ,[_sage_const_3 -p4choice1])
 
 p4func1 = p4c1*p4funcvec[p4choice1](x + p4c2)
 p4func2 = p4c3*p4funcvec[p4choice2](x + p4c4)
 
 p4ans1 = p4func1(p4func2(x))
 p4ans2 = p4func2(p4func1(x))
 
 
 
 
except:
 _st_.goboom(_sage_const_77 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_80 
 _st_.inline(_sage_const_0 , latex(p1func1))
except:
 _st_.goboom(_sage_const_80 )
try:
 _st_.current_tex_line = _sage_const_80 
 _st_.inline(_sage_const_1 , latex(p1func2(x)))
except:
 _st_.goboom(_sage_const_80 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_2 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_84 
 _st_.inline(_sage_const_3 , latex(p1ans2))
except:
 _st_.goboom(_sage_const_84 )
try:
 _st_.current_tex_line = _sage_const_86 
 _st_.inline(_sage_const_4 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.current_tex_line = _sage_const_88 
 _st_.inline(_sage_const_5 , latex(p1ans2))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.current_tex_line = _sage_const_93 
 _st_.inline(_sage_const_6 , latex(p2func1))
except:
 _st_.goboom(_sage_const_93 )
try:
 _st_.current_tex_line = _sage_const_93 
 _st_.inline(_sage_const_7 , latex(p2func2(x)))
except:
 _st_.goboom(_sage_const_93 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_8 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_97 
 _st_.inline(_sage_const_9 , latex(p2ans2))
except:
 _st_.goboom(_sage_const_97 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_10 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_11 , latex(p2ans2))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_106 
 _st_.inline(_sage_const_12 , latex(p3func1))
except:
 _st_.goboom(_sage_const_106 )
try:
 _st_.current_tex_line = _sage_const_106 
 _st_.inline(_sage_const_13 , latex(p3func2(x)))
except:
 _st_.goboom(_sage_const_106 )
try:
 _st_.current_tex_line = _sage_const_108 
 _st_.inline(_sage_const_14 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_108 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_15 , latex(p3ans2))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_112 
 _st_.inline(_sage_const_16 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_112 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_17 , latex(p3ans2))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_119 
 _st_.inline(_sage_const_18 , latex(p4func1))
except:
 _st_.goboom(_sage_const_119 )
try:
 _st_.current_tex_line = _sage_const_119 
 _st_.inline(_sage_const_19 , latex(p4func2(x)))
except:
 _st_.goboom(_sage_const_119 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_20 , latex(p4ans1))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_21 , latex(p4ans2))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_22 , latex(p4ans1))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_23 , latex(p4ans2))
except:
 _st_.goboom(_sage_const_127 )
_st_.endofdoc()
