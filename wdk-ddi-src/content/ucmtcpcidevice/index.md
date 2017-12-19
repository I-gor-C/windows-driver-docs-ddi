---
UID: NA:
---

# Ucmtcpcidevice.h header

## -description

This header is used by UsbRef. For more information, see
- [UsbRef](../_UsbRef/index.md)

Ucmtcpcidevice.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UCMTCPCI_DEVICE_CONFIG_INIT function](nf-ucmtcpcidevice-ucmtcpci_device_config_init.md) | Initializes the UCMTCPCI_DEVICE_CONFIG structure. |
| [UcmTcpciDeviceInitInitialize function](nf-ucmtcpcidevice-ucmtcpcideviceinitinitialize.md) | Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
| [UcmTcpciDeviceInitialize function](nf-ucmtcpcidevice-ucmtcpcideviceinitialize.md) | Initializes the USB Type-C Port Controller Interface framework extension (UcmTcpciCx). |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_UCMTCPCI_DEVICE_CONFIG structure](ns-ucmtcpcidevice-_ucmtcpci_device_config.md) | Used in the client driver's call to UcmTcpciDeviceInitialize. Call UCMTCPCI_DEVICE_CONFIG_INIT to initialize this structure. |
