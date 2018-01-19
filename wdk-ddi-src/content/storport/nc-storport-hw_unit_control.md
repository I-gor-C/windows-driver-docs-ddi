---
UID : NC:storport.HW_UNIT_CONTROL
title : HW_UNIT_CONTROL
author : windows-driver-content
description : A miniport driver's HwStorUnitControl routine is called to perform synchronous operations to control the state of storage unit device. The miniport driver is notified to start a unit or handle a power state transition for a unit device.
old-location : storage\hwstorunitcontrol.htm
old-project : storage
ms.assetid : 33534C7A-C88D-4980-98A7-2B94488D3550
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : storport.h
req.include-header : Storport.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 8.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : HwStorUnitControl
req.alt-loc : Storport.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSTORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER"
req.product : Windows 10 or later.
---


# HW_UNIT_CONTROL callback function
A miniport driver's <b>HwStorUnitControl</b> routine is called to perform synchronous operations to control the state of storage unit device. The miniport driver is notified to  start a unit or handle a power state transition for a unit device.

## Syntax

```
HW_UNIT_CONTROL HwUnitControl;

SCSI_UNIT_CONTROL_STATUS HwUnitControl(
  PVOID DeviceExtension,
  SCSI_UNIT_CONTROL_TYPE ControlType,
  PVOID Parameters
)
{...}
```

## Parameters

`DeviceExtension`

A pointer to the miniport driver's per-unit storage area.

`ControlType`

Specifies  an unit control operation. Each control type initiates an action by the miniport driver. The following are the  control types and their meanings.

<table>
<tr>
<th>Control Type</th>
<th>Meaning</th>
<th>IRQL</th>
<th>Spinlock</th>
</tr>
<tr>
<td>
<b>ScsiQuerySupportedUnitControlTypes</b>

</td>
<td>
Reports the unit-control operations implemented by the miniport driver. The Storport driver calls <b>HwStorUnitControl</b> with this control type after the HBA has been initialized but before the first I/O. The miniport driver fills in the SCSI_SUPPORTED_CONTROL_TYPE_LIST structure at <i>Parameters</i> with the operations it supports. After <b>HwStorUnitControl</b> returns from this call, the Storport driver calls the miniport driver's <b>HwStorUnitControl</b> only for supported operations.

</td>
<td>
PASSIVE_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitUsage</b>

</td>
<td>
Notifies the miniport if  the logical unit is used for any supported usage types. Storport driver will call  <b>HwStorUnitControl</b>  separately for each usage type supported.

</td>
<td>
PASSIVE_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitStart</b>

</td>
<td>
Notifies the miniport to start a unit device.

</td>
<td>
PASSIVE_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitPower</b>

</td>
<td>
Reports the unit power on or power off states. If the miniport supports this control type, it will not receive a storage request block with SRB_FUNCTION_POWER.

</td>
<td>
DISPATCH_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitPoFxPowerInfo</b>

</td>
<td>
Notifies the miniport if idle power management is enabled or disabled on the unit component. The miniport should call <a href="..\storport\nf-storport-storportinitializepofxpower.md">StorPortInitializePoFxPower</a> within this unit control if idle power management was enabled and it if supports runtime power management for the unit device.

</td>
<td>
PASSIVE_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitPoFxPowerRequired</b>

</td>
<td>
Notifies the miniport whether power is required or not for the unit component.

</td>
<td>
DISPATCH_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitPoFxPowerActive</b>

</td>
<td>
Notifies the miniport that the unit component is either active or idle.

</td>
<td>
DISPATCH_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitPoFxPowerSetFState</b>

</td>
<td>
Notifies the miniport to set the unit component to the given functional power state (F-state). The miniport must support this control type if is specifies more than one F-state in the call to <a href="..\storport\nf-storport-storportinitializepofxpower.md">StorPortInitializePoFxPower</a>.

</td>
<td>
DISPATCH_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitPoFxPowerControl</b>

</td>
<td>
Requests a power engine plug-in (PEP) initiated private power control operation for the miniport to execute for the unit.

</td>
<td>
DISPATCH_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitRemove</b>

</td>
<td>
Notifies the miniport that the unit has been removed.

</td>
<td>
PASSIVE_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitSurpriseRemoval</b>

</td>
<td>
Notifies the miniport that the unit has been surprise-removed.

</td>
<td>
PASSIVE_LEVEL

</td>
<td>
None

</td>
</tr>
<tr>
<td>
<b>ScsiUnitRichDescription</b>

</td>
<td>
The miniport can choose to support this if the device reports a longer vendor ID, model number, or firmware revision than is defined in the SCSI spec.


</td>
<td>
PASSIVE_LEVEL

</td>
<td>
None

</td>
</tr>
</table>

`Parameters`

Contains information related to the <i>ControlType</i>.  

<table>
<tr>
<th>Control Type</th>
<th>Parameters</th>
</tr>
<tr>
<td>
<b>ScsiQuerySupportedUnitControlTypes</b>

</td>
<td>
Caller-allocated SCSI_SUPPORTED_CONTROL_TYPE_LIST structure.

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _SCSI_SUPPORTED_CONTROL_TYPE_LIST { 
    IN ULONG MaxControlType;
    OUT BOOLEAN SupportedTypeList[0];
} SCSI_SUPPORTED_CONTROL_TYPE_LIST, *PSCSI_SUPPORTED_CONTROL_TYPE_LIST;</pre>
</td>
</tr>
</table></span></div>


## Return Value

Depending on the control type, <b>HwStorUnitControl</b> returns one of the following SCSI_UNIT_CONTROL_STATUS values:
<dl>
<dt><b>
        ScsiUnitControlSuccess</b></dt>
</dl>The miniport driver completed the requested operation successfully.
<dl>
<dt><b>
        ScsiUnitControlUnsuccessful</b></dt>
</dl>The unit control operation was not successful.

## Remarks

The name <b>HwStorUnitControl</b>  is just a placeholder. The actual prototype of this routine is defined in <i>storport.h</i> as follows:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h (include Storport.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\storport\nc-storport-hw_adapter_control.md">HwStorAdapterControl</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HW_UNIT_CONTROL routine%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>