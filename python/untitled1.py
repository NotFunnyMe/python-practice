import matplotlib.pyplot as ply
import statistics 
estimates = [291, 208, 92, 735, 994, 604, 190, 549, 568, 863, 681, 967, 528, 568, 54, 561, 423, 968, 294, 512, 312, 847, 131, 861, 235, 317, 128, 68, 757, 599, 551, 814, 340, 618, 922, 122, 371, 57, 145, 220, 697, 241, 157, 619, 244, 95, 536, 499, 39, 809, 768, 520, 244, 880, 333, 15, 853, 973, 799, 238, 639, 355, 355, 695, 140, 465, 596, 970, 778, 428, 792, 757, 185, 895, 692]
y=[]

estimates.sort()
tv=int(0.1*(len(estimates)))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
for i in range(len(estimates)):
    y.append(5)

ply.plot(estimates,y,'r--')
ply.plot([statistics.mean(estimates)],[5],'ro')
ply.plot([statistics.median(estimates)],[5],'bs')
ply.plot([375],[5],'g^')
