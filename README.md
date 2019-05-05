# package manager for bazel

## Getting Started

Add the following to your WORKSPACE file:

```python
git_repository(
    name = "com_curoky_rules_pkg",
    branch = "master",
    remote = "https://github.com/curoky/rules_cc",
)

load("@com_curoky_rules_pkg//:rules_dependencies.bzl", "pkg_rules_dependencies")

pkg_rules_dependencies()

load("@com_curoky_rules_pkg//:register_toolchains.bzl", "pkg_register_toolchains")

pkg_register_toolchains()

```

Then, in your BUILD files, import and use the rules:

```python
cc_test(
    name = "example",
    srcs = glob(["**/*.cc"]),
    deps = [
        "@com_github_facebook_folly//:folly",
    ],
)
```
