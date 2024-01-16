# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test'
copyright = '2024, Brendan Wallace'
author = 'Brendan Wallace'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_panels",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Home'
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "external_links": [
        {"name":"CV","url":"https://youtube.com"},
        {"name":"Google Scholar","url":"https://scholar.google.com/citations?hl=en&user=vaf38NgAAAAJ&view_op=list_works&sortby=pubdate"},
    ],
    "github_url": "https://github.com/bc-wallace/",
}
html_sidebars = {
    "index": ['sidebar'],
    "about": ['sidebar'],
    "research": ['research_sidebar'],
    "MR*": ['research_sidebar'],

}
html_static_path = ['_static']

# If you used the blog file path in part one you do not need to set this value, however if you change it,
# this should be set to the same value.
# blog_path = "posts"

# blog_feed_fulltext: Choose to display full text in blog feeds.
blog_feed_fulltext = True

# Glob pattern that grabs all posts so you don't need to specify which posts are blog posts in each post
# This pattern facilitates a folder structure such as posts/2020/my-awesome-post.rst
blog_post_pattern = "posts/*/*"

# post_redirect_refresh: Number of seconds (default is 5) that a redirect page waits before refreshing the page
# to redirect to the post.
post_redirect_refresh = 1

# post_auto_image: Index of the image that will be displayed in the excerpt of the post. Default is 0, meaning no
# image. Setting this to 1 will include the first image
post_auto_image = 1

# post_auto_excerpt: Number of paragraphs (default is 1) that will be displayed as an excerpt from the post. Setting
# this 0 will result in displaying no post excerpt in archive pages.
post_auto_excerpt = 3


def setup(app):
    app.add_css_file("custom.css")