%define debug_package %{nil}
%define snapshot 20210123

Name:		doxypypy
Summary:	Doxygen filter for Python
Version:	0.0.1
Release:	%{?snapshot:0.%{snapshot}.}2
Group:		Development/Tools
Source0:	https://github.com/Feneric/doxypypy/archive/%{name}-master.tar.xz
License:	MIT
BuildRequires:	python
BuildRequires:	python-setuptools

%description
For now Doxygen has limited support for Python. It recognizes Python comments,
but otherwise treats the language as being more or less like Java. It doesn't
understand basic Python syntax constructs like docstrings, keyword arguments,
generators, nested functions, decorators, or lambda expressions.
It likewise doesn't understand conventional constructs like doctests or
ZOPE-style interfaces. It does however support inline filters that can be used
to make input source code a little more like what it's expecting.

The excellent doxypy makes it possible to embed Doxygen commands in Python
docstrings, and have those docstrings converted to Doxygen-recognized
comments on the fly per Doxygen's regular input filtering process. It however
does not address any of the other previously mentioned areas of difficulty.

This project started off as a fork of doxypy but quickly became quite distinct.
It shares little (if any) of the same code at this point (but maintains the
original license just in case). It is meant to support all the same command
line options as doxypy, but handle additional Python syntax beyond docstrings.

%prep
%autosetup -p1 -n %{name}-master

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/doxypypy
%{_prefix}/lib/python*/site-packages/doxypypy-*.egg-info
%{_prefix}/lib/python*/site-packages/doxypypy
