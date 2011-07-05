An Introduction to Bayesian Statistical Modeling using PyMC
===========================================================

PyMC is a Python module that implements Bayesian statistical models and fitting algorithms, including Markov chain Monte Carlo. Its flexibility and extensibility make it applicable to a large suite of problems across all quantitative disciplines. This hands-on tutorial will introduce users to the key components of PyMC and how to employ them to construct, fit and diagnose models. Though some familiarity with statistics is assumed, the tutorial will begin with a brief overview of Bayesian inference, including an introduction to Markov chain Monte Carlo.

Installing PyMC
---------------

PyMC is known to run on Mac OS X, Linux and Windows, but in theory should be
able to work on just about any platform for which Python, a Fortran compiler
and the NumPy module are  available. However, installing some extra
depencies can greatly improve PyMC's performance and versatility.
The following describes the required and optional dependencies and takes you
through the installation process.

Dependencies
------------

PyMC requires some prerequisite packages to be present on the system.
Fortunately, there are currently only a few dependencies, and all are
freely available online.

* `Python`_ version 2.5 or 2.6.

* `NumPy`_ (1.4 or newer): The fundamental scientific programming package, it provides a
  multidimensional array type and many useful functions for numerical analysis.

* `Matplotlib (optional)`_ : 2D plotting library which produces publication
  quality figures in a variety of image formats and interactive environments

* `pyTables (optional)`_ : Package for managing hierarchical datasets and
  designed to efficiently and easily cope with extremely large amounts of data.
  Requires the `HDF5`_ library.

* `pydot (optional)`_ : Python interface to Graphviz's Dot language, it allows
  PyMC to create both directed and non-directed graphical representations of models.
  Requires the `Graphviz`_ library.

* `SciPy (optional)`_ : Library of algorithms for mathematics, science
  and engineering.

* `IPython (optional)`_ : An enhanced interactive Python shell and an
  architecture for interactive parallel computing.

* `nose (optional)`_ : A test discovery-based unittest extension (required
  to run the test suite).


There are prebuilt distributions that include all required dependencies. For
Mac OS X users, we recommend the `MacPython`_ distribution or the
`Enthought Python Distribution`_ on OS X 10.5 (Leopard) and Python 2.6.1 that 
ships with OS X 10.6 (Snow Leopard). Windows users should download and install the
`Enthought Python Distribution`_. The Enthought Python Distribution comes
bundled with these prerequisites. Note that depending on the currency of these
distributions, some packages may need to be updated manually.

For Mac OS X 10.6 (Leopard) users, a script for installing all the key dependencies, as well as a recent build of PyMC, can be downloaded from the `SciPy Superpack page`_.

If instead of installing the prebuilt binaries you prefer (or have) to build
``pymc`` yourself, make sure you have a Fortran and a C compiler. There are free
compilers (gfortran, gcc) available on all platforms. Other compilers have not been
tested with PyMC but may work nonetheless.


.. _`Python`: http://www.python.org/.

.. _`NumPy`: http://www.scipy.org/NumPy

.. _`Matplotlib (optional)`: http://matplotlib.sourceforge.net/

.. _`MacPython`: http://www.activestate.com/Products/ActivePython/

.. _`Enthought Python Distribution`: http://www.enthought.com/products/epddownload.php

.. _`SciPy (optional)`: http://www.scipy.org/

.. _`IPython (optional)`: http://ipython.scipy.org/

.. _`pyTables (optional)`: http://www.pytables.org/moin

.. _`HDF5`: http://www.hdfgroup.org/HDF5/

.. _`pydot (optional)`: http://code.google.com/p/pydot/

.. _`Graphviz`: http://www.graphviz.org/

.. _`nose (optional)`: http://somethingaboutorange.com/mrl/projects/nose/

.. _`SciPy Superpack page`: http://http://stronginference.com/scipy-superpack/

Compiling the source code
-------------------------

You can check out the latest development source of the code from `GitHub`_
repository::

    git clone git://github.com/pymc-devs/pymc.git pymc

Then move into the ``pymc`` directory and follow the platform specific instructions.

Though this code is technically development source, it contains important bug fixes and features absent from the previous release (2.1) and is relatively stable. Hence, we recommend using the latest development code if possible. A new release is in the works, but will not be complete prior to SciPy 2011.

Windows
~~~~~~~

One way to compile PyMC on Windows is to install `MinGW`_ and `MSYS`_. MinGW is
the GNU Compiler Collection (GCC) augmented with Windows specific headers and
libraries. MSYS is a POSIX-like console (bash) with UNIX command line tools.
Download the `Automated MinGW Installer`_ and double-click on it to launch
the installation process. You will be asked to select which
components are to be installed: make sure the g77 compiler is selected and
proceed with the instructions. Then download and install `MSYS-1.0.exe`_,
launch it and again follow the on-screen instructions.

Once this is done, launch the MSYS console, change into the PyMC directory and
type::

    python setup.py install

This will build the C and Fortran extension and copy the libraries and python
modules in the C:/Python26/Lib/site-packages/pymc directory.

.. _`GitHub`: http://github.com

.. _`MinGW`: http://www.mingw.org/

.. _`MSYS`: http://www.mingw.org/wiki/MSYS

.. _`Automated MinGW Installer`: http://sourceforge.net/projects/mingw/files/

.. _`MSYS-1.0.exe`: http://downloads.sourceforge.net/mingw/MSYS-1.0.11.exe


Mac OS X or Linux
~~~~~~~~~~~~~~~~~

In a terminal, type::

    python setup.py config_fc --fcompiler gnu95 build
    python setup.py install

The above syntax also assumes that you have gFortran installed and available. The 
`sudo` command may be required to install PyMC into the Python ``site-packages``
directory if it has restricted privileges.

In addition, the python2.6-dev package may be required to install PyMC on Linux systems. On Ubuntu or Debian, we have had success by installing the following prior to building PyMC::

    sudo apt-get install ipython python-setuptools python-dev python-nose
    python-tk python-numpy python-matplotlib python-scipy python-networkx   
    gfortran libatlas-base-dev


Running the test suite
----------------------

``pymc`` comes with a set of tests that verify that the critical components
of the code work as expected. To run these tests, users must have `nose`_
installed. The tests are launched from a python shell::

    import pymc
    pymc.test()

In case of failures, messages detailing the nature of these failures will
appear. In case this happens (it shouldn't), please report
the problems on the `issue tracker`_ 
specifying the version you are using and the environment.

.. _`nose`: http://somethingaboutorange.com/mrl/projects/nose/

.. _`issue tracker`: http://github.com/pymc-devs/pymc/issues