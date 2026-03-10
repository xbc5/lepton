# lepton

My Qubes script framework. The scripts rely on configured values. The code bridges the gaps between domains.

## The global configuration file

This is the source of truth for how Lepton behaves.

There are two primary namespaces (sections):
```toml
[lepton.common...]
[lepton.mgmt...]
```

- "common": Non-sensitive information. Every domain has access to this.
- "mgmt": Potentially sensitive information. Only management domains have access to this.

Lepton will push the "common" section to configured templates on request.


```toml
[lepton.apps.terminal.default]
cmd = "alacritty" 
exec = "alacritty --command %s" 

[lepton.apps.terminal.graphics]
cmd = "kitty"
exec = "kitty --command %s"

[lepton.qubes.email.apps]
terminal = "default"

[lepton.common.templatevm]
# Used to communicate with the outside world via qrexec.
http_proxy = "http://127.0.0.1:8082" # Sends traffic to a remote HTTP endpoint.
https_proxy = "http://127.0.0.1:8082" # Sends traffic to a remote HTTPS endpoint.
```

### Key descriptions

A description of each key.

#### `lepton.apps`
Application profiles reused by other parts of the configuration.

| Key                                    | Description                                                 |
| -------------------------------------- | ----------------------------------------------------------- |
| `lepton`                               | Root namespace.                                             |
| `lepton.apps`                          | App configurations.                                         |
| `lepton.apps.<type>`                   | An arbitrary category of app.                               |
| `lepton.apps.<type>.<profile>`         | An arbitrary name that describes its use case.              |
| `lepton.apps.<type>.<profile>.cmd`     | The command to run.                                         |
| `lepton.apps.<type>.<profile>.exec`    | Execution template; any `%s` gets interpolated with args.   |

#### `lepton.qube`
Configuration values applied to each qube individually.

| Key                        | Description                                              |
| -------------------------- | -------------------------------------------------------- |
| `lepton.qube`             | Assign configuration values to each qube.                |
| `lepton.qube.<name>.apps` | Maps `lepton.apps.<type>.<profile>` to a specific qube. |

#### `lepton.common.templatevms`
Configuration values applied to all TemplateVMs.

| Key                                     | Description                                          |
| --------------------------------------- | ---------------------------------------------------- |
| `lepton.common`                         | Non-sensitive configuration shared with all domains. |
| `lepton.common.templatevms`             | Configuration values applied to all TemplateVMs.     |
| `lepton.common.templatevms.http_proxy`  | HTTP proxy URL.                                      |
| `lepton.common.templatevms.https_proxy` | HTTPS proxy URL.                                     |

#### `lepton.mgmt`
Sensitive configuration for management domains.

| Key            | Description                                     |
| -------------- | ----------------------------------------------- |
| `lepton.mgmt` | Sensitive configuration for management domains. |
