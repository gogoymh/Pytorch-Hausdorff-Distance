# Pytorch-Hausdorff-Distance
This is pytorch implementation of Hausdorff Distance for 2D image binary segmentation. \
The implementation is made for batch-wise inference.

## Notice: Input and Target dimension
Both dimensions should be like (Batch, Width, Height) or (Batch, Height, Width). \
Notice that there is no Channel dimesion. \
Input and Target should be same dimension.

## Output Dimension
Output Dimension is (Batch). \
You can use it by sum or mean after get result.

## How to use
```
from hausdorff_distance import torch2D_Hausdorff_distance

u = torch.Tensor([[[1.0, 0.0],
                   [0.0, 1.0],
                   [-1.0, 0.0],
                   [0.0, -1.0]]])
v = torch.Tensor([[[2.0, 0.0],
                   [0.0, 2.0],
                   [-2.0, 0.0],
                   [0.0, -4.0]]])
                   
HD = torch2D_Hausdorff_distance(u,v)
print(HD)
```
