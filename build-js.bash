#!/bin/bash
#
# Build ProseMirror JS bundle using Browserify an Babelify
#
set -e

NPM=/usr/local/bin/npm

$NPM install -l --save-dev browserify babelify babel-preset-es2015

if [ ! -e prosemirror ] ; then
    git clone git@github.com:ProseMirror/prosemirror.git
fi

$NPM -l install prosemirror

node_modules/.bin/browserify deform_prosemirror/static/prosemirror.js -o deform_prosemirror/static/prosemirror-bundle.js -t [ babelify --presets [ es2015 ] ]