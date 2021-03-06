## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file solvingUnsimplifiedRadicals-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_172 = Integer(172); _sage_const_138 = Integer(138); _sage_const_170 = Integer(170); _sage_const_154 = Integer(154); _sage_const_152 = Integer(152); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_163 = Integer(163); _sage_const_95 = Integer(95); _sage_const_161 = Integer(161); _sage_const_145 = Integer(145); _sage_const_143 = Integer(143)## This file (solvingUnsimplifiedRadicals-Practice1.sagetex.sage) was *autogenerated* from solvingUnsimplifiedRadicals-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('solvingUnsimplifiedRadicals-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
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
 p1c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p1c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p1c1])
 p1c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1c5 = RandInt(-_sage_const_3 ,_sage_const_3 )
 
 p1f1 = p1c1*x + p1c2
 p1f2 = p1c3*x + p1c4
 
 if p1c5 == _sage_const_0 :
     p1ans1 = _sage_const_0 
     p1TempAns1 = (p1c4-p1c2)/(p1c1-p1c3)
     if p1TempAns1*p1c1 > -p1c2 and p1TempAns1*p1c3 > -p1c4:# Check for domain issues
         p1ans1 = p1TempAns1
 else:
     p1ans1 = _sage_const_0 
     p1TempA = ((p1c1-p1c3)/(_sage_const_2 *p1c5))**_sage_const_2 
     p1TempB = (p1c2-p1c4-p1c5**_sage_const_2 )*(p1c1-p1c3)/(_sage_const_2 *p1c5**_sage_const_2 )-p1c3
     p1TempC = ((p1c2-p1c4-p1c5**_sage_const_2 )/(_sage_const_2 *p1c5))**_sage_const_2 -p1c4
     p1TempAns1 = (-p1TempB + sqrt(p1TempB**_sage_const_2  - _sage_const_4 *p1TempA*p1TempC))/(_sage_const_2 *p1TempA)
     p1TempAns2 = (-p1TempB - sqrt(p1TempB**_sage_const_2  - _sage_const_4 *p1TempA*p1TempC))/(_sage_const_2 *p1TempA)
     if p1TempAns1 * p1c1 > -p1c2 and p1TempAns1 * p1c3 > -p1c4:# Check for domain issues
         if sqrt(p1c1*p1TempAns1 + p1c2) == sqrt(p1c3*p1TempAns1 + p1c4) + p1c5:# Check answer for validity
             p1ans1 = p1ans1 + p1TempAns1
 
     if p1TempAns2 * p1c1 > -p1c2 and p1TempAns2 * p1c3 > -p1c4:# Check for domain issues
         if sqrt(p1c1*p1TempAns2 + p1c2) == sqrt(p1c3*p1TempAns2 + p1c4) + p1c5:# Check answer for validity
             p1ans1 = p1ans1 + p1TempAns2
 
 
 ###### Problem p2
 p2c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p2c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p2c1])
 p2c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2c5 = RandInt(-_sage_const_3 ,_sage_const_3 )
 
 p2f1 = p2c1*x + p2c2
 p2f2 = p2c3*x + p2c4
 
 if p2c5 == _sage_const_0 :
     p2TempAns1 = (p2c4-p2c2)/(p2c1-p2c3)
     if p2TempAns1*p2c1 > -p2c2 and p2TempAns1*p2c3 > -p2c4:
         p2ans1 = p2TempAns1
     else:
         p2ans1 = _sage_const_0 
 else:
     p2ans1 = _sage_const_0 
     p2TempA = ((p2c1-p2c3)/(_sage_const_2 *p2c5))**_sage_const_2 
     p2TempB = (p2c2-p2c4-p2c5**_sage_const_2 )*(p2c1-p2c3)/(_sage_const_2 *p2c5**_sage_const_2 )-p2c3
     p2TempC = ((p2c2-p2c4-p2c5**_sage_const_2 )/(_sage_const_2 *p2c5))**_sage_const_2 -p2c4
     p2TempAns1 = (-p2TempB + sqrt(p2TempB**_sage_const_2  - _sage_const_4 *p2TempA*p2TempC))/(_sage_const_2 *p2TempA)
     p2TempAns2 = (-p2TempB - sqrt(p2TempB**_sage_const_2  - _sage_const_4 *p2TempA*p2TempC))/(_sage_const_2 *p2TempA)
     if p2TempAns1 * p2c1 > -p2c2 and p2TempAns1 * p2c3 > -p2c4:# Check for domain issues
         if sqrt(p2c1*p2TempAns1 + p2c2) == sqrt(p2c3*p2TempAns1 + p2c4) + p2c5:# Check answer for validity
             p2ans1 = p2ans1 + p2TempAns1
 
     if p2TempAns2 * p2c1 > -p2c2 and p2TempAns2 * p2c3 > -p2c4:# Check for domain issues
         if sqrt(p2c1*p2TempAns2 + p2c2) == sqrt(p2c3*p2TempAns2 + p2c4) + p2c5:# Check answer for validity
             p2ans1 = p2ans1 + p2TempAns2
 
 
 ###### Problem p3
 p3c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p3c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p3c1])
 p3c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3c5 = RandInt(-_sage_const_3 ,_sage_const_3 )
 
 p3f1 = p3c1*x + p3c2
 p3f2 = p3c3*x + p3c4
 
 if p3c5 == _sage_const_0 :
     p3TempAns1 = (p3c4-p3c2)/(p3c1-p3c3)
     if p3TempAns1*p3c1 > -p3c2 and p3TempAns1*p3c3 > -p3c4:
         p3ans1 = p3TempAns1
     else:
         p3ans1 = _sage_const_0 
 else:
     p3ans1 = _sage_const_0 
     p3TempA = ((p3c1-p3c3)/(_sage_const_2 *p3c5))**_sage_const_2 
     p3TempB = (p3c2-p3c4-p3c5**_sage_const_2 )*(p3c1-p3c3)/(_sage_const_2 *p3c5**_sage_const_2 )-p3c3
     p3TempC = ((p3c2-p3c4-p3c5**_sage_const_2 )/(_sage_const_2 *p3c5))**_sage_const_2 -p3c4
     p3TempAns1 = (-p3TempB + sqrt(p3TempB**_sage_const_2  - _sage_const_4 *p3TempA*p3TempC))/(_sage_const_2 *p3TempA)
     p3TempAns2 = (-p3TempB - sqrt(p3TempB**_sage_const_2  - _sage_const_4 *p3TempA*p3TempC))/(_sage_const_2 *p3TempA)
     if p3TempAns1 * p3c1 > -p3c2 and p3TempAns1 * p3c3 > -p3c4:# Check for domain issues
         if sqrt(p3c1*p3TempAns1 + p3c2) == sqrt(p3c3*p3TempAns1 + p3c4) + p3c5:# Check answer for validity
             p3ans1 = p3ans1 + p3TempAns1
 
     if p3TempAns2 * p3c1 > -p3c2 and p3TempAns2 * p3c3 > -p3c4:# Check for domain issues
         if sqrt(p3c1*p3TempAns2 + p3c2) == sqrt(p3c3*p3TempAns2 + p3c4) + p3c5:# Check answer for validity
             p3ans1 = p3ans1 + p3TempAns2
 
 
 ###### Problem p4
 p4c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p4c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p4c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p4c1])
 p4c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p4c5 = RandInt(-_sage_const_3 ,_sage_const_3 )
 
 p4f1 = p4c1*x + p4c2
 p4f2 = p4c3*x + p4c4
 
 if p4c5 == _sage_const_0 :
     p4TempAns1 = (p4c4-p4c2)/(p4c1-p4c3)
     if p4TempAns1*p4c1 > -p4c2 and p4TempAns1*p4c3 > -p4c4:
         p4ans1 = p4TempAns1
     else:
         p4ans1 = _sage_const_0 
 else:
     p4ans1 = _sage_const_0 
     p4TempA = ((p4c1-p4c3)/(_sage_const_2 *p4c5))**_sage_const_2 
     p4TempB = (p4c2-p4c4-p4c5**_sage_const_2 )*(p4c1-p4c3)/(_sage_const_2 *p4c5**_sage_const_2 )-p4c3
     p4TempC = ((p4c2-p4c4-p4c5**_sage_const_2 )/(_sage_const_2 *p4c5))**_sage_const_2 -p4c4
     p4TempAns1 = (-p4TempB + sqrt(p4TempB**_sage_const_2  - _sage_const_4 *p4TempA*p4TempC))/(_sage_const_2 *p4TempA)
     p4TempAns2 = (-p4TempB - sqrt(p4TempB**_sage_const_2  - _sage_const_4 *p4TempA*p4TempC))/(_sage_const_2 *p4TempA)
     if p4TempAns1 * p4c1 > -p4c2 and p4TempAns1 * p4c3 > -p4c4:# Check for domain issues
         if sqrt(p4c1*p4TempAns1 + p4c2) == sqrt(p4c3*p4TempAns1 + p4c4) + p4c5:# Check answer for validity
             p4ans1 = p4ans1 + p4TempAns1
 
     if p4TempAns2 * p4c1 > -p4c2 and p4TempAns2 * p4c3 > -p4c4:# Check for domain issues
         if sqrt(p4c1*p4TempAns2 + p4c2) == sqrt(p4c3*p4TempAns2 + p4c4) + p4c5:# Check answer for validity
             p4ans1 = p4ans1 + p4TempAns2
 
 
 
except:
 _st_.goboom(_sage_const_138 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_143 
 _st_.inline(_sage_const_0 , latex(p1f1))
except:
 _st_.goboom(_sage_const_143 )
try:
 _st_.current_tex_line = _sage_const_143 
 _st_.inline(_sage_const_1 , latex(p1f2))
except:
 _st_.goboom(_sage_const_143 )
try:
 _st_.current_tex_line = _sage_const_143 
 _st_.inline(_sage_const_2 , latex(p1c5))
except:
 _st_.goboom(_sage_const_143 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_3 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_4 , latex(p2f1))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_5 , latex(p2f2))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_6 , latex(p2c5))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_7 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_8 , latex(p3f1))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_9 , latex(p3f2))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_10 , latex(p3c5))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_163 
 _st_.inline(_sage_const_11 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_163 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_12 , latex(p4f1))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_13 , latex(p4f2))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_14 , latex(p4c5))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_172 
 _st_.inline(_sage_const_15 , latex(p4ans1))
except:
 _st_.goboom(_sage_const_172 )
_st_.endofdoc()

