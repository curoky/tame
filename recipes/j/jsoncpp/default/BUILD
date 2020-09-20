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

# copy from https://github.com/tensorflow/tensorflow/blob/master/third_party/jsoncpp.BUILD
load("@rules_cc//cc:defs.bzl", "cc_library")
load("@com_curoky_tame//bazel:copts.bzl", "DEFAULT_CPP_COPTS")

cc_library(
    name = "jsoncpp",
    srcs = glob([
        "src/lib_json/*.h",
        "src/lib_json/*.cpp",
    ]),
    hdrs = glob(["include/json/*.h"]),
    copts = DEFAULT_CPP_COPTS + [
        "-DJSON_USE_EXCEPTION=0",
        "-DJSON_HAS_INT64",
    ],
    includes = ["include"],
    visibility = ["//visibility:public"],
    deps = [":private"],
)

cc_library(
    name = "private",
    textual_hdrs = ["src/lib_json/json_valueiterator.inl"],
)
