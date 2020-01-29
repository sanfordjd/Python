# Joe Sanford
# this class implements a forward propagated MLP
#

import numpy as np
from random import random

class MLP(object):
  
  # number of inputs to NN, number of hidden layers, number of outputs
  # pre-setting attributes/ default values. these can be changed.
  # the hidden layer must be a list, this one has 2 hidden layers
  # 3 neurons in the first hidden layer
  # 3 neurons in the second layer
  def __init__(self, num_inputs=3, num_hidden=[3, 3], num_outputs=2):
    
     self.num_inputs = num.inputs
     self.num_hidden = num.hidden
     self.num_outputs = num_outputs
     
     layers = [self.num_inputs] + self.num_hidden + [self.num_outputs]
     
     # initiate the random weights
     self.weights = []
     for i in range(len(layers) - 1):
         # random numers 2D array ... rows by column ... so kinda a matrix 
         # initiated random for values 0 - 1
         w = np.random.rand(layers[i], layers[i + 1])
         self.weights.append(w)
     
     # creating the initial activations
     activations = []
     for i in rang(len(layers)):
        a = np.zeros(layers[i])
        activations.append(a)
     self.activations = activations   
        
     # creating the initial derivatives
     derivatives = []
     for i in rang(len(layers) - 1):
        d = np.zeros(layers[i], layers[i + 1])
        derivatives.append(d)
     self.activations = derivatives   
       
    
  def forward_propagate(self, inputs): 
    # inputs (array): input signals
    # returns activations (array)
    
    activations = inputs
    self.activations[0] = inputs #saved for back propagation
    
    for i, w in enumerate(self.weights):
      # calculate net inputs for a given layer
      # activations (array) by w (weights, matrix)
      
      net_inputs = np.dot(activations, w)
      
      # calculate the activations 
      
      activations = self._sigmoid(net_inputs)
      self.activations[i+1] = activations #this is a +1 because it's the activation of the layer plus 1
      
    return activations  
    
   
   def back_propagate(self, error):
      # back propagates an error signal
      
      # iterating *backwards* through the network layers, starting at last and decrimenting 
      for i in reversed(range(len(self.derivatives))):
        #getting activation from previous layer
        activations = self.activations[i+1]
        
        #applying the sigmoid derivative function
        delta = error * self._sigmoid_derivative(activations)
        
        #reshape delta so it is a 2d array
        delta_reshaped = delta.reshape(delta.shape[0], -1).T #transposed!
        
        #getting activations for the current layer
        current_activations = self.activations[i]
        
        #reshape activations to a 2d column matrix
        current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)
        
        #save after matrix multiplication
        self.derivatives[i] = np.dot(current_activations_reshaped, delta_reshaped)
        
        #back propagated the next error
        error = np.dot(delta, self.weights[i].T)
        
        if verbose:
          print("Derivatives for W{}: {}".format(i, self.derivatives[i]))
        
      return error     
      
   def train(self, inputs, targets, epochs, learning_rate):
    #inputs (nd array): X
    #targets (ndarray): Y
    #epochs (int): number of training iterations
    #learning_rate (float): 
      for i in range(epochs):
        sum_errors = 0
        for input, target in zip(inputs, targets):
          output = self.forward_propagate(input)
          error = target - output
          self.back_propagate(error) 
          self.gradient_descent(learning_rate) #this updates the weights
          sum_errors = sum_errors + self._mse(target, output) #MSE is used later
          
        #one Epoch Complete
        print("Error: {} at epoch {}".format(sum_errors / len(items), i+1))
    print("Training Complete!")
    print("======")
     
      
   def gradient_descent(self, learningRate = 1):
    for i in range(len(self.weights)):
      weights = self.weights[i]
      derivatives = self.derivatives[i]
      weights = weights + derivatives * learningRate # could do += ... but keeping this for readability
   
   def _mse(self, target, output):
      #target is the ground truth, ie what we're "training to" (nd array)
      #output is the predicted values (nd array)
      return np.average((target - output) **2) # **2 is the "square" of the result 
           
   def _sigmoid(self, x):
    return 1 / (1+ np.exp(-x))
   
   def _sigmoid_derivative(self, x):
    return x * (1.0 - x)
   
    
    
if __name__ == "__main__":

    # create a dataset to train a network for the sum operation
    items = np.array([[random()/2 for _ in range(2)] for _ in range(1000)])
    targets = np.array([[i[0] + i[1]] for i in items])

    # create a Multilayer Perceptron with one hidden layer
    mlp = MLP(2, [5], 1)

    # train network
    mlp.train(items, targets, 50, 0.1)

    # create dummy data
    input = np.array([0.3, 0.1])
    target = np.array([0.4])

    # get a prediction
    output = mlp.forward_propagate(input)

    print()
    print("Our network believes that {} + {} is equal to {}".format(input[0], input[1], output[0]))

    
