---
UID: NS.mpiowmi._MPIOMoveDevice_IN
title: MPIOMoveDevice_IN
author: windows-driver-content
description: The MPIOMoveDevice_IN structure is used to set the active path on the device.
old-location: storage\mpiomovedevice_in.htm
ms.assetid: 2652874f-70d0-4eff-a46d-778a68d55cab
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
req.alt-api: MPIOMoveDevice_IN
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
ms.keywords: MPIOMoveDevice_IN, MPIOMoveDevice_IN, *PMPIOMoveDevice_IN
req.iface: 
---

# MPIOMoveDevice_IN structure



## -description
<p>The MPIOMoveDevice_IN structure is used to set the active path on the device.</p>


## -syntax

````
typedef struct _MPIOMoveDevice_IN {
  ULONG     DiskOrdinal;
  ULONG     Flags;
  ULONGLONG PathID;
} MPIOMoveDevice_IN, *PMPIOMoveDevice_IN;
````


## -struct-fields
<dl>

### -field <b>DiskOrdinal</b>

<dd>
<p>A 32-bitfield that specifies the MPIO disk ordinal value.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A 32-bitfield that specifies the flags that are associated with the device move operation.</p>
</dd>

### -field <b>PathID</b>

<dd>
<p>A 64-bitfield that specifies the path that is associated with the device.</p>
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