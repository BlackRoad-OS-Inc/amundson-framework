# Fleet Verification Results
## March 25, 2026

5 independent sovereign nodes. Pure Python. Zero imports.

```
alice:     17/17 PASS | A_G=1.244331783986725 | kappa=0.244331783986725 | VERIFIED
lucidia:   17/17 PASS | A_G=1.244331783986725 | kappa=0.244331783986725 | VERIFIED
octavia:   17/17 PASS | A_G=1.244331783986725 | kappa=0.244331783986725 | VERIFIED
gematria:  17/17 PASS | A_G=1.244331783986725 | kappa=0.244331783986725 | VERIFIED
anastasia: 17/17 PASS | A_G=1.244331783986725 | kappa=0.244331783986725 | VERIFIED
```

| Node | Arch | OS |
|------|------|----|
| Alice | ARM64 | Raspbian 11 |
| Lucidia | ARM64 | Debian 12 |
| Octavia | ARM64 | Debian 13 |
| Gematria | x86_64 | Ubuntu 22.04 |
| Anastasia | x86_64 | CentOS 9 |

Reproduce: `python3 verify.py`
