/*
 * Copyright 2021 curoky(cccuroky@gmail.com).
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once
#include <stdint.h>
/* evconfig-private.h template - see "Configuration Header Templates" */
/* in AC manual.  Kevin Bowling <kevin.bowling@kev009.com */

/* Enable extensions on AIX 3, Interix.  */
#ifndef _ALL_SOURCE
#undef _ALL_SOURCE
#endif
/* Enable GNU extensions on systems that have them.  */
#ifndef _GNU_SOURCE
#undef _GNU_SOURCE
#endif
/* Enable threading extensions on Solaris.  */
#ifndef _POSIX_PTHREAD_SEMANTICS
#undef _POSIX_PTHREAD_SEMANTICS
#endif
/* Enable extensions on HP NonStop.  */
#ifndef _TANDEM_SOURCE
#undef _TANDEM_SOURCE
#endif
/* Enable general extensions on Solaris.  */
#ifndef __EXTENSIONS__
#undef __EXTENSIONS__
#endif

/* Number of bits in a file offset, on hosts where this is settable. */
#undef _FILE_OFFSET_BITS
/* Define for large files, on AIX-style hosts. */
#undef _LARGE_FILES

/* Define to 1 if on MINIX. */
#ifndef _MINIX
#undef _MINIX
#endif

/* Define to 2 if the system does not provide POSIX.1 features except with
   this defined. */
#ifndef _POSIX_1_SOURCE
#undef _POSIX_1_SOURCE
#endif

/* Define to 1 if you need to in order for `stat' and other things to work. */
#ifndef _POSIX_SOURCE
#undef _POSIX_SOURCE
#endif

/* Enable POSIX.2 extensions on QNX for getopt */
#ifdef __QNX__
#ifndef __EXT_POSIX2
#define __EXT_POSIX2
#endif
#endif
