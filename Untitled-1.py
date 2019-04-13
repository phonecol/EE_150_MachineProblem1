import cmath
import math

from utils import *

def main():
    file = open("Sol.txt", "w")
    # Z= complex(4.68,39.20707623)
    # Y = complex (0,0.0005488990684)
    length = 300
    resistance_R = 0.016
    inductance_L = 0.00097
    capacitance_C = 0.0000000115
    conductance_G = 0
    TL_model = 1
    pf = 0.8
    pf1 = 1
    S = 1000000000
    V = 500000
    Z, Y, Zc, gl,g,gphi,zphi,z,y  = TL_length(length, resistance_R,inductance_L,capacitance_C,conductance_G)
        
    # A, B, C, D,T_L_Model = two_port_parameter(Z,Y,TL_model)
    obj = TwoPortParameter()
    obj.calculate()

    obj



    V_s, I_s, I_r, V_r, Vsl, Isl, S_s_P, P_losses,n_eff, V_reg, pf_s =sending_end(A,B,C,D,S,V,pf,pf1)
    file.write("\nThe current, I_r, at the receiving end: %f  %f\n" %(abs(I_r),math.degrees(cmath.phase(I_r))))
    file.write("\nThe voltage, V_r, at the receiving end: %f  %f\n" %(abs(V_r),math.degrees(cmath.phase(V_r))))
    file.write("\nThe current, I_s, at the sending end: %f  %f\n" %(abs(I_s),math.degrees(cmath.phase(I_s))))
    file.write("\nThe voltage, V_r, at the sending end: %f  %f\n" %(abs(V_s),math.degrees(cmath.phase(V_s))))
    file.write("\nThe Complex power at the sending end: %f  %f\n" %(abs(S_s_P),math.degrees(cmath.phase(S_s_P))))
    file.write("\nThe Real power losses of the transmission line: %f  \n" %abs(P_losses))
if __name__ == '__main__':
    main()

class TwoPortParameter():
    A, B, C, D,T_L_Model = self.two_port_parameter( Z,Y,TL_model)

    def calculate(self, Z,Y,TL_model):
        pass
