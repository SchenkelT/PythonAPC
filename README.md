# Python APC PDU manager

![GitHub last commit](https://img.shields.io/github/last-commit/SchenkelT/PythonAPC)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/SchenkelT/PythonAPC)

A Python script for retrieving APC PDU's statistics using SNMPv1

## Modules

* pysnmp

## Connecting to device

Enter ip, port en community name for the device you want te control

``` bash
Welkom to the APC Smart PDU control toolp
-----------------------------------------
Enter the APC PDU ip address:
Enter the APC PDU SNMP port:
Enter Cummunity name:
```

## Controling device

Control a APC PDU using a simple Python menu. Choose what you want to get and the script will get the info from the PDU.

```bash
APC Control options
--------------------
[1] Get device info
[2] Get current device load (Watts)
[3] Get current device load (Amp)
[4] Get device hostname
[5] Get device outlet status
```

## Gettings Help

Do you have a question, suggestion or anything else? [open a new issue on Github](https://github.com/SchenkelT/PythonAPC/issues)

## Contributing

Send a pull request or create an issue, to help the development of this application.
