# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1 
# 
# The contents of this file are subject to the Mozilla Public License Version 
# 1.1 (the "License"); you may not use this file except in compliance with 
# the License. You may obtain a copy of the License at 
# http://www.mozilla.org/MPL/ # 
# Software distributed under the License is distributed on an "AS IS" basis, 
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License 
# for the specific language governing rights and limitations under the 
# License. 
# 
# The Original Code is Marionette Client. 
# 
# The Initial Developer of the Original Code is 
#   Mozilla Foundation. 
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved. 
# 
# Contributor(s): 
# 
# Alternatively, the contents of this file may be used under the terms of 
# either the GNU General Public License Version 2 or later (the "GPL"), or 
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"), 
# in which case the provisions of the GPL or the LGPL are applicable instead 
# of those above. If you wish to allow use of your version of this file only 
# under the terms of either the GPL or the LGPL, and not to allow others to 
# use your version of this file under the terms of the MPL, indicate your 
# decision by deleting the provisions above and replace them with the notice 
# and other provisions required by the GPL or the LGPL. If you do not delete 
# the provisions above, a recipient may use your version of this file under 
# the terms of any one of the MPL, the GPL or the LGPL. 
# 
# ***** END LICENSE BLOCK ***** 

import os
from marionette_test import MarionetteTestCase

class TestSwitchFrame(MarionetteTestCase):
    def test_switch_simple(self):
        self.assertTrue(self.marionette.execute_script("window.location.href = 'about:blank'; return true;"))
        self.assertEqual("about:blank", self.marionette.execute_script("return window.location.href;"))
        test_html = self.marionette.absolute_url("test_iframe.html")
        self.marionette.navigate(test_html)
        self.assertNotEqual("about:blank", self.marionette.execute_script("return window.location.href;"))
        self.assertEqual("Marionette IFrame Test", self.marionette.execute_script("return window.document.title;"))
        self.marionette.switch_to_frame("test_iframe")
        self.assertTrue("test.html" in self.marionette.get_url())

    def test_switch_nested(self):
        self.assertTrue(self.marionette.execute_script("window.location.href = 'about:blank'; return true;"))
        self.assertEqual("about:blank", self.marionette.execute_script("return window.location.href;"))
        test_html = self.marionette.absolute_url("test_nested_iframe.html")
        self.marionette.navigate(test_html)
        self.assertNotEqual("about:blank", self.marionette.execute_script("return window.location.href;"))
        self.assertEqual("Marionette IFrame Test", self.marionette.execute_script("return window.document.title;"))
        self.marionette.switch_to_frame("test_iframe")
        self.assertTrue("test_inner_iframe.html" in self.marionette.get_url())
        self.marionette.switch_to_frame("inner_frame")
        self.assertTrue("test.html" in self.marionette.get_url())
        self.marionette.switch_to_frame() # go back to main frame
        self.assertTrue("test_nested_iframe.html" in self.marionette.get_url())
        #test that we're using the right window object server-side
        self.assertTrue("test_nested_iframe.html" in self.marionette.execute_script("return window.location.href;"))

class TestSwitchFrameChrome(MarionetteTestCase):
    def setUp(self):
        MarionetteTestCase.setUp(self)
        self.marionette.set_context("chrome")
        self.win = self.marionette.get_window()
        #need to get the file:// path for xul
        unit = os.path.abspath(os.path.join(os.path.realpath(__file__), os.path.pardir))
        tests = os.path.abspath(os.path.join(unit, os.path.pardir))
        mpath = os.path.abspath(os.path.join(tests, os.path.pardir))
        xul = "file://" + os.path.join(mpath, "www", "test.xul")
        self.marionette.execute_script("window.open('" + xul +"', '_blank', 'chrome,centerscreen');")

    def tearDown(self):
        self.marionette.execute_script("window.close();")
        self.marionette.switch_to_window(self.win)
        MarionetteTestCase.tearDown(self)

    def test_switch_simple(self):
        self.assertTrue("test.xul" in self.marionette.get_url())
        self.marionette.switch_to_frame(0)
        self.assertTrue("test2.xul" in self.marionette.get_url())
        self.marionette.switch_to_frame()
        self.assertTrue("test.xul" in self.marionette.get_url())
        self.marionette.switch_to_frame("iframe")
        self.assertTrue("test2.xul" in self.marionette.get_url())
        self.marionette.switch_to_frame()
        self.assertTrue("test.xul" in self.marionette.get_url())
        self.marionette.switch_to_frame("iframename")
        self.assertTrue("test2.xul" in self.marionette.get_url())
        self.marionette.switch_to_frame()
        self.assertTrue("test.xul" in self.marionette.get_url())
        
    #I can't seem to access a xul iframe within a xul iframe
    def test_switch_nested(self):
        pass
