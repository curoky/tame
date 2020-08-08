from cpm.recipes import add_cmake_recipe, GitOption, CmakeOption

add_cmake_recipe(
    name="libzmq",
    git_options=GitOption(
        url="https://github.com/zeromq/libzmq",
    ),
    include_dirs=[
        "include",
    ],
    link_libraries=[
    ],
    cmake_options=[
        CmakeOption(key='WITH_DOCS', value='OFF'),
        CmakeOption(key='ZMQ_BUILD_TESTS', value='OFF'),
        CmakeOption(key='BUILD_TESTS', value='OFF'),
    ]
)
