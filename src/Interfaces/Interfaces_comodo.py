from abc import ABC,abstractmethod

class InterfaceComodo(ABC):
   
    @abstractmethod
    def Nome(self)->str:
        pass

    @abstractmethod
    def SetNome(self,nomenovo:str)->None:
        pass

    @abstractmethod
    def Quantidade_dispositivo(self)->int:
         pass
    
    # Cria um  dispositivo de um tipo, sendo Lampada,Cortina,Arcondicionado e  Janela, 1,2,3 e 4  respectivamente e com o nome que o usuario escolher
    @abstractmethod
    def AdicionarDispositivo(self,tipo:int,nome:str)->None:
        pass

    # remove o dispositivo de um tipo,sendo Lampada,Cortina,Arcondicionado e  Janela, 1,2,3 e 4  respectivamente, que possui determinado nome 
    @abstractmethod
    def RemoverDispositivo(self,tipo:int,nome:str)->None:
        pass
    
    @abstractmethod
    def ConfigurarTodos(self,tipo:int,nome:str)->None:
        pass

   