---
UID: NS.mpiowmi._GetPathConfiguration_OUT
title: GetPathConfiguration_OUT
author: windows-driver-content
description: The GetPathConfiguration_OUT structure is used to report the output parameters that are associated with the GetPathConfiguration method.
old-location: storage\getpathconfiguration_out.htm
ms.assetid: 055db46e-59fc-4eb9-93d7-16d680495220
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
req.alt-api: GetPathConfiguration_OUT
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
ms.keywords: GetPathConfiguration_OUT, GetPathConfiguration_OUT, *PGetPathConfiguration_OUT
req.iface: 
---

# GetPathConfiguration_OUT structure



## -description
<p>The GetPathConfiguration_OUT structure is used to report the output parameters that are associated with the GetPathConfiguration method.</p>


## -syntax

````
typedef struct _GetPathConfiguration_OUT {
  ULONG     EntryCount;
  SCSI_ADDR Address[1];
} GetPathConfiguration_OUT, *PGetPathConfiguration_OUT;
````


## -struct-fields
<dl>

### -field <b>EntryCount</b>

<dd>
<p>A 32-bitfield that indicates the number of entries contained in the array of SCSI addresses.</p>
</dd>

### -field <b>Address</b>

<dd>
<p>An array that returns information about the SCSI addresses. The number of elements in the array is given by EntryCount and each element of the array represents an instance of an SCSI_ADDR structure.</p>
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