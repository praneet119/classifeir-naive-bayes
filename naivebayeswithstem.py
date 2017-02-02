#!/usr/bin/env python



import os
import codecs
import json
	



def naivebayes() :
	pathname="F:/work/eattreat classes/"
	path = ['Bakery&Sweets/','Snacks/','Meats/','Organics/','Other/','Drinks/','Restaurants/']
	path1 = ['Bakery&Sweets','Snacks','Meats','Organics','Other','Drinks','Restaurants']
	ies="ies"
	#save_path=

	outputfile=open("dtapost4.txt","a")
	vocab = [{},{},{},{},{},{},{}]
	V =[]
	alltags=set()
	classoccur=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	for p in range(len(path)):
		print path[p]
		for filename in os.listdir(pathname+path[p]):
			classoccur[p]+=1
			inputfile=codecs.open(pathname+path[p]+filename,'r')

			for line in  inputfile:
				line=line.replace('\n','')
				content=line.split("\t")
				post_id=content[0]
				post_title=content[1]
				post_tags=content[2]
				post_tags=post_tags.lower()
				post_tags=post_tags.replace("-"," ")
#				post_tags=post_tags.replace(', ',',')
				tags = post_tags.split(', ')
				for t in tags:
					if t.endswith("s"):
						if t.endswith(ies):
							t=t[:len(t)-len(ies)]
							t=t+"y"
						else:
							t=t[0:len(t)-1]
					if t not in alltags:
						alltags.add(t)
					if t not in vocab[p]:
						vocab[p].update({t:1})
					else:
						vocab[p][t]+=1


		V.append(sum(vocab[p].values()))


	for alpha in range(len(vocab)):
		classdict=open("eattreat dictionary/dictionary_"+path1[alpha]+".txt","a")
		print vocab[alpha]
		print '\n\n'
		for key in vocab[alpha]:
			classdict.write(str(key)+"\t"+str(vocab[alpha][key])+"\n")


	naive = [{},{},{},{},{},{},{}]
	#print vocab
#	print '\n'
#	print V
	lenalltags=len(alltags)

	#for e in vocab:
	#	naive.update({e:float(float(1+vocab[e])/float(1+V))})	

	#print naive

	for file in os.listdir('F:\work\eattreat dataforpost'):
		inputfile=codecs.open('F:/work/eattreat dataforpost/'+file,'r')
		for line in  inputfile:
			line =  line.replace('\n',"")
			content=line.split("\t")
			post_id=content[0]
			post_title=content[1]
			post_tags=content[2]
			post_tags=post_tags.lower()
			post_tags=post_tags.replace("-"," ")
			test_tags= post_tags.split(', ')

		sum1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		for k in range(len(vocab)):
			#print k
			s=1.0
			for eota in test_tags:
				e=eota.lower()
				if e.endswith("s"):
						if e.endswith(ies):
							e=e[:len(e)-len(ies)]
							e=e+"y"
						else:
							e=e[0:len(e)-1]
				if e not in alltags:
					alltags.add(e)
					lenalltags+=1
				if e not in vocab[k]:
					vocab[k].update({e:1})
					V[k]+=1
				else:
					vocab[k][e]+=1
					V[k]+=1
				naive[k].update({e:float(float(1+vocab[k][e])/float(lenalltags+V[k]))})
				s=s*naive[k][e]
#			print ("the s is ")
#			print s
#			print("the classoccur is ")
#			print classoccur[k]

#			print("the beta is ")
#			print("the sum is ")

			
			beta=float(s*(classoccur[k]/sum(classoccur)))
#			print beta
			sum1[k]=beta
#			print sum1

		inputfile.close()
		#for u in naive:
			#print u

#		print sum1
		max_value = max(sum1)
		max_index = sum1.index(max_value)
#		print max_value
#		print max_index
#		print V
		classoccur[max_index]+=1
#		print classoccur
		data = {}
		data['post_id'] = post_id
		data['post_title']=post_title
		data['post_class']=path1[max_index]
		json_data = json.dumps(data)
		#print json_data
		#outputfile.write("post_category={\"post_id\":\""+post_id+"\","+"\"post_title\":\""+post_title+"\",\"post_class\":\""+path[max_index]+"\""+"\n")
		outputfile.write(file+"\t"+post_title+"\t"+post_tags+"\t"+path1[max_index]+"\n")
		#os.rename('F:/work/eattreat dataforpost/'+file, pathname +path[max_index]+file)
	#path1 = ['Bakery&Sweets','Snacks','Meats','Organics','Other']
	
#json_data=
naivebayes()