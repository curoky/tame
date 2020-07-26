from cpm.recipes import add_cmake_recipe, GitOption, CmakeOption

add_cmake_recipe(
    name="libcsptr",
    git_options=GitOption(
        url="https://github.com/Snaipe/libcsptr",
    ),
    include_dirs=[
        '.',
    ],
    link_libraries=[
    ],
    cmake_options=[
        CmakeOption(key='LIBCSPTR_TESTS', value='OFF'),
    ],
)
