/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

// Disables security checking our updates which haven't been signed
Services.prefs.setBoolPref("extensions.checkUpdateSecurity", false);

do_load_httpd_js();
var server;

// nsIAddonUpdateCheckListener implementation
var updateListener = {
  _count: 0,

  onUpdateAvailable: function onAddonUpdateEnded(aAddon, aInstall) {
    do_check_eq(aInstall.version, 10);
  },

  onNoUpdateAvailable: function onNoUpdateAvailable(aAddon) {
    do_throw("Expected an available update for " + aAddon.id);
  },

  onUpdateFinished: function onUpdateFinished() {
    if (++this._count == 2)
      server.stop(do_test_finished);
  },
}

function run_test()
{
  // Setup for test
  do_test_pending();
  createAppInfo("xpcshell@tests.mozilla.org", "XPCShell", "1", "1.9");
  startupManager();

  installAllFiles([do_get_addon("test_bug394300_1"),
                   do_get_addon("test_bug394300_2")], function() {

    restartManager();

    AddonManager.getAddonsByIDs(["bug394300_1@tests.mozilla.org",
                                 "bug394300_2@tests.mozilla.org"], function(updates) {

      do_check_neq(updates[0], null);
      do_check_neq(updates[1], null);

      server = new nsHttpServer();
      server.registerDirectory("/", do_get_file("data"));
      server.start(4444);

      updates[0].findUpdates(updateListener, AddonManager.UPDATE_WHEN_USER_REQUESTED);
      updates[1].findUpdates(updateListener, AddonManager.UPDATE_WHEN_USER_REQUESTED);
    });
  });
}
