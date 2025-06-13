# FortiGate CIS Benchmark Compliance Report

| CIS Benchmark Title | Compliance Status | Recommendations |
|---------------------|------------------|-----------------|
| 1.2 Ensure intra-zone traffic is not always allowed | Non-Compliant | Ensure only authorized traffic is allowed between networks in the same zone, configure to deny default. 【25:1†source】 |
| 1.3 Disable all management related services on WAN port | Non-Compliant | Disable unnecessary services (HTTPS, HTTP, SSH, SNMP, etc.) on the WAN port. 【25:2†source】 |
| 2.1.1 Ensure 'Pre-Login Banner' is set | Compliant | None |
| 2.1.2 Ensure 'Post-Login-Banner' is set | Non-Compliant | Configure the post-login banner message to inform users of policies regarding the system. 【25:3†source】 |
| 2.1.3 Ensure timezone is properly configured | Non-Compliant | Check and configure timezone correctly through GUI/CLI. 【25:4†source】 |
| 2.1.4 Ensure correct system time is configured through NTP | Non-Compliant | Set up NTP for time synchronization. 【25:5†source】 |
| 2.1.5 Ensure hostname is set | Compliant | None |
| 2.1.6 Ensure the latest firmware is installed | Non-Compliant | Ensure the latest firmware is installed from the Fortinet website. 【25:6†source】 |
| 2.1.7 Disable USB Firmware and configuration installation | Compliant | None |
| 2.1.8 Disable static keys for TLS | Non-Compliant | Disable static keys on TLS sessions. 【25:7†source】 |
| 2.1.9 Enable Global Strong Encryption | Compliant | None |
| 2.1.10 Ensure management GUI listens on secure TLS version | Non-Compliant | Ensure the GUI listens on secure TLS versions (TLS 1.2/1.3). 【25:8†source】 |
| 2.1.11 Ensure CDN is enabled for improved GUI performance | Non-Compliant | Enable CDN for GUI performance improvement. 【25:9†source】 |
| 2.1.12 Ensure single CPU core overloaded event is logged | Non-Compliant | Enable logging for single CPU core overload. 【25:10†source】 |
| 2.5.1 Ensure High Availability configuration is enabled | Compliant | None |
| 2.5.2 Ensure "Monitor Interfaces" for High Availability devices is | Non-Compliant | Validate all critical interfaces are selected for monitoring. 【25:11†source】 |
| 3.1 Ensure that unused policies are reviewed regularly | Non-Compliant | Review and disable unused firewall policies regularly. 【25:12†source】 |
| 4.2.1 Ensure Antivirus Definition Push Updates are Configured | Non-Compliant | Ensure automatic updates are enabled. 【25:13†source】 |
| 4.2.2 Apply Antivirus Security Profile to Policies | Non-Compliant | Review policies and apply antivirus profiles where necessary. 【25:14†source】 |
| 4.2.3 Enable Outbreak Prevention Database | Compliant | None |
| 4.2.4 Enable AI / heuristic based malware detection | Non-Compliant | Ensure AI-based detection is enabled. 【25:15†source】 |
| 4.2.5 Enable grayware detection on antivirus | Non-Compliant | Enable grayware detection in settings. 【25:16†source】 |
| 4.2.6 Ensure inline scanning with FortiGuard AI-Based Sandbox | Non-Compliant | Validate and configure inline scanning for traffic. 【25:17†source】 |
| 4.4.1 Ensure categorized blocked applications based on policy | Non-Compliant | Ensure application control policies are in place for high-risk categories. 【25:18†source】 |
| 5.1.1 Enable Compromised Host Quarantine | Non-Compliant | Enable automatic responses for compromised hosts. 【25:19†source】 |
| 6.1.1 Apply a Trusted Signed Certificate for VPN Portal | Non-Compliant | Import a signed certificate from a trusted CA for SSL VPN.   |
| 6.1.2 Enable Limited TLS Versions for SSL VPN | Non-Compliant | Validate only secure TLS versions for SSL VPN are enabled.   |
| 7.1.1 Enable Event Logging | Non-Compliant | Enable logging for security events for auditing.   |