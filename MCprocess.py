from numpy.linalg import inv
import numpy as np
i=-1
errorS=" "
while(i<10):
    with open("may29_transitions.txt") as f:
        i=i+1
        lines = f.readlines()
        errorLine = ""
        for k in range(0, len(lines)):
            line = lines[k]
            if("it("+str(i)+") - gen" in line):
                errorLine = line
                k=k+3
                line = lines[k]
                linex = line.split(",")
                fitnesses = np.array([])
                for item in linex:
                    itemx = item.split("-")
                    fitnesses=np.append(fitnesses,int(itemx[1]))
                    index = np.argsort(fitnesses)
                print(index)
            if("it("+str(i)+");" in line):
                s1=line.split(" ")
                original= np.array([]).reshape(0,int(s1[1]))
                for j in range(int(s1[1])):
                    line = lines[k+j+1]
                    line=line.rstrip()
                    row = line.split(" ")
                    print(line)
                    a = np.array([])
                    for item in row:
                        a = np.append(a, float(item))
                    original = np.vstack([original, a])
                first= np.array([]).reshape(int(s1[1]),0)
                for j in index:
                    first=np.column_stack([first, original[:,j]])
                second= np.array([]).reshape(0,int(s1[1]))
                for j in index:
                    second=np.vstack([second, first[j,:]])
                np.savetxt("second.csv", second, delimiter=",")
                try:
                    iM=np.identity(int(s1[1]))
                    np.savetxt("identity.csv", iM, delimiter=",")
                    mM=iM-second
                    ainv = inv(mM)
                    #print(ainv)
                    np.savetxt("res.csv", ainv, delimiter=",")
                    break
                except:
                    errorS= errorS + errorLine+ '\n'

print(errorS)
                
