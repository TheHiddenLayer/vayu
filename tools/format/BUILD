load("@aspect_rules_lint//format:defs.bzl", "format_multirun", "format_test")

format_multirun(
    name = "format",
    python = "@aspect_rules_lint//format:ruff",
    shell = "@aspect_rules_lint//format:shfmt",
    starlark = "@buildifier_prebuilt//:buildifier",
    visibility = ["//:__subpackages__"],
    yaml = "@aspect_rules_lint//format:yamlfmt",
)

# TODO(TheHiddenLayer) check if this is still needed
# or if format_multirun has a macro underneath for verify
format_test(
    name = "verify",
    size = "small",
    no_sandbox = True,
    python = "@aspect_rules_lint//format:ruff",
    shell = "@aspect_rules_lint//format:shfmt",
    starlark = "@buildifier_prebuilt//:buildifier",
    visibility = ["//:__subpackages__"],
    workspace = "//:requirements_lock.txt",
    yaml = "@aspect_rules_lint//format:yamlfmt",
)
