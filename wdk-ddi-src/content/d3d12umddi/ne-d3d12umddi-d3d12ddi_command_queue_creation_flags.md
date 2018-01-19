---
UID : NE:d3d12umddi.D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
title : D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
author : windows-driver-content
description : Defines command queue creation options.
old-location : display\d3d12ddi_command_queue_creation_flags.htm
old-project : display
ms.assetid : 6BA4B1B4-07D6-4498-BDA4-C559FB3E8843
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS, D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
req.alt-loc : D3d12umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS
---

# D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS Enumeration
Defines command queue creation options.

## Syntax
````
typedef enum D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS { 
  D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_NONE                      = 0x00000000,
  D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_GLOBAL_REALTIME_PRIORITY  = 0x00000001
} D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS;
````

## Constants

<table>

<tr>
<td>D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_GLOBAL_REALTIME_PRIORITY</td>
<td>Requires global real-time priority.</td>
</tr>

<tr>
<td>D3D12DDI_COMMAND_QUEUE_CREATION_FLAG_NONE</td>
<td>Create queue with default value.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |