---
UID: NA:
---

# Ufxproprietarycharger.h header

## -description

This header is used by UsbRef. For more information, see
- [UsbRef](../_UsbRef/index.md)

Ufxproprietarycharger.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [UFX_PROPRIETARY_CHARGER_ABORT_OPERATION callback](nc-ufxproprietarycharger-ufx_proprietary_charger_abort_operation.md) | The filter driver's implementation to abort a charger operation. |
| [UFX_PROPRIETARY_CHARGER_DETECT callback](nc-ufxproprietarycharger-ufx_proprietary_charger_detect.md) | The filter driver's implementation to detect if a charger is attached and get details about the charger. |
| [UFX_PROPRIETARY_CHARGER_RESET_OPERATION callback](nc-ufxproprietarycharger-ufx_proprietary_charger_reset_operation.md) | The filter driver's implementation to reset a charger operation. |
| [UFX_PROPRIETARY_CHARGER_SET_PROPERTY callback](nc-ufxproprietarycharger-ufx_proprietary_charger_set_property.md) | The filter driver's implementation to set a configurable property on the charger. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_UFX_INTERFACE_PROPRIETARY_CHARGER structure](ns-ufxproprietarycharger-_ufx_interface_proprietary_charger.md) | Stores pointers to driver-implemented callback functions for handling proprietary charger operations. |
| [_UFX_PROPRIETARY_CHARGER structure](ns-ufxproprietarycharger-_ufx_proprietary_charger.md) | Describes the proprietary charger's device power requirements. |
