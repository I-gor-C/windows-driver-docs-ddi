# Hpmi.h header


This header is used by Power metering. For more information, see
- [Power metering](../_powermeter/index.md)

Hpmi.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [HPMI_BATTERY_UTILIZATION_HINT structure](ns-hpmi--hpmi-battery-utilization-hint.md) | This hint indicates if the OEM Battery Manager should attempt to save as much charge as possible in the non-hot swappable batteries (i.e. |
| [HPMI_QUERY_CAPABILITIES structure](ns-hpmi--hpmi-query-capabilities.md) | The HPMI_QUERY_CAPABILITIES structure is used to query HPMI capabilities. |
| [HPMI_QUERY_CAPABILITIES_RESPONSE structure](ns-hpmi--hpmi-query-capabilities-response.md) | HPMI_QUERY_CAPABILITIES_RESPONSE is a structure used to return information about software defined batteries (SDB). |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_HPMI_BATTERY_UTILIZATION_HINT IOCTL](ni-hpmi-ioctl-hpmi-battery-utilization-hint.md) | Set command sent to HPMI to provide battery utilization hints. |
| [IOCTL_HPMI_QUERY_CAPABILITIES IOCTL](ni-hpmi-ioctl-hpmi-query-capabilities.md) | The IOCTL_HPMI_QUERY_CAPABILITIES command is sent to query features supported by HPMI and Windows services requested by HPMI. Windows will issue this IOCL to HPMI once after a new HPMI driver instance is discovered. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [HPMI_HINT_BOOL enumeration](ne-hpmi--hpmi-hint-bool.md) | Boolean type value used to track availability of HPMI hint data. |
