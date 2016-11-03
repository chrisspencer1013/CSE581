from math import sqrt

SSEa = 0
SSEb = 0
SSEc = 0

x1 = [4,5]
x2 = [1,4]
x3 = [0,1]
x4 = [5,0]
data = [x1,x2,x3,x4]

att1P1meanC = (x1[0]+x2[0]+x3[0])/3
att2P1meanC = (x1[1]+x2[1]+x3[1])/3
P1meansC = [att1P1meanC,att2P1meanC]

att1P2meanC = (x4[0])
att2P2meanC = (x4[1])
P2meansC = [att1P2meanC,att2P2meanC]

print("Partition C means: \nP1:", P1meansC, "\nP2:", P2meansC)
i=1
for i in range(4):
    distC = sqrt( (P1meansC[0]-data[i][0])**2 + (P1meansC[1]-data[i][1])**2 )
    SSEc += distC**2

print("SSE for Partition C: ",SSEc)

att1P1meanB = (x1[0]+x4[0])/2
att2P1meanB = (x1[1]+x4[1])/2
P1meansB = [att1P1meanB,att2P1meanB]

att1P2meanB = (x3[0]+x2[0])/2
att2P2meanB = (x3[1]+x2[1])/2
P2meansB = [att1P2meanB,att2P2meanB]

print("Partition B means: \nP1:", P1meansB, "\nP2:",P2meansB)
i=1
for i in range(4):
    distB = sqrt( (P1meansB[0]-data[i][0])**2 + (P1meansB[1]-data[i][1])**2 )
    SSEb += distB**2

print("SSE for Partition B: ",SSEb)

att1P1meanA = (x1[0]+x2[0])/2
att2P1meanA = (x1[1]+x2[1])/2
P1meansA = [att1P1meanA,att2P1meanA]

att1P2meanA = (x3[0]+x4[0])/2
att2P2meanA = (x3[1]+x4[1])/2
P2meansA = [att1P2meanA,att2P2meanA]

print ("Partition A means: \nP1:", P1meansA, "\nP2:",P2meansA)
i=0
for i in range(4):
    distA = sqrt( (P1meansA[0]-data[i][0])**2 + (P1meansA[1]-data[i][1])**2 )
    SSEa += distA**2

print("SSE for Partition A: ",SSEa)

