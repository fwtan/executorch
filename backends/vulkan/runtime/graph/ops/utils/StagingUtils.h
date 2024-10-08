/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */

#pragma once

#include <executorch/backends/vulkan/runtime/graph/ComputeGraph.h>

namespace vkcompute {

//
// Functions to copy data into and out of a staging buffer
//

void copy_ptr_to_staging(
    const void* src,
    api::StagingBuffer& staging,
    const size_t nbytes);
void copy_staging_to_ptr(
    api::StagingBuffer& staging,
    void* dst,
    const size_t nbytes);

void set_staging_zeros(api::StagingBuffer& staging, const size_t nbytes);

//
// Functions to get shaders
//

vkapi::ShaderInfo get_nchw_to_tensor_shader(
    const api::vTensor& v_dst,
    bool int8_buffer_enabled = true);
vkapi::ShaderInfo get_tensor_to_nchw_shader(
    const api::vTensor& v_src,
    bool int8_buffer_enabled = true);

} // namespace vkcompute
