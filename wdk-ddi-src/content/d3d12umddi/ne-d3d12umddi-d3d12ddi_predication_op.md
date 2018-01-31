---
UID : NE:d3d12umddi.D3D12DDI_PREDICATION_OP
title : D3D12DDI_PREDICATION_OP
author : windows-driver-content
description : Contains values for predication operation options.
old-location : display\d3d12ddi_predication_op.htm
old-project : display
ms.assetid : 70676251-BCD7-4996-B5B7-96A8D9B107DB
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDI_PREDICATION_OP, D3D12DDI_PREDICATION_OP_NOT_EQUAL_ZERO, d3d12umddi/D3D12DDI_PREDICATION_OP, D3D12DDI_PREDICATION_OP_EQUAL_ZERO, D3D12DDI_PREDICATION_OP enumeration [Display Devices], display.d3d12ddi_predication_op, d3d12umddi/D3D12DDI_PREDICATION_OP_EQUAL_ZERO, d3d12umddi/D3D12DDI_PREDICATION_OP_NOT_EQUAL_ZERO
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
req.typenames : D3D12DDI_PREDICATION_OP
---

# D3D12DDI_PREDICATION_OP Enumeration
Contains values for predication operation options.

## Syntax
````
typedef enum D3D12DDI_PREDICATION_OP { 
  D3D12DDI_PREDICATION_OP_EQUAL_ZERO      = 0,
  D3D12DDI_PREDICATION_OP_NOT_EQUAL_ZERO  = 1
} D3D12DDI_PREDICATION_OP;
````

## Constants

<table>

<tr>
<td>D3D12DDI_PREDICATION_OP_EQUAL_ZERO</td>
<td>All the bits in a 64 bit buffer are zero (0).</td>
</tr>

<tr>
<td>D3D12DDI_PREDICATION_OP_NOT_EQUAL_ZERO</td>
<td>Not all of the bits in a 64 bit buffer are zero (0).</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |