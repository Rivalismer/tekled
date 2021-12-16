#include "nnv.h"
#define tol 0.001

static float temp_nnv = 0;


float nnv_finite(float* k_arr, float g, int n_e, float r){
    float nnv = -g;
    for(int i = 0; i < n_e; i++){
        nnv += 1 / pow(1+r, 1+i) * k_arr[i];
    }

    return nnv;
}

float nnv_ir_finite(float* k_arr, float g, int n_e){
    float temp_r = 0.5;
    temp_nnv = nnv_finite(k_arr, g, n_e, temp_r);

    while(abs(temp_nnv) > tol){

        if(temp_nnv > 0)
        {
            temp_r += temp_r/2;
        }

        else
        {
            temp_r -= temp_r/2;
        }

        temp_nnv = nnv_finite(k_arr, g, n_e, temp_r);
    }
    return temp_r;
}