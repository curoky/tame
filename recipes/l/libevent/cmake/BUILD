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

# https://github.com/oneapi-src/oneTBB/blob/master/cmake/README.md

load("@rules_foreign_cc//foreign_cc:cmake.bzl", "cmake")

filegroup(
    name = "srcs",
    srcs = glob(["**"]),
    visibility = ["//visibility:public"],
)

cmake(
    name = "libevent",
    generate_args = [
        "-GNinja",
        "-DEVENT__DISABLE_MBEDTLS=ON",
        "-DEVENT__DISABLE_BENCHMARK=ON",
        "-DEVENT__DISABLE_TESTS=ON",
        "-DEVENT__DISABLE_REGRESS=ON",
        "-DEVENT__DISABLE_SAMPLES=ON",
        "-DEVENT__LIBRARY_TYPE=STATIC",
    ],
    lib_source = ":srcs",
    # out_shared_libs = ["libevent.so"],
    out_static_libs = ["libevent.a"],
    visibility = ["//visibility:public"],
    deps = [
        "@org_openssl//:ssl",
    ],
)
