---
UID: NF.fltkernel.FltFastIoMdlWriteComplete
title: FltFastIoMdlWriteComplete
author: windows-driver-content
description: The FltFastIoMdlWriteComplete routine frees the resources that FltFastIoPrepareMdlWrite allocated.
old-location: ifsk\fltfastiomdlwritecomplete.htm
old-project: ifsk
ms.assetid: 7B67BB47-6F95-4B1A-A823-F796529D5C48
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltFastIoMdlWriteComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlMdlWriteCompleteDev
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

# FltFastIoMdlWriteComplete function



## -description
<p>The <b>FltFastIoMdlWriteComplete</b> routine frees the resources that <a href="https://msdn.microsoft.com/library/windows/hardware/hh706192">FltFastIoPrepareMdlWrite</a> allocated.</p>


## -syntax

````
BOOLEAN FsRtlMdlWriteCompleteDev(
       PFLT_INSTANCE  InitiatingInstance,
  _In_ PFILE_OBJECT   FileObject,
  _In_ PLARGE_INTEGER FileOffset,
  _In_ PMDL           MdlChain
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

### -param <i>FileOffset</i> [in]

<dd>
<p>A pointer to a value that specifies the starting byte offset within the cache that holds the data.</p>
</dd>

### -param <i>MdlChain</i> [in]

<dd>
<p>A pointer to a linked list of memory descriptor lists (MDLs) that <a href="https://msdn.microsoft.com/library/windows/hardware/hh706192">FltFastIoPrepareMdlWrite</a> allocated.</p>
</dd>
</dl>

## -returns
<p>The <b>FltFastIoMdlWriteComplete</b> routine returns <b>TRUE</b> if the operation succeeds and <b>FALSE</b> if the operation fails or if the FO_WRITE_THROUGH flag is set in the file object.</p>

## -remarks
<p>The <b>FltFastIoMdlWriteComplete</b> routine frees the memory descriptor lists (MDLs) that <a href="https://msdn.microsoft.com/library/windows/hardware/hh706192">FltFastIoPrepareMdlWrite</a> allocated and unlocks the cache memory that <b>FltFastIoPrepareMdlWrite</b> locked.</p>

<p>If the FO_WRITE_THROUGH flag is set on the file object pointed to by the <i>FileObject</i> parameter, <b>FltFastIoMdlWriteComplete</b> immediately flushes the cached memory to disk. This flush operation re-enters the file system and can cause <b>FltFastIoMdlWriteComplete</b> to raise an exception if the flush operation fails. </p>

<p>Each call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh706192">FltFastIoPrepareMdlWrite</a> must be followed by a call to <b>FltFastIoMdlWriteComplete</b>.</p>

<p>The <b>FltFastIoMdlWriteComplete</b> routine frees the memory descriptor lists (MDLs) that <a href="https://msdn.microsoft.com/library/windows/hardware/hh706192">FltFastIoPrepareMdlWrite</a> allocated and unlocks the cache memory that <b>FltFastIoPrepareMdlWrite</b> locked.</p>

<p>If the FO_WRITE_THROUGH flag is set on the file object pointed to by the <i>FileObject</i> parameter, <b>FltFastIoMdlWriteComplete</b> immediately flushes the cached memory to disk. This flush operation re-enters the file system and can cause <b>FltFastIoMdlWriteComplete</b> to raise an exception if the flush operation fails. </p>

<p>Each call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh706192">FltFastIoPrepareMdlWrite</a> must be followed by a call to <b>FltFastIoMdlWriteComplete</b>.</p>

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
<p>Available starting with  Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh706192">FltFastIoPrepareMdlWrite</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltFastIoMdlWriteComplete routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
