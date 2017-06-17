import re
"""

def filtering(message): 
	message=message.lower()
	mes_split=re.findall("(\d|\w)+",message)	



	




	modals=[r"c+a+n+",r"m+a+y+",r"m+u*s+t+",r"s+h+a*l+",r"w+i+l+",r"c+o*u*l+d+",r"m+i+g+h+t+",r"o+u*g+h+t+",r"s+h+o+u*l+d+",r"w+o+u*l+d+"]
	stat_of__beng=[r""]	
	



	

	


	"""




	
			


	
class filter_message:
	
	#article
	a_the=[r"a",r"t+h+e+",r"d"]	
	replace_dict={"$":r"[e|i]+","%":r"[y|i]+","#":r"[u|o]+","@":r"[a|e]+"}
	#interjection
	intrjectve_hap=[r"h+#r+@y+",r"b+r+@v+o+",r"(w+e+l+)\s*(d+o*n+e*)"]
	intrjectve_amze=[r"w+o+w+",r"h+e+y+",r"h+a+y+",r"(o+h+)\s+(m+y+)\s+(g+o*s+h+)"]
	intrjectve_sd=[r"o+p+s+",r"o+u+c+h+",r"a+l+a*s+",r"o+h+\s*,*\s*n+o+"]
	
	#proposition
	pro_time=[r"o+n+",r"a+t+",r"i+n+"]
	prepostion=[r"w+i+t+h+",r"f+r+o+m+",r"i+n+t+o+",r"d+u+r+i*n+g+",r"i+n+c+l+u*d+i*n+g+",r"u+n+t+i*l+",r"a+g+a*i*n+s*t+",r"a+m+o*n+g+",r"t+h+r+o*u*g+h+",r"t+h+r+o*u*g+h+o+u*t+"]
	pro_verb=[r"o+f+",r"t+o+",r"i+n+",r"f+o+r+",r"o+n+",r"b+y+",r"a+b+o*u*t+",r"l+i*k+e+",r"o+v+e*r+",r"b+e+f+o+r+e+",r"b+e*t+w+e+n+",r"a+f+t+e*r+",r"s+i+n+c+e+",r"w+i+t+h+o*u*t+"]
	pro_verb2=[r"w+i+t+h*i*n+"]	

	#pronoun
	pron=[r"i+", r"i+t+", r"h+e+", r"s+h+e+",  r"w+e+", r"t+h+e+y+"]
	pos_pron=[r"m+i*n+e+", r"h+i+s+", r"h+e*r+s+",r"t+h+e*i*r+s+", r"o*u+r+s+"]	

	#conjecation
	conj_cor=[r"a+n+d+",r"o+r+"]
	nei_ei=[r"n+e*i*t+h*e*r+",r"e+i*t+h+e*r+",r"n+o*r+",r"o+r+"]
	conj_sub=[r"b+e*a*c+a*u+s+e+",r"s+o+",r"t+h+e+n+",r"w+h+i+l+e+",r"b+u+t+"]
	and_or=set()
	sen_break=set()	

	#behavior
	greeting=[r"h+i+",r"h+e*l+o+",r"y+o+",r"y+u+p+"]
	command=[r""]
	request=[r"p+l+z+s*",r"p+l+e*a*s+e*"]	
	abusive=[r"f+u*c+k+\s*o*f*",r"b+i+t+c+h+",r""]


	def __init__(self,message):
		self.message=message.lower()
		self.mes_split=re.findall("[(\d|\w)]+",self.message)
		self.info={"sen_type":0 ,"intr_type":0,"intr_set":set(),"behavior":"","beh_set":set()}
		
		self.filtering()
		


	def filtering(self):
		self.sentence_type()
		self.filter_method(filter_message.a_the)
		self.info["intr_type"]=self.advance_filter_method({"start":0,0:1,1:-1,2:.6},self.info["intr_set"],filter_message.intrjectve_hap,filter_message.intrjectve_sd,filter_message.intrjectve_amze)
		self.filter_method(filter_message.pro_time,filter_message.prepostion,filter_message.pro_verb,filter_message.pro_verb2)
		self.filter_method(filter_message.conj_cor,filter_message.conj_sub,filter_message.nei_ei)
		self.filter_method(filter_message.pron,filter_message.pos_pron)
		self.info["behavior"]=self.advance_filter_method({"start":"",0:"g",1:"r",2:"b",3:"c"},self.info["beh_set"],self.greeting,self.request,self.abusive)


	# simplying removes the values 
	def filter_method(self,*filters_array):
		mes_tmp=self.mes_split[:]
		for i in mes_tmp:
			for k in filters_array:
				for j in k:
					for key , value in filter_message.replace_dict.items():
						j=j.replace(key,value)
					if re.search(r"\s"+j+r"\s"," "+i+" "):
						self.mes_split.remove(i)
						break

	# measuring qualities
	def advance_filter_method(self,value_set,store,*filters_array):
		value_int=value_set["start"]
		mes_tmp=self.mes_split[:]
		for i in mes_tmp:
			for k in filters_array:
				for j in k:
					for key ,value in filter_message.replace_dict.items():
						j=j.replace(key,value)
					if re.search(r"\s"+j+r"\s"," "+i+" "):
							store.add(i)
							self.mes_split.remove(i)
							value_int+=value_set[filters_array.index(k)]
							break
		return value_int

	# 2 "interogative" ,3 "excalmation" ,1 "else"
	def sentence_type(self):
		if '!' in self.message:
			self.info["sen_type"]=3
		elif '?' in self.message:
			self.info["sen_type"]=2
		else: 
			self.info["sen_type"]=1

	def get_filtered_message(self):
		return " ".join(self.mes_split) ,self.info