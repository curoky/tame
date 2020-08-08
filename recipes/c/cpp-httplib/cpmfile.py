from cpm.recipes import add_cmake_recipe, GitOption

add_cmake_recipe(
    name='cpp-httplib',
    git_options=GitOption(url='https://github.com/yhirose/cpp-httplib',),
    include_dirs=['.'],
    header_only=True,
)
