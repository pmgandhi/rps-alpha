# hiera datadir

This directory is the data directory for hiera, as configured in `../hiera.yaml`.

Each file is named after the hostname of the machine it applies to, with the exception
of `common.yaml`, which is at the root of the hierarchy defined in `../hiera.yaml`, which
means the variables therein are applicable to all hosts.

For new files, please begin them with the standard YAML separator - `---`. All top-level
vars must be Ruby symbols, beginning with a colon - `:`. 

### Example

```yaml
---
:classes:
  - base_packages
  - awesome_app
:users:
  - ops
  - dev
  - backup
```
