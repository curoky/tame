from cpm.recipes import add_cmake_recipe, GitOption, CmakeOption

add_cmake_recipe(
    name="sandboxed-api",
    git_options=GitOption(
        url="https://github.com/google/sandboxed-api",
    ),
    include_dirs=[
        '.',
    ],
    link_libraries=[
    ],
)
