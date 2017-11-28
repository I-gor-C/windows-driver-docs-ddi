---
UID: NF.fltkernel.FltFastIoMdlReadComplete
title: FltFastIoMdlReadComplete
author: windows-driver-content
description: The FltFastIoMdlReadComplete routine completes the read operation that the FltFastIoMdlRead routine initiated.
old-location: ifsk\fltfastiomdlreadcomplete.htm
old-project: ifsk
ms.assetid: 6F5E808C-9E35-4BE8-AE67-FDD354D6FD0E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltFastIoMdlReadComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlMdlReadCompleteDev
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltFastIoMdlReadComplete function



## -description
<p>The <b>FltFastIoMdlReadComplete</b> routine completes the read operation that the <a href="https://msdn.microsoft.com/library/windows/hardware/hh706188">FltFastIoMdlRead</a> routine initiated.</p>


## -syntax

````
BOOLEAN FsRtlMdlReadCompleteDev(
       PFLT_INSTANCE InitiatingInstance,
  _In_ PFILE_OBJECT  FileObject,
  _In_ PMDL          MdlChain
);
````


## -parameters
<dl>

### -param <i>InitiatingInstance</i> 

<dd>
<p>Opaque instance pointer for the caller. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>A pointer to the file object.</p>
</dd>

### -param <i>MdlChain</i> [in]

<dd>
<p>On return, a pointer to a linked list of one or more MDLs that point to the cached file data.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>FltFastIoMdlReadComplete</b> routine unlocks the pages in cache memory that the <a href="https://msdn.microsoft.com/library/windows/hardware/hh706188">FltFastIoMdlRead</a> routine allocated.</p>

<p>The <b>FltFastIoMdlReadComplete</b> routine unlocks the pages in cache memory that the <a href="https://msdn.microsoft.com/library/windows/hardware/hh706188">FltFastIoMdlRead</a> routine allocated.</p>

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
<dt>Fltkernel.h (include Ntifs.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh706188">FltFastIoMdlRead</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltFastIoMdlReadComplete routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
