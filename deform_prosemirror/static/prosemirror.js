/**
 * npm install --save-dev browserify babelify babel-preset-es2015
 *
 * node_modules/.bin/browserify dist/prosemirror.js -o dist/prosermirror-bundle.js -t [ babelify --presets [ es2015 ] ]
 */

import {ProseMirror} from "../src/edit/main";
window.ProseMirror = ProseMirror;

