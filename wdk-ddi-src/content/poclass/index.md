# Poclass.h header


This header is used by Windows kernel. For more information, see
- [Windows kernel](../_kernel/index.md)

Poclass.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [DEVICE_ACTIVE_COOLING callback](nc-poclass-device-active-cooling.md) | The ActiveCooling callback routine engages or disengages a device's active-cooling function. |
| [DEVICE_PASSIVE_COOLING callback](nc-poclass-device-passive-cooling.md) | The PassiveCooling callback routine controls the degree to which the device must throttle its performance to meet cooling requirements. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [THERMAL_COOLING_INTERFACE structure](ns-poclass--thermal-cooling-interface.md) | The THERMAL_COOLING_INTERFACE structure enables the operating system to control the thermal management settings of a device. |
