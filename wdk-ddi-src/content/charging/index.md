---
UID: NA:charging
ms.assetid: ea5ea45e-3345-3551-94ef-8fd0f279aa6b
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# charging.h header



charging.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_CAD_DISABLE_CHARGING](ni-charging-ioctl_cad_disable_charging.md) | This IOCTL is for internal use only. |
| [IOCTL_CAD_GET_BATTERY_PROVISIONING_STATUS](ni-charging-ioctl_cad_get_battery_provisioning_status.md) | This IOCTL is for internal use only. |
| [IOCTL_CAD_GET_CHARGING_STATUS_COMPLETE](ni-charging-ioctl_cad_get_charging_status_complete.md) | This IOCTL is for internal use only. |
| [IOCTL_CAD_POWER_SOURCE_UPDATE_EX](ni-charging-ioctl_cad_power_source_update_ex.md) | This IOCTL is for internal use only. |
| [IOCTL_INTERNAL_CAD_POWER_SOURCE_UPDATE](ni-charging-ioctl_internal_cad_power_source_update.md) | This IOCTL is for internal use only. |
| [IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY](ni-charging-ioctl_internal_configure_charger_property.md) | The IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY control code is sent from a configurable charger to a device that handles configurable chargers. It configures charger properties. |




## Structures
| Title | Description |
| ---- |:---- |
| [_BATTERYPROVISIONINGSTATUS](ns-charging-_batteryprovisioningstatus.md) | This structure is for internal use only. |
| [_CAD_POWER_SOURCE_INFO](ns-charging-_cad_power_source_info.md) | This structure is for internal use only. |
| [_CAD_POWER_SOURCE_INFO_USB](ns-charging-_cad_power_source_info_usb.md) | This structure is for internal use only. |
| [_CHARGINGSTATUSCOMPLETE](ns-charging-_chargingstatuscomplete.md) | This structure is for internal use only. |
| [_CONFIGURABLE_CHARGER_PROPERTY_HEADER](ns-charging-_configurable_charger_property_header.md) | The CONFIGURABLE_CHARGER_PROPERTY_HEADER structure is a header that is used to create your own structure as an input to IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY. |
| [_POWERSOURCESTATUS](ns-charging-_powersourcestatus.md) | This struct is for internal use only. |
| [_POWERSOURCEUPDATE](ns-charging-_powersourceupdate.md) | This structure is for internal use only. |
| [_POWERSOURCEUPDATEEX](ns-charging-_powersourceupdateex.md) | This structure is for internal use only. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_POWERSOURCEID](ne-charging-_powersourceid.md) | This enum is for internal use only. |