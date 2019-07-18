import operator
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

def adverseImpact(minoritySelected, majoritySelected, minority, majority):
    rateOfMinority = float(float(minoritySelected) / float(minority))

    rateOfMajority = float(float(majoritySelected) / float(majority))
    if rateOfMajority == 0:
        adverseImpactMinority = 879645.000000202020
    else:
        adverseImpactMinority = float(float(rateOfMinority) / float(rateOfMajority))
    if rateOfMinority == 0:
        adverseImpactMajority = 0
    else:
        adverseImpactMajority = float(float(rateOfMajority) / float(rateOfMinority))
    # print('Rate of Minority: ' + str(rateOfMinority))
    # print('Rate of Majority: ' + str(rateOfMajority))
    # print('Adverse Impact on Minority: ' + str(adverseImpactMinority))
    # print('Adverse Impact on Majority: ' + str(adverseImpactMajority))
    return adverseImpactMinority

def nCr(n, r):
	r = min(r, n-r)
	num = reduce (operator.mul, range(n,n-r,-1), 1)
	den = reduce (operator.mul, range(1,r+1),1)
	return num/den

def array_x_axis(females):
	x_axis=females
	return x_axis

def array_y_axis(probability):
	y_axis= probability
	return y_axis

def plot_bar(graph_list_pro , graph_list_females):
	index = np.arange(len(graph_list_pro))
	plt.bar(index, graph_list_pro)
	plt.xlabel('Number of female Applicants Selected', fontsize=10)

	plt.xticks(index, graph_list_females, fontsize=5)
	plt.title('Probability Distribution of the variable: Number of Female Selected.', fontsize=12)
	plt.show()

def near(onelist, val):
	onelist = np.asarray(onelist)
	idx = (np.abs(onelist - val)).argmin()
	return onelist[idx]

