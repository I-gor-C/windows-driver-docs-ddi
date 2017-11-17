# Declarations in the scsiwmi header
This header Scsiwmi contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [ScsiPortWmiSetData function](nf-scsiwmi-scsiportwmisetdata.md) | The ScsiPortWmiSetData routine updates the WNODE_ALL_DATA structure within the request context to specify the position and length of the data for an instance. |
| [ScsiPortWmiFireLogicalUnitEvent function](nf-scsiwmi-scsiportwmifirelogicalunitevent.md) | The ScsiPortWmiFireLogicalUnitEvent routine sends an event associated with a logical unit to the port driver for delivery to WMI data consumers that have requested notification of the event.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [ScsiPortWmiFireAdapterEvent function](nf-scsiwmi-scsiportwmifireadapterevent.md) | TBD |
| [ScsiPortWmiGetReturnSize function](nf-scsiwmi-scsiportwmigetreturnsize.md) | TBD |
| [ScsiPortWmiSetInstanceCount function](nf-scsiwmi-scsiportwmisetinstancecount.md) | The ScsiPortWmiSetInstanceCount specifies the number of instances for which data buffers must be set aside within the WNODE_ALL_DATA structure in the request context. |
| [ScsiPortWmiDispatchFunction function](nf-scsiwmi-scsiportwmidispatchfunction.md) | The ScsiPortWmiDispatchFunction routine is a dispatch routine for miniport drivers that support WMI. |
| [ScsiPortWmiIsQueryAllData function](nf-scsiwmi-scsiportwmiisqueryalldata.md) | TBD |
| [ScsiPortWmiGetReturnStatus function](nf-scsiwmi-scsiportwmigetreturnstatus.md) | TBD |
| [ScsiPortWmiGetInstanceName function](nf-scsiwmi-scsiportwmigetinstancename.md) | The ScsiPortWmiGetInstanceName routine returns a pointer to the instance name associated with the indicated the Windows Management Instrumentation (WMI) SCSI Request Block (SRB). |
| [ScsiPortWmiPostProcess function](nf-scsiwmi-scsiportwmipostprocess.md) | The ScsiPortWmiPostProcess routine updates a request context for a WMI SRB.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. |
| [ScsiPortWmiSetInstanceName function](nf-scsiwmi-scsiportwmisetinstancename.md) | The ScsiPortWmiSetInstanceName routine updates the WNODE_ALL_DATA structure within the request context to specify the position and length of an instance name. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PSCSIWMI_SET_DATABLOCK callback function](nc-scsiwmi-pscsiwmi-set-datablock.md) | TBD |
| [PSCSIWMI_SET_DATAITEM callback function](nc-scsiwmi-pscsiwmi-set-dataitem.md) | TBD |
| [PSCSIWMI_FUNCTION_CONTROL callback function](nc-scsiwmi-pscsiwmi-function-control.md) | TBD |
| [PSCSIWMI_QUERY_REGINFO callback function](nc-scsiwmi-pscsiwmi-query-reginfo.md) | TBD |
| [PSCSIWMI_EXECUTE_METHOD callback function](nc-scsiwmi-pscsiwmi-execute-method.md) | TBD |
| [PSCSIWMI_QUERY_DATABLOCK callback function](nc-scsiwmi-pscsiwmi-query-datablock.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PSCSIWMI_REQUEST_CONTEXT structure](ns-scsiwmi-pscsiwmi-request-context.md) | A SCSIWMI_REQUEST_CONTEXT structure contains context information for a WMI SRB. |
| [SCSIWMILIB_CONTEXT structure](ns-scsiwmi--scsiwmilib-context.md) | A SCSI_WMILIB_CONTEXT structure provides registration information for a miniport driver's data and event blocks and defines entry points for the miniport driver's HwScsiWmiXxx callback routines. |
| [PSCSIWMIGUIDREGINFO structure](ns-scsiwmi-pscsiwmiguidreginfo.md) | The SCSIWMIGUIDREGINFO structure contains information about a given data or event block supported by a SCSI miniport driver. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SCSIWMI_ENABLE_DISABLE_CONTROL enumeration](ne-scsiwmi-scsiwmi-enable-disable-control.md) | The SCSIWMI_ENABLE_DISABLE_CONTROL enumerator is used to specify what to enable or disable. |

This header is used in these topics:

- [Storage](..content/_Storage)
