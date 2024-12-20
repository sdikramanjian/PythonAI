## GitHub Copilot Chat

- Extension Version: 0.23.0 (prod)
- VS Code: vscode/1.96.0
- OS: Mac

## Network

User Settings:
```json
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 140.82.113.5 (31 ms)
- DNS ipv6 Lookup: ::ffff:140.82.113.5 (1 ms)
- Proxy URL: http://127.0.0.1:9000 (0 ms)
- Proxy Connection: 200 Connection Established
	proxy-agent: Zscaler/6.2 (20 ms)
- Electron fetch (configured): HTTP 200 (68 ms)
- Node.js https: HTTP 200 (130 ms)
- Node.js fetch: HTTP 200 (481 ms)
- Helix fetch: HTTP 200 (257 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.114.21 (1 ms)
- DNS ipv6 Lookup: ::ffff:140.82.114.21 (1 ms)
- Proxy URL: http://127.0.0.1:9000 (34 ms)
- Proxy Connection: 200 Connection Established
	proxy-agent: Zscaler/6.2 (19 ms)
- Electron fetch (configured): HTTP 403 (128 ms)
- Node.js https: HTTP 403 (56 ms)
- Node.js fetch: HTTP 403 (58 ms)
- Helix fetch: HTTP 403 (140 ms)

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).