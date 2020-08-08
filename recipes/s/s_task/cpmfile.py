from cpm.recipes import add_cmake_recipe, GitOption

add_cmake_recipe(
    name='s_task',
    git_options=GitOption(url='https://github.com/xhawk18/s_task',),
    include_dirs=[
        '.',
    ],
    link_libraries=[],
    cmake_path='build',
)
