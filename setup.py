from distutils.core import setup
setup(
  name = 'foreman-python-client',         # How you named your package folder (MyLib)
  packages = ['foreman-python-client'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A client made to manage Foreman resources via API',   # Give a short description about your library
  author = 'Juan Augusto',                   # Type in your name
  author_email = 'jotaugusto93@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/juanaugusto/foreman-python-client',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/juanaugusto/foreman-python-client/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['python', 'foreman', 'client'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests==2.22.0',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.x',      #Specify which pyhton versions that you want to support
  ],
)