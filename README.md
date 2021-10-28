# Pytorch-Hausdorff-Distance

This is pytorch implementation of Hausdorff Distance for 2D image binary segmentation.

## How to use
'''
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
'''
