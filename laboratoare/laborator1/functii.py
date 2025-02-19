def cmmdc(a:int, b:int) -> int:
   return a if not b else cmmdc(b, a%b) 


   
