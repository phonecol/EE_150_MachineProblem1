import cmath
import math

from utils import *

def main():
    Z= complex(2,7)
    Y = complex (0,0)
    TL_model = 1
    pf = 0.8
    pf1 = 1
    S = 70000000
    V = 64000
    A, B, C, D = two_port_parameter(Z,Y,TL_model)
    V_s, I_s, I_r, V_r, Vsl, Isl, S_s_P, P_losses,n_eff, V_reg, pf_s =sending_end(A,B,C,D,S,V,pf,pf1)
if __name__ == '__main__':
    main()
    