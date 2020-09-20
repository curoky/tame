# Copyright 2021 curoky(cccuroky@gmail.com).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

load("@rules_cc//cc:defs.bzl", "cc_library")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "llvm",
    srcs = glob([
        "lib/*.so",
    ]),
    hdrs = glob(["include/**"]),
    includes = ["include"],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "clang",
    srcs = [
        "lib/libLLVM.so",
        "lib/libclang.so",
        "lib/libclang-cpp.so",
    ],
    hdrs = glob(["include/**"]),
    includes = ["include"],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "clangTooling",
    srcs = ["lib/libclangTooling.a"],
    hdrs = glob(["include/**"]),
    includes = ["include"],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "clangBasic",
    srcs = ["lib/libclangBasic.a"],
    hdrs = glob(["include/**"]),
    includes = ["include"],
    visibility = ["//visibility:public"],
)

cc_library(
    name = "clangASTMatchers",
    srcs = [
        "lib/libclangAST.a",
        "lib/libclangASTMatchers.a",
    ],
    hdrs = glob(["include/**"]),
    includes = ["include"],
    visibility = ["//visibility:public"],
)
