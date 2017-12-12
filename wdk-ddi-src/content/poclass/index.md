---
UID: NA:
---

# Poclass.h header

## -description

This header is used by Battery, Windows kernel. For more information, see
- [Battery](../_battery/index.md)
- [Windows kernel](../_kernel/index.md)

Poclass.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [DEVICE_ACTIVE_COOLING callback](nc-poclass-device_active_cooling.md) | The ActiveCooling callback routine engages or disengages a device's active-cooling function. |
| [DEVICE_PASSIVE_COOLING callback](nc-poclass-device_passive_cooling.md) | The PassiveCooling callback routine controls the degree to which the device must throttle its performance to meet cooling requirements. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_BATTERY_INFORMATION structure](ns-poclass-_battery_information.md) | Battery miniclass drivers fill in this structure in response to certain BatteryMiniQueryInformation requests. |
| [_BATTERY_MANUFACTURE_DATE structure](ns-poclass-_battery_manufacture_date.md) | Battery miniclass drivers fill in this structure in response to certain BatteryMiniQueryInformation requests. |
| [_BATTERY_STATUS structure](ns-poclass-_battery_status.md) | The BATTERY_STATUS structure is used by battery miniclass drivers to return status information in response to a call to BatteryMiniQueryStatus. |
| [_THERMAL_COOLING_INTERFACE structure](ns-poclass-_thermal_cooling_interface.md) | The THERMAL_COOLING_INTERFACE structure enables the operating system to control the thermal management settings of a device. |
