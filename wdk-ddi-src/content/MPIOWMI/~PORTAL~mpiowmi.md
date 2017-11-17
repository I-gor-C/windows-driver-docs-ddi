# Declarations in the mpiowmi header
This header Mpiowmi contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DSM_PARAMETERS structure](ns-mpiowmi--dsm-parameters.md) | The DSM_PARAMETERS structure holds the DSM version and timer counters information. |
| [DSM_VERSION structure](ns-mpiowmi--dsm-version.md) | The DSM_VERSION structure represents version information that is associated with a DSM binary or package. |
| [MPIO_DRIVE_INFO structure](ns-mpiowmi--mpio-drive-info.md) | The MPIO_DRIVE_INFO structure represents a multi-path disk in the system. |
| [MPIO_PATH_INFORMATION structure](ns-mpiowmi--mpio-path-information.md) | The MPIO_PATH_INFORMATION structure represents a top-level view of all the paths that are under MPIO control. To query the path information, the request must be sent to the MPIO control object by using its WMI instance name. |
| [ClearMpioDiskHealthCounters_IN structure](ns-mpiowmi--clearmpiodiskhealthcounters-in.md) | The ClearMpioDiskHealthCounters_IN structure is used to provide an input parameter to the ClearMpioDiskHealthCounters method. |
| [MPIO_DISK_HEALTH_CLASS structure](ns-mpiowmi--mpio-disk-health-class.md) | The MPIO_DISK_HEALTH_CLASS structure contains the health information for a multi-path disk. |
| [MPIO_PATH_HEALTH_CLASS structure](ns-mpiowmi--mpio-path-health-class.md) | The MPIO_PATH_HEALTH_CLASS structure represents the health information for a path. |
| [SCSI_ADDR structure](ns-mpiowmi--scsi-addr.md) | The SCSI_ADDR structure represents a SCSI address. |
| [MPIO_DISK_INFO structure](ns-mpiowmi--mpio-disk-info.md) | The MPIO_DISK_INFO structure allows applications to query the system for the top level view of its disk topology. The request must be directed to the MPIO control object by using its WMI instance name. |
| [MPIO_EventEntry structure](ns-mpiowmi--mpio-evententry.md) | The MPIO_EventEntry structure is used to return events that MPIO has logged. |
| [GetPathConfiguration_OUT structure](ns-mpiowmi--getpathconfiguration-out.md) | The GetPathConfiguration_OUT structure is used to report the output parameters that are associated with the GetPathConfiguration method. |
| [GetPathConfiguration_IN structure](ns-mpiowmi--getpathconfiguration-in.md) | The GetPathConfiguration_IN structure is used to retrieve the per path device information. |
| [SetDSMCounters_IN structure](ns-mpiowmi--setdsmcounters-in.md) | The SetDSMCounters_IN structure is used to set the timer counters for a particular DSM. |
| [MPIO_CONTROLLER_CONFIGURATION structure](ns-mpiowmi--mpio-controller-configuration.md) | The MPIO_CONTROLLER_CONFIGURATION structure provides a top-level view of the storage controllers and the targets that are connected to them in the system. |
| [DSM_COUNTERS structure](ns-mpiowmi--dsm-counters.md) | The DSM_COUNTERS structure holds the various timer counters that are applicable to all LUNs that are controlled by the DSM. |
| [MPIO_ADAPTER_INFORMATION structure](ns-mpiowmi--mpio-adapter-information.md) | The MPIO_ADAPTER_INFORMATION structure contains information that pertains to MPIO's view of a path. |
| [ClearPathHealthCounters_IN structure](ns-mpiowmi--clearpathhealthcounters-in.md) | The ClearPathHealthCounters_IN structure is used to provide an input parameter to the ClearPathHealthCounters method. |
| [MPIO_PATH_HEALTH_INFO structure](ns-mpiowmi--mpio-path-health-info.md) | The MPIO_PATH_HEALTH_INFO structure is used to query the available health information for every path that is exposed to the system. |
| [MPIO_CONTROLLER_INFO structure](ns-mpiowmi--mpio-controller-info.md) | The MPIO_CONTROLLER_INFO structure represents a storage controller. |
| [MPIO_TIMERS_COUNTERS structure](ns-mpiowmi--mpio-timers-counters.md) | The MPIO_TIMERS_COUNTERS structure controls the timer counters that affect all devices whose controlling DSMs do not implement independent timer counter settings. |
| [MPIO_REGISTERED_DSM structure](ns-mpiowmi--mpio-registered-dsm.md) | The MPIO_REGISTERED_DSM structure represents the top-level view of the registered DSMs on the system. To query this information, the request must be sent to the MPIO control object by using its WMI instance name. |
| [MPIO_DISK_HEALTH_INFO structure](ns-mpiowmi--mpio-disk-health-info.md) | The MPIO_DISK_HEALTH_INFO structure is used to query the available health information for every multi-path disk in the system. |
| [MPIOMoveDevice_IN structure](ns-mpiowmi--mpiomovedevice-in.md) | The MPIOMoveDevice_IN structure is used to set the active path on the device. |

This header is used in these topics:

- [Storage](..content/_Storage)
