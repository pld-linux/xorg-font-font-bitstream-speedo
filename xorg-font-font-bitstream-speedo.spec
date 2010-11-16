Summary:	Bitstream Speedo fonts
Summary(pl.UTF-8):	Fonty Speedo Bitstream
Name:		xorg-font-font-bitstream-speedo
Version:	1.0.2
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-bitstream-speedo-%{version}.tar.bz2
# Source0-md5:	13f6f107be164cfbf6be40d35ecf0c0f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.3
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Speedo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bitstream Charter and Courier fonts in Speedo format.

%description -l pl.UTF-8
Fonty Bitstream Charter i Courier w formacie Speedo.

%prep
%setup -q -n font-bitstream-speedo-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--with-fontdir=%{_fontsdir}/Speedo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc COPYING ChangeLog README
%{_fontsdir}/Speedo/font*.spd
%{_fontsdir}/Speedo/fonts.scale.bitstream
