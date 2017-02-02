#!/usr/bin/env python
def naivebayes() :
	import sys
	import os
	import codecs
	import json
	pathname="F:/work/eattreat classes/"
	path = ['Bakery&Sweets/','Snacks/','Meats/','Organics/','Other/','Drinks/','Restaurants/']
	path1 = ['Bakery&Sweets','Snacks','Meats','Organics','Other','Drinks','Restaurants']
	#save_path=

	outputfile=open("dtapost4.txt","a")
	vocab = [{},{},{},{},{},{},{}]
	V =[]
	alltags=set()
	classoccur=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	for p in range(len(path)):
		
		for filename in os.listdir(pathname+path[p]):
			classoccur[p]+=1
			inputfile=codecs.open(pathname+path[p]+filename,'r')
			for line in  inputfile:
				content=line.split("\t")
				post_id=content[0]
				post_title=content[1]
				post_tags=content[2]
				post_tags=post_tags.lower()
				post_tags=post_tags.replace("-"," ")
				tags = post_tags.split(', ')
				for t in tags:
					
					if t not in alltags:
						alltags.add(t)
					if t not in vocab[p]:
						vocab[p].update({t:1})
					else:
						vocab[p][t]+=1


		V.append(sum(vocab[p].values()))

	naive = [{},{},{},{},{},{},{}]
	#print vocab
	print '\n'
	#print V
	lenalltags=len(alltags)

	#for e in vocab:
	#	naive.update({e:float(float(1+vocab[e])/float(1+V))})	

	#print naive
#	for file in os.listdir('F:\work\eattreat dataforpost'):
#		inputfile=codecs.open('F:/work/eattreat dataforpost/'+file,'r')
#		for line in  inputfile:
#			content=line.split("\t")
#			post_id=content[0]
#			post_title=content[1]
#			post_tags=content[2]
#			test_tags= post_tags.split(',')
	test_tags=[]
	for loop in range(len(sys.argv)-1):
		clean_tags=sys.argv[loop+1]
		clean_tags=clean_tags.lower()
		clean_tags=clean_tags.replace("-"," ")
		test_tags.append(clean_tags)

	sum1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	for k in range(len(vocab)):
			#print k
		s=1.0
		for e in test_tags:
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
		#print ("the s is ")
		#print s
		#print("the classoccur is ")
		#print classoccur[k]

		#print("the beta is ")
		
		
		beta=float(s*(classoccur[k]/sum(classoccur)))
		#print beta
		sum1[k]=beta
		

	inputfile.close()
	#for u in naive:
		#print u
	print("the sum is ")

	print sum1
	#print sum1
	max_value = max(sum1)
	max_index = sum1.index(max_value)
	#print max_value
	#print max_index
	#print V
	classoccur[max_index]+=1
	#print classoccur
	data = {}
	data['post_id'] = post_id
	data['post_title']=post_title
	data['post_class']=path1[max_index]
	json_data = json.dumps(data)
	#print json_data
	print path1[max_index]
		#outputfile.write("post_category={\"post_id\":\""+post_id+"\","+"\"post_title\":\""+post_title+"\",\"post_class\":\""+path[max_index]+"\""+"\n")
		#os.rename('F:/work/eattreat dataforpost/'+file, pathname +path[max_index]+file)
	#path1 = ['Bakery&Sweets','Snacks','Meats','Organics','Other']
	#for alpha in range(len(vocab)):
	#	classdict=open("dictionary"+path1[alpha]+".txt","a")
	#	for key in vocab[alpha]:
	#		classdict.write(str(key)+"\t"+str(vocab[alpha][key])+"\n")
#json_data=
naivebayes()