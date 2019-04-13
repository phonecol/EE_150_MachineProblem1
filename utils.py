import math,cmath

def acsr_list(acsr):
    print( "\n\ngetting acsr values...\n\n")
    this_list = [
        {'name': 'Waxwing', 'val': {'Ds': 0.0198, 'd': 0.609, 'opm': 0.3488}}, 
        {'name': 'Partridge', 'val':{'Ds': 0.0217, 'd': 0.640, 'opm': 0.3452}}, 
        {'name': 'Ostrich', 'val':{'Ds': 0.0229, 'd': 0.680, 'opm': 0.3070}}, 
        {'name': 'Merlin', 'val':{'Ds': 0.0211, 'd': 0.684, 'opm': 0.2767}}, 
        {'name': 'Linnet', 'val':{'Ds': 0.0243, 'd': 0.721, 'opm': 0.2737}}, 
        {'name': 'Oriole', 'val':{'Ds': 0.0255, 'd': 0.741, 'opm': 0.2719}}, 
        {'name': 'Chickadee', 'val':{'Ds': 0.0241, 'd': 0.743, 'opm': 0.2342}}, 
        {'name': 'Ibis', 'val':{'Ds': 0.0264, 'd': 0.783 , 'opm': 0.2323}}, 
        {'name': 'Pelican', 'val':{'Ds': 0.0264, 'd': 0.814, 'opm': 0.1957}}, 
        {'name': 'Flicker', 'val':{'Ds': 0.0284, 'd': 0.846, 'opm': 0.1943}}, 
        {'name': 'Hawk', 'val':{'Ds': 0.0289, 'd': 0.858, 'opm': 0.1931}}, 
        {'name': 'Hen', 'val':{'Ds': 0.0304, 'd': 0.883, 'opm': 0.1919}}, 
        {'name': 'Osprey', 'val':{'Ds': 0.0284, 'd': 0.879, 'opm': 0.1679}}, 
        {'name': 'Parakeet', 'val':{'Ds': 0.0306, 'd': 0.914, 'opm': 0.1669}}, 
        {'name': 'Dove', 'val':{'Ds': 0.0314, 'd': 0.927, 'opm': 0.1663}}, 
        {'name': 'Rook', 'val':{'Ds': 0.0327, 'd': 0.977, 'opm': 0.1461}}, 
        {'name': 'Grosbeak', 'val':{'Ds': 0.0335, 'd': 0.990, 'opm': 0.1454}}, 
        {'name': 'Drake', 'val':{'Ds': 0.0373, 'd': 1.108, 'opm': 0.1172}}, 
        {'name': 'Tern', 'val':{'Ds': 0.0352, 'd': 1.063, 'opm': 0.1188}}, 
        {'name': 'Rail', 'val':{'Ds': 0.0386, 'd': 1.165, 'opm': 0.0997}}, 
        {'name': 'Cardinal', 'val':{'Ds': 0.0402, 'd': 1.196, 'opm': 0.0998}}, 
        {'name': 'Ortolan', 'val':{'Ds': 0.0402, 'd': 1.213, 'opm': 0.0921}}, 
        {'name': 'Bluejay', 'val':{'Ds': 0.0415, 'd': 1.259, 'opm': 0.0861}}, 
        {'name': 'Finch', 'val':{'Ds': 0.0436, 'd': 1.293, 'opm': 0.0856}}, 
        {'name': 'Bittern', 'val':{'Ds': 0.0444, 'd': 1.345, 'opm': 0.0762}}, 
        {'name': 'Pheasant', 'val':{'Ds': 0.0466, 'd': 1.382, 'opm': 0.0751}}, 
        {'name': 'Bobolink', 'val':{'Ds': 0.0470, 'd': 1.427, 'opm': 0.0684}},  
        {'name': 'Plover', 'val':{'Ds': 0.0494, 'd': 1.465, 'opm': 0.0673}}, 
        {'name': 'Lapwing', 'val':{'Ds': 0.0498, 'd': 1.502, 'opm': 0.0623}}, 
        {'name': 'Falcon', 'val':{'Ds': 0.0523, 'd': 1.545, 'opm': 0.0612,}}, 
        {'name': 'Bluebird', 'val':{'Ds': 0.0586, 'd': 1.762, 'opm': 0.0476}}
    ]

    for item in this_list:
        if item['name'] == acsr:
            print("acsr_val =", str(item['val']))
            print("The ACSR used: ", acsr)
            return item['val']['Ds'], item['val']['d'], item['val']['opm']
    #print("acsr_val[default] =", '0.0198, 0.0609, 0.3488')
    print("acsr_val =", str(item['val']))
    print("The ACSR used: ", acsr)
    #return 0.0470, 1.427, 0.0684
    return item['val']['Ds'], item['val']['d'], item['val']['opm']

def gmd(ckt):
    if ckt == 1:
        D1=list(map(int,input('Distances between lines: ').split()))
        GMD = math.pow((D1[0]*D1[1]*D1[2]), 1/3)
       
    elif ckt == 2:
        
        D1 =list(map(int,input("Distance between lines [Daa',Dbb',Dcc']: ").split()))
        Dab = list(map(int,input("Distance between lines [Dab, Dab', Da'b, Da'b']: ").split()))
        Da = math.pow((Dab[0]*Dab[1]*Dab[2]*Dab[3]), 1/4)
        Dbc = list(map(int,input("Distance between lines [Dbc, Dbc', Db'c, Db'c']: ").split()))
        Db = math.pow((Dbc[0]*Dbc[1]*Dbc[2]*Dbc[3]), 1/4)
        Dca =input("Distance between lines [Dca, Dca', Dc'a, Dc'a']: ")
        Dca =list(map(int,input("Distance between lines [Dca, Dca', Dc'a, Dc'a']: ").split()))
        Dc = math.pow((Dca[0]*Dca[1]*Dca[2]*Dca[3]), 1/4)
        GMD = math.pow((Da*Db*Dc), 1/3)
    print('GMD: ', GMD)
    return GMD, D1

def bundling(b,Ds,r,ckt):
    if b == 1:
        print( 'b=1')
        gmr_L = Ds
        gmr_C = r

    else:
        print ('b= ', b) 
        bundleD = float(input('Distance of each bundled conductor: '))
        gmr_L, gmr_C = gmr_bundle(Ds,r,bundleD,b,ckt)
    return gmr_L,gmr_C



def gmr_bundle(Ds,r,bundleD,b,ckt):
    if ckt == 1:
        print ("\n\ncalculating gmr_bundle...\n\n")
        k = bundleD/(2*math.sin(3.1416/b))
        print ('k', k)
        print ('b' ,b)
        rbs = math.pow((r*b*(k)**(b-1)),(1.0/b))  
        Dbs = math.pow((Ds*b*(k)**(b-1)),(1.0/b))
        gmr_L = Dbs
        gmr_C = rbs    
        print ("gmr_L =", gmr_L)
        print ("gmr_C =", gmr_C)
        
    elif ckt == 2:
        print ("\n\ncalculating gmr_bundle...\n\n")
        k = bundleD/(2*math.sin(3.1416/b))
        print ('k', k)
        print ('b' ,b)
        rbs = math.pow((r*b*(k)**(b-1)),(1.0/b))  
        Dbs = math.pow((Ds*b*(k)**(b-1)),(1.0/b))
        Dsa = math.sqrt(Dbs*DD[1])
        Dsb = math.sqrt(Dbs*DD[2])
        Dsc = math.sqrt(Dbs*DD[3])
        rsa = math.sqrt(rbs*DD[1])
        rsb = math.sqrt(rbs*DD[2])
        rsc = math.sqrt(rbs*DD[3])
        gmr_L = math.pow((Dsa*Dsb*Dsc),(1.0/3)) 
        gmr_C = math.pow((rsa*rsb*rsc),(1.0/3))
    return gmr_L, gmr_C

def line_parameters(gmr_L,gmr_C,GMD,opm,b):
   
    inductance_L = (0.2*math.log(GMD/gmr_L))/1000
    capacitance_C = (0.0556/(math.log(GMD/gmr_C)))/1000000  
    resistance_R = opm
    conductance_G = 0
    print ('L =',inductance_L) 
    print ('C =',capacitance_C)
    print ('R =',resistance_R)
    return inductance_L, capacitance_C, resistance_R

def TL_length(b,length, resistance_R,inductance_L,capacitance_C,conductance_G):
    f = 60
    if length < 80:
        print('The transmission line is a short line')
        print('Shunt effects are neglected')
        z =  complex(resistance_R/b , (2*math.pi*f*inductance_L))
        y =  0
        print ('z =',z)
        print ('y =',y)
        Z = length*complex(resistance_R/b , (2*math.pi*f*inductance_L))
        Y = 0
        Zc = 0
        g = 0
        gl = 0
        gphi = 0
        zphi = 0
    

    elif 80<length and length<240:
        print('The transmission line is a medium line')
        z =  complex(resistance_R/b , (2*math.pi*f*inductance_L))
        y =  complex(0 , (2*math.pi*f*capacitance_C))
        Z = length*complex(resistance_R/b , (2*math.pi*f*inductance_L))
        Y = length*complex(0 , (2*math.pi*f*capacitance_C))
        print ('z =',z)
        print ('y =',y)
        Zc = 0
        g = 0
        gl = 0
        gphi = 0
        zphi = 0

    else: 
        print('The transmission line is a long line')
        z =  complex(resistance_R/b , (2*math.pi*f*inductance_L))
        y =  complex(0 , (2*math.pi*f*capacitance_C))
        print ('z =',z)
        print ('y =',y)
        gphi = (cmath.phase(z)+(cmath.phase(y)))/2
        print ('gphi = ',gphi)
    
        zphi = (cmath.phase(z)-(cmath.phase(y)))/2
        print ('zphi =',zphi)
        g = cmath.rect(math.sqrt(abs(z)*abs(y)),gphi)
        gl = g*length
        print ('gl =',gl)
        print('g= ',g)
        Zc = cmath.rect(math.sqrt(abs(z)/abs(y)),zphi)
       
        print ('Zc =',Zc)
        Z = Zc * cmath.sinh(gl)
        print('Z =', Z)
        Y1 = (1/Zc) * cmath.tanh(gl/2)
        print ('Y1', Y1)
        Y = 2*Y1
    return Z, Y, Zc, gl, g,gphi,zphi,z,y

def two_port_parameter(Z,Y,TL_model):
    if TL_model == 1:
        T_L_Model = 'Nominal Pi'
        A =1+ Z*Y/2
        B =Z
        C =Y*((Z*Y/4)+1)
        D =A
        #A = cmath.cosh(gl)
        #B = Zc * cmath.sinh(gl)
        #C = 1/Zc * cmath.sinh(gl)
        #D = A

    elif TL_model ==2:
        T_L_Model = 'Nominal T'
        A = 1+ Z*Y/2
        B = Z*(1+ (Z*Y/4))
        C = Y
        D = A
        #A = cmath.cosh(gl)
        #B = Zc * cmath.sinh(gl)
        #C = 1/Zc * cmath.sinh(gl)
        #D = A

    print ('A', A)
    print ('B', B)
    print ('C', C)
    print ('D', D)
    print ('Transmission Line Model: ', T_L_Model)
    adbc = A*D-B*C
    print ('ad-bc',adbc)
    return A, B, C, D,T_L_Model

def sending_end(A,B,C,D,S,V,pf,pf1):
    if pf1 ==1:
        phi = math.acos(pf)     #phase angle
        theta= math.degrees(phi)
    elif pf1 ==2:
        phi = -math.acos(pf)
        theta = math.degrees(phi)
    else:
        phi = 0
        theta =0
    #return phi, theta
    Vr = V/math.sqrt(3)    #ref voltage(phase load voltage)
    V_r = complex(Vr,0)
    Ir = S*1000/(3*Vr)          #magnitude line/phase current
    S_r = S *(math.cos(phi) + math.sin(phi)*1j)
    I_r = Ir*(math.cos(-phi) + math.sin(-phi)*1j) #line current with phase angle
    V_s = A*V_r + B*I_r/1000
    I_s = C*V_r*1000 + D*I_r
    thirty_rad = math.pi/6
    thirty_deg = math.degrees(thirty_rad)
    Vsl= V_s*cmath.rect(math.sqrt(3),thirty_rad) 
    Isl= I_s
    S_s_P = 3*V_s*(I_s.conjugate())/1000  
    P_losses = S_s_P.real - S_r.real
    n_eff = (100*S_r.real/S_s_P.real)
    V_reg = 100*(abs(V_s/A)-Vr)/Vr
    pf_s = math.cos(cmath.phase(S_s_P))
    print ('phi: ',phi)
    print ('S_r: %f <%f MVA' %(abs(S_r),math.degrees(cmath.phase(S_r))))
    print ('V_r: %f <%f kV'  %(abs(V_r),math.degrees(cmath.phase(V_r))))
    print ('I_r: %f <%f A'   %(abs(I_r),math.degrees(cmath.phase(I_r))))
    print ('P_r: %f MW' %S_r.real )
    print ('P_losses: %f MW' %P_losses )
    print ('Sending-end Line-to-Line Voltage magnitude: %f kV' %abs(Vsl))
    print ('V_s: %f <%f kV' %(abs(V_s),math.degrees(cmath.phase(V_s))))
    print ('I_s: %f <%f A' %(abs(I_s),math.degrees(cmath.phase(I_s))))
    print ('S_s_P: %f <%f MVA' %(abs(S_s_P),math.degrees(cmath.phase(S_s_P))))
    print ('Sending end power factor: ', pf_s )
    print ('Effeciency: ', n_eff)
    print ('Voltage Regulation: ', V_reg)

    return V_s, I_s, I_r, V_r, Vsl, Isl, S_s_P, P_losses, n_eff, V_reg, pf_s


