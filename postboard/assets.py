"""Create and bundle CSS and JS files."""
from flask_assets import Environment, Bundle


def compile_static_assets(app):
    """Configure static asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundles
    account_less_bundle = Bundle(
        'src/less/account.less',
        filters='less,cssmin',
        output=f'dist/css/account.css',
        extra={'rel': 'stylesheet/less'}
    )
    add_article_less_bundle = Bundle(
        'src/less/add_article.less',
        filters='less,cssmin',
        output=f'dist/css/add_article.css',
        extra={'rel': 'stylesheet/less'}
    )
    table_less_bundle = Bundle(
        'src/less/table.less',
        filters='less,cssmin',
        output=f'dist/css/table.css',
        extra={'rel': 'stylesheet/less'}
    )
    # JavaScript Bundle
    js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )
    # Register assets
    assets.register('account_less_bundle', account_less_bundle)
    assets.register('add_article_less_bundle', add_article_less_bundle)
    assets.register('table_less_bundle', table_less_bundle)
    assets.register('js_all', js_bundle)
    # Build assets
    account_less_bundle.build()
    add_article_less_bundle.build()
    table_less_bundle.build()
    js_bundle.build()
