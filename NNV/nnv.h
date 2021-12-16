#ifndef __NNV_H__
#define __NNV_H__

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

float nnv_finite(float* k_arr, float g, uint8_t n_e, float r);

float nnv_ir_finite(float* k_arr, float g, uint8_t n_e);

#endif