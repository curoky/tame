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
load("@com_curoky_tame//:recipes/abseil-cpp/config.bzl", abseil_cpp_config = "config")
load("@com_curoky_tame//:recipes/apple_support/config.bzl", apple_support_config = "config")
load("@com_curoky_tame//:recipes/baiduhook/config.bzl", baiduhook_config = "config")
load("@com_curoky_tame//:recipes/bazel-compilation-database/config.bzl", bazel_compilation_database_config = "config")
load("@com_curoky_tame//:recipes/bazel-compile-commands-extractor/config.bzl", bazel_compile_commands_extractor_config = "config")
load("@com_curoky_tame//:recipes/bazel-gazelle/config.bzl", bazel_gazelle_config = "config")
load("@com_curoky_tame//:recipes/bazel-skylib/config.bzl", bazel_skylib_config = "config")
load("@com_curoky_tame//:recipes/benchmark/config.bzl", benchmark_config = "config")
load("@com_curoky_tame//:recipes/better-enums/config.bzl", better_enums_config = "config")
load("@com_curoky_tame//:recipes/binutils/config.bzl", binutils_config = "config")
load("@com_curoky_tame//:recipes/bitsery/config.bzl", bitsery_config = "config")
load("@com_curoky_tame//:recipes/boringssl/config.bzl", boringssl_config = "config")
load("@com_curoky_tame//:recipes/brotli/config.bzl", brotli_config = "config")
load("@com_curoky_tame//:recipes/catch2/config.bzl", catch2_config = "config")
load("@com_curoky_tame//:recipes/cista/config.bzl", cista_config = "config")
load("@com_curoky_tame//:recipes/cityhash/config.bzl", cityhash_config = "config")
load("@com_curoky_tame//:recipes/cjson/config.bzl", cjson_config = "config")
load("@com_curoky_tame//:recipes/concurrentqueue/config.bzl", concurrentqueue_config = "config")
load("@com_curoky_tame//:recipes/cpp-httplib/config.bzl", cpp_httplib_config = "config")
load("@com_curoky_tame//:recipes/cpp-peglib/config.bzl", cpp_peglib_config = "config")
load("@com_curoky_tame//:recipes/cppitertools/config.bzl", cppitertools_config = "config")
load("@com_curoky_tame//:recipes/cpr/config.bzl", cpr_config = "config")
load("@com_curoky_tame//:recipes/crc32c/config.bzl", crc32c_config = "config")
load("@com_curoky_tame//:recipes/curl/config.bzl", curl_config = "config")
load("@com_curoky_tame//:recipes/diff-match-patch/config.bzl", diff_match_patch_config = "config")
load("@com_curoky_tame//:recipes/double-conversion/config.bzl", double_conversion_config = "config")
load("@com_curoky_tame//:recipes/envoy-api/config.bzl", envoy_api_config = "config")
load("@com_curoky_tame//:recipes/fatal/config.bzl", fatal_config = "config")
load("@com_curoky_tame//:recipes/fbthrift/config.bzl", fbthrift_config = "config")
load("@com_curoky_tame//:recipes/fizz/config.bzl", fizz_config = "config")
load("@com_curoky_tame//:recipes/flatbuffers/config.bzl", flatbuffers_config = "config")
load("@com_curoky_tame//:recipes/fmt/config.bzl", fmt_config = "config")
load("@com_curoky_tame//:recipes/folly/config.bzl", folly_config = "config")
load("@com_curoky_tame//:recipes/gflags/config.bzl", gflags_config = "config")
load("@com_curoky_tame//:recipes/glog/config.bzl", glog_config = "config")
load("@com_curoky_tame//:recipes/googleapis/config.bzl", googleapis_config = "config")
load("@com_curoky_tame//:recipes/googletest/config.bzl", googletest_config = "config")
load("@com_curoky_tame//:recipes/grpc/config.bzl", grpc_config = "config")
load("@com_curoky_tame//:recipes/hiredis/config.bzl", hiredis_config = "config")
load("@com_curoky_tame//:recipes/icecream-cpp/config.bzl", icecream_cpp_config = "config")
load("@com_curoky_tame//:recipes/immer/config.bzl", immer_config = "config")
load("@com_curoky_tame//:recipes/jemalloc/config.bzl", jemalloc_config = "config")
load("@com_curoky_tame//:recipes/json/config.bzl", json_config = "config")
load("@com_curoky_tame//:recipes/jsoncpp/config.bzl", jsoncpp_config = "config")
load("@com_curoky_tame//:recipes/laugh/config.bzl", laugh_config = "config")
load("@com_curoky_tame//:recipes/libaio/config.bzl", libaio_config = "config")
load("@com_curoky_tame//:recipes/libdwarf/config.bzl", libdwarf_config = "config")
load("@com_curoky_tame//:recipes/libevent/config.bzl", libevent_config = "config")
load("@com_curoky_tame//:recipes/libiberty/config.bzl", libiberty_config = "config")
load("@com_curoky_tame//:recipes/libsodium/config.bzl", libsodium_config = "config")
load("@com_curoky_tame//:recipes/libunwind/config.bzl", libunwind_config = "config")
load("@com_curoky_tame//:recipes/liburing/config.bzl", liburing_config = "config")
load("@com_curoky_tame//:recipes/libuv/config.bzl", libuv_config = "config")
load("@com_curoky_tame//:recipes/llvm/config.bzl", llvm_config = "config")
load("@com_curoky_tame//:recipes/lua/config.bzl", lua_config = "config")
load("@com_curoky_tame//:recipes/lz4/config.bzl", lz4_config = "config")
load("@com_curoky_tame//:recipes/m4/config.bzl", m4_config = "config")
load("@com_curoky_tame//:recipes/msgpack-c/config.bzl", msgpack_c_config = "config")
load("@com_curoky_tame//:recipes/nameof/config.bzl", nameof_config = "config")
load("@com_curoky_tame//:recipes/openssl/config.bzl", openssl_config = "config")
load("@com_curoky_tame//:recipes/parallel-hashmap/config.bzl", parallel_hashmap_config = "config")
load("@com_curoky_tame//:recipes/phc-winner-argon2/config.bzl", phc_winner_argon2_config = "config")
load("@com_curoky_tame//:recipes/protobuf/config.bzl", protobuf_config = "config")
load("@com_curoky_tame//:recipes/proxygen/config.bzl", proxygen_config = "config")
load("@com_curoky_tame//:recipes/qt/config.bzl", qt_config = "config")
load("@com_curoky_tame//:recipes/rapidjson/config.bzl", rapidjson_config = "config")
load("@com_curoky_tame//:recipes/re2/config.bzl", re2_config = "config")
load("@com_curoky_tame//:recipes/readerwriterqueue/config.bzl", readerwriterqueue_config = "config")
load("@com_curoky_tame//:recipes/refl-cpp/config.bzl", refl_cpp_config = "config")
load("@com_curoky_tame//:recipes/restclient-cpp/config.bzl", restclient_cpp_config = "config")
load("@com_curoky_tame//:recipes/rttr/config.bzl", rttr_config = "config")
load("@com_curoky_tame//:recipes/rules_apple/config.bzl", rules_apple_config = "config")
load("@com_curoky_tame//:recipes/rules_bison/config.bzl", rules_bison_config = "config")
load("@com_curoky_tame//:recipes/rules_boost/config.bzl", rules_boost_config = "config")
load("@com_curoky_tame//:recipes/rules_flex/config.bzl", rules_flex_config = "config")
load("@com_curoky_tame//:recipes/rules_foreign_cc/config.bzl", rules_foreign_cc_config = "config")
load("@com_curoky_tame//:recipes/rules_go/config.bzl", rules_go_config = "config")
load("@com_curoky_tame//:recipes/rules_m4/config.bzl", rules_m4_config = "config")
load("@com_curoky_tame//:recipes/rules_pkg/config.bzl", rules_pkg_config = "config")
load("@com_curoky_tame//:recipes/rules_proto/config.bzl", rules_proto_config = "config")
load("@com_curoky_tame//:recipes/rules_python/config.bzl", rules_python_config = "config")
load("@com_curoky_tame//:recipes/smhasher/config.bzl", smhasher_config = "config")
load("@com_curoky_tame//:recipes/snappy/config.bzl", snappy_config = "config")
load("@com_curoky_tame//:recipes/spdlog/config.bzl", spdlog_config = "config")
load("@com_curoky_tame//:recipes/taskflow/config.bzl", taskflow_config = "config")
load("@com_curoky_tame//:recipes/tbb/config.bzl", tbb_config = "config")
load("@com_curoky_tame//:recipes/thrift/config.bzl", thrift_config = "config")
load("@com_curoky_tame//:recipes/upb/config.bzl", upb_config = "config")
load("@com_curoky_tame//:recipes/usrefl/config.bzl", usrefl_config = "config")
load("@com_curoky_tame//:recipes/wangle/config.bzl", wangle_config = "config")
load("@com_curoky_tame//:recipes/xxhash/config.bzl", xxhash_config = "config")
load("@com_curoky_tame//:recipes/xz/config.bzl", xz_config = "config")
load("@com_curoky_tame//:recipes/zlib/config.bzl", zlib_config = "config")
load("@com_curoky_tame//:recipes/zstd/config.bzl", zstd_config = "config")

