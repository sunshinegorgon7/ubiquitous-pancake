# FortiGate CIS Benchmark Compliance Report

| CIS Benchmark Title | Compliance Status | Recommendations |
|---------------------|------------------|-----------------|
| 1.1 Ensure DNS server is configured | Compliant | None |
| 1.2 Ensure intra-zone traffic is not always allowed | Non-Compliant | Ensure that only specific authorized traffic is allowed between networks in the same zone and configure it to deny by default. |
| 1.3 Disable all management related services on WAN port | Non-Compliant | Review WAN interface settings and disable any unnecessary services such as HTTPS, HTTP, SSH, SNMP, and Radius. |
| 2.1.1 Ensure 'Pre-Login Banner' is set | Compliant | None |
| 2.1.2 Ensure 'Post-Login-Banner' is set | Non-Compliant | Configure the post-login banner message to inform users of policies regarding the system. |
| 2.1.3 Ensure timezone is properly configured | Compliant | None |
| 2.1.4 Ensure correct system time is configured through NTP | Non-Compliant | Configure the device to synchronize time with a reliable NTP server. |
| 2.1.5 Ensure hostname is set | Compliant | None |
| 2.1.6 Ensure the latest firmware is installed | Non-Compliant | Verify against Fortinet's website that the latest firmware version is installed. |
| 2.1.7 Disable USB Firmware and configuration installation | Compliant | None |
| 2.1.8 Disable static keys for TLS | Non-Compliant | Disable support for static keys on TLS sessions by configuring the system appropriately. |
| 2.1.9 Enable Global Strong Encryption | Compliant | None |
| 2.1.10 Ensure management GUI listens on secure TLS version | Compliant | None |
| 2.1.11 Ensure CDN is enabled for improved GUI performance | Non-Compliant | Enable CDN for enhanced performance when accessing the management GUI. |
| 2.1.12 Ensure single CPU core overloaded event is logged | Non-Compliant | Enable logging for single CPU core overload event to monitor performance. |
| 2.5.1 Ensure High Availability configuration is enabled | Compliant | None |
| 2.5.2 Ensure "Monitor Interfaces" for High Availability devices is | Non-Compliant | Validate and select all applicable interfaces for monitoring in HA settings. |
| 2.5.3 Ensure HA Reserved Management Interface is configured | Non-Compliant | Validate that management interface reservations are set correctly. |
| 3.1 Ensure that unused policies are reviewed regularly | Non-Compliant | Review firewall policies regularly for relevance and disable any that are unused. |
| 4.2.1 Ensure Antivirus Definition Push Updates are Configured | Non-Compliant | Ensure that automatic antivirus updates are enabled in the settings. |
| 4.2.2 Apply Antivirus Security Profile to Policies | Non-Compliant | Review policies and ensure that the appropriate antivirus profiles are applied where necessary. |
| 4.2.3 Enable Outbreak Prevention Database | Compliant | None |
| 4.2.4 Enable AI /heuristic based malware detection | Non-Compliant | Validate that AI-based malware detection is enabled in the antivirus settings. |
| 4.2.5 Enable grayware detection on antivirus | Non-Compliant | Enable grayware detection within antivirus settings. |
| 4.2.6 Ensure inline scanning with FortiGuard AI-Based Sandbox | Non-Compliant | Validate and configure inline scanning for traffic. |
| 4.3.1 Enable Botnet C&C Domain Blocking DNS Filter | Non-Compliant | Enable domain filtering features to block botnet domains. |
| 4.4.1 Ensure categorized blocked applications based on policy | Non-Compliant | Ensure that application control policies are in place that block high-risk categories. |
| 5.1.1 Enable Compromised Host Quarantine | Non-Compliant | Configure to enable automated responses for compromised hosts in the network settings. |
| 6.1.1 Apply a Trusted Signed Certificate for VPN Portal | Non-Compliant | Import a signed certificate from a trusted CA for the SSL VPN portal. |
| 6.1.2 Enable Limited TLS Versions for SSL VPN | Non-Compliant | Ensure only secure TLS versions are enabled for SSL VPN connections. |
| 7.1.1 Enable Event Logging | Non-Compliant | Enable event logging for security events to ensure sufficient logging for audits. 
