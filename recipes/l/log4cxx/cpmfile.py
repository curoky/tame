from cpm.recipes import add_cmake_recipe, GitOption

add_cmake_recipe(
    name="log4cxx",
    git_options=GitOption(
        url="https://github.com/apache/logging-log4cxx",
    ),
    include_dirs=[
        '.',
    ],
    link_libraries=[
    ],
)