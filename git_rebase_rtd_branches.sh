#!/bin/sh

set -e

fmt='
git checkout %(refname)
git rebase master
git push origin HEAD:%(refname:lstrip=3) --force
'

eval "$(git for-each-ref --shell --format="$fmt" \
    refs/remotes/origin/breadcrumbs \
    refs/remotes/origin/sphinx3 \
    refs/remotes/origin/sphinx4 \
    refs/remotes/origin/readthedocs-sphinx-search \
    refs/remotes/origin/rightsidebar \
    )"

git checkout master
