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



def ProbabilityDistribution(minoritySelected, majoritySelected, minority, majority):
	total = minoritySelected + majoritySelected
	ans = ''
	mina=0
	maxa=0
	mean_mina=0
	mean_maja=0
	ans+= '\nMajority: '+str(majority)+'\tMajority Selected: '+str(majoritySelected)
	ans+= '\nMinority: '+str(minority)+'\tMinority Selected: '+str(minoritySelected)+'\n\n'


	if(minority == majority ):
		if((minoritySelected+majoritySelected) > majority):
			# print('1st')
			for val in range(0,minority+1):
				if(((minoritySelected+majoritySelected) - majority + val) > majority):
					# print('break1')
					break
				mino = (minoritySelected+majoritySelected) - majority + val
				majo = majority - val
				if(mino == minoritySelected):
					if( majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'Selected-> '+str(mino) + ' ' + str(majo)+'\n'
						
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + ' ' + str(majo) +'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
					
					mina=mino
					maxa=majo
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo

					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					if(adverseImpact(mino,majo,minority,majority) == 1):
						mean_mina=mino
						mean_maja=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'

			# return ans

		elif((minoritySelected+majoritySelected) <= majority):
			# print('2nd')
			for val in range(0,minority+1):
				if((total-val) < 0):
					# print('break1')
					break
				mino = val
				majo = total - val 
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'Selected-> '+str(mino) + ' ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + ' ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					if(adverseImpact(mino,majo,minority,majority) == 1):
						mean_mina=mino
						mean_maja=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			# return ans
	elif(minority > majority):
		if((majoritySelected+minoritySelected) <= majority):
			# print('3rd')
			for val in range(0,(majoritySelected+minoritySelected)+1):
				if(((minoritySelected+majoritySelected) - val) < 0):
					# print('break3')
					break
				mino = val
				majo = (minoritySelected+majoritySelected) - val

				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+ '\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+ '\n'
				# print(str(mino)+' '+str(majo)+' '+str(minority)+' '+str(majority))
				# print(adverseImpact(mino,majo,minority,majority))
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					if(adverseImpact(mino,majo,minority,majority) == 1):
						mean_mina=mino
						mean_maja=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			# return ans

		elif((majoritySelected+minoritySelected) > majority):
			# print('4th')
			for val in range(0,majority+1):
				if((((minoritySelected+majoritySelected) - majority) + val) > minority):
					# print('break4')
					break
				mino = ((minoritySelected+majoritySelected) - majority) + val
				majo = min(majority, minority) - val
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+ '\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+ '\n'

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					if(adverseImpact(mino,majo,minority,majority) == 1):
						mean_mina=mino
						mean_maja=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			# return ans

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
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print() 
					if(adverseImpact(mino,majo,minority,majority) == 1):
						mean_mina=mino
						mean_maja=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			# return ans

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
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					if(adverseImpact(mino,majo,minority,majority) == 1):
						mean_mina=mino
						mean_maja=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			# return ans

		elif((minoritySelected+majoritySelected) > majority):
			# print('7th')
			for val in range(0,majority+1):
				if(((minoritySelected+majoritySelected) - minority) + val > majority ):
					# print('break7')
					break
				mino = ((minoritySelected+majoritySelected) - majority) + val
				majo = majority - val
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					mina=mino
					maxa=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					if(adverseImpact(mino,majo,minority,majority) == 1):
						mean_mina=mino
						mean_maja=majo
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			# return ans

	ans+= '\n\nFrom the given data above, total '+str(mino+majo)+' Applicants were Selected out of '+str(majority)+ ' Majority Applicants and '+str(minority)+' Minority Applicants.\n'
	ans+= 'And if you select less than or equal to '+str(mina)+' Minority Applicants, Adverse Impact would be FOUND.\n'
	# ans+= 'Also Inorder to avoid any Adverse Impact, the required number of Minority Applicants should be '+str(mean_mina)+'. As this is the mean of Probability Distribution.(\n Here the adverse impact ration becomes 1.)'
	return ans

print(ProbabilityDistribution(9,48,10,50))
#print(adverseImpact(1,17,100,100))
