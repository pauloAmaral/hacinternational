def get_assets_pipeline(is_debug=False):
    """
    Returns the assets files pipeline.

    If is_debug is True, pipeline is not enabled.
    """
    pipeline_enabled = not is_debug

    return {
        'PIPELINE_ENABLED': pipeline_enabled,
        'JAVASCRIPT': {
            # External libraries
            'jquery': {
                'source_filenames': (
                    'scripts/external/jquery/jquery-3.3.1.min.js',
                ),
                'output_filename': 'jquery.js',
            },
            'bootstrap': {
                'source_filenames': (
                    'scripts/external/bootstrap/bootstrap-4.3.1.min.js',
                ),
                'output_filename': 'bootstrap.js',
            },
            'main': {
                'source_filenames': (
                    'scripts/main.js',
                ),
                'output_filename': 'main.js',
            }
        },
        'STYLESHEETS': {
            'boostrap': {
                'source_filenames': (
                    'styles/external/boostrap/bootstrap-4.3.1.min.css',
                ),
                'output_filename': 'bootstrap.css',
            },
            'base': {
                'source_filenames': (
                    'styles/base.scss',
                ),
                'output_filename': 'base.css',
            },
            'pages-home': {
                'source_filenames': (
                    'styles/pages/home.scss',
                ),
                'output_filename': 'home.css',
            },
            'pages-about-us': {
                'source_filenames': (
                    'styles/pages/about_us.scss',
                ),
                'output_filename': 'about_us.css',
            },
            'pages-meet-the-team': {
                'source_filenames': (
                    'styles/pages/meet_the_team.scss',
                ),
                'output_filename': 'meet_the_team.css',
            },
            'pages-donate': {
                'source_filenames': (
                    'styles/pages/donate.scss',
                ),
                'output_filename': 'donate.css',
            },
        },
        'COMPILERS': (
            'pipeline.compilers.sass.SASSCompiler',
        ),
        'SASS_BINARY': '/usr/bin/sass',
    }
