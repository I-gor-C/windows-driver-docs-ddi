# Charging.h header


This header is used by Battery. For more information, see
- [Battery](../_battery/index.md)

Charging.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [BATTERYPROVISIONINGSTATUS structure](ns-charging--batteryprovisioningstatus.md) | This structure is for internal use only. |
| [CAD_POWER_SOURCE_INFO structure](ns-charging--cad-power-source-info.md) | This structure is for internal use only. |
| [CAD_POWER_SOURCE_INFO_USB structure](ns-charging--cad-power-source-info-usb.md) | This structure is for internal use only. |
| [CHARGINGSTATUSCOMPLETE structure](ns-charging--chargingstatuscomplete.md) | This structure is for internal use only. |
| [CONFIGURABLE_CHARGER_PROPERTY_HEADER structure](ns-charging--configurable-charger-property-header.md) | The CONFIGURABLE_CHARGER_PROPERTY_HEADER structure is a header that is used to create your own structure as an input to IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY. |
| [POWERSOURCESTATUS structure](ns-charging--powersourcestatus.md) | This struct is for internal use only. |
| [POWERSOURCEUPDATE structure](ns-charging--powersourceupdate.md) | This structure is for internal use only. |
| [POWERSOURCEUPDATEEX structure](ns-charging--powersourceupdateex.md) | This structure is for internal use only. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY IOCTL](ni-charging-ioctl-internal-configure-charger-property.md) | The IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY control code is sent from a configurable charger to a device that handles configurable chargers. It configures charger properties. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [POWERSOURCEID enumeration](ne-charging--powersourceid.md) | This enum is for internal use only. |
