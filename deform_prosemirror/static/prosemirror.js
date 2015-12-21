/**
 * npm install --save-dev browserify babelify babel-preset-es2015
 *
 * node_modules/.bin/browserify dist/prosemirror.js -o dist/prosermirror-bundle.js -t [ babelify --presets [ es2015 ] ]
 */

import {ProseMirror} from "../../prosemirror/src/edit/main";
import "../../prosemirror/src/parse/markdown";
import "../../prosemirror/src/serialize/markdown";
import "../../prosemirror/src/menu/tooltipmenu";
import "../../prosemirror/src/menu/menubar";

window.ProseMirror = ProseMirror;

