import numpy as np
import math as mt

class Dataset():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y  

class Matematicas(Dataset):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def MatrizX(self):
        x = np.array(self.x)
        ns1 = np.ones((len(x), 1))
        x_squand = np.square(self.x)
        join = np.concatenate((ns1, x.reshape(-1, 1), x_squand.reshape(-1, 1)), axis=1)
        np.set_printoptions(formatter={'float': '{:.2f}'.format})
        return join

    def traspuesta(self):
        matrixTras = self.MatrizX()
        traspuestaM = np.transpose(matrixTras)
        return traspuestaM

    def MultiMatrixial(self):
        varMatrixNormal = self.MatrizX()
        varMatrixTras = self.traspuesta()
        Total = np.dot(varMatrixTras, varMatrixNormal)
        return Total

    def InverMAtrix(self):
        varMultiMat = self.MultiMatrixial()
        inver = np.linalg.inv(varMultiMat)
        return inver

    def MultiXTrasPInver(self):
        varInverMatrix = self.InverMAtrix()
        varTrasMatrix = self.traspuesta()
        total = np.dot(varInverMatrix, varTrasMatrix)
        return total


class main(Matematicas):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def MultiPY(self):
        vary = np.array(self.y)
        varMultiTrasPinver = self.MultiXTrasPInver()
        total = np.dot(varMultiTrasPinver, vary)
        #total = np.inner() es lo mismo que lo de arriva 
        return total
    
    def passTList(self):
        listaR2 =[] 
        listaR = self.MultiPY()
        for i  in listaR:
            listaR2.append(i)
            
        return listaR2


    def Prediccion(self,numero):
        varlist = self.passTList()
        listX = [numero, numero ** 2]
        
        calculo1 = varlist[1] * listX[0] 
        calculo2 = varlist[2] * listX[1]
        #print(f"calculo 1 {calculo1}, calculo2 {calculo2}")
        Total = varlist[0]  + calculo1 + calculo2
        return Total


    def R_cuadrado(self):
        y_hat = np.asarray([self.Prediccion(x_val) for x_val in self.x])
        y_mean = np.mean(self.y)
        SS_res = np.sum((self.y - y_hat) ** 2)
        SS_tot = np.sum((self.y - y_mean) ** 2)
        R2 = 1 - (SS_res / SS_tot)
        return R2
    


    
#x 
x=[108,115,106,97,95,91,97,83,83,78,54,67,56,53,61,115,81,78,30,45,99,32,25,28,90,89]
#y
y=[95,96,95,97,93,94,95,93,92,86,73,80,65,69,77,96,87,89,60,63,95,61,55,56,94,93]


print("\n----------------Y\U0001F600---R\u00B2----------------")

objet_0 = main(x,y)
print(objet_0.passTList())
print(f"La R\u00B2 = {objet_0.R_cuadrado()}")


print("\n-----------------------1\U0001F600-----------------------")

objet_1 = main(x,y)
print(objet_1.Prediccion(108))
#print(objet_1.R_cuadrado())

print("\n-----------------------2\U0001F600-------------------------")
objet_2 = main(x,y)
print(objet_2.Prediccion(97))
#print(objet_2.R_cuadrado())

print("\n-----------------------3\U0001F600--------------------------")
objet_3 = main(x,y)
print(objet_3.Prediccion(20))
#print(objet_3.R_cuadrado())

print("\n-----------------------4\U0001F600---------------------------")
objet_4 = main(x,y)
print(objet_4.Prediccion(40))
#print(objet_4.R_cuadrado())

print("\n-----------------------5\U0001F600---------------------------")
objet_5 = main(x,y)
print(objet_5.Prediccion(39))
print("\n\n")
#print(objet_5.R_cuadrado())
