# Developer Docs

By leveraging the power of Bazel, vayu runs on various target hardware platforms with ease.

As a developer, you will either contribute to the frontend (Python) or backend (C++). Both are managed by Bazel. Download bazelisk and place in on your `$PATH` as `bazel`.


### Code Quality

```bash
# run all the tests
$ bazel test ...

# format everything
$ bazel run format

# generate or update BUILD files
$ bazel run gazelle
```
