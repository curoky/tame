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
load("@com_curoky_rules_pkg//:recipes/rapidjson/config.bzl", rapidjson_config = "config")
load("@com_curoky_rules_pkg//:recipes/restclient-cpp/config.bzl", restclient_cpp_config = "config")
load("@com_curoky_rules_pkg//:recipes/rules_m4/config.bzl", rules_m4_config = "config")
load("@com_curoky_rules_pkg//:recipes/proxygen/config.bzl", proxygen_config = "config")
load("@com_curoky_rules_pkg//:recipes/icecream-cpp/config.bzl", icecream_cpp_config = "config")
load("@com_curoky_rules_pkg//:recipes/bazel-compilation-database/config.bzl", bazel_compilation_database_config = "config")
load("@com_curoky_rules_pkg//:recipes/glog/config.bzl", glog_config = "config")
load("@com_curoky_rules_pkg//:recipes/llvm/config.bzl", llvm_config = "config")
load("@com_curoky_rules_pkg//:recipes/libsodium/config.bzl", libsodium_config = "config")
load("@com_curoky_rules_pkg//:recipes/libaio/config.bzl", libaio_config = "config")
load("@com_curoky_rules_pkg//:recipes/libunwind/config.bzl", libunwind_config = "config")
load("@com_curoky_rules_pkg//:recipes/cpp-peglib/config.bzl", cpp_peglib_config = "config")
load("@com_curoky_rules_pkg//:recipes/openssl/config.bzl", openssl_config = "config")
load("@com_curoky_rules_pkg//:recipes/googletest/config.bzl", googletest_config = "config")
load("@com_curoky_rules_pkg//:recipes/thrift/config.bzl", thrift_config = "config")
load("@com_curoky_rules_pkg//:recipes/tbb/config.bzl", tbb_config = "config")
load("@com_curoky_rules_pkg//:recipes/msgpack-c/config.bzl", msgpack_c_config = "config")
load("@com_curoky_rules_pkg//:recipes/concurrentqueue/config.bzl", concurrentqueue_config = "config")
load("@com_curoky_rules_pkg//:recipes/curl/config.bzl", curl_config = "config")
load("@com_curoky_rules_pkg//:recipes/rules_flex/config.bzl", rules_flex_config = "config")
load("@com_curoky_rules_pkg//:recipes/catch2/config.bzl", catch2_config = "config")
load("@com_curoky_rules_pkg//:recipes/flatbuffers/config.bzl", flatbuffers_config = "config")
load("@com_curoky_rules_pkg//:recipes/phc-winner-argon2/config.bzl", phc_winner_argon2_config = "config")
load("@com_curoky_rules_pkg//:recipes/cppitertools/config.bzl", cppitertools_config = "config")
load("@com_curoky_rules_pkg//:recipes/wangle/config.bzl", wangle_config = "config")
load("@com_curoky_rules_pkg//:recipes/zstd/config.bzl", zstd_config = "config")
load("@com_curoky_rules_pkg//:recipes/usrefl/config.bzl", usrefl_config = "config")
load("@com_curoky_rules_pkg//:recipes/libevent/config.bzl", libevent_config = "config")
load("@com_curoky_rules_pkg//:recipes/qt/config.bzl", qt_config = "config")
load("@com_curoky_rules_pkg//:recipes/lz4/config.bzl", lz4_config = "config")
load("@com_curoky_rules_pkg//:recipes/rules_boost/config.bzl", rules_boost_config = "config")
load("@com_curoky_rules_pkg//:recipes/bazel-gazelle/config.bzl", bazel_gazelle_config = "config")
load("@com_curoky_rules_pkg//:recipes/json/config.bzl", json_config = "config")
load("@com_curoky_rules_pkg//:recipes/boringssl/config.bzl", boringssl_config = "config")
load("@com_curoky_rules_pkg//:recipes/crc32c/config.bzl", crc32c_config = "config")
load("@com_curoky_rules_pkg//:recipes/libiberty/config.bzl", libiberty_config = "config")
load("@com_curoky_rules_pkg//:recipes/diff-match-patch/config.bzl", diff_match_patch_config = "config")
load("@com_curoky_rules_pkg//:recipes/fbthrift/config.bzl", fbthrift_config = "config")
load("@com_curoky_rules_pkg//:recipes/cpr/config.bzl", cpr_config = "config")
load("@com_curoky_rules_pkg//:recipes/nameof/config.bzl", nameof_config = "config")
load("@com_curoky_rules_pkg//:recipes/cpp-httplib/config.bzl", cpp_httplib_config = "config")
load("@com_curoky_rules_pkg//:recipes/wolic/config.bzl", wolic_config = "config")
load("@com_curoky_rules_pkg//:recipes/taskflow/config.bzl", taskflow_config = "config")
load("@com_curoky_rules_pkg//:recipes/rules_foreign_cc/config.bzl", rules_foreign_cc_config = "config")
load("@com_curoky_rules_pkg//:recipes/gflags/config.bzl", gflags_config = "config")
load("@com_curoky_rules_pkg//:recipes/snappy/config.bzl", snappy_config = "config")
load("@com_curoky_rules_pkg//:recipes/rules_bison/config.bzl", rules_bison_config = "config")
load("@com_curoky_rules_pkg//:recipes/benchmark/config.bzl", benchmark_config = "config")
load("@com_curoky_rules_pkg//:recipes/cityhash/config.bzl", cityhash_config = "config")
load("@com_curoky_rules_pkg//:recipes/jsoncpp/config.bzl", jsoncpp_config = "config")
load("@com_curoky_rules_pkg//:recipes/abseil-cpp/config.bzl", abseil_cpp_config = "config")
load("@com_curoky_rules_pkg//:recipes/fatal/config.bzl", fatal_config = "config")
load("@com_curoky_rules_pkg//:recipes/refl-cpp/config.bzl", refl_cpp_config = "config")
load("@com_curoky_rules_pkg//:recipes/better-enums/config.bzl", better_enums_config = "config")
load("@com_curoky_rules_pkg//:recipes/xz/config.bzl", xz_config = "config")
load("@com_curoky_rules_pkg//:recipes/jemalloc/config.bzl", jemalloc_config = "config")
load("@com_curoky_rules_pkg//:recipes/rules_python/config.bzl", rules_python_config = "config")
load("@com_curoky_rules_pkg//:recipes/fmt/config.bzl", fmt_config = "config")
load("@com_curoky_rules_pkg//:recipes/parallel-hashmap/config.bzl", parallel_hashmap_config = "config")
load("@com_curoky_rules_pkg//:recipes/libuv/config.bzl", libuv_config = "config")
load("@com_curoky_rules_pkg//:recipes/double-conversion/config.bzl", double_conversion_config = "config")
load("@com_curoky_rules_pkg//:recipes/protobuf/config.bzl", protobuf_config = "config")
load("@com_curoky_rules_pkg//:recipes/readerwriterqueue/config.bzl", readerwriterqueue_config = "config")
load("@com_curoky_rules_pkg//:recipes/lua/config.bzl", lua_config = "config")
load("@com_curoky_rules_pkg//:recipes/folly/config.bzl", folly_config = "config")
load("@com_curoky_rules_pkg//:recipes/libdwarf/config.bzl", libdwarf_config = "config")
load("@com_curoky_rules_pkg//:recipes/rttr/config.bzl", rttr_config = "config")
load("@com_curoky_rules_pkg//:recipes/spdlog/config.bzl", spdlog_config = "config")
load("@com_curoky_rules_pkg//:recipes/zlib/config.bzl", zlib_config = "config")
load("@com_curoky_rules_pkg//:recipes/immer/config.bzl", immer_config = "config")
load("@com_curoky_rules_pkg//:recipes/re2/config.bzl", re2_config = "config")
load("@com_curoky_rules_pkg//:recipes/fizz/config.bzl", fizz_config = "config")
load("@com_curoky_rules_pkg//:recipes/brotli/config.bzl", brotli_config = "config")
load("@com_curoky_rules_pkg//:recipes/rules_go/config.bzl", rules_go_config = "config")
load("@com_curoky_rules_pkg//:recipes/smhasher/config.bzl", smhasher_config = "config")
load("@com_curoky_rules_pkg//:recipes/xxhash/config.bzl", xxhash_config = "config")
load("@com_curoky_rules_pkg//:recipes/hiredis/config.bzl", hiredis_config = "config")
load("@com_curoky_rules_pkg//:recipes/liburing/config.bzl", liburing_config = "config")
load("@com_curoky_rules_pkg//:recipes/cjson/config.bzl", cjson_config = "config")

configs = {
    "rapidjson": rapidjson_config,
    "restclient-cpp": restclient_cpp_config,
    "rules_m4": rules_m4_config,
    "proxygen": proxygen_config,
    "icecream-cpp": icecream_cpp_config,
    "bazel-compilation-database": bazel_compilation_database_config,
    "glog": glog_config,
    "llvm": llvm_config,
    "libsodium": libsodium_config,
    "libaio": libaio_config,
    "libunwind": libunwind_config,
    "cpp-peglib": cpp_peglib_config,
    "openssl": openssl_config,
    "googletest": googletest_config,
    "thrift": thrift_config,
    "tbb": tbb_config,
    "msgpack-c": msgpack_c_config,
    "concurrentqueue": concurrentqueue_config,
    "curl": curl_config,
    "rules_flex": rules_flex_config,
    "catch2": catch2_config,
    "flatbuffers": flatbuffers_config,
    "phc-winner-argon2": phc_winner_argon2_config,
    "cppitertools": cppitertools_config,
    "wangle": wangle_config,
    "zstd": zstd_config,
    "usrefl": usrefl_config,
    "libevent": libevent_config,
    "qt": qt_config,
    "lz4": lz4_config,
    "rules_boost": rules_boost_config,
    "bazel-gazelle": bazel_gazelle_config,
    "json": json_config,
    "boringssl": boringssl_config,
    "crc32c": crc32c_config,
    "libiberty": libiberty_config,
    "diff-match-patch": diff_match_patch_config,
    "fbthrift": fbthrift_config,
    "cpr": cpr_config,
    "nameof": nameof_config,
    "cpp-httplib": cpp_httplib_config,
    "wolic": wolic_config,
    "taskflow": taskflow_config,
    "rules_foreign_cc": rules_foreign_cc_config,
    "gflags": gflags_config,
    "snappy": snappy_config,
    "rules_bison": rules_bison_config,
    "benchmark": benchmark_config,
    "cityhash": cityhash_config,
    "jsoncpp": jsoncpp_config,
    "abseil-cpp": abseil_cpp_config,
    "fatal": fatal_config,
    "refl-cpp": refl_cpp_config,
    "better-enums": better_enums_config,
    "xz": xz_config,
    "jemalloc": jemalloc_config,
    "rules_python": rules_python_config,
    "fmt": fmt_config,
    "parallel-hashmap": parallel_hashmap_config,
    "libuv": libuv_config,
    "double-conversion": double_conversion_config,
    "protobuf": protobuf_config,
    "readerwriterqueue": readerwriterqueue_config,
    "lua": lua_config,
    "folly": folly_config,
    "libdwarf": libdwarf_config,
    "rttr": rttr_config,
    "spdlog": spdlog_config,
    "zlib": zlib_config,
    "immer": immer_config,
    "re2": re2_config,
    "fizz": fizz_config,
    "brotli": brotli_config,
    "rules_go": rules_go_config,
    "smhasher": smhasher_config,
    "xxhash": xxhash_config,
    "hiredis": hiredis_config,
    "liburing": liburing_config,
    "cjson": cjson_config,
}
