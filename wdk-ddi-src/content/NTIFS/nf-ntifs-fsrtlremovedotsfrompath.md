---
UID: NF.ntifs.FsRtlRemoveDotsFromPath
title: FsRtlRemoveDotsFromPath
author: windows-driver-content
description: The FsRtlRemoveDotsFromPath routine removes unnecessary occurrences of '.' and '..' from the specified path.
old-location: ifsk\fsrtlremovedotsfrompath.htm
ms.assetid: af6ecdb7-8713-460d-8fd9-ef027ac15b39
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlRemoveDotsFromPath
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
ms.keywords: FsRtlRemoveDotsFromPath
req.iface: 
---

# FsRtlRemoveDotsFromPath function



## -description
<p>The <b>FsRtlRemoveDotsFromPath</b> routine removes unnecessary occurrences of '.' and '..' from the specified path.</p>


## -syntax

````
NTSTATUS FsRtlRemoveDotsFromPath(
  _Inout_ PWSTR  OriginalString,
  _In_    USHORT PathLength,
  _Out_   USHORT *NewLength
);
````


## -parameters
<dl>

### -param <i>OriginalString</i> [in, out]

<dd>
<p>A pointer to the buffer to be processed.</p>
</dd>

### -param <i>PathLength</i> [in]

<dd>
<p>The length of buffer (in bytes).</p>
</dd>

### -param <i>NewLength</i> [out]

<dd>
<p>A pointer to the new length of the buffer, after processing.</p>
</dd>
</dl>

## -returns
<p>The<b> FsRtlRemoveDotsFromPath</b> routine returns either STATUS_SUCCESS value for success or STATUS_IO_REPARSE_DATA_INVALID if the operation could not be completed.</p>

## -remarks
<p>This routine would take a path as <i>OriginalString</i> like the following example:</p>

<p>The routine would modify <i>OriginalString</i> as follows:</p>

<p>The routine will fail with STATUS_IO_REPARSE_DATA_INVALID if any of the following strings are passed as <i>OriginalString</i>:</p>

<p>This routine would take a path as <i>OriginalString</i> like the following example:</p>

<p>The routine would modify <i>OriginalString</i> as follows:</p>

<p>The routine will fail with STATUS_IO_REPARSE_DATA_INVALID if any of the following strings are passed as <i>OriginalString</i>:</p>

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
<p> Available in Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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