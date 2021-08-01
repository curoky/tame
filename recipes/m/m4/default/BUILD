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

# ref: https://github.com/cockroachdb/cockroach/blob/64c888ffa869dc254f6f14dbbcb308efc1d89a64/c-deps/BUILD.bazel

load("@rules_foreign_cc//foreign_cc:configure.bzl", "configure_make")

filegroup(
    name = "all",
    srcs = glob(["**"]),
    visibility = ["//visibility:public"],
)

configure_make(
    name = "m4",
    configure_in_place = True,
    lib_source = ":all",
    out_binaries = ["m4"],
    visibility = ["//visibility:public"],
)
