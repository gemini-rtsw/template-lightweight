# template-lightweight

Minimal **non-EPICS** package (scripts, config files, a service) for the
[gemini-rtsw-ci](https://github.com/gemini-rtsw/gemini-rtsw-ci) pipeline.
It installs one script, `/usr/bin/template-lightweight`, and one config file,
`/etc/template-lightweight.conf`.

The pipeline needs two files: `.github/workflows/ci.yml` (with `profile: lightweight`)
and `template-lightweight.spec`. No EPICS, no rpm-repo dependencies: `BuildRequires`
resolve from the stock Rocky Linux repos.

## Use it for a new package

1. On GitHub, click **Use this template** → **Create a new repository**.
2. Within a minute, the **Template cleanup** workflow (Actions tab) renames everything
   called `template-lightweight` after your repo — file names, the spec's name, and their
   contents — and commits it as `Rename template-lightweight to <repo>`. Clone after that,
   or `git pull` if you already had:
   ```bash
   git clone --recurse-submodules git@github.com:gemini-rtsw/<name>.git
   ```
   The `gemini-rtsw-ci` submodule comes with the copy; there is nothing to add.
3. Grant the new repo **Write** access to `rpm-repo`: org **Packages** → `rpm-repo` →
   **Package settings** → **Manage Actions access** → add the repo, role **Write**.
   This can only be done once the repo exists, so the **Build** run GitHub starts on
   the first commit fails at the rpm-repo push, harmlessly. **Do not re-run it** after
   granting: it builds the template as it was before the rename, and would publish a
   second `template-lightweight` RPM. Push a commit or open a PR instead.
4. Replace `hello.sh` and the `.conf` with your own files, and list them in
   `%install` and `%files`.

The RPM may be named differently from the repo (`hrwfs` for `hrwfs_dm`, say): change
`Name:` in the spec, and rename the files named after it with it.

**If the cleanup did not run** (an org that keeps `GITHUB_TOKEN` read-only, say), rename
by hand before pushing to `main`: the spec file name and `Name:`, the `.conf` file name, and the paths in `%install`/`%files`. CI finds the spec by `*.spec`, so its file
name does not matter to the build, but `Name:` does — an unrenamed copy publishes a
second `template-lightweight` RPM into the shared rpm-repo. Doing it in a PR is safe, since PR builds
publish nothing.

## Build locally

```bash
./gemini-rtsw-ci/build_rpm.sh --profile lightweight --el 9   # RPM lands in rpms/
```
