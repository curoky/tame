from cpm.recipes import add_cmake_recipe, GitOption, CmakeOption

add_cmake_recipe(
    name='clickhouse',
    git_options=GitOption(url='https://github.com/ClickHouse/ClickHouse',),
    include_dirs=[
        'src',
    ],
    link_libraries=[],
    cmake_options=[
        CmakeOption(key='ENABLE_TESTS', value='OFF'),
    ],
)
