# template-lightweight

Minimal **non-EPICS** package (scripts, config files, a service) for the
[gemini-rtsw-ci](https://github.com/gemini-rtsw/gemini-rtsw-ci) pipeline.
It installs one script, `/usr/bin/template-lightweight`, and one config file,
`/etc/template-lightweight.conf`.

The pipeline needs two files: `.github/workflows/ci.yml` (with `profile: lightweight`)
and `template-lightweight.spec`. No EPICS, no rpm-repo dependencies: `BuildRequires`
resolve from the stock Rocky Linux repos.

## Use it for a new package

1. On GitHub, click **Use this template** → **Create a new repository**, then clone it
   with its submodule:
   ```bash
   git clone --recurse-submodules git@github.com:gemini-rtsw/<name>.git
   ```
   The `gemini-rtsw-ci` submodule comes with the copy; there is nothing to add.
2. Grant the new repo **Write** access to `rpm-repo`: org **Packages** → `rpm-repo` →
   **Package settings** → **Manage Actions access** → add the repo, role **Write**.
   This can only be done once the repo exists, so the build GitHub starts on the new
   repo's first commit fails here, harmlessly.
3. **Rename before you push to `main`**: `template-lightweight` in the spec file name
   and in `Name:`. The file name does not matter to CI -- it builds whatever `*.spec` it
   finds -- but `Name:` does: an unrenamed copy publishes a second
   `template-lightweight` RPM into the shared rpm-repo, where it competes with this
   template's own builds. Doing the rename on a branch with a PR is safe, since PR
   builds publish nothing.
4. Replace `hello.sh` and the `.conf` with your own files, and list them in
   `%install` and `%files`.

## Build locally

```bash
./gemini-rtsw-ci/build_rpm.sh --profile lightweight --el 9   # RPM lands in rpms/
```
