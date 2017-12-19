---
UID: NF.ntifs.IoUnregisterFileSystem
title: IoUnregisterFileSystem function
author: windows-driver-content
description: The IoUnregisterFileSystem routine removes a file system's control device object from the global file system queue.
old-location: ifsk\iounregisterfilesystem.htm
old-project: ifsk
ms.assetid: f6a0bff7-85b6-479a-b952-9a3a637e339e
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IoUnregisterFileSystem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoUnregisterFileSystem
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
---

# IoUnregisterFileSystem function



## -description
The <b>IoUnregisterFileSystem</b> routine removes a file system's control device object from the global file system queue.



## -syntax

````
VOID IoUnregisterFileSystem(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters

### -param DeviceObject [in]

Pointer to the control device object for the file system.


## -returns
None


## -remarks
<b>IoUnregisterFileSystem</b> unregisters the file system as an active file system by removing the file system's control device object from the global file system queue, and decrements the reference count on the file system's control device object. 

<b>IoUnregisterFileSystem</b> calls the notification routines of file system filter drivers that have registered for this notification by calling <a href="ifsk.ioregisterfsregistrationchange">IoRegisterFsRegistrationChange</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt; DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.ioregisterfilesystem">IoRegisterFileSystem</a>
</dt>
<dt>
<a href="ifsk.ioregisterfsregistrationchange">IoRegisterFsRegistrationChange</a>
</dt>
<dt>
<a href="ifsk.iounregisterfsregistrationchange">IoUnregisterFsRegistrationChange</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoUnregisterFileSystem routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

