import torch

# Scalar
scalar = torch.tensor(7)
# print(scalar)

scalar.ndim

# Vector
vector = torch.tensor([7, 7])
# print(vector)
# print(vector.ndim)

# Check shape of vector
# print(vector.shape)

# Matrix
MATRIX = torch.tensor([[7, 8], 
                       [9, 10]])
# print(MATRIX)
# print(MATRIX.ndim)

# Tensor
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
#print(TENSOR)
#print(TENSOR.ndim)
#print(TENSOR.shape)

# Create a random tensor of size (224, 224, 3)
random_image_size_tensor = torch.rand(size=(224, 224, 3))
print(random_image_size_tensor.shape)
print(random_image_size_tensor.ndim)

float_16_tensor = torch.tensor([3.0, 6.0, 9.0],dtype=torch.float16) # torch.half would also work

float_16_tensor.dtype