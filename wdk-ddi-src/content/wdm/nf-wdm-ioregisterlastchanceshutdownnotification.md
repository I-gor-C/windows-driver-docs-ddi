---
UID: NF.wdm.IoRegisterLastChanceShutdownNotification
title: IoRegisterLastChanceShutdownNotification
author: windows-driver-content
description: The IoRegisterLastChanceShutdownNotification routine registers a driver to receive an IRP_MJ_SHUTDOWN IRP when the system is shut down, after all file systems have been flushed.
old-location: kernel\ioregisterlastchanceshutdownnotification.htm
old-project: kernel
ms.assetid: 9ee590ce-e822-4c15-bb01-6f726268f163
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoRegisterLastChanceShutdownNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows. Not available in Microsoft Windows 98/Me.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRegisterLastChanceShutdownNotification
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoRegisterLastChanceShutdownNotification function



## -description
<p>The <b>IoRegisterLastChanceShutdownNotification</b> routine registers a driver to receive an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a> IRP when the system is shut down, after all file systems have been flushed. </p>


## -syntax

````
NTSTATUS IoRegisterLastChanceShutdownNotification(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object of the device for which the driver requests shutdown notification. The system passes this pointer to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff543405">DispatchShutdown</a> routine. </p>
</dd>
</dl>

## -returns
<p><b>IoRegisterLastChanceShutdownNotification</b> returns STATUS_SUCCESS on success, or the appropriate NTSTATUS error code on failure.</p>

## -remarks
<p>The <b>IoRegisterLastChanceShutdownNotification</b> routine registers the driver to receive an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a> IRP for the specified device when the system shuts down. The driver receives one such IRP for each device it registers to receive notification for. Drivers handle <b>IRP_MJ_SHUTDOWN</b> IRPs within their <a href="https://msdn.microsoft.com/library/windows/hardware/ff543405">DispatchShutdown</a> routines.</p>

<p>For any device that is registered with this routine, the system sends the <b>IRP_MJ_SHUTDOWN</b> IRP after all file systems are flushed. Only one driver in a device stack should register to receive shutdown notification, by calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff549541">IoRegisterShutdownNotification</a> or <b>IoRegisterLastChanceShutdownNotification</b>.</p>

<p>If the driver ceases to require shutdown notification for that device, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550409">IoUnregisterShutdownNotification</a> to remove the driver from the shutdown notification queue.</p>

<p>A driver that calls <b>IoRegisterLastChanceShutdownNotification</b> must satisfy the following restrictions in its <i>DispatchShutdown</i> routine:</p>

<p>The <i>DispatchShutdown</i> routine must not call any pageable routines.</p>

<p>The <i>DispatchShutdown</i> routine must not access pageable memory.</p>

<p>The <i>DispatchShutdown</i> routine must not perform any file I/O operations.</p>

<p>Most drivers that require shutdown notification should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549541">IoRegisterShutdownNotification</a> routine, which does not impose these limitations on the <i>DispatchShutdown</i> routine, and which causes the <i>DispatchShutdown</i> routine to be called before the file systems are flushed. Only drivers that must do some cleanup after the file systems are flushed, such as a driver for a mass storage device, should use <b>IoRegisterLastChanceShutdownNotification</b>.</p>

<p>The registered <i>DispatchShutdown</i> routine is called before the power manager sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> request for <b>PowerSystemShutdown</b>. The <i>DispatchShutdown</i> routine is not called for transitions to any other power states.</p>

<p>The <b>IoRegisterLastChanceShutdownNotification</b> routine registers the driver to receive an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a> IRP for the specified device when the system shuts down. The driver receives one such IRP for each device it registers to receive notification for. Drivers handle <b>IRP_MJ_SHUTDOWN</b> IRPs within their <a href="https://msdn.microsoft.com/library/windows/hardware/ff543405">DispatchShutdown</a> routines.</p>

<p>For any device that is registered with this routine, the system sends the <b>IRP_MJ_SHUTDOWN</b> IRP after all file systems are flushed. Only one driver in a device stack should register to receive shutdown notification, by calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff549541">IoRegisterShutdownNotification</a> or <b>IoRegisterLastChanceShutdownNotification</b>.</p>

<p>If the driver ceases to require shutdown notification for that device, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550409">IoUnregisterShutdownNotification</a> to remove the driver from the shutdown notification queue.</p>

<p>A driver that calls <b>IoRegisterLastChanceShutdownNotification</b> must satisfy the following restrictions in its <i>DispatchShutdown</i> routine:</p>

<p>The <i>DispatchShutdown</i> routine must not call any pageable routines.</p>

<p>The <i>DispatchShutdown</i> routine must not access pageable memory.</p>

<p>The <i>DispatchShutdown</i> routine must not perform any file I/O operations.</p>

<p>Most drivers that require shutdown notification should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549541">IoRegisterShutdownNotification</a> routine, which does not impose these limitations on the <i>DispatchShutdown</i> routine, and which causes the <i>DispatchShutdown</i> routine to be called before the file systems are flushed. Only drivers that must do some cleanup after the file systems are flushed, such as a driver for a mass storage device, should use <b>IoRegisterLastChanceShutdownNotification</b>.</p>

<p>The registered <i>DispatchShutdown</i> routine is called before the power manager sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> request for <b>PowerSystemShutdown</b>. The <i>DispatchShutdown</i> routine is not called for transitions to any other power states.</p>

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
<p>Available in Windows 2000 and later versions of Windows. Not available in Microsoft Windows 98/Me.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543405">DispatchShutdown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549541">IoRegisterShutdownNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550409">IoUnregisterShutdownNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRegisterLastChanceShutdownNotification routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
