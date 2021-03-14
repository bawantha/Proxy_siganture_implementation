class ProxySigner():
    __signma=0;
    __K=0;

    def passKeys(self,sigma,k):
        self.__K=k;
        self.__signma=sigma;
    def printVals(self):
        print(self.__K,self.__signma);
    def __str__(self):
        return "This is proxy Signer"
    def sigma(self):
        return self.__signma
    def K(self):
        return self.__K
