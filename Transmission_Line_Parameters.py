#Transmission_Line_Parameters_and_Performance

#askuser
import math , cmath
from utils import *

def main():
    print('Transmission Line Parameters and Performance Calculator')
    while True:
        is_default = input("Use defaults? ")
        if is_default:
            

            S = 2000
            V = 735
            pf = 0.8
            pf1 = 1
            length = 400
            acsr = 'Bobolink'
            TL_model = 1
            ckt = 1
            b = 4
            GMD,D1 =gmd(ckt)
            bundleD = 0.45
            Ds_1, d_1, opmi, = acsr_list(acsr)
            Ds = Ds_1 *0.3048
            r = d_1*0.0254/(2)
            opm = opmi * (1/1.60934)
            #gmr_L = Ds
            #gmr_C = r
            print ('Ds', Ds)
            print ('r', r)
            print (opm)
            gmr_L, gmr_C =gmr_bundle(Ds,r,bundleD,b,ckt)
            inductance_L, capacitance_C, resistance_R = line_parameters(gmr_L,gmr_C,GMD,opm,b)
            conductance_G = 0
            Z, Y, Zc, gl,g,gphi,zphi,z,y  = TL_length(b,length, resistance_R,inductance_L,capacitance_C,conductance_G)
            A, B, C, D, T_L_Model = two_port_parameter(Z,Y,TL_model)
            V_s, I_s, I_r, V_r, Vsl, Isl, S_s_P, P_losses,n_eff, V_reg, pf_s =sending_end(A,B,C,D,S,V,pf,pf1)
            
        else:
            
            acsr = str(input("What is the name of the conductor used in the transmission line: "))
            length = float(input("What is the length of the Transmission Line: "))
            TL_model = int(input("Is it nominal pi network (type: 1 ), or nominal T network (type: 2 ): "))
            ckt = int(input("Is it single circuit (type: 1 ) or double circuit (type: 2): "))                    
            b = int(input("Number of bundles per phase: "))
            GMD,D1 = gmd(ckt)
            Ds_1, d_1, opmi, = acsr_list(acsr)
            Ds = Ds_1 *0.3048
            r = d_1*0.0254/(2)
            opm = opmi * (1/1.60934)*0
            print ('Ds', Ds)
            print ('r', r)
            print (opm)

            gmr_L, gmr_C = bundling(b,Ds,r,ckt)
            

            inductance_L, capacitance_C, resistance_R = line_parameters(gmr_L,gmr_C,GMD,opm,b)
            conductance_G = 0
            Z, Y, Zc, gl,g,gphi,zphi,z,y = TL_length(b,length, resistance_R,inductance_L,capacitance_C,conductance_G)
            A, B, C, D, T_L_Model = two_port_parameter(Z,Y,TL_model)
            S = float(input("What is the rated power of the transmission line's recieving end: "))
            V = float(input("What is the rated voltage of the transmission line's recieving end: "))
            pf= float(input("What is the power factor of the load at the recieving end: "))
            pf1 = int(input("Type: '1' if lagging, Type: '2' if leading, and Type: '3' if unity: "))
            
            V_s, I_s, I_r,V_r, Vsl, Isl,S_s_P, P_losses,n_eff, V_reg, pf_s =sending_end(A,B,C,D,S,V,pf,pf1)

        write_to_file(S,V,pf,pf1,length,acsr,
                    D1,b,gmr_L, gmr_C,Ds, r,
                    opm,inductance_L, capacitance_C,
                    resistance_R, conductance_G,Z, Y,
                    Zc, gl, g,gphi,zphi,z,y,A, B, C,
                    D, T_L_Model,V_s, I_s, I_r, V_r,
                    Vsl, Isl, S_s_P, P_losses,
                    n_eff, V_reg, pf_s)

        print('Press Ctrl+C to exit the application')
        
    


if __name__ == '__main__':
    main()
    


