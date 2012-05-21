/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package org.mozilla.gecko.sync;

import org.mozilla.gecko.R;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;

/*
 * Activity is just here for testing.
 */
public class StubActivity extends Activity {
  private static final String LOG_TAG = "StubActivity";

  /** Called when the activity is first created. */
  @Override
  public void onCreate(Bundle savedInstanceState) {
      Log.i(LOG_TAG, "In StubActivity onCreate.");
      super.onCreate(savedInstanceState);
      setContentView(R.layout.sync_stub);
      Log.i(LOG_TAG, "Done with onCreate.");
  }
}
