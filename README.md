# template-lightweight

Minimal **non-EPICS** package (scripts, config files, a service) for the
[gemini-rtsw-ci](https://github.com/gemini-rtsw/gemini-rtsw-ci) pipeline.
It installs one script, `/usr/bin/template-lightweight`, and one config file,
`/etc/template-lightweight.conf`.

The pipeline needs two files: `.github/workflows/ci.yml` (with `profile: lightweight`)
and `template-lightweight.spec`. No EPICS, no rpm-repo dependencies: `BuildRequires`
resolve from the stock Rocky Linux repos.

## Use it for a new package

1. Copy this repo, then rename `template-lightweight` in the spec file name and in `Name:`.
2. Replace `hello.sh` and the `.conf` with your own files, and list them in
   `%install` and `%files`.
3. Add the submodule and grant the repo **Write** access to `rpm-repo`, as
   described in the gemini-rtsw-ci README ("Start a new repo").

## Build locally

```bash
./gemini-rtsw-ci/build_rpm.sh --profile lightweight --el 9   # RPM lands in rpms/
```
