---
UID: NF.wdm.PoFxReportDevicePoweredOn
title: PoFxReportDevicePoweredOn
author: windows-driver-content
description: The PoFxReportDevicePoweredOn routine notifies the power management framework (PoFx) that the device completed the requested transition to the D0 (fully on) power state.
old-location: kernel\pofxreportdevicepoweredon.htm
ms.assetid: 3138F5D7-CF7E-47B4-817C-AFF00C310AD5
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxReportDevicePoweredOn
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: <= DISPATCH_LEVEL
ms.keywords: PoFxReportDevicePoweredOn
req.iface: 
req.product: Windows 10 or later.
---

# PoFxReportDevicePoweredOn function



## -description
<p>The <b>PoFxReportDevicePoweredOn</b> routine notifies the power management framework (PoFx) that the device completed the requested transition to the D0 (fully on) power state.</p>


## -syntax

````
VOID PoFxReportDevicePoweredOn(
  _In_ POHANDLE Handle
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle that represents the registration of the device with the power management framework (PoFx). The device driver previously received this handle from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a> routine.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The driver for a registered device must call <b>PoFxReportDevicePoweredOn</b> after either of the following occurrences:</p>

<p>In response to either occurrence, the driver sends D0 IRP (an <b>IRP_MN_SET_POWER</b> request) down its device stack to initiate a transition to the D0 power state, if the device is not already in the D0 state. After the driver completes (and all lower drivers complete) the transition to the D0 state, the driver calls <b>PoFxReportDevicePoweredOn</b> to notify PoFx.</p>

<p>Each time the <i>DevicePowerRequiredCallback</i> routine is called, the driver must respond by calling <b>PoFxReportDevicePoweredOn</b>. The <b>PoFxReportDevicePoweredOn</b> call can occur either during or after the <i>DevicePowerRequiredCallback</i> call. The driver must call <b>PoFxReportDevicePoweredOn</b> regardless of whether no D0 IRP is required, the D0 IRP request fails, or the dispatched D0 IRP succeeds or fails.</p>

<p>During a system transition to the S0 state, PoFx sends the driver an <b>IRP_MN_SET_POWER</b> request to notify the driver of the pending S0 transition. In response, the driver must complete this request as soon as possible, switch the device to the D0 power state, and call <b>PoFxReportDevicePoweredOn</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546749">Handling a System Set-Power IRP in a Device Power Policy Owner</a>.</p>

<p>On entry to <b>PoFxReportDevicePoweredOn</b>, the device might be in an uninitialized D0 power state in which all of the components in the device are turned on. In response to the <b>PoFxReportDevicePoweredOn</b> call, PoFx configures the device in an initialized D0 state. During this configuration, PoFx switches as many components as it can to low-power Fx power states.</p>

<p>The driver for a registered device must call <b>PoFxReportDevicePoweredOn</b> after either of the following occurrences:</p>

<p>In response to either occurrence, the driver sends D0 IRP (an <b>IRP_MN_SET_POWER</b> request) down its device stack to initiate a transition to the D0 power state, if the device is not already in the D0 state. After the driver completes (and all lower drivers complete) the transition to the D0 state, the driver calls <b>PoFxReportDevicePoweredOn</b> to notify PoFx.</p>

<p>Each time the <i>DevicePowerRequiredCallback</i> routine is called, the driver must respond by calling <b>PoFxReportDevicePoweredOn</b>. The <b>PoFxReportDevicePoweredOn</b> call can occur either during or after the <i>DevicePowerRequiredCallback</i> call. The driver must call <b>PoFxReportDevicePoweredOn</b> regardless of whether no D0 IRP is required, the D0 IRP request fails, or the dispatched D0 IRP succeeds or fails.</p>

<p>During a system transition to the S0 state, PoFx sends the driver an <b>IRP_MN_SET_POWER</b> request to notify the driver of the pending S0 transition. In response, the driver must complete this request as soon as possible, switch the device to the D0 power state, and call <b>PoFxReportDevicePoweredOn</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546749">Handling a System Set-Power IRP in a Device Power Policy Owner</a>.</p>

<p>On entry to <b>PoFxReportDevicePoweredOn</b>, the device might be in an uninitialized D0 power state in which all of the components in the device are turned on. In response to the <b>PoFxReportDevicePoweredOn</b> call, PoFx configures the device in an initialized D0 state. During this configuration, PoFx switches as many components as it can to low-power Fx power states.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450949">DevicePowerRequiredCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxReportDevicePoweredOn routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
