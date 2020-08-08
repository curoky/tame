from cpm.recipes import add_cmake_recipe, GitOption

add_cmake_recipe(
    name='readerwriterqueue',
    git_options=GitOption(url='https://github.com/cameron314/readerwriterqueue',),
    include_dirs=['.'],
    header_only=True,
)
