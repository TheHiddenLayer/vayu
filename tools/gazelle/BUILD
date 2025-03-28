load("@bazel_gazelle//:def.bzl", "gazelle")

gazelle(
    name = "gazelle",
    extra_args = [
        "--build_file_name",
        "BUILD",
    ],
    gazelle = "@rules_python_gazelle_plugin//python:gazelle_binary",
    visibility = ["//:__subpackages__"],
)
