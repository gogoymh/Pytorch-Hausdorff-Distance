import torch

def torch2D_Hausdorff_distance(x,y): # Input be like (Batch,width,height)
    x = x.float()
    y = y.float()
    distance_matrix = torch.cdist(x,y,p=2) # p=2 means Euclidean Distance
    
    value1 = distance_matrix.min(2)[0].max(1, keepdim=True)[0]
    value2 = distance_matrix.min(1)[0].max(1, keepdim=True)[0]
    
    value = torch.cat((value1, value2), dim=1)
    
    return value.max(1)[0]

if __name__ == "__main__":
    u = torch.Tensor([[[1.0, 0.0],
                       [0.0, 1.0],
                       [-1.0, 0.0],
                       [0.0, -1.0]],
                      [[1.0, 0.0],
                       [0.0, 1.0],
                       [-1.0, 0.0],
                       [0.0, -1.0]],
                      [[2.0, 0.0],
                       [0.0, 2.0],
                       [-2.0, 0.0],
                       [0.0, -4.0]]])

    v = torch.Tensor([[[0.0, 0.0],
                       [0.0, 2.0],
                       [-2.0, 0.0],
                       [0.0, -3.0]],
                      [[2.0, 0.0],
                       [0.0, 2.0],
                       [-2.0, 0.0],
                       [0.0, -4.0]],
                      [[1.0, 0.0],
                       [0.0, 1.0],
                       [-1.0, 0.0],
                       [0.0, -1.0]]])
    
    print("Input shape is (B,W,H):", u.shape, v.shape)
    HD = torch2D_Hausdorff_distance(u,v)
    print("Hausdorff Distance is:", HD)
    
