---
UID: NE.d3dkmddi._DXGK_MEMORY_TRANSFER_DIRECTION
title: DXGK_MEMORY_TRANSFER_DIRECTION
author: windows-driver-content
description: DXGK_MEMORY_TRANSFER_DIRECTION is used as part of an allocation transfer operation to specify the direction of the transfer.
old-location: display\dxgk_memory_transfer_direction.htm
old-project: display
ms.assetid: A45411DF-AD08-4349-A134-091343E7989E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MEMORY_TRANSFER_DIRECTION
req.alt-loc: d3dkmddi.h
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
req.iface: 
---

# DXGK_MEMORY_TRANSFER_DIRECTION enumeration



## -description
<p><b>DXGK_MEMORY_TRANSFER_DIRECTION</b> is used as part of an allocation transfer operation to specify the direction of the transfer.

</p>


## -syntax

````
typedef enum _DXGK_MEMORY_TRANSFER_DIRECTION { 
  DXGK_MEMORY_TRANSFER_LOCAL_TO_SYSTEM  = 0,
  DXGK_MEMORY_TRANSFER_SYSTEM_TO_LOCAL  = 1,
  DXGK_MEMORY_TRANSFER_LOCAL_TO_LOCAL   = 2
} DXGK_MEMORY_TRANSFER_DIRECTION;
````


## -enum-fields
<dl>

### -field <a id="DXGK_MEMORY_TRANSFER_LOCAL_TO_SYSTEM"></a><a id="dxgk_memory_transfer_local_to_system"></a><b>DXGK_MEMORY_TRANSFER_LOCAL_TO_SYSTEM</b>

<dd>
<p>Transfer from local GPU memory to system memory.</p>
</dd>

### -field <a id="DXGK_MEMORY_TRANSFER_SYSTEM_TO_LOCAL"></a><a id="dxgk_memory_transfer_system_to_local"></a><b>DXGK_MEMORY_TRANSFER_SYSTEM_TO_LOCAL</b>

<dd>
<p>Transfer from system memory to local GPU memory.</p>
</dd>

### -field <a id="DXGK_MEMORY_TRANSFER_LOCAL_TO_LOCAL"></a><a id="dxgk_memory_transfer_local_to_local"></a><b>DXGK_MEMORY_TRANSFER_LOCAL_TO_LOCAL</b>

<dd>
<p>Transfer from local GPU memory to local GPU memory.</p>
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
<p>Windows 10</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>