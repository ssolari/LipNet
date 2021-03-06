from setuptools import setup, find_packages

setup(name='lipnet',
    version='0.1.6',
    description='End-to-end sentence-level lipreading',
    url='http://github.com/rizkiarm/LipNet',
    author='Muhammad Rizki A.R.M',
    author_email='rizki@rizkiarm.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
	install_requires=[
        #'Keras==2.0.2',
        #'editdistance==0.5.2',
	#	'h5py==2.6.0',
	#	'matplotlib==2.0.0',
	#	'numpy==1.12.1',
	#	'python-dateutil==2.6.0',
	#	'scipy==0.19.0',
	#	'Pillow==4.1.0',
		#'tensorflow-gpu==1.0.1',
		#'tensorflow==1.0.0',  # non-gpu version
	#	'Theano==0.9.0',
        #'nltk==3.2.2',
        #'sk-video==1.1.10',
        # 'dlib==19.4.0'  # let conda handle dlib install
    ])
