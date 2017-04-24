# TC2017 Anti-Honeypot Demo

Scripts for vaccinating your PC against paranoid malware, as demonstrated on FIRST TC Amsterdam 2017.

This repository contains:
1. Scripts for vaccination
2. One of IRONGATE's components source code
3. A list of malware which will be prevented during the live demo

## Demo Samples 
 
### Andromeda\Gamarue Bot
periodically checks if any of the running processes are in a hardcoded anlysis related blacklist, if none are found it will create malicious child process - otherwise it will keep running and test later again which processes are running.
31f81b5e6854dfee0739c1f8266668622b13f36a5499d98809fcc04603ee7152

### IRONGATE - SCADA\ICS Targeted
Uveiled by Fireeye's researchers, see attached source if you wish to have a closer look at its VM detection function.
386ed16fece9cc24c4d123cdf91a371829098ba7abd4c8fefb40b4e376e7ac6a

### Locky Ransomware
Searches if specific AV vendor is installed by indicatiors in the Windows' registry
17c3d74e3c0645edb4b5145335b342d2929c92dff856cca1a5e79fa5d935fec2

### Spora Ransomware
Searches for a mutex and terminates if it detects it already exists
5ab9b586eaf1bcaa76443b4f69d67e57a057d57cb30b6d863a7cfab3d0882c2a

### TeslaCrypt Ransomware
Searches if specific AV vendor is installed by indicatiors in the Windows' registry
ca7cb56b9a254748e983929953df32f219905f96486d91390e8d5d641dc9916d

**Use at your own risk!** 
