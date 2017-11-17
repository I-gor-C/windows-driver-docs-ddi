---
UID: NF.ntifs.IoRegisterFileSystem
title: IoRegisterFileSystem
author: windows-driver-content
description: The IoRegisterFileSystem routine adds a file system's control device object to the global file system queue.
old-location: ifsk\ioregisterfilesystem.htm
ms.assetid: 19d53afd-b63c-4fd3-9b08-c51e2a1247af
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
req.alt-api: IoRegisterFileSystem
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
ms.keywords: IoRegisterFileSystem
req.iface: 
---

# IoRegisterFileSystem function



## -description
<p>The <b>IoRegisterFileSystem</b> routine adds a file system's control device object to the global file system queue.</p>


## -syntax

````
VOID IoRegisterFileSystem(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the control device object for the file system.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>IoRegisterFileSystem</b> registers a file system as an active file system by inserting the file system's control device object into the global file system queue, and increments the reference count on the file system's control device object.</p>

<p>The file system control device object's device type must be one of the following:</p><dl>
<dd>
<p>FILE_DEVICE_NETWORK_FILE_SYSTEM</p>
</dd>
<dd>
<p>FILE_DEVICE_CD_ROM_FILE_SYSTEM</p>
</dd>
<dd>
<p>FILE_DEVICE_DISK_FILE_SYSTEM</p>
</dd>
</dl><p>FILE_DEVICE_NETWORK_FILE_SYSTEM</p>

<p>FILE_DEVICE_CD_ROM_FILE_SYSTEM</p>

<p>FILE_DEVICE_DISK_FILE_SYSTEM</p>

<p>If the device type is not one of these values, the file system is not registered.</p>

<p>In addition, the file system control device object must be named. If it is not named, this does not cause the call to <b>IoRegisterFileSystem</b> to fail. However, file system filter drivers, as well as many system components and support routines, use this name to distinguish the file system's control device objects, which are always named, from its volume device objects, which are never named. </p>

<p>If the DO_LOW_PRIORITY_FILESYSTEM flag is set on the file system's control device object, the device object is inserted into the next-to-last position in the queue. (The RAW file system occupies the last position in the queue.) If this flag is not set, the device object is inserted at the head of the queue.</p>

<p><b>IoRegisterFileSystem</b> calls the notification routines of file system filter drivers that have registered for this notification by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548499">IoRegisterFsRegistrationChange</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548508">IoRegisterFsRegistrationChangeEx</a>.</p>

<p><b>IoRegisterFileSystem</b> registers a file system as an active file system by inserting the file system's control device object into the global file system queue, and increments the reference count on the file system's control device object.</p>

<p>The file system control device object's device type must be one of the following:</p><dl>
<dd>
<p>FILE_DEVICE_NETWORK_FILE_SYSTEM</p>
</dd>
<dd>
<p>FILE_DEVICE_CD_ROM_FILE_SYSTEM</p>
</dd>
<dd>
<p>FILE_DEVICE_DISK_FILE_SYSTEM</p>
</dd>
</dl><p>FILE_DEVICE_NETWORK_FILE_SYSTEM</p>

<p>FILE_DEVICE_CD_ROM_FILE_SYSTEM</p>

<p>FILE_DEVICE_DISK_FILE_SYSTEM</p>

<p>If the device type is not one of these values, the file system is not registered.</p>

<p>In addition, the file system control device object must be named. If it is not named, this does not cause the call to <b>IoRegisterFileSystem</b> to fail. However, file system filter drivers, as well as many system components and support routines, use this name to distinguish the file system's control device objects, which are always named, from its volume device objects, which are never named. </p>

<p>If the DO_LOW_PRIORITY_FILESYSTEM flag is set on the file system's control device object, the device object is inserted into the next-to-last position in the queue. (The RAW file system occupies the last position in the queue.) If this flag is not set, the device object is inserted at the head of the queue.</p>

<p><b>IoRegisterFileSystem</b> calls the notification routines of file system filter drivers that have registered for this notification by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548499">IoRegisterFsRegistrationChange</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548508">IoRegisterFsRegistrationChangeEx</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548499">IoRegisterFsRegistrationChange</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoRegisterFileSystem routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
