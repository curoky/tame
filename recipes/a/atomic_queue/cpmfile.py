from cpm.recipes import add_cmake_recipe, GitOption

add_cmake_recipe(
    name="atomic_queue",
    git_options=GitOption(
        url="https://github.com/max0x7ba/atomic_queue",
    ),
    include_dirs=[
        '.',
    ],
    link_libraries=[
    ],
)