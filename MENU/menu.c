#include "menu.h"
#include "../NNV/nnv.h"

void menu_run(){
    int menu_choice = 0;

    printf("Welcome to the tekled automator\n");
    printf("Please input a number corresponding to the task you would like to solve\n");

    while(1){
        printf("1 - Finite NNV\n 2 - Finite IR\n");
        scanf("%d", &menu_choice);

        switch (menu_choice)
        {
        case FINITE_NNV:
        {
            float nnv;
            float* k_arr;
            float g;
            uint8_t n_e;

            printf("Please provide (in this order):\n An array of k-values\n Start capital invested\n How long the project will run for\n");
            scanf("%f%")
            break;
        }

        case FINITE_IR:
        {
            break;
        }

        default:
            break;
        }
    }
}