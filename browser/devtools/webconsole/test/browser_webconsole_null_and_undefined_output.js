/* vim:set ts=2 sw=2 sts=2 et: */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

// Test that JavaScript expressions that evaluate to null or undefined produce
// meaningful output.

const TEST_URI = "http://example.com/browser/browser/devtools/webconsole/test/test-console.html";

function test() {
  addTab(TEST_URI);
  browser.addEventListener("load", function onLoad() {
    browser.removeEventListener("load", onLoad, true);
    openConsole(null, testNullAndUndefinedOutput);
  }, true);
}

function testNullAndUndefinedOutput(hud) {
  let jsterm = hud.jsterm;
  let outputNode = jsterm.outputNode;

  jsterm.clearOutput();
  jsterm.execute("null;");

  let nodes = outputNode.querySelectorAll(".hud-msg-node");
  is(nodes.length, 2, "2 nodes in output");
  ok(nodes[1].textContent.indexOf("null") > -1, "'null' printed to output");

  jsterm.clearOutput();
  jsterm.execute("undefined;");

  nodes = outputNode.querySelectorAll(".hud-msg-node");
  is(nodes.length, 2, "2 nodes in output");
  ok(nodes[1].textContent.indexOf("undefined") > -1, "'undefined' printed to output");

  executeSoon(finishTest);
}

