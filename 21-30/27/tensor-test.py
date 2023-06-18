import torch
x = torch.rand(5, 3)
print(x)

# See: https://pytorch.org/get-started/locally/
print(f'CUDA is available: {torch.cuda.is_available()}')
