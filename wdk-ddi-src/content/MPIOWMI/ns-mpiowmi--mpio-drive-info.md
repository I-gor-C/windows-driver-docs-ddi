---
UID: NS.mpiowmi._MPIO_DRIVE_INFO
title: MPIO_DRIVE_INFO
author: windows-driver-content
description: The MPIO_DRIVE_INFO structure represents a multi-path disk in the system.
old-location: storage\mpio_drive_info.htm
ms.assetid: 38d79fae-9701-4e92-bf73-4732e02c17ab
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_DRIVE_INFO
req.alt-loc: mpiowmi.h
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
ms.keywords: MPIO_DRIVE_INFO, MPIO_DRIVE_INFO, *PMPIO_DRIVE_INFO
req.iface: 
---

# MPIO_DRIVE_INFO structure



## -description
<p>The MPIO_DRIVE_INFO structure represents a multi-path disk in the system.</p>


## -syntax

````
typedef struct _MPIO_DRIVE_INFO {
  ULONG NumberPaths;
  WCHAR Name[63 + 1];
  WCHAR SerialNumber[63 + 1];
  WCHAR DsmName[63 + 1];
} MPIO_DRIVE_INFO, *PMPIO_DRIVE_INFO;
````


## -struct-fields
<dl>

### -field <b>NumberPaths</b>

<dd>
<p>An unsigned 32-bitfield that represents the number of paths to the LUN.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>A string field (of maximum length 63 characters) that returns the device name that was created by MPIO for the LUN.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>A string field (of maximum length 63 characters) that returns the serial number that was created for the LUN by either the DSM or by MPIO itself.</p>
</dd>

### -field <b>DsmName</b>

<dd>
<p>A string field (of maximum length 63 characters) that returns the friendly name of the controlling DSM for the device.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>