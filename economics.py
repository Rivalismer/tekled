def NNV(k_arr, g, n_e, r, s):
    nnv = -g
    for i in range(0, n_e):
        nnv += 1/pow(1+r, i+1) * k_arr[i]
    return nnv + 1/pow(1+r, n_e) * s


def IRR(k_arr, g, n_e, s):
    tolerance = 0.001
    r = 0.5
    
    nnv = NNV(k_arr, g, n_e, r, s)
    
    while abs(nnv) > tolerance:
        
        if nnv > 0:
            r += r/2
    
        elif nnv < 0:
            r -= r/2
            
        nnv = NNV(k_arr, g, n_e, r, s)
    return r

def ANNU(k_arr, g, n_e, r, s):
    nnv = NNV(k_arr, g, n_e, r, s)
    return nnv * r / (1 - pow((1 + r), -n_e))

def NNV_QUOTA(k_arr, g, n_e, r, s):
    nnv = NNV(k_arr, g, n_e, r, s)
    return nnv/g

def menu_run():
    run = 1
    nnv = 0
    g = 0
    n_e = 0
    r = 0
    s = 0
    temp_k = 0
    menu_choice = 0

    print("Welcome to the tekled automator\n")
    print("Please input a number corresponding to the task you would like to solve")

    while run:
        print("1 - Finite NNV\n2 - Finite IR\n3 - Annuitet\n4 - NNV Quota\n5 - Quit")
        menu_choice = int(input())

        if menu_choice == 1:
            print("Please provide (in this order):\nStart capital invested\nRent\nHow long the project will run for\nS-value\nAn array of k-values")
            g = float(input())
            r = float(input())
            n_e = int(input())
            s = int(input())
            k_arr = []

            for i in range (0, n_e):
                temp_k = float(input())
                k_arr.append(temp_k)

            nnv = NNV(k_arr, g, n_e, r, s)
            print("Resulting NNV:\n", nnv)

        elif menu_choice == 2:  
            print("Please provide (in this order):\nStart capital invested\nHow long the project will run for\nS-value\nAn array of k-values")
            g = float(input())
            n_e = int(input())
            s = int(input())
            k_arr = []

            for i in range (0, n_e):
                temp_k = float(input())
                k_arr.append(temp_k)
            nnv = NNV(k_arr, g, n_e, r, s)

            r = IRR(k_arr, g, n_e, s)
            print("Resulting IR:\n", r)
        
        elif menu_choice == 3:
            cont = 0
            if nnv != 0:
                cont = input("Do you want to continue using the same NNV (y/n)?")
            if cont != 'y':
                print("Please provide (in this order):\nStart capital invested\nRent\nHow long the project will run for\nS-value\nAn array of k-values")
                g = float(input())
                r = float(input())
                n_e = int(input())
                s = int(input())
                k_arr = []

                for i in range (0, n_e):
                    temp_k = float(input())
                    k_arr.append(temp_k)

                nnv = NNV(k_arr, g, n_e, r, s)

            annu = ANNU(k_arr, g, n_e, r, s)
            print("Resulting annuitet:\n", annu)
            
        elif menu_choice == 4:
            cont = 0
            if nnv != 0:
                cont = input("Do you want to continue using the same NNV (y/n)?")
            if cont != 'y':
                print("Please provide (in this order):\nStart capital invested\nRent\nHow long the project will run for\nS-value\nAn array of k-values")
                g = float(input())
                r = float(input())
                n_e = int(input())
                s = int(input())
                k_arr = []

                for i in range (0, n_e):
                    temp_k = float(input())
                    k_arr.append(temp_k)
                        
            nnv_quota = NNV_QUOTA(k_arr, g, n_e, r, s)
            print("Resulting quota:\n", nnv_quota)
            
        elif menu_choice == 5:
            run = 0
            
        else:
            print("Illegal input")
            print(menu_choice)

    return


def main():
    menu_run()
    return 0

main()