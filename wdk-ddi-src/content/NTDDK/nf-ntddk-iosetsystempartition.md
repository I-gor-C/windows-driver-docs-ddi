---
UID: NF.ntddk.IoSetSystemPartition
title: IoSetSystemPartition
author: windows-driver-content
description: The IoSetSystemPartition routine sets the boot partition for the system.
old-location: kernel\iosetsystempartition.htm
ms.assetid: f1606881-da8b-4034-bbdf-53c75e594032
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetSystemPartition
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
ms.keywords: IoSetSystemPartition
req.iface: 
---

# IoSetSystemPartition function



## -description
<p>The <b>IoSetSystemPartition</b> routine sets the boot partition for the system.</p>


## -syntax

````
NTSTATUS IoSetSystemPartition(
  _In_ PUNICODE_STRING VolumeNameString
);
````


## -parameters
<dl>

### -param <i>VolumeNameString</i> [in]

<dd>
<p>Pointer to a Unicode string that specifies the MS-DOS name of the system partition. </p>
</dd>
</dl>

## -returns
<p>STATUS_SUCCESS if the boot partition can be set, or an error code on failure. </p>

## -remarks
<p>The specified partition must contain the boot loader.</p>

<p>The specified partition must contain the boot loader.</p>

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
<p>Available in Windows XP and later versions of Windows. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
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