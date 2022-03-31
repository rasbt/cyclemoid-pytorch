# Sebastian Raschka 2022
# cyclemoid_pytorch
# Author: Sebastian Raschka <mail@sebastianraschka.com>
#
# License: MIT

import torch


def cyclemoid(x):
    term1 = torch.tanh(torch.pi*x)
    term2 = torch.tanh(torch.pi*torch.square(x)-0.95)**2
    term3 = torch.cos(torch.clamp(x, min=-3., max=3.))**2 
    return term1 * term2 * term3


class CycleMoid(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return cyclemoid(x)