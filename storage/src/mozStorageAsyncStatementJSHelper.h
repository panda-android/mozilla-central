/* -*- Mode: C++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*-
 * vim: sw=2 ts=2 et lcs=trail\:.,tab\:>~ :
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

#ifndef mozilla_storage_mozStorageAsyncStatementJSHelper_h_
#define mozilla_storage_mozStorageAsyncStatementJSHelper_h_

#include "nsIXPCScriptable.h"

class AsyncStatement;

namespace mozilla {
namespace storage {

/**
 * A modified version of StatementJSHelper that only exposes the async-specific
 * 'params' helper.  We do not expose 'row' or 'step' as they do not apply to
 * us.
 */
class AsyncStatementJSHelper : public nsIXPCScriptable
{
public:
  NS_DECL_ISUPPORTS
  NS_DECL_NSIXPCSCRIPTABLE

private:
  nsresult getParams(AsyncStatement *, JSContext *, JSObject *, jsval *);
};

} // namespace storage
} // namespace mozilla

#endif // mozilla_storage_mozStorageAsyncStatementJSHelper_h_
