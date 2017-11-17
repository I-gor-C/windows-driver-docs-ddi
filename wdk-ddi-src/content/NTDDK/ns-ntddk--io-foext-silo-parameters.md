---
UID: NS.ntddk._IO_FOEXT_SILO_PARAMETERS
title: IO_FOEXT_SILO_PARAMETERS
author: windows-driver-content
description: This structure describes the Container context that's identified by the IoGetSiloParameters routine.
old-location: ifsk\io_foext_silo_parameters.htm
ms.assetid: EC7C59D0-96AE-400D-9502-D6DBFD9918DC
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IO_FOEXT_SILO_PARAMETERS
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
req.irql: PASSIVE_LEVEL
ms.keywords: IO_FOEXT_SILO_PARAMETERS, IO_FOEXT_SILO_PARAMETERS, *PIO_FOEXT_SILO_PARAMETERS
req.iface: 
---

# IO_FOEXT_SILO_PARAMETERS structure



## -description
<p>This structure describes the Container context that's identified by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt734262">IoGetSiloParameters</a> routine.</p>


## -syntax

````
typedef struct _IO_FOEXT_SILO_PARAMETERS {
  ULONG  Length;
  PESILO SiloContext;
} IO_FOEXT_SILO_PARAMETERS, *PIO_FOEXT_SILO_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The length of the structure. This also serves as the structure version.</p>
</dd>

### -field <b>SiloContext</b>

<dd>
<p>The container context.</p>
</dd>
</dl>

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