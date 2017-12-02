---
UID: NF.ntddk.IoIsFileOriginRemote
title: IoIsFileOriginRemote
author: windows-driver-content
description: The IoIsFileOriginRemote routine determines whether a given file object is for a remote create request.
old-location: ifsk\ioisfileoriginremote.htm
old-project: ifsk
ms.assetid: 46655cbe-0483-4897-bd12-ce108af326c6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IoIsFileOriginRemote
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoIsFileOriginRemote
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
req.irql: Any level
req.iface: 
---

# IoIsFileOriginRemote function



## -description
<p>The <b>IoIsFileOriginRemote</b> routine determines whether a given file object is for a remote create request. </p>


## -syntax

````
BOOLEAN IoIsFileOriginRemote(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param FileObject [in]

<dd>
<p>Pointer to a file object for the file. </p>
</dd>
</dl>

## -returns
<p><b>IoIsFileOriginRemote</b> returns <b>TRUE</b> if the file object was created to satisfy a remote create request, otherwise <b>FALSE</b>. </p>

## -remarks
<p>File system filter drivers call <b>IoIsFileOriginRemote</b> for a file object to determine whether it represents a remote create request. </p>

<p><b>IoIsFileOriginRemote</b> must be called after the create request has entirely completed. In other words, it cannot be called in the create dispatch ("pre-create") path or the create completion ("post-create") path. </p>

<p><b>IoIsFileOriginRemote</b> checks the FO_REMOTE_ORIGIN flag on the file object pointed to by <i>FileObject</i>. Network file systems set or clear this flag by calling <a href="..\ntddk\nf-ntddk-iosetfileorigin.md">IoSetFileOrigin</a>. </p>

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
<p>This routine is available on Microsoft Windows XP and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-iosetfileorigin.md">IoSetFileOrigin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoIsFileOriginRemote routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
