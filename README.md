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
