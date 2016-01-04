%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from fog-json-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-json

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 3%{?dist}
Summary: JSON parsing for fog providers
Group: Development/Languages
License: MIT
URL: http://github.com/fog/fog-json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(fog-core)
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ror}rubygem(multi_json)
BuildRequires: %{?scl_prefix_ror}rubygem(builder)
BuildArch: noarch

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ror}rubygem(multi_json) >= 1.0
Requires: %{?scl_prefix_ror}rubygem(multi_json) < 2
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Extraction of the JSON parsing tools shared between a number
of providers in the 'fog' gem.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite

%check
#pushd .%{gem_instdir}
#%{?scl:scl enable %{scl} - << \EOF}
#ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
#%{?scl:EOF}
#popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-json.gemspec
%{gem_instdir}/test

%changelog
* Thu Nov 27 2014 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- rebuilt

* Wed Nov 26 2014 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Initial vagrant1 scl build

* Fri May 23 2014 Vít Ondruch <vondruch@redhat.com> - 1.0.0-1
- Initial package
