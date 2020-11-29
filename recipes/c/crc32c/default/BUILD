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
load("@com_curoky_tame//bazel:copts.bzl", "DEFAULT_CPP_COPTS")

cc_library(
    name = "crc32c",
    srcs = glob(
        [
            "src/*.cc",
            "src/*.h",
        ],
        exclude = [
            "src/*test.cc",
            "src/*benchmark.cc",
            "src/*test_main.cc",
        ],
    ),
    hdrs = glob(["include/crc32c/*.h"]),
    copts = DEFAULT_CPP_COPTS + ["-Isrc"],
    includes = ["include"],
    visibility = ["//visibility:public"],
    deps = ["@com_curoky_tame//recipes/c/crc32c/default/extra:config"],
)
