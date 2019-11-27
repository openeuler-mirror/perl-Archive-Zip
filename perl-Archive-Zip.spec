%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

Name:           perl-Archive-Zip
Version:        1.64
Release:        2
Summary:        Perl library for accessing Zip archives
License:        (GPL+ or Artistic) and BSD
URL:            https://metacpan.org/release/Archive-Zip
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/Archive-Zip-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  git-core make perl-interpreter perl-generators perl(:VERSION) >= 5.4
BuildRequires:  perl(Config) perl(ExtUtils::MakeMaker) >= 6.76 perl(strict)
BuildRequires:  perl(:VERSION) >= 5.6 perl(bytes) perl(Carp) perl(Compress::Raw::Zlib)
BuildRequires:  perl(constant) perl(Cwd) perl(Data::Dumper) perl(Encode) perl(Exporter)
BuildRequires:  perl(File::Basename) perl(File::Copy) perl(File::Find) perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.80 perl(File::Temp) perl(FileHandle) perl(integer)
BuildRequires:  perl(IO::File) perl(IO::Seekable) perl(Time::Local) perl(vars) perl(lib)
BuildRequires:  perl(File::Spec::Unix) perl(Test::MockModule) perl(Test::More) >= 0.88
BuildRequires:  perl(utf8) perl(warnings) unzip zip
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Exporter) perl(File::Spec) >= 0.80

%description
The Archive::Zip module allows a Perl program to create, manipulate, read, and write Zip archive files.
Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.
Members can be added, removed, extracted, replaced, rearranged, and enumerated.
They can also be renamed or have their dates, comments, or other attributes queried or modified.
Their data can be compressed or uncompressed as needed.
Members can be created from members in existing Zip files, or from existing directories, files, or strings.
This module uses the Compress::Raw::Zlib library to read and write the compressed streams inside the files.
One can use Archive::Zip::MemberRead to read the zip file archive members as if they were files.

%package        help
BuildArch:      noarch
Summary:        Help documents for perl-Archive-Zip

%description    help
The perl-Archive-Zip-help package conatins manual pages for perl-Archive-Zip.

%prep
%autosetup -n Archive-Zip-%{version} -p1 -S git
for F in examples/*.pl; do
    perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(q{$F})"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes examples/
%{_bindir}/crc32
%{perl_vendorlib}/Archive/

%files help
%{_mandir}/man3/Archive*.3*

%changelog
* Tue Nov 26 2019 liujing<liujing144@huawei.com> - 1.64-2
- Package init
