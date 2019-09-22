#### snappy

Snappy 1.1.7 with error

```bash
/usr/bin/ld: CMakeFiles/snappy_unittest.dir/snappy_unittest.cc.o: in function `snappy::Snappy_ZeroOffsetCopy_Test::TestBody()':
snappy_unittest.cc:(.text+0x6477): undefined reference to `testing::Message::Message()'
/usr/bin/ld: snappy_unittest.cc:(.text+0x64a2): undefined reference to `testing::internal::GetBoolAssertionFailureMessage[abi:cxx11](testing::AssertionResult const&, char const*, char const*, char const*)'
/usr/bin/ld: snappy_unittest.cc:(.text+0x64d7): undefined reference to `testing::internal::AssertHelper::AssertHelper(testing::TestPartResult::Type, char const*, int, char const*)'
/usr/bin/ld: snappy_unittest.cc:(.text+0x64f0): undefined reference to `testing::internal::AssertHelper::operator=(testing::Message const&) const'
/usr/bin/ld: snappy_unittest.cc:(.text+0x64ff): undefined reference to `testing::internal::AssertHelper::~AssertHelper()'
/usr/bin/ld: snappy_unittest.cc:(.text+0x6550): undefined reference to `testing::internal::AssertHelper::~AssertHelper()'

```

- solution1 `https://github.com/google/snappy/pull/73`
- solution2 `-DSNAPPY_BUILD_TESTS=OFF`

#### folly

```bash
boost/crc.hpp: In member function ‘void boost::crc_basic<Bits>::process_bits(unsigned char, std::size_t)’:
boost/crc.hpp:759:1: error: declaration of ‘bit_count’ shadows a previous local [-Werror=shadow=compatible-local]
 )
 ^
In file included from boost/config.hpp:61,
                 from boost/crc.hpp:12,
                 from folly/hash/Checksum.cpp:18:
boost/crc.hpp:154:41: note: shadowed declaration is here
     BOOST_STATIC_CONSTANT( std::size_t, bit_count = Bits );
                                         ^~~~~~~~~
```

- issues https://github.com/facebook/folly/issues
- solution1 with boost 1.69.0 ? 1.68.0
- solution2 ignore it ?

#### fizz

1. Not find zlib.h
    for add `include_directories(${zlib_path})` to CmakeList.txt
2. zlib library not link
    add to CmakeList.txt
    `list(APPEND FIZZ_LINK_LIBRARIES /home/icecory/Cpp3rdlib/lib/libz.a)`
3. gflags not link

    ```cmake
    # delete in CmakeList.tx
    find_package(gflags CONFIG QUIET)
    if (gflags_FOUND)
      message(STATUS "Found gflags from package config")
      ...
    else()
    ```

#### m4

```bash
/m4_1.4.18/./lib/freadahead.c:92:3: error: #error "Please port gnulib freadahead.c to your platform! Look at the definition of fflush, fread, ungetc on your system, then report this to bug-gnulib."
  #error "Please port gnulib freadahead.c to your platform! Look at the definition of fflush, fread, ungetc on your system, then report this to bug-gnulib."
   ^~~~~
  CC       fseek.o
make[3]: *** [Makefile:1910: freadahead.o] Error 1
```

参考此处: https://bugzilla.redhat.com/show_bug.cgi?id=1573342
