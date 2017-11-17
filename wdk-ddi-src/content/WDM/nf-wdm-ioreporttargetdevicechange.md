---
UID: NF.wdm.IoReportTargetDeviceChange
title: IoReportTargetDeviceChange
author: windows-driver-content
description: The IoReportTargetDeviceChange routine notifies the PnP manager that a custom event has occurred on a device.
old-location: kernel\ioreporttargetdevicechange.htm
ms.assetid: b0107cb1-4828-4ede-813e-934b929c9874
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReportTargetDeviceChange
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
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: IoReportTargetDeviceChange
req.iface: 
req.product: Windows 10 or later.
---

# IoReportTargetDeviceChange function



## -description
<p>The <b>IoReportTargetDeviceChange</b> routine notifies the PnP manager that a custom event has occurred on a device.</p>


## -syntax

````
NTSTATUS IoReportTargetDeviceChange(
  _In_ PDEVICE_OBJECT PhysicalDeviceObject,
  _In_ PVOID          NotificationStructure
);
````


## -parameters
<dl>

### -param <i>PhysicalDeviceObject</i> [in]

<dd>
<p>Pointer to the PDO of the device being reported.</p>
</dd>

### -param <i>NotificationStructure</i> [in]

<dd>
<p>Pointer to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff564596">TARGET_DEVICE_CUSTOM_NOTIFICATION</a> structure describing the custom event. The PnP manager sends this structure to drivers that registered for notification of the event.</p>
<p><i>NotificationStructure</i>.<b>FileObject</b> must be <b>NULL</b>. <i>NotificationStructure</i>.<b>Event</b> must contain the custom GUID for the event. The other fields of the <i>NotificationStructure</i> must be filled in as appropriate for the custom event.</p>
<p>The PnP manager fills in the <i>NotificationStructure</i>.<b>FileObject</b> field when it sends notifications to registrants.</p>
</dd>
</dl>

## -returns
<p><b>IoReportTargetDeviceChange</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status values include the following.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The caller specified a system PnP event, such as GUID_TARGET_DEVICE_QUERY_REMOVE. This routine is only for custom events.</p>

<p> </p>

## -remarks
<p>After <b>IoReportTargetDeviceChange</b> notifies the PnP manager that a custom event has occurred on a device, the PnP manager sends notification of the event to drivers that registered for notification on the device. Do not use this routine to report system PnP events, such as GUID_TARGET_DEVICE_REMOVE_COMPLETE.</p>

<p>A driver that defines a custom device event calls <b>IoReportTargetDeviceChange</b> to inform the PnP manager that the custom event has occurred. Custom notification can be used for events like a volume label change.</p>

<p>A driver should call the asynchronous form of this routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549634">IoReportTargetDeviceChangeAsynchronous</a>, instead of this routine, to prevent deadlocks.</p>

<p>Certain kernel-mode components can call this synchronous routine. For example, a file system can call <b>IoReportTargetDeviceChange</b> to report a "get off the volume" custom event when a component tries to open the volume for exclusive access. Clients that register for notification on file system volumes are careful to not request an exclusive open in a PnP notification callback routine.</p>

<p>The custom notification structure contains a driver-defined event with its own GUID. Driver writers can generate GUIDs with Uuidgen.exe or Guidgen.exe (which are included in the Microsoft Windows SDK).</p>

<p>Callers of <b>IoReportTargetDeviceChange</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread. To report a target device change from IRQL &gt; PASSIVE_LEVEL, call <b>IoReportTargetDeviceChangeAsynchronous</b>.</p>

<p><b>IoReportTargetDeviceChange</b> is not supported on Windows 98/Me; it returns STATUS_NOT_IMPLEMENTED.</p>

<p>After <b>IoReportTargetDeviceChange</b> notifies the PnP manager that a custom event has occurred on a device, the PnP manager sends notification of the event to drivers that registered for notification on the device. Do not use this routine to report system PnP events, such as GUID_TARGET_DEVICE_REMOVE_COMPLETE.</p>

<p>A driver that defines a custom device event calls <b>IoReportTargetDeviceChange</b> to inform the PnP manager that the custom event has occurred. Custom notification can be used for events like a volume label change.</p>

<p>A driver should call the asynchronous form of this routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549634">IoReportTargetDeviceChangeAsynchronous</a>, instead of this routine, to prevent deadlocks.</p>

<p>Certain kernel-mode components can call this synchronous routine. For example, a file system can call <b>IoReportTargetDeviceChange</b> to report a "get off the volume" custom event when a component tries to open the volume for exclusive access. Clients that register for notification on file system volumes are careful to not request an exclusive open in a PnP notification callback routine.</p>

<p>The custom notification structure contains a driver-defined event with its own GUID. Driver writers can generate GUIDs with Uuidgen.exe or Guidgen.exe (which are included in the Microsoft Windows SDK).</p>

<p>Callers of <b>IoReportTargetDeviceChange</b> must be running at IRQL = PASSIVE_LEVEL in the context of a system thread. To report a target device change from IRQL &gt; PASSIVE_LEVEL, call <b>IoReportTargetDeviceChangeAsynchronous</b>.</p>

<p><b>IoReportTargetDeviceChange</b> is not supported on Windows 98/Me; it returns STATUS_NOT_IMPLEMENTED.</p>

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
<p>Available starting with Windows 2000.</p>
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
<p>PASSIVE_LEVEL (see Remarks section)</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549634">IoReportTargetDeviceChangeAsynchronous</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564596">TARGET_DEVICE_CUSTOM_NOTIFICATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoReportTargetDeviceChange routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
