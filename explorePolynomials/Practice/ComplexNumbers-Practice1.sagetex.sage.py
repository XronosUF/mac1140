## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file ComplexNumbers-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_64 = Integer(64); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_70 = Integer(70); _sage_const_5 = Integer(5); _sage_const_61 = Integer(61); _sage_const_9 = Integer(9); _sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_82 = Integer(82); _sage_const_10 = Integer(10); _sage_const_76 = Integer(76); _sage_const_6 = Integer(6)## This file (ComplexNumbers-Practice1.sagetex.sage) was *autogenerated* from ComplexNumbers-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('ComplexNumbers-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_9 
_st_.blockbegin()
try:
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
 
 
 var('i')
 ###### Problem p1
 p1c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p1c2 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 
 p1f1 = p1c1 - p1c2*i
 p1f2 = p1c1 + p1c2*i
 
 
 ###### Problem p2
 p2c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p2c2 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 
 p2f1 = p2c1 - p2c2*i
 p2f2 = p2c1 + p2c2*i
 
 
 ###### Problem p3
 p3c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p3c2 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 
 p3f1 = p3c1 - p3c2*i
 p3f2 = p3c1 + p3c2*i
 
 
 ###### Problem p4
 p4c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p4c2 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 
 p4f1 = p4c1 - p4c2*i
 p4f2 = p4c1 + p4c2*i
 
 
 
 
except:
 _st_.goboom(_sage_const_61 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_0 , latex(p1f1))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_1 , latex(p1f2))
except:
 _st_.goboom(_sage_const_64 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_2 , latex(p2f1))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_3 , latex(p2f2))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_4 , latex(p3f1))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_5 , latex(p3f2))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_6 , latex(p4f1))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_7 , latex(p4f2))
except:
 _st_.goboom(_sage_const_82 )
_st_.endofdoc()

