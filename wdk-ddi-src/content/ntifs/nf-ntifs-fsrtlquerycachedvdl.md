---
UID: NF.ntifs.FsRtlQueryCachedVdl
title: FsRtlQueryCachedVdl
author: windows-driver-content
description: The current valid data length (VDL) for a cached file is retrieved with the FsRtlQueryCachedVdl routine.
old-location: ifsk\fsrtlquerycachedvdl.htm
old-project: ifsk
ms.assetid: 5D4F3D70-6E2B-4B2E-91A4-6852AF8FEAD0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlQueryCachedVdl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlQueryCachedVdl
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

# FsRtlQueryCachedVdl function



## -description
<p>The current valid data length (VDL) for a cached file is retrieved with the <b>FsRtlQueryCachedVdl</b> routine.</p>


## -syntax

````
NTSTATUS FsRtlQueryCachedVdl(
  _In_  PFILE_OBJECT FileObject,
  _Out_ PLONGLONG    Vdl
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>The file object to retrieve the cached VDL for.</p>
</dd>

### -param <i>Vdl</i> [out]

<dd>
<p> A pointer to a caller supplied value which receives the VDL.</p>
</dd>
</dl>

## -returns
<p><b>FsRtlQueryCachedVdl</b> returns <b>STATUS_SUCCESS</b> if the cached VDL is obtained successfully for the <i>FileObject</i> specified. Otherwise, another appropriate <b>NTSTATUS</b> value is returned.</p>

## -remarks
<p>The <b>FsRtlQueryCachedVdl</b> routine will return the VDL for a full span file region. This is a region beginning at an offset of 0 and having a length of <b>MAXLONGLONG</b>.</p>

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
<p>Available in starting with Windows 8.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>