BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def itoBase(s, b):
    res = ""
    try:
    	while s:
        	res+=BS[s%b]
        	s//= b
    except TypeError:
    		print ('usage')
    else:		
    	return res[::-1] or "0"