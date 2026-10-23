"""Configuration file for the Sphinx documentation builder."""
import os
import shutil
import re

import rocm_docs.theme as rocm_theme

def _parse_version(version_string):
    """Keep name: version lines and drop a line that has no colon."""
    parsed = {}
    for line in (version_string or "").splitlines():
        name, separator, version = line.partition(":")
        if separator and name.strip() and version.strip():
            parsed[name.strip()] = version.strip()
    return parsed

rocm_theme._parse_version = _parse_version

shutil.copy2("../RELEASE.md", "./about/release-notes.md")

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "rocm.docs.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "ROCm for Life Science"

version = "26.10"
release = version
html_title = "AMD Life Science 26.10 documentation"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2026 Advanced Micro Devices, Inc. All rights reserved."
setting_all_article_info = True
all_article_info_os = ["linux"]
all_article_info_author = ""

# Required settings
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "rocm-ls",
    # Add any additional theme options here
}

'''
docs_header_version is used to manually configure the version in the header. If
there exists a non-null value mapped to docs_header_version, then the header in
the documentation page will contain the given version string.
'''
html_context = {
    "docs_header_version": "26.10"
}

html_static_path = ["sphinx/static/css"]
html_css_files = ["rocm_custom.css"]

extensions = ["rocm_docs"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']
