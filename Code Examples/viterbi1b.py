
"""Global Alignment with Viterbi Algorithm"""


observations = "666666666"
trellis=[]
directions=[]
trellis.append([0]*(len(observations)+1))
trellis.append([0]*(len(observations)+1))
directions.append([0]*(len(observations)+1))
directions.append([0]*(len(observations)+1))
transitionProbs =[[0.95,0.05],[0.1,0.9]] #[[ff,fl],[lf,ll]]
emitProbFair = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
emitProbLoad = [1/10, 1/10, 1/10, 1/10, 1/10, 1/2]
print(trellis)

trellis[0][0] = 0.9 # start in fair probability
trellis[1][0] = 0.1 # start in loaded probability
for i in range(1,len(observations)+1):
    
    fairTofair = trellis[0][i-1]*transitionProbs[0][0]*emitProbFair[int(observations[i-1])-1]
    loadTofair = trellis[1][i-1]*transitionProbs[1][0]*emitProbFair[int(observations[i-1])-1]
    trellis[0][i] = max(fairTofair,loadTofair)
    
    if(fairTofair > loadTofair):
        directions[0][i] = 'f'
    else:
        directions[0][i] = 'l'
    
    fairToload = trellis[0][i-1]*transitionProbs[0][1]*emitProbLoad[int(observations[i-1])-1]
    loadToload = trellis[1][i-1]*transitionProbs[1][1]*emitProbLoad[int(observations[i-1])-1]
    
    if(fairToload > loadToload):
        directions[1][i] = 'f'
    else:
        directions[1][i] = 'l'
    trellis[1][i] = max(fairToload,loadToload)

if(trellis[0][-1] > trellis[1][-1]):
    state = 0 #start in the fair state
else:
    state = 1 #start in the loaded state

states = [state]

for i in range (len(observations)-1,0,-1):

    if(directions[state][i] == 'f'):
        states.append(0) #came from fair state
        state = 0
    else:
        states.append(1) #came from loaded state
        state = 1

states.reverse()
print(states)

print(trellis[0])
print(trellis[1])
print(directions[0])
print(directions[1])