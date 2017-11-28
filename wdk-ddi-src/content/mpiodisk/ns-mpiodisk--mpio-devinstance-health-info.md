---
UID: NS.mpiodisk._MPIO_DEVINSTANCE_HEALTH_INFO
title: MPIO_DEVINSTANCE_HEALTH_INFO
author: windows-driver-content
description: The MPIO_DEVINSTANCE_HEALTH_INFO structure is used to query the available health information for every instance of a multi-path disk on each of the paths through which it is exposed.
old-location: storage\mpio_devinstance_health_info.htm
old-project: storage
ms.assetid: 7f254389-58cf-43da-8611-a1598cc2eb66
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_DEVINSTANCE_HEALTH_INFO, MPIO_DEVINSTANCE_HEALTH_INFO, *PMPIO_DEVINSTANCE_HEALTH_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiodisk.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_DEVINSTANCE_HEALTH_INFO
req.alt-loc: mpiodisk.h
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
req.iface: 
---

# MPIO_DEVINSTANCE_HEALTH_INFO structure



## -description
<p>The MPIO_DEVINSTANCE_HEALTH_INFO structure is used to query the available health information for every instance of a multi-path disk on each of the paths through which it is exposed.</p>


## -syntax

````
typedef struct _MPIO_DEVINSTANCE_HEALTH_INFO {
  ULONG                         NumberDevInstancePackets;
  ULONG                         Reserved;
  MPIO_DEVINSTANCE_HEALTH_CLASS DevInstanceHealthPackets[1];
} MPIO_DEVINSTANCE_HEALTH_INFO, *PMPIO_DEVINSTANCE_HEALTH_INFO;
````


## -struct-fields
<dl>

### -field <b>NumberDevInstancePackets</b>

<dd>
<p>An unsigned 32-bitfield that returns the number of health packets that are available and that correspond to the number of available path instances associated with all multi-path disks.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>DevInstanceHealthPackets</b>

<dd>
<p>A field that returns an array with health information about all the available instances of multi-path disks. The number of elements of the array is given by <i>NbrDevInfoPkts</i> and each element of the array is an instance of the MPIO_DEVINSTANCE_HEALTH_CLASS structure.</p>
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
<dt>Mpiodisk.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>