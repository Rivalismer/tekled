import math as m

def NNV(k_arr, g, n_e, r):
    nnv = -g
    for i in range(0, n_e):
        nnv += 1/pow(1+r, i+1) * k_arr[i]
    return nnv


def IRR(k_arr, g, n_e):
    tolerance = 0.001
    r = 0.5
    
    nnv = NNV(k_arr, g, n_e, r)
    
    while abs(nnv) > tolerance:
        
        if nnv > 0:
            r += r/2
    
        elif nnv < 0:
            r -= r/2
        nnv = NNV(k_arr, g, n_e, r)
    return r

def menu_run():
    run = 1
    menu_choice = 0
    nnv = 0
    g = 0
    n_e = 0
    r = 0
    temp_k = 0

    print("Welcome to the tekled automator\n")
    print("Please input a number corresponding to the task you would like to solve\n")

    while run:
        print("1 - Finite NNV\n 2 - Finite IR\n 3 - Quit")
        input(menu_choice)

        if menu_choice == 1:
            print("Please provide (in this order):\n Start capital invested\n How long the project will run for\n Rent\n An array of k-values\n")
            input(g, n_e, r)
            k_arr = []

            for i in range (0, n_e):
                input(temp_k)
                k_arr.append(temp_k)

            nnv = NNV(k_arr, g, n_e, r)
            print("Resulting NNV:\n", nnv)

        elif menu_choice == 2:
            print("Please provide (in this order):\n Start capital invested\n How long the project will run for\n An array of k-values\n")
            input(g, n_e)
            k_arr = []

            for i in range (0, n_e):
                input(temp_k)
                k_arr.append(temp_k)

            r = IRR(k_arr, g, n_e)
            print("Resulting IR:\n", r)
        
        elif menu_choice == 3:
            run = 0
            
        else:
            print("Illegal input")

    return


def main():
    menu_run()
    return 0