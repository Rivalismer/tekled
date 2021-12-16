#ifndef __NNV_H__
#define __NNV_H__

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <math.h>

float nnv_finite(float* k_arr, float g, int n_e, float r);

float nnv_ir_finite(float* k_arr, float g, int n_e);

#endif