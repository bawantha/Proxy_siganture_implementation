import random
from ProxySigner import ProxySigner
class OriginalSigner:
    __primeNumber=0;
    __pirvateKey=0;
    __verifyKey=0;
    __generator=0;
    def getVerifyKey():
        return __verifyKey;

    def __init__(self,p):
        self.__primeNumber=p;
        self.__secretKeyandGgen()
        print("private=",self.__pirvateKey)
        print("generator=",self.__generator)
        self.__verifyKeyGen()
        print("verify=",self.__verifyKey)
        

    def getVerifyKey(self):
        return self.__verifyKey;

    def __keyPairGenerate(self):

        return "pass"        

    def __setOfZp(self):
        return list(range(1,self.__primeNumber))

    def __setOfZpMinus1Exlcude0(self):
        return list(range(1,self.__primeNumber-1))

    def __secretKeyandGgen(self):
        zpMinus1=self.__setOfZpMinus1Exlcude0()
        zp=self.__setOfZp()
        self.__generator=random.choice(zp)
        self.__pirvateKey=random.choice(zpMinus1)

    def __verifyKeyGen(self):
        self.__verifyKey= self.__generator**self.__pirvateKey % self.__primeNumber


    def genrateProxyKeypair(self,ps ):
        zpMinus1=self.__setOfZpMinus1Exlcude0()
        k=random.choice(zpMinus1)
        K=self.__generator**k % self.__primeNumber
        sigma=self.__pirvateKey+k*K
        ps.passKeys(sigma,K)


    def proxyVerification(self,proxy):
        if (self.__generator** proxy.sigma()  % self.__primeNumber == self.__verifyKey*proxy.K() **proxy.K() % self.__primeNumber):
            print("benign  proxy")
        else:
            print("bogus proxy")
        

        

# Create Original Signer with Prime (p) number 91
o=OriginalSigner(91);
#  Craete Proxy Signer
proxy1=ProxySigner();

# Pass proxy1 to generate Proxy (sigma,K)
o.genrateProxyKeypair(proxy1);

# validate proxy1 

o.proxyVerification(proxy1)

