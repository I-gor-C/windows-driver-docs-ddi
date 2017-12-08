# Power metering

Overview of the Power metering technology.

To develop Power metering, you need these headers:

 * [hpmi.h](..\hpmi\index.md)
 * [pmi.h](..\pmi\index.md)

For the programming guide, see [Power metering](https://docs.microsoft.com/en-us/windows-hardware/drivers/powermeter).

## Structures

| Title   | Description   |
| ---- |:---- |
| [HPMI_BATTERY_UTILIZATION_HINT structure](..\hpmi\ns-hpmi--hpmi-battery-utilization-hint.md) | This hint indicates if the OEM Battery Manager should attempt to save as much charge as possible in the non-hot swappable batteries (i.e. |
| [HPMI_QUERY_CAPABILITIES structure](..\hpmi\ns-hpmi--hpmi-query-capabilities.md) | The HPMI_QUERY_CAPABILITIES structure is used to query HPMI capabilities. |
| [HPMI_QUERY_CAPABILITIES_RESPONSE structure](..\hpmi\ns-hpmi--hpmi-query-capabilities-response.md) | HPMI_QUERY_CAPABILITIES_RESPONSE is a structure used to return information about software defined batteries (SDB). |
| [PMI_BUDGETING_CONFIGURATION structure](..\pmi\ns-pmi--pmi-budgeting-configuration.md) | The PMI_BUDGETING_CONFIGURATION structure contains information about the current power budget of a power meter. A power budget defines how much power that the system can consume from the set of power supplies monitored by the power meter. |
| [PMI_CAPABILITIES structure](..\pmi\ns-pmi--pmi-capabilities.md) | The PMI_CAPABILITIES structure contains information about the power metering and budgeting capabilities of a power meter. |
| [PMI_CONFIGURATION structure](..\pmi\ns-pmi--pmi-configuration.md) | The PMI_CONFIGURATION structure contains information about the current power metering and budgeting configuration of a power meter. |
| [PMI_EVENT structure](..\pmi\ns-pmi--pmi-event.md) | The PMI_EVENT structure contains information about a power metering and budgeting event that is signaled through the Power Meter Interface (PMI). |
| [PMI_MEASUREMENT_CONFIGURATION structure](..\pmi\ns-pmi--pmi-measurement-configuration.md) | The PMI_MEASUREMENT_CONFIGURATION structure contains information about the current power measurement configuration of a power meter. |
| [PMI_MEASUREMENT_DATA structure](..\pmi\ns-pmi--pmi-measurement-data.md) | The PMI_MEASUREMENT_DATA structure contains the current power measurement that is collected by a power meter. |
| [PMI_METERED_HARDWARE_INFORMATION structure](..\pmi\ns-pmi--pmi-metered-hardware-information.md) | The PMI_METERED_HARDWARE_INFORMATION structure contains information about one or more power supplies that are monitored by the power meter. |
| [PMI_REPORTED_CAPABILITIES structure](..\pmi\ns-pmi--pmi-reported-capabilities.md) | The PMI_REPORTED_CAPABILITIES structure contains information about the type of power metering and budgeting capabilities a power meter supports. Additionally, this structure contains asset information about the power meter itself. |
| [PMI_THRESHOLD_CONFIGURATION structure](..\pmi\ns-pmi--pmi-threshold-configuration.md) | The PMI_THRESHOLD_CONFIGURATION structure contains information about the threshold configuration of the power meter. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [HPMI_HINT_BOOL enumeration](..\hpmi\ne-hpmi--hpmi-hint-bool.md) | Boolean type value used to track availability of HPMI hint data. |
| [PMI_CAPABILITIES_TYPE enumeration](..\pmi\ne-pmi-pmi-capabilities-type.md) | The PMI_CAPABILITIES_TYPE enumeration defines the type of capabilities data that is referenced by the Capability member of the PMI_CAPABILITIES structure. |
| [PMI_CONFIGURATION_TYPE enumeration](..\pmi\ne-pmi-pmi-configuration-type.md) | The PMI_CONFIGURATION_TYPE enumeration defines the type of PMI configuration data that is referenced by the Configuration member of the PMI_CONFIGURATION structure. |
| [PMI_EVENT_TYPE enumeration](..\pmi\ne-pmi-pmi-event-type.md) | The PMI_EVENT_TYPE enumeration defines the type of PMI power meter event that is returned through the successful completion of an IOCTL_PMI_REGISTER_EVENT_NOTIFY request. |
| [PMI_MEASUREMENT_TYPE enumeration](..\pmi\ne-pmi-pmi-measurement-type.md) | The PMI_MEASUREMENT_TYPE enumeration defines the source of the PMI measurement data. |
| [PMI_MEASUREMENT_UNIT enumeration](..\pmi\ne-pmi-pmi-measurement-unit.md) | The PMI_MEASUREMENT_UNIT enumeration defines the units of the PMI measurement data. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_HPMI_BATTERY_UTILIZATION_HINT IOCTL](..\hpmi\ni-hpmi-ioctl-hpmi-battery-utilization-hint.md) | Set command sent to HPMI to provide battery utilization hints. |
| [IOCTL_HPMI_QUERY_CAPABILITIES IOCTL](..\hpmi\ni-hpmi-ioctl-hpmi-query-capabilities.md) | The IOCTL_HPMI_QUERY_CAPABILITIES command is sent to query features supported by HPMI and Windows services requested by HPMI. Windows will issue this IOCL to HPMI once after a new HPMI driver instance is discovered. |
| [IOCTL_PMI_GET_CAPABILITIES IOCTL](..\pmi\ni-pmi-ioctl-pmi-get-capabilities.md) | The IOCTL_PMI_GET_CAPABILITIES request obtains the capability and asset information about a power meter. |
| [IOCTL_PMI_GET_CONFIGURATION IOCTL](..\pmi\ni-pmi-ioctl-pmi-get-configuration.md) | The IOCTL_PMI_GET_CONFIGURATION request returns information about the current configuration of a power meter. |
| [IOCTL_PMI_GET_MEASUREMENT IOCTL](..\pmi\ni-pmi-ioctl-pmi-get-measurement.md) | The IOCTL_PMI_GET_MEASUREMENT request returns the current measurement data from a power meter. |
| [IOCTL_PMI_REGISTER_EVENT_NOTIFY IOCTL](..\pmi\ni-pmi-ioctl-pmi-register-event-notify.md) | The IOCTL_PMI_REGISTER_EVENT_NOTIFY request registers the IOCTL initiator to be notified about a power meter event. When the event occurs, the Power Meter Interface (PMI) completes the IOCTL request and returns information about the event. |
| [IOCTL_PMI_SET_CONFIGURATION IOCTL](..\pmi\ni-pmi-ioctl-pmi-set-configuration.md) | The IOCTL_PMI_SET_CONFIGURATION request sets the configuration data for a power meter. |
