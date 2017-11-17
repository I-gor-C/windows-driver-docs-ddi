---
UID: NF.ntddk.IoGetSiloParameters
title: IoGetSiloParameters
author: windows-driver-content
description: This routine indicates if a file is within a Container context.
old-location: ifsk\iogetsiloparameters.htm
ms.assetid: C8F42E83-2122-4871-972B-9FD06379C271
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetSiloParameters
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: IoGetSiloParameters
req.iface: 
---

# IoGetSiloParameters function



## -description
<p>This routine indicates if a file is within a Container context.</p>


## -syntax

````
PIO_FOEXT_SILO_PARAMETERS IoGetSiloParameters;

PIO_FOEXT_SILO_PARAMETERS IoGetSiloParameters(
  _In_ PFILE_OBJECT FileObject
)
{ ... }
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>The file in question.</p>
</dd>
</dl>

## -returns
<p>If <b>null</b>, the file is not in a container context. Otherwise, a non-null value of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt734263">IO_FOEXT_SILO_PARAMETERS</a> indicates that the file is within a Container context.</p>

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
</table>