### Hexlet tests and linter status:
[![Actions Status](https://github.com/WestNach/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/WestNach/python-project-50/actions)
### Codeclimate Mantainability
[![Maintainability](https://api.codeclimate.com/v1/badges/515baf296b4236f33618/maintainability)](https://codeclimate.com/github/WestNach/python-project-50/maintainability)
### Codeclimate Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/515baf296b4236f33618/test_coverage)](https://codeclimate.com/github/WestNach/python-project-50/test_coverage)

# Difference Calculator

A command line tool to calculate the difference between two data structures.
Runs from the command line, compares two configuration files and shows a difference.
Working with JSON and YAML.
Provides output in stylish, plain and json format.

## Usage

**help:**

```bash
$ gendiff -h
```

**Running:**

```bash
$ gendiff <file_path1> <file_path2> --format <format>
```

format - optional parameter, default value is 'stylish'.
Possible values: 'stylish', 'plain', 'json'.


## Setup

using Makefile:

```bash
$ make install
$ make build
$ make package-install
```

## Without installation

```sh
$ python3 -m gendiff.scripts.gendiff <file_path1> <file_path2> --format <format>
```


## DEMO

Comparison of two files in the JSON format:

[![asciicast](https://asciinema.org/a/ejkADXLd9g2msAOn69mFGF4QA.svg)](https://asciinema.org/a/j8L3ffQ925i2T0zeS4twAkQ6o)

Comparison of two nested files in the YAML format:

[![asciicast](https://asciinema.org/a/GPsU3IE88CcxFpnzOwH9sSgqN.svg)](https://asciinema.org/a/81A63revGsotXWQp1lYen0O8E)

Comparison of two files in the JSON format with plain output:

[![asciicast](https://asciinema.org/a/HP4Y0O4C2tGsWBXspZRYU5BJK.svg)](https://asciinema.org/a/HP4Y0O4C2tGsWBXspZRYU5BJK)

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
