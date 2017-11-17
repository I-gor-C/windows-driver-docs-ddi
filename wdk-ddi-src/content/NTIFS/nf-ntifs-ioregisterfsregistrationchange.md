---
UID: NF.ntifs.IoRegisterFsRegistrationChange
title: IoRegisterFsRegistrationChange
author: windows-driver-content
description: The IoRegisterFsRegistrationChange routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system.
old-location: ifsk\ioregisterfsregistrationchange.htm
ms.assetid: 132951ef-7bb3-417e-a7b7-eb21f08aa846
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRegisterFsRegistrationChange
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: < DISPATCH_LEVEL
ms.keywords: IoRegisterFsRegistrationChange
req.iface: 
---

# IoRegisterFsRegistrationChange function



## -description
<p>The <b>IoRegisterFsRegistrationChange</b> routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system.</p>


## -syntax

````
NTSTATUS IoRegisterFsRegistrationChange(
  _In_ PDRIVER_OBJECT          DriverObject,
  _In_ PDRIVER_FS_NOTIFICATION DriverNotificationRoutine
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>Pointer to the driver object for the file system filter driver.</p>
</dd>

### -param <i>DriverNotificationRoutine</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551037">PDRIVER_FS_NOTIFICATION</a> routine, which the file system calls when it registers or unregisters itself.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The notification routine was successfully registered.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A notification packet could not be allocated for the notification routine.</p>

<p> </p>

## -remarks
<p><b>IoRegisterFsRegistrationChange</b> registers a file system filter driver to be notified whenever a file system calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548494">IoRegisterFileSystem</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548552">IoUnregisterFileSystem</a>. </p>

<p>To stop receiving such notifications, the filter driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548557">IoUnregisterFsRegistrationChange</a>. </p><p class="note">Because the caller's notification routine can be called even before <b>IoRegisterFsRegistrationChange</b> returns, a filter driver should not call this routine until after it has created any data structures that it needs in order to process these notifications. </p><p class="note">Additionally, in Windows XP and later, <b>IoRegisterFsRegistrationChange</b> ignores RAW devices. For information about attaching to the RAW file system by name, see <a href="ifsk.attaching_the_filter_device_object_to_the_target_device_object">Attaching the Filter Device Object to the Target Device Object</a>. </p>

<p><b>IoRegisterFsRegistrationChange</b> increments the reference count on the filter driver's driver object. </p>

<p>In Update Rollup for Windows 2000 SP4, file system filter drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548508">IoRegisterFsRegistrationChangeEx</a> instead of <b>IoRegisterFsRegistrationChange</b>. The effect of <b>IoRegisterFsRegistrationChangeEx</b> is identical to that of <b>IoRegisterFsRegistrationChange</b> on Windows XP and later. </p>

<p><b>IoRegisterFsRegistrationChange</b> registers a file system filter driver to be notified whenever a file system calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548494">IoRegisterFileSystem</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548552">IoUnregisterFileSystem</a>. </p>

<p>To stop receiving such notifications, the filter driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548557">IoUnregisterFsRegistrationChange</a>. </p><p class="note">Because the caller's notification routine can be called even before <b>IoRegisterFsRegistrationChange</b> returns, a filter driver should not call this routine until after it has created any data structures that it needs in order to process these notifications. </p><p class="note">Additionally, in Windows XP and later, <b>IoRegisterFsRegistrationChange</b> ignores RAW devices. For information about attaching to the RAW file system by name, see <a href="ifsk.attaching_the_filter_device_object_to_the_target_device_object">Attaching the Filter Device Object to the Target Device Object</a>. </p>

<p><b>IoRegisterFsRegistrationChange</b> increments the reference count on the filter driver's driver object. </p>

<p>In Update Rollup for Windows 2000 SP4, file system filter drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548508">IoRegisterFsRegistrationChangeEx</a> instead of <b>IoRegisterFsRegistrationChange</b>. The effect of <b>IoRegisterFsRegistrationChangeEx</b> is identical to that of <b>IoRegisterFsRegistrationChange</b> on Windows XP and later. </p>

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
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548494">IoRegisterFileSystem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548508">IoRegisterFsRegistrationChangeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548552">IoUnregisterFileSystem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548557">IoUnregisterFsRegistrationChange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoRegisterFsRegistrationChange routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
