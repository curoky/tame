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

# genrule(
#     name = "version.h",
#     srcs = [
#         "cmake/cprver.h.in",
#         "CMakeLists.txt",
#     ],
#     outs = ["include/cpr/cprver.h"],
#     cmd = """
#         # version = 1.7.0
#         export cpr_VERSION=$$(grep "cpr VERSION " $(location CMakeLists.txt) | grep -Po "\\d+.\\d+.\\d+")
#         export cpr_VERSION_MAJOR=$${cpr_VERSION%%.*}
#         suffix=$${cpr_VERSION#*.}
#         export cpr_VERSION_MINOR=$${suffix%.*}
#         export cpr_VERSION_PATCH=$${cpr_VERSION##*.}
#         export cpr_VERSION_NUM=$$(printf "0x%02x%02x%02x" $${cpr_VERSION_MAJOR} $${cpr_VERSION_MINOR} $${cpr_VERSION_PATCH})
#         envsubst < $(location cmake/cprver.h.in) > $@
#     """,
# )

cc_library(
    name = "cppfs",
    srcs = glob(
        ["source/cppfs/source/**/*.cpp"],
        # exclude = [],
    ),
    hdrs = glob(["source/cppfs/include/**/*.h"]),  # + [":version.h"],
    copts = DEFAULT_CPP_COPTS,
    includes = ["source/cppfs/include"],
    visibility = ["//visibility:public"],
    # deps = ["@com_github_curl_curl//:curl"],
)
