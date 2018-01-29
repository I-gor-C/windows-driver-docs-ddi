---
UID : NE:d3d12umddi.D3D12DDI_HEAP_FLAGS
title : D3D12DDI_HEAP_FLAGS
author : windows-driver-content
description : Contains Direct3D 12 heap flags.
old-location : display\d3d12ddi_heap_flags.htm
old-project : display
ms.assetid : 8224E497-7F52-469B-98C9-ECC5F1970894
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDI_HEAP_FLAG_NON_RT_DS_TEXTURES, d3d12umddi/D3D12DDI_HEAP_FLAG_PRIMARY, D3D12DDI_HEAP_FLAG_CONTENT_PROTECTION, D3D12DDI_HEAP_FLAGS, D3D12DDI_HEAP_FLAG_RT_DS_TEXTURES, d3d12umddi/D3D12DDI_HEAP_FLAG_NON_RT_DS_TEXTURES, d3d12umddi/D3D12DDI_HEAP_FLAGS, d3d12umddi/D3D12DDI_HEAP_FLAG_CONTENT_PROTECTION, d3d12umddi/D3D12DDI_HEAP_FLAG_BUFFERS, D3D12DDI_HEAP_FLAG_COHERENT_SYSTEMWIDE, d3d12umddi/D3D12DDI_HEAP_FLAG_COHERENT_SYSTEMWIDE, D3D12DDI_HEAP_FLAG_PRIMARY, d3d12umddi/D3D12DDI_HEAP_FLAG_RT_DS_TEXTURES, D3D12DDI_HEAP_FLAGS enumeration [Display Devices], D3D12DDI_HEAP_FLAG_NONE, d3d12umddi/D3D12DDI_HEAP_FLAG_NONE, display.d3d12ddi_heap_flags, D3D12DDI_HEAP_FLAG_BUFFERS
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
req.typenames : D3D12DDI_HEAP_FLAGS
---

# D3D12DDI_HEAP_FLAGS Enumeration
Contains Direct3D 12 heap flags.

## Syntax
````
typedef enum D3D12DDI_HEAP_FLAGS { 
  D3D12DDI_HEAP_FLAG_NONE                 = 0x0,
  D3D12DDI_HEAP_FLAG_NON_RT_DS_TEXTURES   = 0x2,
  D3D12DDI_HEAP_FLAG_BUFFERS              = 0x4,
  D3D12DDI_HEAP_FLAG_COHERENT_SYSTEMWIDE  = 0x8,
  D3D12DDI_HEAP_FLAG_PRIMARY              = 0x10,
  D3D12DDI_HEAP_FLAG_RT_DS_TEXTURES       = 0x20,
  D3D12DDI_HEAP_FLAG_CONTENT_PROTECTION   = 0x40
} D3D12DDI_HEAP_FLAGS;
````

## Constants

<table>

<tr>
<td>D3D12DDI_HEAP_FLAG_BUFFERS</td>
<td>The heap supports resources allocated for buffers.</td>
</tr>

<tr>
<td>D3D12DDI_HEAP_FLAG_COHERENT_SYSTEMWIDE</td>
<td>The heap supports resources allocated for coherent systemwide.</td>
</tr>

<tr>
<td>D3D12DDI_HEAP_FLAG_NON_RT_DS_TEXTURES</td>
<td>The heap supports resources allocated for other than Render Target (RT) and Depth-Stencil (DS) textures.</td>
</tr>

<tr>
<td>D3D12DDI_HEAP_FLAG_NONE</td>
<td>No flags.</td>
</tr>

<tr>
<td>D3D12DDI_HEAP_FLAG_PRIMARY</td>
<td>The heap supports resources allocated for primary.</td>
</tr>

<tr>
<td>D3D12DDI_HEAP_FLAG_RT_DS_TEXTURES</td>
<td>The heap supports resources allocated for RT and DS textures.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |