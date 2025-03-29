load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
    name = "vayu",
    srcs = [
        "__init__.py",
        "engine.py",
    ],
    visibility = ["//:__subpackages__"],
)

py_binary(
    name = "vayu_bin",
    srcs = ["__main__.py"],
    main = "__main__.py",
    visibility = ["//:__subpackages__"],
)
