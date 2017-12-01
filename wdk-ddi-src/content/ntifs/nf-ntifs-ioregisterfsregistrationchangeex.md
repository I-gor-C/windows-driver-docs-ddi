---
UID: NF.ntifs.IoRegisterFsRegistrationChangeEx
title: IoRegisterFsRegistrationChangeEx
author: windows-driver-content
description: The IoRegisterFsRegistrationChangeEx routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system.
old-location: ifsk\ioregisterfsregistrationchangeex.htm
old-project: ifsk
ms.assetid: e318e13b-8b6c-4593-93ce-17d2a1056ac2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IoRegisterFsRegistrationChangeEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: This routine is only available on the Update Rollup for Windows 2000 Service Pack 4 (SP4) operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRegisterFsRegistrationChangeEx
req.alt-loc: ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# IoRegisterFsRegistrationChangeEx function



## -description
<p>The <b>IoRegisterFsRegistrationChangeEx</b> routine registers a file system filter driver's notification routine to be called whenever a file system registers or unregisters itself as an active file system.</p>


## -syntax

````
NTSTATUS IoRegisterFsRegistrationChangeEx(
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
<p>A pointer to the <a href="ifsk.pdriver_fs_notification">PDRIVER_FS_NOTIFICATION</a> routine, which the file system calls when it registers or unregisters itself.</p>
</dd>
</dl>

## -returns
<p><b>IoRegisterFsRegistrationChangeEx</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The notification routine was successfully registered.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A notification packet could not be allocated for the notification routine.</p>

<p> </p>

## -remarks
<p>The effect of <b>IoRegisterFsRegistrationChangeEx</b> is identical to that of <a href="..\ntifs\nf-ntifs-ioregisterfsregistrationchange.md">IoRegisterFsRegistrationChange</a> on Windows XP and later. </p>

<p><b>IoRegisterFsRegistrationChangeEx</b> registers a file system filter driver to be notified whenever a file system calls <a href="..\ntifs\nf-ntifs-ioregisterfilesystem.md">IoRegisterFileSystem</a> or <a href="..\ntifs\nf-ntifs-iounregisterfilesystem.md">IoUnregisterFileSystem</a>. </p>

<p>To stop receiving such notifications, the filter driver should call <a href="..\ntifs\nf-ntifs-iounregisterfsregistrationchange.md">IoUnregisterFsRegistrationChange</a>. </p>

<p>When a file system filter driver calls <b>IoRegisterFsRegistrationChangeEx</b>, its notification routine is also called immediately for all currently registered file systems (that is, file systems that have already called <a href="..\ntifs\nf-ntifs-ioregisterfilesystem.md">IoRegisterFileSystem</a> but have not yet called <a href="..\ntifs\nf-ntifs-iounregisterfilesystem.md">IoUnregisterFileSystem</a>). </p>

<p>Because the caller's notification routine can be called even before <b>IoRegisterFsRegistrationChangeEx</b> returns, a filter driver should not call this routine until after it has created any data structures that it needs to process these notifications. </p>

<p><b>IoRegisterFsRegistrationChangeEx</b> ignores RAW devices. For information about attaching to the RAW file system by name, see <a href="ifsk.attaching_the_filter_device_object_to_the_target_device_object">Attaching the Filter Device Object to the Target Device Object</a>. </p>

<p><b>IoRegisterFsRegistrationChangeEx</b> increments the reference count on the filter driver's driver object. </p>

<p>If a file system filter driver calls <b>IoRegisterFsRegistrationChangeEx</b> twice in succession (without calling <a href="..\ntifs\nf-ntifs-iounregisterfsregistrationchange.md">IoUnregisterFsRegistrationChange</a> in between), passing the same values for the <i>DriverObject</i> and <i>DriverNotificationRoutine</i> parameters that it registered in the previous call to <b>IoRegisterFsRegistrationChangeEx</b>, and no other filter drivers have registered since the first call, <b>IoRegisterFsRegistrationChangeEx</b> returns STATUS_DEVICE_ALREADY_ATTACHED. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>This routine is only available on the Update Rollup for Windows 2000 Service Pack 4 (SP4) operating system.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-ioregisterfilesystem.md">IoRegisterFileSystem</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ioregisterfsregistrationchange.md">IoRegisterFsRegistrationChange</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-iounregisterfilesystem.md">IoUnregisterFileSystem</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-iounregisterfsregistrationchange.md">IoUnregisterFsRegistrationChange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoRegisterFsRegistrationChangeEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
