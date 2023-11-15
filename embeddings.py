from sentence_transformers import SentenceTransformer

class Embeddings():
    def __init__(self) -> None:
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def encode(self,data : list = None) -> list:
        """ input : context or context in list
                example text : "Hello" , 
                example context in list : ["Hello" , "Hi" , "IM" ]

            output : type same input   
             """
        embedding = self.model.encode(data)
        return embedding 