load("@aspect_rules_lint//format:defs.bzl", "format_multirun", "format_test")

format_multirun(
    name = "format",
    python = "@aspect_rules_lint//format:ruff",
    shell = "@aspect_rules_lint//format:shfmt",
    starlark = "@buildifier_prebuilt//:buildifier",
    visibility = ["//:__subpackages__"],
    yaml = "@aspect_rules_lint//format:yamlfmt",
)

# check if everything is formatted
format_test(
    name = "check",
    size = "small",
    no_sandbox = True,
    python = "@aspect_rules_lint//format:ruff",
    shell = "@aspect_rules_lint//format:shfmt",
    starlark = "@buildifier_prebuilt//:buildifier",
    visibility = ["//:__subpackages__"],
    workspace = "//:requirements.txt",
    yaml = "@aspect_rules_lint//format:yamlfmt",
)
