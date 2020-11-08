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
load("@com_curoky_tame//bazel:copts.bzl", "DEFAULT_C_COPTS")

# genrule(
#     name = "config_h",
#     srcs = [
#         "configure",
#     ] + glob(["**/*.in"]),
#     outs = ["src/include/liburing/compat.h"],
#     cmd = "./$(location configure) " +
#           "&& cp config.h $(location config.h)",
# )

cc_library(
    name = "liburing",
    srcs = glob(
        ["src/*.c"],
        exclude = ["src/nolibc.c"],
    ),
    hdrs = glob(["src/**/*.h"]),
    copts = DEFAULT_C_COPTS,
    includes = ["src/include"],
    linkstatic = 1,
    visibility = ["//visibility:public"],
    deps = ["@com_curoky_tame//recipes/l/liburing/default/extra:compat"],
)
