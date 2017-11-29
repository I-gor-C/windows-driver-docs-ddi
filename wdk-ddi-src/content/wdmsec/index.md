# Wdmsec.h header


This header is used by Windows kernel. For more information, see
- [Windows kernel](../_kernel/index.md)

Wdmsec.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WdmlibIoCreateDeviceSecure function](nf-wdmsec-wdmlibiocreatedevicesecure.md) | The WdmlibIoCreateDeviceSecure function creates a named device object and applies the specified security settings. |
| [WdmlibIoValidateDeviceIoControlAccess function](nf-wdmsec-wdmlibiovalidatedeviceiocontrolaccess.md) | The WdmlibIoValidateDeviceIoControlAccess function verifies that the sender of an IRP_MJ_DEVICE_CONTROL or IRP_MJ_FILE_SYSTEM_CONTROL IRP has the specified access to the device object. |
| [WdmlibRtlInitUnicodeStringEx function](nf-wdmsec-wdmlibrtlinitunicodestringex.md) | The WdmlibRtlInitUnicodeStringEx function initializes a counted string of Unicode characters. |
