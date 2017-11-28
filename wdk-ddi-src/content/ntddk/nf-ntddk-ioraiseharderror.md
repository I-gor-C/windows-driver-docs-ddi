---
UID: NF.ntddk.IoRaiseHardError
title: IoRaiseHardError
author: windows-driver-content
description: The IoRaiseHardError routine causes a dialog box to appears that warns the user that a device I/O error has occurred, which might indicate that a physical device is failing.
old-location: kernel\ioraiseharderror.htm
old-project: kernel
ms.assetid: 140561ce-e2ad-45be-976a-86fb1d0d1e87
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoRaiseHardError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRaiseHardError
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoApcLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
---

# IoRaiseHardError function



## -description
<p>The <b>IoRaiseHardError</b> routine causes a dialog box to appears that warns the user that a device I/O error has occurred, which might indicate that a physical device is failing.</p>


## -syntax

````
VOID IoRaiseHardError(
  _In_     PIRP           Irp,
  _In_opt_ PVPB           Vpb,
  _In_     PDEVICE_OBJECT RealDeviceObject
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the IRP that failed because of a device I/O error. </p>
</dd>

### -param <i>Vpb</i> [in, optional]

<dd>
<p>Pointer to the volume parameter block (VPB), if any, for the mounted file object. This parameter is <b>NULL</b> if no VPB is associated with the device object.</p>
</dd>

### -param <i>RealDeviceObject</i> [in]

<dd>
<p>Pointer to the device object that represents the physical device on which the I/O operation failed. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Highest-level drivers, particularly file system drivers, call <b>IoRaiseHardError</b>.</p>

<p>An upper-level filter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a> (which disables normal kernel APCs) and sends an I/O request to a file system driver. The filter driver waits on the completion of the request by the file system driver before the filter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a> (which reenables normal kernel APCs).</p>

<p>An error occurs on the file system, and the file system driver calls <b>IoRaiseHardError</b> to report the error to the user. The file system driver waits on the dialog box.</p>

<p>Deadlock now exists: The normal kernel APC created by <b>IoRaiseHardError</b> to create the dialog box waits for normal kernel APCs to be enabled. The file system waits on the dialog box before it completes the I/O request. The filter driver waits on completion of the I/O request before it calls <b>KeLeaveCriticalRegion</b> (which reenables normal kernel APCs).</p>

<p>The behavior of this routine is dependent of the current state of hard errors for the running thread. If hard errors have been disabled by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550342">IoSetThreadHardErrorMode</a>, this routine completes the IRP specified by <i>Irp</i> without transferring any data into user buffers. In addition, no message is sent to notify the user of this failure. </p>

<p>Highest-level drivers, particularly file system drivers, call <b>IoRaiseHardError</b>.</p>

<p>An upper-level filter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a> (which disables normal kernel APCs) and sends an I/O request to a file system driver. The filter driver waits on the completion of the request by the file system driver before the filter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a> (which reenables normal kernel APCs).</p>

<p>An error occurs on the file system, and the file system driver calls <b>IoRaiseHardError</b> to report the error to the user. The file system driver waits on the dialog box.</p>

<p>Deadlock now exists: The normal kernel APC created by <b>IoRaiseHardError</b> to create the dialog box waits for normal kernel APCs to be enabled. The file system waits on the dialog box before it completes the I/O request. The filter driver waits on completion of the I/O request before it calls <b>KeLeaveCriticalRegion</b> (which reenables normal kernel APCs).</p>

<p>The behavior of this routine is dependent of the current state of hard errors for the running thread. If hard errors have been disabled by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550342">IoSetThreadHardErrorMode</a>, this routine completes the IRP specified by <i>Irp</i> without transferring any data into user buffers. In addition, no message is sent to notify the user of this failure. </p>

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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547759">IrqlIoApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549277">IoGetRelatedDeviceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549707">IoSetHardErrorOrVerifyDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550342">IoSetThreadHardErrorMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRaiseHardError routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
