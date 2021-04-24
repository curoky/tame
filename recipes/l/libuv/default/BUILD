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

# Reference:
# https://chromium.googlesource.com/external/github.com/grpc/grpc/+/HEAD/third_party/libuv.BUILD
# https://github.com/ofrobots/no-bazel/blob/master/libuv.BUILD.bazel
# https://github.com/libuv/help/issues/83

load("@rules_cc//cc:defs.bzl", "cc_library")
load("@com_curoky_tame//bazel:copts.bzl", "DEFAULT_C_COPTS")

ANDROID_LIBUV_SOURCES = [
    "src/unix/android-ifaddrs.c",
    "src/unix/pthread-fixes.c",
]

DARWIN_LIBUV_SOURCES = [
    "src/unix/bsd-ifaddrs.c",
    "src/unix/darwin.c",
    "src/unix/fsevents.c",
    "src/unix/kqueue.c",
    "src/unix/darwin-proctitle.c",
    "src/unix/proctitle.c",
]

cc_library(
    name = "libuv",
    srcs = glob(
        [
            "src/*.h",
            "src/*.c",
            "src/unix/*.h",
            "src/unix/*.c",
        ],
        exclude = ANDROID_LIBUV_SOURCES + DARWIN_LIBUV_SOURCES + [
            "src/unix/aix-common.c",
            "src/unix/aix.c",
            "src/unix/freebsd.c",
            "src/unix/haiku.c",
            "src/unix/ibmi.c",
            "src/unix/netbsd.c",
            "src/unix/openbsd.c",
            "src/unix/os390-syscalls.c",
            "src/unix/os390.c",
            "src/unix/posix-poll.c",
            "src/unix/qnx.c",
            "src/unix/sunos.c",
        ],
    ),
    hdrs = glob(["include/**/*.h"]),
    copts = DEFAULT_C_COPTS + [
        "-I external/com_github_libuv_libuv/src",
        "-I external/com_github_libuv_libuv/src/unix",
        "-D_GNU_SOURCE",
    ],
    includes = ["include"],
    linkstatic = 1,
    visibility = ["//visibility:public"],
)
