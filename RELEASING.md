# Releasing EMDB schemas

Use this checklist when releasing a new schema version. Set the version once
before running the release commands, for example:

```bash
export new_version="3.0.11.13"
```

In the manual edits below, `${new_version}` means the value of that shell
variable; write the expanded version number, not the literal `${new_version}`.

1. Start from an up-to-date `main` branch and check the working tree.

   ```bash
   git pull
   git status
   ```

2. Make the schema changes in both XSD files:

   ```text
   emdb_schemas/current/emdb.xsd
   emdb_schemas/current/emdb_relaxed.xsd
   ```

   Update the schema version in both files. The version is the default value
   of the `version` attribute on `entry_type`, near the top of each XSD:

   ```xml
   <xs:attribute name="version" type="xs:token" default="${new_version}"/>
   ```

   In `emdb_relaxed.xsd`, keep the existing formatting style:

   ```xml
   <xs:attribute name="version" type="xs:token" default="${new_version}" />
   ```

3. Generate both Python models using generateDS. Activate the environment that
   contains generateDS, if needed:

   ```bash
   conda activate emdb_schemas
   ```

   Then regenerate the strict and relaxed Python models from the XSD files:

   ```bash
   generateDS --root-element="emd" -f -o "emdb_schemas/current/emdb.py" --no-warnings --external-encoding="utf-8" emdb_schemas/current/emdb.xsd
   generateDS --root-element="emd" -f -o "emdb_schemas/current/emdb_relaxed.py" --no-warnings --external-encoding="utf-8" emdb_schemas/current/emdb_relaxed.xsd
   ```

4. Generate the schema documentation using Oxygen XML Editor. Use the XML
   Schema Documentation generator for `emdb_schemas/current/emdb.xsd` and
   write the output to `emdb_schemas/current/doc`. Overwrite the old generated
   documentation, then review the changes:

   ```bash
   git status --short emdb_schemas/current/doc
   ```

5. Add a line for the new version to the changelog in `README.md`:

   ```text
   ${new_version}: Summary of the schema changes.
   ```

6. Update the package version in `setup.py`, then check every active version
   reference agrees:

   ```bash
   grep -n "version='${new_version}'" setup.py
   grep -n "default=\"${new_version}\"" emdb_schemas/current/emdb.xsd
   grep -n "default=\"${new_version}\"" emdb_schemas/current/emdb_relaxed.xsd
   grep -n "${new_version}:" README.md
   ```

7. Commit the release changes and push `main`:

   ```bash
   git add README.md RELEASING.md setup.py emdb_schemas .github MANIFEST.in pyproject.toml LICENSE
   git commit -m "Update schema to v${new_version}"
   git push origin main
   ```

8. Create and push the version tag:

   ```bash
   git tag -a "v${new_version}" -m "EMDB schema v${new_version}"
   git push origin "v${new_version}"
   ```

Pushing the tag triggers the existing schema deployment workflow and the PyPI
publishing workflow. The PyPI workflow builds and tests the distributions,
then publishes using PyPI Trusted Publishing. The tag must match the version
in `setup.py`.
