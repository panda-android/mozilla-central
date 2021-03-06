dnl This Source Code Form is subject to the terms of the Mozilla Public
dnl License, v. 2.0. If a copy of the MPL was not distributed with this
dnl file, You can obtain one at http://mozilla.org/MPL/2.0/.

dnl Set MOZ_FRAMEPTR_FLAGS to the flags that should be used for enabling or
dnl disabling frame pointers in this architecture based on the configure
dnl options

AC_DEFUN([MOZ_SET_FRAMEPTR_FLAGS], [
  if test "$GNU_CC"; then
    MOZ_ENABLE_FRAME_PTR="-fno-omit-frame-pointer"
    MOZ_DISABLE_FRAME_PTR="-fomit-frame-pointer"
  else
    case "$target" in
    *-mingw*)
      MOZ_ENABLE_FRAME_PTR="-Oy-"
      MOZ_DISABLE_FRAME_PTR="-Oy"
    ;;
    esac
  fi

  # if we are debugging or profiling, we want a frame pointer.
  if test -z "$MOZ_OPTIMIZE" -o \
          -n "$MOZ_PROFILING" -o -n "$MOZ_DEBUG"; then
    MOZ_FRAMEPTR_FLAGS="$MOZ_ENABLE_FRAME_PTR"
  else
    MOZ_FRAMEPTR_FLAGS="$MOZ_DISABLE_FRAME_PTR"
  fi
])
