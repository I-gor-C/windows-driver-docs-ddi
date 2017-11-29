# Battery

Overview of the Battery technology.

To develop Battery, you need these headers:

 * [charging.h](..\charging\index.md)
 * [upssvc.h](..\upssvc\index.md)

For the programming guide, see [Battery](https://docs.microsoft.com/en-us/windows-hardware/drivers/battery).

## Functions

| Title   | Description   |
| ---- |:---- |
| [UPSCancelWait function](..\upssvc\nf-upssvc-upscancelwait.md) | The UPSCancelWait function cancels all waits initiated by calls to UPSWaitForStateChange. |
| [UPSGetState function](..\upssvc\nf-upssvc-upsgetstate.md) | The UPSGetState function returns the operational state of the UPS. |
| [UPSInit function](..\upssvc\nf-upssvc-upsinit.md) | The UPSInit function initializes a UPS minidriver, opens communication to the UPS unit, updates the registry, and causes the minidriver to start monitoring the UPS unit. |
| [UPSStop function](..\upssvc\nf-upssvc-upsstop.md) | The UPSStop function causes a UPS minidriver to stop monitoring its UPS unit. |
| [UPSTurnOff function](..\upssvc\nf-upssvc-upsturnoff.md) | The UPSTurnOff function turns off the UPS unit's power outlets, after a specified delay time. |
| [UPSWaitForStateChange function](..\upssvc\nf-upssvc-upswaitforstatechange.md) | The UPSWaitForStateChange function waits until a specified UPS state changes, or until a time-out interval elapses. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [BATTERYPROVISIONINGSTATUS structure](..\charging\ns-charging--batteryprovisioningstatus.md) | This structure is for internal use only. |
| [CAD_POWER_SOURCE_INFO structure](..\charging\ns-charging--cad-power-source-info.md) | This structure is for internal use only. |
| [CAD_POWER_SOURCE_INFO_USB structure](..\charging\ns-charging--cad-power-source-info-usb.md) | This structure is for internal use only. |
| [CHARGINGSTATUSCOMPLETE structure](..\charging\ns-charging--chargingstatuscomplete.md) | This structure is for internal use only. |
| [CONFIGURABLE_CHARGER_PROPERTY_HEADER structure](..\charging\ns-charging--configurable-charger-property-header.md) | The CONFIGURABLE_CHARGER_PROPERTY_HEADER structure is a header that is used to create your own structure as an input to IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY. |
| [POWERSOURCESTATUS structure](..\charging\ns-charging--powersourcestatus.md) | This struct is for internal use only. |
| [POWERSOURCEUPDATE structure](..\charging\ns-charging--powersourceupdate.md) | This structure is for internal use only. |
| [POWERSOURCEUPDATEEX structure](..\charging\ns-charging--powersourceupdateex.md) | This structure is for internal use only. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [POWERSOURCEID enumeration](..\charging\ne-charging--powersourceid.md) | This enum is for internal use only. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY IOCTL](..\charging\ni-charging-ioctl-internal-configure-charger-property.md) | The IOCTL_INTERNAL_CONFIGURE_CHARGER_PROPERTY control code is sent from a configurable charger to a device that handles configurable chargers. It configures charger properties. |
