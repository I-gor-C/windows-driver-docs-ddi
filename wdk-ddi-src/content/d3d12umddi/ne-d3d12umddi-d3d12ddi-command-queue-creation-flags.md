---
UID: NE.d3d12umddi.D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
title: D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
author: windows-driver-content
description: Defines command queue creation options.
old-location: display\d3d12ddi_command_queue_creation_flags.htm
old-project: display
ms.assetid: 6BA4B1B4-07D6-4498-BDA4-C559FB3E8843
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS enumeration



## -description
<p>Defines command queue creation options. </p>


## -syntax

````
typedef enum D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS { 
  D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_NONE                      = 0x00000000,
  D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_GLOBAL_REALTIME_PRIORITY  = 0x00000001
} D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS;
````


## -enum-fields
<dl>

### -field D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_NONE

<dd>
<p>Create queue with default value.</p>
</dd>

### -field D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_GLOBAL_REALTIME_PRIORITY

<dd>
<p>Requires global real-time priority.</p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>