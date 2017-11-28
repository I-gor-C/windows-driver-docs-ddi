---
UID: NC.irb.IDE_ADAPTER_CONTROL
title: IDE_ADAPTER_CONTROL
author: windows-driver-content
description: The AtaAdapterControl miniport driver routine is called to perform Plug and Play (PnP) and Power Management operations on the HBA.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataadaptercontrol.htm
old-project: storage
ms.assetid: 50125022-7450-4582-b98d-1d597e4e96d4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: WdmlibIoGetAffinityInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: irb.h
req.include-header: Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaAdapterControl
req.alt-loc: irb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# IDE_ADAPTER_CONTROL callback



## -description
<p>The <i>AtaAdapterControl</i> miniport driver routine is called to perform Plug and Play (PnP) and Power Management operations on the HBA.</p>


## -prototype

````
IDE_ADAPTER_CONTROL AtaAdapterControl;

BOOLEAN AtaAdapterControl(
  _In_    PVOID              ControllerExtension,
  _In_    IDE_CONTROL_ACTION ControlAction,
  _Inout_ PVOID              Parameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>ControllerExtension</i> [in]

<dd>
<p>A pointer to the controller extension.</p>
</dd>

### -param <i>ControlAction</i> [in]

<dd>
<p>
      One of five actions that the miniport driver must perform as defined in the following table.
  </p>
<table>
<tr>
<th>ControlAction</th>
<th>Parameters</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>IdeStart</p>
</td>
<td>
<p>IDE_CONTROLLER_CONFIGURATION</p>
</td>
<td>
<p>Indicates that the adapter is being started. The miniport driver should update the member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559036">IDE_CONTROLLER_CONFIGURATION</a> structure. If it is required, the miniport driver could obtain its hardware resources from the <b>IDE_CONTROLLER_CONFIGURATION</b> structure.</p>
</td>
</tr>
<tr>
<td>
<p>IdeStop</p>
</td>
<td>
<p>None</p>
</td>
<td>
<p>The miniport driver should stop using any resources that are allocated for this controller. Be aware that the port driver guarantees that all the channels that  are exposed by the adapter are stopped before it stops the adapter.</p>
</td>
</tr>
<tr>
<td>
<p>IdePowerUp</p>
</td>
<td>
<p>None</p>
</td>
<td>
<p>Indicates that the adapter is being turned on. Anything that does not persist across a power cycle must be configured during IdePowerUp.  </p>
</td>
</tr>
<tr>
<td>
<p>IdePowerDown</p>
</td>
<td>
<p>None</p>
</td>
<td>
<p>Indicates that the adapter is being turned off.</p>
</td>
</tr>
<tr>
<td>
<p>IdeVendorDefined</p>
</td>
<td>
<p>None</p>
</td>
<td>
<p>Indicates that the miniport driver should perform a vendor-defined control action..</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Parameters</i> [in, out]

<dd>
<p>Parameters associated with the given action.</p>
</dd>
</dl>

## -returns
<p>The miniport driver must return <b>TRUE</b> to acknowledge the completion of the requested action. A return value of <b>FALSE</b> indicates that the miniport driver was unable to complete the action successfully. A return value of <b>FALSE</b> for certain actions might cause the device installation to fail.</p>

## -remarks
<p>The port driver guarantees that there is no outstanding I/O on the adapter before it invokes the <i>AtaAdapterControl</i> routine.</p>

<p>The port driver guarantees that there is no outstanding I/O on the adapter before it invokes the <i>AtaAdapterControl</i> routine.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559036">IDE_CONTROLLER_CONFIGURATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaAdapterControl routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
