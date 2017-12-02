---
UID: NF.ntddk.IoGetSiloParameters
title: IoGetSiloParameters
author: windows-driver-content
description: This routine indicates if a file is within a Container context.
old-location: ifsk\iogetsiloparameters.htm
old-project: ifsk
ms.assetid: C8F42E83-2122-4871-972B-9FD06379C271
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IoGetSiloParameters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetSiloParameters
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
req.irql: 
req.iface: 
---

# IoGetSiloParameters function



## -description
<p>This routine indicates if a file is within a Container context.</p>


## -syntax

````
PIO_FOEXT_SILO_PARAMETERS IoGetSiloParameters(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param FileObject [in]

<dd>
<p>The file in question.</p>
</dd>
</dl>

## -returns
<p>If <b>null</b>, the file is not in a container context. Otherwise, a non-null value of type <a href="..\ntddk\ns-ntddk--io-foext-silo-parameters.md">IO_FOEXT_SILO_PARAMETERS</a> indicates that the file is within a Container context.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1607</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
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
</table>