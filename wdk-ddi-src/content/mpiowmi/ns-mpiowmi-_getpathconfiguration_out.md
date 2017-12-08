---
UID: NS.MPIOWMI._GETPATHCONFIGURATION_OUT
title: _GetPathConfiguration_OUT
author: windows-driver-content
description: The GetPathConfiguration_OUT structure is used to report the output parameters that are associated with the GetPathConfiguration method.
old-location: storage\getpathconfiguration_out.htm
old-project: storage
ms.assetid: 055db46e-59fc-4eb9-93d7-16d680495220
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _GetPathConfiguration_OUT, GetPathConfiguration_OUT, *PGetPathConfiguration_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# _GetPathConfiguration_OUT structure



## -description
The GetPathConfiguration_OUT structure is used to report the output parameters that are associated with the GetPathConfiguration method.


## -syntax

````
typedef struct _GetPathConfiguration_OUT {
  ULONG     EntryCount;
  SCSI_ADDR Address[1];
} GetPathConfiguration_OUT, *PGetPathConfiguration_OUT;
````


## -struct-fields

### -field EntryCount

A 32-bitfield that indicates the number of entries contained in the array of SCSI addresses.

### -field Address

An array that returns information about the SCSI addresses. The number of elements in the array is given by EntryCount and each element of the array represents an instance of an SCSI_ADDR structure.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>