---
UID : NS:d3d12umddi.D3D12DDIARG_CREATECOMMANDQUEUE_0023
title : D3D12DDIARG_CREATECOMMANDQUEUE_0023
author : windows-driver-content
description : Contains arguments used to create a command queue.
old-location : display\d3d12ddiarg_createcommandqueue_0023.htm
old-project : display
ms.assetid : F8194BA0-325F-48B8-994F-FA2EA80C70D9
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDIARG_CREATECOMMANDQUEUE_0023, D3D12DDIARG_CREATECOMMANDQUEUE_0023 structure [Display Devices], display.d3d12ddiarg_createcommandqueue_0023, d3d12umddi/D3D12DDIARG_CREATECOMMANDQUEUE_0023
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3D12DDIARG_CREATECOMMANDQUEUE_0023
---

# D3D12DDIARG_CREATECOMMANDQUEUE_0023 structure
Contains arguments used to create a command queue.

## Syntax
````
typedef struct D3D12DDIARG_CREATECOMMANDQUEUE_0023 {
  D3D12DDI_COMMAND_QUEUE_FLAGS          QueueFlags;
  UINT                                  NodeMask;
  D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS QueueCreationFlags;
} D3D12DDIARG_CREATECOMMANDQUEUE_0023;
````

## Members


`NodeMask`

A mask for a node.

`QueueCreationFlags`

Command queue creation flag, as a <a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi_command_queue_creation_flags.md">D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS</a> value.

`QueueFlags`

Command queue flags.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |