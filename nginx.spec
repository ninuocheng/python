Name:		nginx
Version:	1.10
Release:	3
Summary:	NGINX is the fastest growing and highest performing software for modern web architectures.

Group:		mysoft
License:	GPLv2
URL:		http://nginx.org/
Source0:	nginx-%{version}.%{release}.tar.gz
Source1:	myconf.patch
Source2:	nginx.service
Source3:	conf.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%define		debug_package %{nil}
BuildRequires:	glibc gcc perl pkgconfig zlib-devel lua-devel pcre-devel openssl-devel nss-devel
Requires:	nss-tools nss-util bash lua pcre openssl
Packager:	luck
%description
	Nginx WWW services .

%prep
%setup -q -c -n nginx-1.10.3

%build
cd nginx-%{version}.%{release}
./configure --prefix=/usr/local/nginx \
--with-http_ssl_module --with-http_v2_module \
--with-http_realip_module --with-http_stub_status_module --with-pcre \
--without-mail_pop3_module --without-mail_imap_module --without-mail_smtp_module
make

%install
cd nginx-%{version}.%{release}
make DESTDIR=${RPM_BUILD_ROOT} install
cd %{buildroot}/usr/local/nginx
cp %{SOURCE1} %{buildroot}/usr/local/nginx/conf/
patch -p1 -i %{SOURCE3}
mkdir -p %{buildroot}/{usr/lib/systemd/system,var/log/weblog}
cp %{SOURCE2} %{buildroot}/usr/lib/systemd/system/

%clean
rm -rf %{buildroot} %{_builddir}

%files
%defattr(-,root,root,-)
/usr/local/nginx
/usr/lib/systemd/system/nginx.service
%defattr(-,web,web,0775)
/var/log/weblog

%pre
if  ! $(id web &>/dev/null);then
    groupadd -g 1000 web
    useradd -u 1000 -g 1000 web -s /sbin/nologin
fi

%post

%preun
systemctl stop nginx

%postun
rm -rf /var/cache/nginx

%changelog

