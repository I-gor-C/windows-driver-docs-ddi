---
UID : NA:ufxproprietarycharger
ms.assetid : d02b3696-a339-37ca-89b4-4a16b2ccf5c4
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# ufxproprietarycharger.h header



ufxproprietarycharger.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [UFX_PROPRIETARY_CHARGER_ABORT_OPERATION](nc-ufxproprietarycharger-ufx_proprietary_charger_abort_operation.md) | The filter driver's implementation to abort a charger operation. |
| [UFX_PROPRIETARY_CHARGER_DETECT](nc-ufxproprietarycharger-ufx_proprietary_charger_detect.md) | The filter driver's implementation to detect if a charger is attached and get details about the charger. |
| [UFX_PROPRIETARY_CHARGER_RESET_OPERATION](nc-ufxproprietarycharger-ufx_proprietary_charger_reset_operation.md) | The filter driver's implementation to reset a charger operation. |
| [UFX_PROPRIETARY_CHARGER_SET_PROPERTY](nc-ufxproprietarycharger-ufx_proprietary_charger_set_property.md) | The filter driver's implementation to set a configurable property on the charger. |



## Structures
| Title | Description |
| ---- |:---- |
| [_UFX_INTERFACE_PROPRIETARY_CHARGER](ns-ufxproprietarycharger-_ufx_interface_proprietary_charger.md) | Stores pointers to driver-implemented callback functions for handling proprietary charger operations. |
| [_UFX_PROPRIETARY_CHARGER](ns-ufxproprietarycharger-_ufx_proprietary_charger.md) | Describes the proprietary charger's device power requirements. |