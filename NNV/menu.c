#include "menu.h"
#include "nnv.h"

void menu_run(){
    int menu_choice = 0;
    float nnv = 0;
    float g = 0;
    int n_e = 0;
    float r = 0;
    float k_arr[MAX_LENGTH_K];

    printf("Welcome to the tekled automator\n");
    printf("Please input a number corresponding to the task you would like to solve\n");

    while(1){
        printf("1 - Finite NNV\n 2 - Finite IR\n");
        scanf("%d", &menu_choice);

        switch (menu_choice)
        {
        case FINITE_NNV:
        {
            printf("Please provide (in this order):\n Start capital invested\n How long the project will run for\n Rent\n An array of k-values\n");
            scanf("%f%d%f", &g, &n_e, &r);

            for(int i = 0; i < n_e; i++){
                scanf("%f", &k_arr[i]);
            }

            nnv = nnv_finite(k_arr, g, n_e, r);
            printf("Resulting NNV:\n %f", nnv);
            break;
        }

        case FINITE_IR:
        {
            printf("Please provide (in this order):\n Start capital invested\n How long the project will run for\n An array of k-values\n");
            scanf("%f%d", &g, &n_e);

            for(int i = 0; i < n_e; i++){
                scanf("%f", &k_arr[i]);
            }

            r = nnv_ir_finite(k_arr, g, n_e);
            printf("Resulting IR:\n%f", r);
            break;
        }

        default:
            break;
        }
    }
}