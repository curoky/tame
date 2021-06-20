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

load("@com_github_nelhage_rules_boost//:boost/boost.bzl", "boost_deps")
load("@rules_bison//bison:bison.bzl", "bison_register_toolchains")
load("@rules_flex//flex:flex.bzl", "flex_register_toolchains")
load("@rules_m4//m4:m4.bzl", "m4_register_toolchains")
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
load("@rules_foreign_cc//foreign_cc:repositories.bzl", "rules_foreign_cc_dependencies")
load("@hedron_compile_commands//:workspace_setup.bzl", "hedron_compile_commands_setup")
load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
load("@build_bazel_apple_support//lib:repositories.bzl", "apple_support_dependencies")
load("@build_bazel_rules_apple//apple:repositories.bzl", "apple_rules_dependencies")
# load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")
# load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")

def pkg_register_toolchains():
    # https://github.com/nelhage/rules_boost/blob/master/BUILD.boost
    boost_deps()

    m4_register_toolchains()

    flex_register_toolchains()

    bison_register_toolchains()

    go_rules_dependencies()

    go_register_toolchains("1.17.6")

    gazelle_dependencies()

    rules_foreign_cc_dependencies()

    hedron_compile_commands_setup()

    bazel_skylib_workspace()

    protobuf_deps()

    rules_proto_dependencies()

    rules_proto_toolchains()

    apple_support_dependencies()

    apple_rules_dependencies(ignore_version_differences = True)

    # grpc_deps()

    # grpc_extra_deps()