def write_to_file(S,V,pf,pf1,length,acsr,
                  D1,b,gmr_L, gmr_C,Ds, r,
                  opm,inductance_L, capacitance_C,
                  resistance_R, conductance_G,Z, Y,
                  Zc, gl, g,gphi,zphi,z,y,A, B, C,
                  D, T_L_Model,V_s, I_s, I_r, V_r,
                  Vsl, Isl, S_s_P, P_losses, n_eff, V_reg, pf_s):
    file = open("Solutions.txt", "w")
    file.write("\nRated power at the receiving end: %f VA\n" %S)
    file.write("\nRated voltage at the receiving end: %f V\n" %V)
    file.write("\nPower factor at the receiving end: %f\n" %pf)
    file.write("\nLagging if 1, Leading if 2, Unity if 3 at the receiving end: %d\n" %pf1)
    file.write("\nLength of the transmission line: %d km\n" %length)
    file.write("\nACSR used in the transmission line is: %s \n" %acsr)
    file.write("\nTransmission line model: %s\n" %T_L_Model)
    file.write("\nTransmission line is single: \n")
    file.write("\nThe distance between phases A and B of the transmission line: %d m\n" %D1[0])
    file.write("\nThe distance between phases B and C of the transmission line: %d m\n" %D1[1])
    file.write("\nThe distance between phases C and A of the transmission line: %d m\n" %D1[2])
    file.write("\nNumber of bundles of each phase in the transmission line: %d\n" %b)
    file.write("\nThe GMRL of the conductor: %f m\n" %gmr_L)
    file.write("\nThe GMRC of the conductor: %f m\n" %gmr_C)
    file.write("\nThe inductance per km per phase of the transmission line: %f H/km\n" %inductance_L)
    file.write("\nThe capacitance per km per phase of the transmission line: %0.12f F/km\n" %capacitance_C)
    file.write("\nThe resistance per km per phase of the transmission line: %f Ohms/km\n" %resistance_R)
    file.write("\nThe conductance per km per phase of the transmission line: %f S/km\n" %conductance_G)
    file.write("\nThe impedance per km per phase of the transmission line: %f %fi  Ohm/km\n" %(z.real,z.imag))
    file.write("\nThe admittance per km per phase of the transmission line: %0.12f %0.12fi  S/km\n" %(y.real,y.imag))
    file.write("\nThe total impedance per phase of the transmission line: %f %fi Ohm\n" %(Z.real,Z.imag))
    file.write("\nThe total admittance per phase of the transmission line: %f %fi S\n" %(Y.real,Y.imag))
    file.write("\nThe characteristic impedance of the transmission line: %f %fi Ohm\n" %(Zc.real, Zc.imag))
    file.write("\nThe propagation constant of the transmission line: %f angle  %f\n" %(abs(g),cmath.phase(g)))
    file.write("\nThe propagation constant multiplied by the length of the transmission line: %f angle %f\n" %(abs(gl),cmath.phase(gl)))
    file.write("\nThe Parameter A: %f" %abs(A))
    file.write("     Angle: %f degrees\n" %math.degrees(cmath.phase(A)))
    file.write("\nThe Parameter B: %f" %abs(B))
    file.write("   Angle: %f degrees\n" %math.degrees(cmath.phase(B)))
    file.write("\nThe Parameter C: %f" %abs(C))
    file.write("     Angle: %f degrees\n" %math.degrees(cmath.phase(C)))
    file.write("\nThe Parameter D: %f" %abs(D))
    file.write("     Angle: %f degrees\n" %math.degrees(cmath.phase(D)))
    file.write("\nThe current, I_r, at the receiving end: %f < %f  A\n" %(abs(I_r),math.degrees(cmath.phase(I_r))))
    file.write("\nThe voltage, V_r, at the receiving end: %f < %f  V\n" %(abs(V_r),math.degrees(cmath.phase(V_r))))
    file.write("\nThe current, I_s, at the sending end: %f < %f  A\n" %(abs(I_s),math.degrees(cmath.phase(I_s))))
    file.write("\nThe voltage, V_r, at the sending end: %f < %f  V\n" %(abs(V_s),math.degrees(cmath.phase(V_s))))
    file.write("\nThe Complex power at the sending end: %f < %f  VA\n" %(abs(S_s_P),math.degrees(cmath.phase(S_s_P))))
    file.write("\nSending-end Line-to-Line Voltage magnitude: %f kV" %abs(Vsl))
    file.write("\nThe Real power losses of the transmission line: %f  W\n" %abs(P_losses))
    file.write("\nThe Effeciency of the transmission line: %f  percent\n" %n_eff)
    file.write("\nThe Power Factor at the sending end: %f  \n" %pf_s)
    file.write("\nThe Voltage Regulation of the transmission line: %f  percent\n" %V_reg)
    file.close()