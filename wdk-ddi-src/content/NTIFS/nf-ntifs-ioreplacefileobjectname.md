---
UID: NF.ntifs.IoReplaceFileObjectName
title: IoReplaceFileObjectName
author: windows-driver-content
description: The IoReplaceFileObjectName routine replaces the name of a file object.
old-location: ifsk\ioreplacefileobjectname.htm
ms.assetid: 1550a35f-2733-4ee8-9715-d82f96eb5da7
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReplaceFileObjectName
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
ms.keywords: IoReplaceFileObjectName
req.iface: 
---

# IoReplaceFileObjectName function



## -description
<p>The <b>IoReplaceFileObjectName</b> routine replaces the name of a file object.</p>


## -syntax

````
NTSTATUS IoReplaceFileObjectName(
  _In_ PFILE_OBJECT FileObject,
  _In_ PWSTR        NewFileName,
  _In_ USHORT       FileNameLength
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to the file object whose file name is being replaced. </p>
</dd>

### -param <i>NewFileName</i> [in]

<dd>
<p>Pointer to the string buffer for the new name for the file object.</p>
</dd>

### -param <i>FileNameLength</i> [in]

<dd>
<p>Length, in bytes, of the new name for the file object. </p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS or one of the following NTSTATUS values otherwise:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that the file object provided does not have a name to replace.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates that inadequate memory is available to allocate a buffer to complete this operation.</p>

<p> </p>

## -remarks
<p>Drivers should use <b>IoReplaceFileObjectName</b> to safely replace the name in a file object. This allows the I/O manager to control the lifetime of the buffer associated with the file object. Replacing a file object name directly without using <b>IoReplaceFileObjectName</b> may conflict with other uses of the name and should be avoided when possible.</p>

<p>This routine should be used to replace the file object name instead of doing so manually to allow the kernel to manage the lifetime of the name correctly.</p>

<p>Drivers should use <b>IoReplaceFileObjectName</b> to safely replace the name in a file object. This allows the I/O manager to control the lifetime of the buffer associated with the file object. Replacing a file object name directly without using <b>IoReplaceFileObjectName</b> may conflict with other uses of the name and should be avoided when possible.</p>

<p>This routine should be used to replace the file object name instead of doing so manually to allow the kernel to manage the lifetime of the name correctly.</p>

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
<p>Available starting with Windows 7.</p>
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