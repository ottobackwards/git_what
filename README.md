# git_what
Python library to document git repositories in a directory structure

git_what will recurse the passed directory and find all the git repos there.
It outputs json with information about each repo

such as:

    "swift-lldb": {
    "Remote Branches": [
      "beanz-lldb-in-tree-build-fix",
      "master",
      "master-next",
      "stable-swift-3.0-merge-branch",
      "stop-format",
      "swift-2.2-branch",
      "swift-2.3-branch",
      "swift-3.0-branch",
      "swift-3.0-preview-1-branch",
      "swift-3.0-preview-2-branch",
      "swift-3.0-preview-3-branch",
      "swift-3.0-preview-4-branch",
      "swift-3.0-preview-5-branch",
      "swift-3.0-preview-5-speculative",
      "swift-3.0.1-preview-2-branch",
      "swift-3.1-branch",
      "swift-4.0-branch",
      "upstream",
      "upstream-with-swift"
    ],
    "path": "/Users/someone/src/apple/apple_swift/swift-lldb",
    "Fetch URL": "https://github.com/apple/swift-lldb.git",
    "HEAD branch": "master",
    "Push URL": "https://github.com/apple/swift-lldb.git"
  },

## Calling
    Usage: git-what.py [options]

Options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory=DIRECTORY
                        The directory to start in