def ProbabilityDistribution(minoritySelected, majoritySelected, minority, majority):
	total = minoritySelected + majoritySelected
	ans = ''
	pro=0
	cumpro=0
	mina=0
	maxa=0
	mean_mina=0
	mean_maja=0
	start=0
	stop=0
	graph_list_females = []
	onelist = []
	onelist_min = []
	graph_list_pro = [] 
	# ans+= '\nMajority: '+str(majority)+'\tMajority Selected: '+str(majoritySelected)
	# ans+= '\nMinority: '+str(minority)+'\tMinority Selected: '+str(minoritySelected)+'\n\n'
	temp=True

	if(minority == majority ):
		if((minoritySelected+majoritySelected) > majority):
			# print('1st')

			for val in range(0,minority+1,2):
				if(((minoritySelected+majoritySelected) - majority + val) > majority):
					# print('break1')
					break
				mino = (minoritySelected+majoritySelected) - majority + val
				majo = majority - val
				# #if(mino == minoritySelected):
					# if( majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						# ans += 'Selected-> '+str(mino) + ' ' + str(majo)+'\n'
						
				# else:
					# print(str(mino) + '  ' + str(majo))
					# ans += str(mino) + ' ' + str(majo) +'\n'

				if(temp == True):
					start=mino
					temp=False	

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
					mina=mino
					maxa=majo
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# if(adverseImpact(mino,majo,minority,majority) == 1):
					# 	mean_mina=mino
					# 	mean_maja=majo
					onelist.append(adverseImpact(mino,majo,minority,majority))
					onelist_min.append(mino)
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)

					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
			# return ans
			stop = mino
		elif((minoritySelected+majoritySelected) <= majority):
			# print('2nd')
			for val in range(0,minority+1):
				if((total-val) < 0):
					# print('break1')
					break
				mino = val
				majo = total - val 
				# #if(mino == minoritySelected):
					# #if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						# ans += 'Selected-> '+str(mino) + ' ' + str(majo)+'\n'
				# else:
					# print(str(mino) + '  ' + str(majo))
					# ans += str(mino) + ' ' + str(majo)+'\n'

				if(temp == True):
					start=mino
					temp=False

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)

					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'				
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)

					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# if(adverseImpact(mino,majo,minority,majority) == 1):
					# 	mean_mina=mino
					# 	mean_maja=majo
					onelist.append(adverseImpact(mino,majo,minority,majority))
					onelist_min.append(mino)
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
			# return ans
			stop = mino
	elif(minority > majority):
		if((majoritySelected+minoritySelected) <= majority):
			# print('3rd')
			for val in range(0,(majoritySelected+minoritySelected)+1):
				if(((minoritySelected+majoritySelected) - val) < 0):
					# print('break3')
					break
				mino = val
				majo = (minoritySelected+majoritySelected) - val

				#if(mino == minoritySelected):
					#if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						# ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+ '\n'
				# else:
					# print(str(mino) + '  ' + str(majo))
					# ans += str(mino) + '  ' + str(majo)+ '\n'
				# print(str(mino)+' '+str(majo)+' '+str(minority)+' '+str(majority))
				# print(adverseImpact(mino,majo,minority,majority))
				if(temp == True):
					start=mino
					temp=False

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# if(adverseImpact(mino,majo,minority,majority) == 1):
					# 	mean_mina=mino
					# 	mean_maja=majo
					onelist.append(adverseImpact(mino,majo,minority,majority))
					onelist_min.append(mino)
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
			# return ans
			stop = mino
		elif((majoritySelected+minoritySelected) > majority):
			# print('4th')
			for val in range(0,majority+1):
				if((((minoritySelected+majoritySelected) - majority) + val) > minority):
					# print('break4')
					break
				mino = ((minoritySelected+majoritySelected) - majority) + val
				majo = min(majority, minority) - val
				#if(mino == minoritySelected):
					#if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						# ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+ '\n'
				# else:
					# print(str(mino) + '  ' + str(majo))
					# ans += str(mino) + '  ' + str(majo)+ '\n'

				if(temp == True):
					start=mino
					temp=False

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# if(adverseImpact(mino,majo,minority,majority) == 1):
					# 	mean_mina=mino
					# 	mean_maja=majo
					onelist.append(adverseImpact(mino,majo,minority,majority))
					onelist_min.append(mino)
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
			# return ans
			stop = mino
	#majority>minority	
	else:
		if((minoritySelected+majoritySelected) <= minority):
			# print('5th')
			for val in range(0,(minoritySelected+majoritySelected)+1):
				if(((majoritySelected+minoritySelected)+ val) < 0):
					# print('break5')
					break
				mino = val
				majo = (minoritySelected+majoritySelected) - val
				#if(mino == minoritySelected):
					#if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						# ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				# else:
					# print(str(mino) + '  ' + str(majo))
					# ans += str(mino) + '  ' + str(majo)+'\n'
				
				if(temp == True):
					start=mino
					temp=False

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print() 
					# if(adverseImpact(mino,majo,minority,majority) == 1):
					# 	mean_mina=mino
					# 	mean_maja=majo
					onelist.append(adverseImpact(mino,majo,minority,majority))
					onelist_min.append(mino)
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
			# return ans
			stop = mino
		elif(((minoritySelected+majoritySelected) > minority) & ((minoritySelected+majoritySelected) <= majority)):
			# print('6th')
			# print('(minoritySelected+majoritySelected) '+ str(minoritySelected)+ ' ' + str(majoritySelected)+ ' '+ str(minoritySelected+majoritySelected))
			# print(str(majority))
			for val in range(0,minority +1):
				if((((minoritySelected+majoritySelected) - minority) + val) > majority):
					# print('break6')
					break
				mino = val
				majo = (minoritySelected+majoritySelected) - val
				#if(mino == minoritySelected):
					#if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						# ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				# else:
					# print(str(mino) + '  ' + str(majo))
					# ans += str(mino) + '  ' + str(majo)+'\n'
				
				if(temp == True):
					start=mino
					temp=False

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# if(adverseImpact(mino,majo,minority,majority) == 1):
					# 	mean_mina=mino
					# 	mean_maja=majo
					onelist.append(adverseImpact(mino,majo,minority,majority))
					onelist_min.append(mino)
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
			# return ans
			stop = mino
		elif((minoritySelected+majoritySelected) > majority):
			# print('7th')
			for val in range(0,majority+1):
				if(((minoritySelected+majoritySelected) - minority) + val > majority ):
					# print('break7')
					break
				mino = ((minoritySelected+majoritySelected) - majority) + val
				majo = majority - val
				#if(mino == minoritySelected):
					#if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						# ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				# else:
					# print(str(mino) + '  ' + str(majo))
					# ans += str(mino) + '  ' + str(majo)+'\n'
				
				if(temp == True):
					start=mino
					temp=False

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					# if(adverseImpact(mino,majo,minority,majority) == 1):
					# 	mean_mina=mino
					# 	mean_maja=majo
					onelist.append(adverseImpact(mino,majo,minority,majority))
					onelist_min.append(mino)
					# ans += 'Adverse Impact Ratio of Minority: '+str(round(adverseImpact(mino,majo,minority,majority),4))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
					pro = round(( (nCr(minority,mino)*nCr(majority,majo)) / nCr(minority+majority, mino+majo)),4)
					if(pro != 0.0):
						graph_list_pro.append(pro)
						graph_list_females.append(mino)
					cumpro += pro
					cumpro = round(cumpro, 4)
					# ans += 'Probability = '+ str(pro)+'\nCumulative Probability = '+str(cumpro)+'\n\n'
			stop =mino
			# return ans

	ans+= '\n\nFrom the given data above, total '+str(mino+majo)+' Applicants were Selected out of '+str(majority)+ ' Majority Applicants and '+str(minority)+' Minority Applicants.\n'
	ans+= 'Adverse Impact would be found if you Select '+str(mina)+' or fewer Minority.\n'
	# ans+= 'Also Inorder to avoid any Adverse Impact, the required number of Minority Applicants should be '+str(mean_mina)+'. As this is the mean of Probability Distribution.(\n Here the adverse impact ration becomes 1.)'
	# print('\n\n'+str(graph_list_females)+'\n'+str(graph_list_pro))
	# print(array_x_axis(graph_list_females))
	# print(array_y_axis(graph_list_pro))

	#ans += str(mean_mina) + '  ' +str(mean_maja)
	# print(str(onelist))
	minimum = near(onelist, 1)
	# print(str(onelist))
	# print('minimum: '+str(minimum))
	indexx = onelist.index(minimum)

	ans += '\nThe probability distribution of having Selected from '+str(start)+' to '+str(stop)+' minority is displayed above. The graph above is shown starting with '+str(graph_list_females[0])+' since the \n'
	ans += 'probabilities below this point are near zero. As can be seen, the most likely event (highest probability) to have occurred by chance (or decisions not affected by any\n'
	ans += 'form of bias) is to have Selected '+str(onelist_min[indexx])+' minority Applicants. This represents the mean of the probability distribution. Approximately half of the probability distribution is above this point and approximately half is below this point.'
	# 
	ans += '\n\n'+str(array_x_axis(graph_list_females))+'\n\n'+str(array_y_axis(graph_list_pro))
	plot_bar(graph_list_pro, graph_list_females)
	return ans

print(ProbabilityDistribution(40,50,50,80))
#print(adverseImpact(1,17,100,100))
