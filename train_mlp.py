from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

class Model:
    def __init__(self , 
                 neural_network=( 128,64, 64, 128, 64, 32, 16,),
                 max_iter=1000,
                 activation='relu',
                 learning_rate_init=0.001,
                 alpha=1e-3
                 ) -> None:
        self.neural_network = neural_network
        self.mlp = MLPClassifier(max_iter=max_iter,
                                 activation=activation, 
                                 learning_rate_init=learning_rate_init,
                                 solver='adam', 
                                 alpha=alpha,
                                 hidden_layer_sizes=self.neural_network, 
                                 random_state=42)

    def train(self,X_train,y_train):
        self.mlp.fit(X_train, y_train)

    def score(self,X_test,y_test):
        accuracy_score(y_test, self.mlp.predict(X_test))