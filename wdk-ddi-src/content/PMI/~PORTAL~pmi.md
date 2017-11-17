# Declarations in the pmi header
This header Pmi contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PMI_MEASUREMENT_CONFIGURATION structure](ns-pmi--pmi-measurement-configuration.md) | The PMI_MEASUREMENT_CONFIGURATION structure contains information about the current power measurement configuration of a power meter. |
| [PMI_CAPABILITIES structure](ns-pmi--pmi-capabilities.md) | The PMI_CAPABILITIES structure contains information about the power metering and budgeting capabilities of a power meter. |
| [PMI_REPORTED_CAPABILITIES structure](ns-pmi--pmi-reported-capabilities.md) | The PMI_REPORTED_CAPABILITIES structure contains information about the type of power metering and budgeting capabilities a power meter supports. Additionally, this structure contains asset information about the power meter itself. |
| [PMI_MEASUREMENT_DATA structure](ns-pmi--pmi-measurement-data.md) | The PMI_MEASUREMENT_DATA structure contains the current power measurement that is collected by a power meter. |
| [PMI_METERED_HARDWARE_INFORMATION structure](ns-pmi--pmi-metered-hardware-information.md) | The PMI_METERED_HARDWARE_INFORMATION structure contains information about one or more power supplies that are monitored by the power meter. |
| [PMI_BUDGETING_CONFIGURATION structure](ns-pmi--pmi-budgeting-configuration.md) | The PMI_BUDGETING_CONFIGURATION structure contains information about the current power budget of a power meter. A power budget defines how much power that the system can consume from the set of power supplies monitored by the power meter. |
| [PMI_CONFIGURATION structure](ns-pmi--pmi-configuration.md) | The PMI_CONFIGURATION structure contains information about the current power metering and budgeting configuration of a power meter. |
| [PMI_THRESHOLD_CONFIGURATION structure](ns-pmi--pmi-threshold-configuration.md) | The PMI_THRESHOLD_CONFIGURATION structure contains information about the threshold configuration of the power meter. |
| [PMI_EVENT structure](ns-pmi--pmi-event.md) | The PMI_EVENT structure contains information about a power metering and budgeting event that is signaled through the Power Meter Interface (PMI). |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_PMI_SET_CONFIGURATION IOCTL](ni-pmi-ioctl-pmi-set-configuration.md) | The IOCTL_PMI_SET_CONFIGURATION request sets the configuration data for a power meter. |
| [IOCTL_PMI_GET_CAPABILITIES IOCTL](ni-pmi-ioctl-pmi-get-capabilities.md) | The IOCTL_PMI_GET_CAPABILITIES request obtains the capability and asset information about a power meter. |
| [IOCTL_PMI_GET_CONFIGURATION IOCTL](ni-pmi-ioctl-pmi-get-configuration.md) | The IOCTL_PMI_GET_CONFIGURATION request returns information about the current configuration of a power meter. |
| [IOCTL_PMI_GET_MEASUREMENT IOCTL](ni-pmi-ioctl-pmi-get-measurement.md) | The IOCTL_PMI_GET_MEASUREMENT request returns the current measurement data from a power meter. |
| [IOCTL_PMI_REGISTER_EVENT_NOTIFY IOCTL](ni-pmi-ioctl-pmi-register-event-notify.md) | The IOCTL_PMI_REGISTER_EVENT_NOTIFY request registers the IOCTL initiator to be notified about a power meter event. When the event occurs, the Power Meter Interface (PMI) completes the IOCTL request and returns information about the event. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PMI_CAPABILITIES_TYPE enumeration](ne-pmi-pmi-capabilities-type.md) | The PMI_CAPABILITIES_TYPE enumeration defines the type of capabilities data that is referenced by the Capability member of the PMI_CAPABILITIES structure. |
| [PMI_EVENT_TYPE enumeration](ne-pmi-pmi-event-type.md) | The PMI_EVENT_TYPE enumeration defines the type of PMI power meter event that is returned through the successful completion of an IOCTL_PMI_REGISTER_EVENT_NOTIFY request. |
| [PMI_MEASUREMENT_UNIT enumeration](ne-pmi-pmi-measurement-unit.md) | The PMI_MEASUREMENT_UNIT enumeration defines the units of the PMI measurement data. |
| [PMI_MEASUREMENT_TYPE enumeration](ne-pmi-pmi-measurement-type.md) | The PMI_MEASUREMENT_TYPE enumeration defines the source of the PMI measurement data. |
| [PMI_CONFIGURATION_TYPE enumeration](ne-pmi-pmi-configuration-type.md) | The PMI_CONFIGURATION_TYPE enumeration defines the type of PMI configuration data that is referenced by the Configuration member of the PMI_CONFIGURATION structure. |

This header is used in these topics:

- [powermeter](..content/_powermeter)
