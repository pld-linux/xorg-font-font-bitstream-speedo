Summary:	bitstream-speedo font
Summary(pl.UTF-8):	Font bitstream-speedo
Name:		xorg-font-font-bitstream-speedo
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/font/font-bitstream-speedo-%{version}.tar.bz2
# Source0-md5:	1399dc18aeb9571b0951d9570ea1059d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Speedo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bitstream-speedo font.

%description -l pl.UTF-8
Font bitstream-speedo.

%prep
%setup -q -n font-bitstream-speedo-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/Speedo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm
cd $RPM_BUILD_ROOT%{_fontsdir}/Speedo
sed -e '1d' fonts.scale > fonts.scale.bitstream
rm -f fonts.scale fonts.dir fonts.cache-1

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Speedo

%postun
fontpostinst Speedo

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/Speedo/*.spd
%{_fontsdir}/Speedo/fonts.scale.bitstream