configs = {
    "abseil-cpp": abseil_cpp_config,
    "apple_support": apple_support_config,
    "baiduhook": baiduhook_config,
    "bazel-compilation-database": bazel_compilation_database_config,
    "bazel-compile-commands-extractor": bazel_compile_commands_extractor_config,
    "bazel-gazelle": bazel_gazelle_config,
    "bazel-skylib": bazel_skylib_config,
    "benchmark": benchmark_config,
    "better-enums": better_enums_config,
    "binutils": binutils_config,
    "bitsery": bitsery_config,
    "boringssl": boringssl_config,
    "brotli": brotli_config,
    "catch2": catch2_config,
    "cista": cista_config,
    "cityhash": cityhash_config,
    "cjson": cjson_config,
    "concurrentqueue": concurrentqueue_config,
    "cpp-httplib": cpp_httplib_config,
    "cpp-peglib": cpp_peglib_config,
    "cppitertools": cppitertools_config,
    "cpr": cpr_config,
    "crc32c": crc32c_config,
    "curl": curl_config,
    "diff-match-patch": diff_match_patch_config,
    "double-conversion": double_conversion_config,
    "envoy-api": envoy_api_config,
    "fatal": fatal_config,
    "fbthrift": fbthrift_config,
    "fizz": fizz_config,
    "flatbuffers": flatbuffers_config,
    "fmt": fmt_config,
    "folly": folly_config,
    "gflags": gflags_config,
    "glog": glog_config,
    "googleapis": googleapis_config,
    "googletest": googletest_config,
    "grpc": grpc_config,
    "hiredis": hiredis_config,
    "icecream-cpp": icecream_cpp_config,
    "immer": immer_config,
    "jemalloc": jemalloc_config,
    "json": json_config,
    "jsoncpp": jsoncpp_config,
    "laugh": laugh_config,
    "libaio": libaio_config,
    "libdwarf": libdwarf_config,
    "libevent": libevent_config,
    "libiberty": libiberty_config,
    "libsodium": libsodium_config,
    "libunwind": libunwind_config,
    "liburing": liburing_config,
    "libuv": libuv_config,
    "llvm": llvm_config,
    "lua": lua_config,
    "lz4": lz4_config,
    "m4": m4_config,
    "msgpack-c": msgpack_c_config,
    "nameof": nameof_config,
    "openssl": openssl_config,
    "parallel-hashmap": parallel_hashmap_config,
    "phc-winner-argon2": phc_winner_argon2_config,
    "protobuf": protobuf_config,
    "proxygen": proxygen_config,
    "qt": qt_config,
    "rapidjson": rapidjson_config,
    "re2": re2_config,
    "readerwriterqueue": readerwriterqueue_config,
    "refl-cpp": refl_cpp_config,
    "restclient-cpp": restclient_cpp_config,
    "rttr": rttr_config,
    "rules_apple": rules_apple_config,
    "rules_bison": rules_bison_config,
    "rules_boost": rules_boost_config,
    "rules_flex": rules_flex_config,
    "rules_foreign_cc": rules_foreign_cc_config,
    "rules_go": rules_go_config,
    "rules_m4": rules_m4_config,
    "rules_pkg": rules_pkg_config,
    "rules_proto": rules_proto_config,
    "rules_python": rules_python_config,
    "smhasher": smhasher_config,
    "snappy": snappy_config,
    "spdlog": spdlog_config,
    "taskflow": taskflow_config,
    "tbb": tbb_config,
    "thrift": thrift_config,
    "upb": upb_config,
    "usrefl": usrefl_config,
    "wangle": wangle_config,
    "xxhash": xxhash_config,
    "xz": xz_config,
    "zlib": zlib_config,
    "zstd": zstd_config,
}
