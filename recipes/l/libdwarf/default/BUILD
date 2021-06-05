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

load("@rules_foreign_cc//foreign_cc:configure.bzl", "configure_make")

filegroup(
    name = "all",
    srcs = glob(
        ["**"],
        exclude = ["gcc/**"],
    ),
    visibility = ["//visibility:public"],
)

configure_make(
    name = "libdwarf",
    configure_command = "./configure",
    configure_options = [
        # "--enable-install-libiberty",
    ],
    includes = ["libdwarf-0"],
    lib_source = "@libdwarf//:all",
    out_static_libs = ["libdwarf.a"],
    visibility = ["//visibility:public"],
)
