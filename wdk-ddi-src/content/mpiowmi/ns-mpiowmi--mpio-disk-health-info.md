---
UID: NS.mpiowmi._MPIO_DISK_HEALTH_INFO
title: MPIO_DISK_HEALTH_INFO
author: windows-driver-content
description: The MPIO_DISK_HEALTH_INFO structure is used to query the available health information for every multi-path disk in the system.
old-location: storage\mpio_disk_health_info.htm
old-project: storage
ms.assetid: 20813e29-907f-42b0-9229-a9ef78f46e1d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_DISK_HEALTH_INFO, MPIO_DISK_HEALTH_INFO, *PMPIO_DISK_HEALTH_INFO
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
req.alt-api: MPIO_DISK_HEALTH_INFO
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
req.iface: 
---

# MPIO_DISK_HEALTH_INFO structure



## -description
<p>The MPIO_DISK_HEALTH_INFO structure is used to query the available health information for every multi-path disk in the system.</p>


## -syntax

````
typedef struct _MPIO_DISK_HEALTH_INFO {
  ULONG                  NumberDiskPackets;
  ULONG                  Reserved;
  MPIO_DISK_HEALTH_CLASS DiskHealthPackets[1];
} MPIO_DISK_HEALTH_INFO, *PMPIO_DISK_HEALTH_INFO;
````


## -struct-fields
<dl>

### -field <b>NumberDiskPackets</b>

<dd>
<p>An unsigned 32-bitfield that returns the number of available health packets that correspond to the number of multi-path disks under MPIO control.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>DiskHealthPackets</b>

<dd>
<p>An array of health information packets for all the available multi-path disks under MPIO control. The number of elements in the array is given by NumberDiskPackets, and each element of the array is an instance of an MPIO_DISK_HEALTH_CLASS structure.</p>
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