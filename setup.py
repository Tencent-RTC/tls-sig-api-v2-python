# coding: utf-8
from setuptools import setup, find_packages

setup (
        name = 'tls-sig-api-v2',
        version = '1.1',
        description ='tls-sig-api-v2 Applicable to Tencent Cloud TRTC and CHAT services to generate user account signatures',
        long_description = "Applicable to the new version of key, the previous asymmetric key is not applicable, use the asymmetric key reference https://github.com/tencentcloud/tls-sig-api-python",
        author = 'weijunyi',
        author_email = 'weijunyi@tencent.com',
        license = 'MIT Licence',
        packages = find_packages(),
        py_modules = [
            'TLSSigAPIv2'
            ],
        install_requires = [],
        url = 'https://github.com/tencentcloud/tls-sig-api-v2-python',
        platforms = "any"
        )
