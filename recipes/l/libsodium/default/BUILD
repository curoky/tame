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
load("@com_curoky_tame//bazel:copts.bzl", "IGNORED_COPTS")

# TODO: get version num from source
genrule(
    name = "gen_sh",
    outs = [
        "gen.sh",
    ],
    cmd = """
cat > $@ <<"EOF"
#! /bin/sh
sed -e 's/@VERSION@/1.0.15/g' \
    -e 's/@SODIUM_LIBRARY_VERSION_MAJOR@/10/g' \
    -e 's/@SODIUM_LIBRARY_VERSION_MINOR@/0/g' \
    -e 's/@SODIUM_LIBRARY_MINIMAL_DEF@//g'
EOF""",
)

config_setting(
    name = "windows",
    constraint_values = [
        "@bazel_tools//platforms:windows",
    ],
    visibility = ["//visibility:public"],
)

genrule(
    name = "version_h",
    srcs = ["src/libsodium/include/sodium/version.h.in"],
    outs = ["src/libsodium/include/sodium/version.h"],
    cmd = "$(location :gen_sh) < $(<) > $(@)",
    tools = [":gen_sh"],
)

cc_library(
    name = "sodium",
    srcs = glob(
        [
            "src/**/*.c",
            "src/**/*.h",
        ],
        exclude = ["src/libsodium/crypto_pwhash/argon2/argon2.c"],
    ),
    hdrs = [":version_h"] + glob(["src/**/*.h"]),
    copts = select({
        ":windows": [],
        "//conditions:default": ["-DHAVE_PTHREAD"],
    }) + [
        # TODO(th0br0) add bazel support for determining this on the fly
        # mmx
        # "-DHAVE_MMINTRIN_H",
        # sse2
        # "-DHAVE_EMMINTRIN_H",
        # avx
        # "-DHAVE_AVXINTRIN_H",
    ] + IGNORED_COPTS,
    includes = [
        "src/libsodium/crypto_core/curve25519/ref10",
        "src/libsodium/crypto_generichash/blake2b/ref",
        "src/libsodium/crypto_onetimeauth/poly1305",
        "src/libsodium/crypto_onetimeauth/poly1305/donna",
        "src/libsodium/crypto_onetimeauth/poly1305/sse2",
        "src/libsodium/crypto_pwhash/argon2",
        "src/libsodium/crypto_pwhash/scryptsalsa208sha256",
        "src/libsodium/crypto_scalarmult/curve25519",
        "src/libsodium/crypto_scalarmult/curve25519/donna_c64",
        "src/libsodium/crypto_scalarmult/curve25519/ref10",
        "src/libsodium/crypto_scalarmult/curve25519/sandy2x",
        "src/libsodium/crypto_shorthash/siphash24/ref",
        "src/libsodium/crypto_sign/ed25519/ref10",
        "src/libsodium/crypto_stream/chacha20",
        "src/libsodium/crypto_stream/chacha20/dolbeau",
        "src/libsodium/crypto_stream/chacha20/ref",
        "src/libsodium/crypto_stream/salsa20",
        "src/libsodium/crypto_stream/salsa20/ref",
        "src/libsodium/crypto_stream/salsa20/xmm6",
        "src/libsodium/crypto_stream/salsa20/xmm6int",
        "src/libsodium/include",
        "src/libsodium/include/sodium",
        "src/libsodium/include/sodium/private",
    ],
    linkopts = select({
        ":windows": [],
        "//conditions:default": [
            "-lpthread",
        ],
    }),
    visibility = ["//visibility:public"],
    deps = ["@com_github_p_h_c_phc_winner_argon2//:phc-winner-argon2"],
)
