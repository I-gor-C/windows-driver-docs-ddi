---
UID: NF.portcls.IAdapterPowerManagement.PowerChangeState
title: IAdapterPowerManagement::PowerChangeState
author: windows-driver-content
description: The PowerChangeState method requests that the device change to a new power state.
old-location: audio\iadapterpowermanagement_powerchangestate.htm
old-project: audio
ms.assetid: b3e0fca7-d5ab-4d52-9702-dae83c540a71
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IAdapterPowerManagement, PowerChangeState, IAdapterPowerManagement::PowerChangeState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IAdapterPowerManagement.PowerChangeState
req.alt-loc: portcls.h
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
req.iface: IAdapterPowerManagement
---

# IAdapterPowerManagement::PowerChangeState method



## -description
<p>The <code>PowerChangeState</code> method requests that the device change to a new power state.</p>


## -syntax

````
void PowerChangeState(
  [in] POWER_STATE NewState
);
````


## -parameters
<dl>

### -param NewState [in]

<dd>
<p>Specifies the new power state being requested for the device. This parameter is a union of type POWER_STATE. The new power state (<i>NewState</i>.<b>DeviceState</b>) can be one of the DEVICE_POWER_STATE enumeration values shown in the following table.</p>
<table>
<tr>
<th>Power State</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>PowerDeviceD0</p>
</td>
<td>
<p>Full power state (D0). This code may be a function of the current power state. Save the new state. This local value is used to determine when to cache property accesses and when to permit the driver from accessing the hardware.</p>
</td>
</tr>
<tr>
<td>
<p>PowerDeviceD1</p>
</td>
<td>
<p>The sleep state having the lowest latency with respect to the latency time required to return to D0</p>
</td>
</tr>
<tr>
<td>
<p>PowerDeviceD2</p>
</td>
<td>
<p>A medium latency sleep state. In this state, the device driver cannot assume that it can touch the hardware, so any accesses need to be cached and the hardware restored upon entering D0.</p>
</td>
</tr>
<tr>
<td>
<p>PowerDeviceD3</p>
</td>
<td>
<p>A full hibernation state and is the longest latency sleep state. The driver cannot access the hardware in this state and must cache any hardware accesses and restore the hardware upon returning to D0 or D1</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>PortCls calls the <code>PowerChangeState</code> method in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> power IRP. This call must not fail. PortCls and the system use the <code>PowerChangeState</code> call to place the device in the desired power state. When the system attempts to suspend or resume an active audio stream, the driver must be capable of saving or restoring its device context appropriately.</p>

<p>To assist the driver, PortCls will pause any active audio streams prior to calling this method to place the device in a sleep state. After calling this method, PortCls will unpause active audio streams, to wake the device up. Miniports can opt for additional notification by utilizing the <a href="..\portcls\nn-portcls-ipowernotify.md">IPowerNotify</a> interface.</p>

<p>The miniport driver must perform the requested change to the device's power state before it returns from the <code>PowerChangeState</code> call. If the miniport driver needs to save or restore any device state before a power-state change, the miniport driver should support the <b>IPowerNotify</b> interface, which allows it to receive advance warning of any such change. Before returning from a successful <code>PowerChangeState</code> call, the miniport driver should cache the new power state.</p>

<p>While the miniport driver is in one of the sleep states (any state other than PowerDeviceD0), it must avoid writing to the hardware. The miniport driver must cache any hardware accesses that need to be deferred until the device powers up again. If the power state is changing from one of the sleep states to PowerDeviceD0, the miniport driver should perform any deferred hardware accesses after it has powered up the device. If the power state is changing from PowerDeviceD0 to a sleep state, the miniport driver can perform any necessary hardware accesses during the <code>PowerChangeState</code> call before it powers down the device.</p>

<p>While powered down, a miniport driver is never asked to create a miniport driver object or stream object. PortCls always places the device in the PowerDeviceD0 state before calling the miniport driver's <b>NewStream</b> method.</p>

<p>The code for this method must reside in paged memory.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iadapterpowermanagement.md">IAdapterPowerManagement</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-ipowernotify.md">IPowerNotify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IAdapterPowerManagement::PowerChangeState method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
