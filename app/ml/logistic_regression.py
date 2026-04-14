import numpy as np

class LogisticRegression:
    def __init__(self, lr, epochs = 1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.losses = [] 
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def predict_proba(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear_model)
    
    def predict(self, X):
        if self.weights is None or self.bias is None:
            raise Exception("Model is not trained!")
        
        y_pred = self.predict_proba(X)
        return np.array([1 if i > 0.5 else 0 for i in y_pred])
    
    def compute_loss(self, y_true, y_pred):
        # binary cross entropy
        epsilon = 1e-9
        y1 = y_true * np.log(y_pred + epsilon)
        y2 = (1-y_true) * np.log(1 - y_pred + epsilon)
        return -np.mean(y1 + y2)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            # forward pass
            linear_model = np.dot(X, self.weights) + self.bias
            A = self.sigmoid(linear_model)
            
            # gradients
            dz = A - y
            dw = (1 / n_samples) * np.dot(X.T, dz)
            db = (1 / n_samples) * np.sum(dz)

            # update
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            # loss
            loss = self.compute_loss(y, A)
            self.losses.append(loss)
        
        def accuracy(self, y_true, y_pred):
            return np.mean(y_true == y_pred)