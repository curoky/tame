# Jemalloc

## Build

At present, the official only supports using autotool to compile, cmake's compilation support is only promoted by individual developers, you can learn more details from the following discussion

- <https://github.com/jemalloc/jemalloc/issues/303>

Currently more reliable [fork](https://github.com/mattsta/jemalloc/commits/add/cmake-2019) are provided by [mattsta](https://github.com/mattsta), and mattsta provided detailed [instructions](https://github.com/jemalloc/jemalloc/issues/303#issuecomment-487329588), and then [leezu](https://github.com/leezu/) gives a patch on it, so we can use leezu's patched [fork](https://github.com/leezu/jemalloc/commits/add/cmake-2019).

### cmake-2019.patch

1. don't run test

   ```bash
   /usr/bin/ld: third_party/jemalloc/test/integration/CMakeFiles/jemalloc-test-smallocx.dir/smallocx.c.o: in function `purge':
   /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:70: undefined reference to `mallctl'
   /usr/bin/ld: third_party/jemalloc/test/integration/CMakeFiles/jemalloc-test-smallocx.dir/smallocx.c.o: in function `test_oom':
   /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:169: undefined reference to `smallocx_6e461dd46fdb4e350e642d8e9554264f26cfdbd0'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:172: undefined reference to `smallocx_6e461dd46fdb4e350e642d8e9554264f26cfdbd0'
   /usr/bin/ld: third_party/jemalloc/test/integration/CMakeFiles/jemalloc-test-smallocx.dir/smallocx.c.o: in function `test_basic':
   /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:195: undefined reference to `smallocx_6e461dd46fdb4e350e642d8e9554264f26cfdbd0'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:200: undefined reference to `sallocx'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:204: undefined reference to `dallocx'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:206: undefined reference to `smallocx_6e461dd46fdb4e350e642d8e9554264f26cfdbd0'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:211: undefined reference to `dallocx'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:213: undefined reference to `nallocx'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:216: undefined reference to `smallocx_6e461dd46fdb4e350e642d8e9554264f26cfdbd0'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:221: undefined reference to `sallocx'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:224: undefined reference to `dallocx'
   /usr/bin/ld: third_party/jemalloc/test/integration/CMakeFiles/jemalloc-test-smallocx.dir/smallocx.c.o: in function `purge':
   /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:70: undefined reference to `mallctl'
   /usr/bin/ld: third_party/jemalloc/test/integration/CMakeFiles/jemalloc-test-smallocx.dir/smallocx.c.o: in function `test_basic':
   /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:189: undefined reference to `nallocx'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/integration/smallocx.c:193: undefined reference to `nallocx'
   /usr/bin/ld: lib/libjemallocIntegrationTest.a(test.c.o): in function `p_test_impl':
   /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/src/test.c:138: undefined reference to `nallocx'
   /usr/bin/ld: /home/curoky/repos/taro/_build/../third_party/jemalloc/jemalloc/test/src/test.c:138: undefined reference to `nallocx'
   collect2: error: ld returned 1 exit status
   ```

2. remove `hash.c`, `prng.c`, `ticker.c` in `JEMALLOC_CMAKE_SOURCES`, because they were included twice.

   ```bash
   ninja: error: build.ninja:41212: multiple rules generate third_party/jemalloc/src/syms/hash.c.o.sym.jet [-w dupbuild=err]
   ```
