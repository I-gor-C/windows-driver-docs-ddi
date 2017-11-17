---
UID: NS.d3d12umddi.D3D12DDIARG_CREATECOMMANDQUEUE_0023
title: D3D12DDIARG_CREATECOMMANDQUEUE_0023
author: windows-driver-content
description: Contains arguments used to create a command queue.
old-location: display\d3d12ddiarg_createcommandqueue_0023.htm
ms.assetid: F8194BA0-325F-48B8-994F-FA2EA80C70D9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDIARG_CREATECOMMANDQUEUE_0023
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
ms.keywords: D3D12DDIARG_CREATECOMMANDQUEUE_0023, D3D12DDIARG_CREATECOMMANDQUEUE_0023
req.iface: 
---

# D3D12DDIARG_CREATECOMMANDQUEUE_0023 structure



## -description
<p>Contains arguments used to create a command queue.</p>


## -syntax

````
typedef struct D3D12DDIARG_CREATECOMMANDQUEUE_0023 {
  D3D12DDI_COMMAND_QUEUE_FLAGS          QueueFlags;
  UINT                                  NodeMask;
  D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS QueueCreationFlags;
} D3D12DDIARG_CREATECOMMANDQUEUE_0023;
````


## -struct-fields
<dl>

### -field <b>QueueFlags</b>

<dd>
<p>Command queue flags. </p>
</dd>

### -field <b>NodeMask</b>

<dd>
<p>A mask for a node.</p>
</dd>

### -field <b>QueueCreationFlags</b>

<dd>
<p>Command queue creation flag, as a <a href="https://msdn.microsoft.com/6BA4B1B4-07D6-4498-BDA4-C559FB3E8843">D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS</a> value. </p>
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