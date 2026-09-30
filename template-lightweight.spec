# Non-EPICS package template (scripts, config, a service) for the
# gemini-rtsw-ci pipeline. To reuse: rename this file, change Name, and set Version.

# $GIT_HASH is passed in by build_rpm.sh; git is only the fallback.
%define git_hash %(if [ -n "$GIT_HASH" ]; then echo "$GIT_HASH"; else git rev-parse --short HEAD 2>/dev/null || echo nogit; fi)

Name:      template-lightweight
Version:   0.1.0
Release:   1.git%{git_hash}%{?dist}
Summary:   Template non-EPICS package for the gemini-rtsw-ci pipeline
License:   Proprietary
Source0:   %{name}-%{version}.tar.gz
BuildArch: noarch

%description
A minimal non-EPICS package: one script and one config file.

%prep
%autosetup

%install
install -Dpm 0755 hello.sh %{buildroot}%{_bindir}/template-lightweight
install -Dpm 0644 template-lightweight.conf %{buildroot}%{_sysconfdir}/template-lightweight.conf

%files
%{_bindir}/template-lightweight
%config(noreplace) %{_sysconfdir}/template-lightweight.conf

%changelog
* Wed Sep 30 2026 Hawi Stecher <hawi.stecher@noirlab.edu> - 0.1.0-1
- Initial template.
