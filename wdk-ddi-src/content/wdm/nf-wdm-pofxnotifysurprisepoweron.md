---
UID: NF.wdm.PoFxNotifySurprisePowerOn
title: PoFxNotifySurprisePowerOn
author: windows-driver-content
description: The PoFxNotifySurprisePowerOn routine notifies the power management framework (PoFx) that a device was turned on as a side effect of supplying power to some other device.
old-location: kernel\pofxnotifysurprisepoweron.htm
old-project: kernel
ms.assetid: AB9C7D32-D536-4B2B-9C85-DF5A0031798C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoFxNotifySurprisePowerOn
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxNotifySurprisePowerOn
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
req.iface: 
req.product: Windows 10 or later.
---

# PoFxNotifySurprisePowerOn function



## -description
<p>The <b>PoFxNotifySurprisePowerOn</b> routine notifies the power management framework (PoFx) that a device was turned on as a side effect of supplying power to some other device.</p>


## -syntax

````
VOID PoFxNotifySurprisePowerOn(
  _In_ PDEVICE_OBJECT Pdo
);
````


## -parameters
<dl>

### -param <i>Pdo</i> [in]

<dd>
<p>A pointer to a <a href="wdkgloss.p#wdkgloss.physical_device_object__pdo_#wdkgloss.physical_device_object__pdo_">physical device object</a> (PDO). This parameter points to a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure that represents the physical device that was turned on as a side effect. The caller is always the bus driver that enumerated the PDO.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Device drivers should not call this routine. This routine should be called only by bus drivers.</p>

<p>A bus driver calls this routine to inform PoFx that a device that is not currently being used was incidentally turned on at the same time as a second device. For example, the first device might share a power rail with the second device. Thus, power cannot be supplied to the second device without supplying power, as a side effect, to the first device. Because the first device is not being used, this device should be configured to consume as little power as possible.</p>

<p>To request a transition to a D0 power state, a device driver sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> request down its device stack. Through the PDO in this stack, the bus driver that is the parent of this device receives the request and responds by supplying power to the device. However, if the bus driver cannot turn on this device without also turning on a second, unused device, the bus driver can call <b>PoFxNotifySurprisePowerOn</b> to reduce the power consumed by the unused device.</p>

<p>On entry to <b>PoFxNotifySurprisePowerOn</b>, the device represented by the <i>Pdo</i> parameter is in an uninitialized D0 power state. In this state, all of the components in the device are typically turned on. In response to the <b>PoFxNotifySurprisePowerOn</b> call, PoFx configures the device in an initialized D0 state. During this configuration, PoFx switches as many components as it can to low-power Fx power states. If possible, PoFx configures the device in a "hot D3" state, which is really a D0 state in which all of the individual components in the device are turned off.</p>

<p><b>PoFxNotifySurprisePowerOn</b> can configure only a device that was registered with PoFx when the device was previously turned off. However, unless the bus driver knows that a device is not registered, the bus driver should call <b>PoFxNotifySurprisePowerOn</b> when the device is turned on as a side effect.</p>

<p>If the bus driver fails to call this routine when the device is turned on, the device hardware might stay in the fully on state for an indefinite time, during which PoFx assumes that the device remains in the D3 (fully off) power state.</p>

<p>Call <b>PoFxNotifySurprisePowerOn</b> only if the device was turned on incidentally, as a side effect of turning on some other device. If the bus driver restores power to a device in response to a <a href="kernel.devicepowerrequiredcallback">DevicePowerRequiredCallback</a> callback or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> request for a D0 transition, call the <a href="..\wdm\nf-wdm-pofxreportdevicepoweredon.md">PoFxReportDevicePoweredOn</a> routine instead to inform PoFx when power is restored to the device.</p>

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
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="kernel.devicepowerrequiredcallback">DevicePowerRequiredCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pofxreportdevicepoweredon.md">PoFxReportDevicePoweredOn</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxNotifySurprisePowerOn routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
