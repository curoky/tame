from cpm.recipes import add_cmake_recipe, GitOption

add_cmake_recipe(
    name="c-ares",
    git_options=GitOption(
        url="https://github.com/c-ares/c-ares",
    ),
    include_dirs=[
        '.',
    ],
    link_libraries=[
    ],
)