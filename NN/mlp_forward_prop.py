# Joe Sanford
# this class implements a forward propagated MLP
#

import numpy as np

class MLP:
  
  # number of inputs to NN, number of hidden layers, number of outputs
  # pre-setting attributes/ default values. these can be changed.
  # the hidden layer must be a list, this one has 2 hidden layers
  # 3 neurons in the first hidden layer
  # 5 neurons in the second layer
  def __init__(self, num_inputs=3, num_hidden=[3, 5], num_outputs=2):
    
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
         
  def forward_propagate(self, inputs):
    
    activations = inputs
    
    for w in self.weights:
      # calculate net inputs for a given layer
      # activations (array) by w (weights, matrix)
      
      net_inputs = np.dot(activations, w)
      
      # calculate the activations 
      
      activations = self._sigmoid(net_inputs)
      
    return activations  
    
   def _sigmoid(self, x):
    return 1 / (1+ np.exp(-x))
   
   
if __name__ == "__main__":
  
  # create an MLP
  
  mlp = MLP() #without passing in new parameters ... defaults to as above
  
  # create inputs
  # same as number of inputs in first layer of NN
  
  inputs = np.random.rand(mlp.num_inputs)
  
  # perform the forward propagation
  
  outputs = mlp.forward_propagate(inputs)
  
  # print results
  print("the network inputs are: {}".format(inputs))
  print("the network outputs are: {}".format(outputs))  
