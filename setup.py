from setuptools import setup
setup(
        name = 'psnpricealert',
        packages = ['psnpricealert'],
        version = '1.0',
        description = 'An interface for the undocumented Sony PlayStation Store PSN Api',
        author = 'Matthias Kuech',
        author_email = 'halde@matthias-kuech.de',
        url = 'https://github.com/snipem/playstation-price-drop-alert',
        download_url = 'https://github.com/snipem/playstation-price-drop-alert/tarball/0.1',
        keywords = ['playstation', 'store', 'prices'],
        license = 'GPL2',
        classifiers = [],
        test_suite='nose.collector',
        tests_require=['nose'],
        entry_points = {
            'console_scripts': ['psncli=psnpricealert.psncli:main',
                                'psndealsmailalert=psnpricealert.psndealsmailalert:main',
                                'psnmailalert=psnpricealert.psnmailalert:main'],
        }
        )