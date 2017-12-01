---
UID: NC.irb.IDE_HW_CONTROL
title: IDE_HW_CONTROL
author: windows-driver-content
description: The IdeHwControl miniport driver routine notifies the miniport driver about Plug and Play (PnP) and power events.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\idehwcontrol.htm
old-project: storage
ms.assetid: 53f85f8d-3b50-4cfe-8bdd-d41d8c057f3e
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
req.alt-api: IdeHwControl
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

# IDE_HW_CONTROL callback



## -description
<p>The <i>IdeHwControl</i> miniport driver routine notifies the miniport driver about Plug and Play (PnP) and power events.</p>


## -prototype

````
IDE_HW_CONTROL IdeHwControl;

BOOLEAN IdeHwControl(
  _In_    PVOID              ChannelExtension,
  _In_    IDE_CONTROL_ACTION ControlAction,
  _Inout_ PVOID              Parameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>ChannelExtension</i> [in]

<dd>
<p>A pointer to the channel extension.</p>
</dd>

### -param <i>ControlAction</i> [in]

<dd>
<p>Contains an enumerator value of type <a href="..\irb\ne-irb-ide-control-action.md">IDE_CONTROL_ACTION</a> that indicates the control action to perform. </p>
</dd>

### -param <i>Parameters</i> [in, out]

<dd>
<p>A pointer to a buffer that contains the parameters that are associated with the control action. This parameter can have one of the values in the following table.</p>
<table>
<tr>
<th>Control action</th>
<th>Parameters</th>
<th>Description</th>
</tr>
<tr>
<td>
<p><b>IdeStart</b></p>
</td>
<td>
<p>Parameter points to a structure of type IDE_CHANNEL_CONFIGURATION.</p>
</td>
<td>
<p>Indicates that the port driver is starting the channel.</p>
</td>
</tr>
<tr>
<td>
<p><b>IdeVendorDefined</b></p>
</td>
<td>
<p>Parameter points to a structure of type IDE_VENDOR_DEFINED_POWER_INFO.</p>
</td>
<td>
<p>Indicates that there is a vendor defined power event coming.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><i>IdeHwControl</i> returns <b>TRUE</b> if the operation was successful. Otherwise, it returns <b>FALSE</b>. </p>

## -remarks
<p>The port driver makes sure that there is no outstanding I/O on the channel before it invokes this routine. The miniport driver can have its own power policy methods when the system enters a different power state. In order to achieve this, the miniport driver needs to do the following:</p>

<p>Add a power policy setting scheme into the miniport driver's INF file. A GUID is needed to present a miniport driver-defined power policy. For more information about the power settings directive, see <a href="NULL">INF AddPowerSetting Directive</a>. More information about the GUIDs can be found at <a href="https://msdn.microsoft.com/library/windows/hardware/mt608265">Disk settings</a>.</p>

<p>After vendor-defined power management is registered, the miniport driver will be able to receive calls to its <i>IdeHwControl</i> routine with control action <b>IdeVendorDefined</b> when the system power scheme changes.</p>

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
<a href="..\irb\nf-irb-ataportgetuncachedextension.md">AtaPortGetUncachedExtension</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IdeHwControl routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
