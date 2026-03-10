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

A description of each key. The `required` field is relative to its parent. For example, `lepton` is always required, but `lepton.apps` is not. However, if you create a `lepton.app`, you MUST specify a `lepton.apps.type`.

#### `lepton.apps`
Application profiles reused by other parts of the configuration.

| Key                                        | Required | Description                                          |
| ------------------------------------------ | -------- | ---------------------------------------------------- |
| `lepton`                                   | Yes      | Root namespace.                                      |
| `lepton.apps`                              | No      | App configurations.         |
| `lepton.apps.<type>`                       | Yes      | An arbitrary category of app.            |
| `lepton.apps.<type>.<profile>`         | Yes      | An arbitrary name that describes its use case.                                 |
| `lepton.apps.<type>.<profile>.cmd`         | Yes      | The command to run.                                  |
| `lepton.apps.<type>.<profile>.exec`        | No      | Execution template; any `%s` gets interpolated with args.  |

#### `lepton.qube`
Configuration values applied to each qube individually.
| Key                                        | Required | Description                                          |
| ------------------------------------------ | -------- | ---------------------------------------------------- |
| `lepton.qube`                             | No      | Assign configuration values to each qube.                                |
| `lepton.qube.<name>.apps`                 | Yes      | Maps `lepton.apps.<type>.<profile>` to a specific qube.            |

#### `lepton.common.templatevms`
Configuration values applied to all TemplateVMs.
| Key                                        | Required | Description                                          |
| ------------------------------------------ | -------- | ---------------------------------------------------- |
| `lepton.common`                            | No       | Non-sensitive configuration shared with all domains. |
| `lepton.common.templatevms`                 | No       | Configuration values applied to all TemplateVMs.               |
| `lepton.common.templatevms.http_proxy`      | Yes      | HTTP proxy URL.                                      |
| `lepton.common.templatevms.https_proxy`     | Yes      | HTTPS proxy URL.                                     |
#### `lepton.mgmt`
Sensitive configuration for management domains.
| Key                                        | Required | Description                                          |
| ------------------------------------------ | -------- | ---------------------------------------------------- |
| `lepton.mgmt`                              | No       | Sensitive configuration for management domains.      |
