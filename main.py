import re


def filtering(message): 
	mes_split=re.findall("(\d|\w)+",message)	
	sen_type=0	
	a_the=[r"a",r"t+h+e+",r"d"]	
	intr_set=set()
	intrjectve_hap=[r"h+u+r+(a+|e+)y+",r"b+r+(a+|e+)+v+o+",r"(w+e+l+)\s*(d+o*n+e*)"]
	intrjectve_amze=[r"w+o+w+",r"h+e+y+",r"h+a+y+",r"(o+h+)\s+(m+y+)\s+(g+o*s+h+)"]
	intrjectve_sd=[r"o+p+s+",r"o+u+c+h+",r"a+l+a*s+",r"o+h+\s*,*\s*n+o+"]
	intr_type=0	

	greeting=[r"h+i+",r"h+e*l+o+",r"y+o+",r"y+u+p+"]
	command=[r""]
	request=[r"p+l+z+s*",r"p+l+e*a*s+e*"]	

	conj_cor=[r"a+n+d+",r"o+r+"]
	nei_ei=[r"n+e*i*t+h*e*r+",r"e+i*t+h+e*r+",r"n+o*r+",r"o+r+"]
	conj_sub=[r"b+e*a*c+a*u+s+e+",r"s+o+",r"t+h+e+n+",r"w+h+i+l+e+",r"b+u+t+"]
	and_or=set()
	sen_break=set()	

	

	pro_time=[r"o+n+",r"a+t+",r"i+n+"]
	prepostion=[r"w+i+t+h+",r"f+r+o+m+",r"i+n+t+o+",r"d+u+r+i*n+g+",r"i+n+c+l+u*d+i*n+g+",r"u+n+t+i*l+",r"a+g+a*i*n+s*t+",r"a+m+o*n+g+",r"t+h+r+o*u*g+h+",r"t+h+r+o*u*g+h+o+u*t+"]
	pro_verb=[r"o+f+",r"t+o+",r"i+n+",r"f+o+r+",r"o+n+",r"b+y+",r"a+b+o*u*t+",r"l+i*k+e+",r"o+v+e*r+",r"b+e+f+o+r+e+",r"b+e*t+w+e+n+",r"a+f+t+e*r+",r"s+i+n+c+e+",r"w+i+t+h+o*u*t+"]
	pro_verb2=[r"w+i+t+h*i*n+"]	


	pron=[r"i+", r"i+t+", r"h+e+", r"s+h+e+",  r"w+e+", r"t+h+e+y+"]
	pos_pron=[r"m+i*n+e+", r"h+i+s+", r"h+e*r+s+",r"t+h+e*i*r+s+", r"o*u+r+s+"]	
	modals=[r"c+a+n+",r"m+a+y+",r"m+u*s+t+",r"s+h+a*l+",r"w+i+l+",r"c+o*u*l+d+",r"m+i+g+h+t+",r"o+u*g+h+t+",r"s+h+o+u*l+d+",r"w+o+u*l+d+"]
	stat_of__beng=[r""]	

	

	if '!' in message:
		sen_type=3
	elif '?' in message:
		sen_type=2
	else: 
		sen_type=1	

	

	mes_tmp=mes_split[:]
	for i in mes_tmp:
		for j in a_the:
			if re.search(r"\s"+j+r"\s"," "+i+" "):
				mes_split.remove(i)

	mes_tmp=mes_split[:]
	for i in mes_tmp:
		for j in intrjectve_hap:
			if re.search(r"\s"+j+r"\s"," "+i+" "):
				intr_set.add(i)
				mes_split.remove(i)
				intr_type+=1
				continue

		for j in intrjectve_amze:
			if re.search(r"\s"+j+r"\s"," "+i+" "):
				intr_set.add(i)
				mes_split.remove(i)
				intr_type+=.6
				continue

		for j in intrjectve_sd:
			if re.search(r"\s"+j+r"\s"," "+i+" "):
				intr_set.add(i)
				mes_split.remove(i)
				intr_type-=1
				continue

	return " ".join(mes_split)





			


