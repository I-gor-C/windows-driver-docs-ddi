---
UID : NE:d3d12umddi.D3D12DDI_CREATE_SHADER_FLAGS
title : D3D12DDI_CREATE_SHADER_FLAGS
author : windows-driver-content
description : Defines flags for shader creation.
old-location : display\d3d12ddi_create_shader_flags.htm
old-project : display
ms.assetid : 93F27775-3E74-4310-8E09-DCB079436706
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDI_CREATE_SHADER_FLAG_NONE, d3d12umddi/D3D12DDI_CREATE_SHADER_FLAG_NONE, d3d12umddi/D3D12DDI_CREATE_SHADER_FLAG_ENABLE_SHADER_TRACING, d3d12umddi/D3D12DDI_CREATE_SHADER_FLAG_DISABLE_OPTIMIZATION, D3D12DDI_CREATE_SHADER_FLAG_DISABLE_OPTIMIZATION, d3d12umddi/D3D12DDI_CREATE_SHADER_FLAGS, D3D12DDI_CREATE_SHADER_FLAG_ENABLE_SHADER_TRACING, D3D12DDI_CREATE_SHADER_FLAGS enumeration [Display Devices], D3D12DDI_CREATE_SHADER_FLAGS, display.d3d12ddi_create_shader_flags
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
req.typenames : D3D12DDI_CREATE_SHADER_FLAGS
---

# D3D12DDI_CREATE_SHADER_FLAGS Enumeration
Defines flags for shader creation.

## Syntax
````
typedef enum D3D12DDI_CREATE_SHADER_FLAGS { 
  D3D12DDI_CREATE_SHADER_FLAG_NONE                   = 0x0,
  D3D12DDI_CREATE_SHADER_FLAG_ENABLE_SHADER_TRACING  = 0x1,
  D3D12DDI_CREATE_SHADER_FLAG_DISABLE_OPTIMIZATION   = 0x2
} D3D12DDI_CREATE_SHADER_FLAGS;
````

## Constants

<table>

<tr>
<td>D3D12DDI_CREATE_SHADER_FLAG_DISABLE_OPTIMIZATION_0024</td>
<td></td>
</tr>

<tr>
<td>D3D12DDI_CREATE_SHADER_FLAG_ENABLE_SHADER_TRACING</td>
<td>The shader is tracing.</td>
</tr>

<tr>
<td>D3D12DDI_CREATE_SHADER_FLAG_NONE</td>
<td>No flag value for shader creation.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |