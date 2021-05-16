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

"""

"""

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")
load("@com_curoky_tame//:bazel/recipes.legacy.bzl", "configs")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def _get_namespace(config, default):
    namespace = default
    if "name" in config:
        namespace = config["name"]
    elif "remote" in config:
        remote = config["remote"]
        if remote.startswith("https://github.com/"):
            namespace = remote.replace("https://github.com/", "com_github_")
    return namespace.replace("/", "_").replace("-", "_").lower()

def _get_versioned_config(config, version = ""):
    """select version from config

    Args:
        config: config
        version: specified version, default is "".

    Returns:
        updated config with specified version
    """
    versioned_config = {}
    versioned_config.update(config)

    used_version = config["used_version"]
    if version and version in config["versions"]:
        used_version = version

    versioned_config.update(config["versions"][used_version])

    if used_version.startswith("heads/"):
        versioned_config["branch"] = used_version.split("/")[1]
    elif used_version.startswith("tags/"):
        versioned_config["tag"] = used_version.split("/")[1]

    versioned_config.pop("versions")
    versioned_config.pop("used_version")
    return versioned_config

def pkg_rules_dependencies(ignored_pkgs_list = []):
    """register all rules"""
    for key in configs:
        config = _get_versioned_config(configs[key])

        config["name"] = _get_namespace(config, key)

        if config["name"] in ignored_pkgs_list:
            continue

        # print("register namespace: {}".format(config["name"]))

        repo_type = config["type"]
        config.pop("type")

        if "build_file" in config:
            config["build_file"] = "@com_curoky_tame//:recipes/{}/{}".format(key, config["build_file"])
        if "patches" in config:
            patches = []
            for f in config["patches"]:
                patches.append("@com_curoky_tame//:recipes/{}/{}".format(key, f))
            config["patches"] = patches

        if repo_type == "git_repository":
            git_repository(**config)
        elif repo_type == "new_local_repository":
            config.pop("branch")
            native.new_local_repository(**config)
        elif repo_type == "new_git_repository":
            new_git_repository(**config)
        elif repo_type == "http_archive":
            config.pop("branch")
            http_archive(**config)
