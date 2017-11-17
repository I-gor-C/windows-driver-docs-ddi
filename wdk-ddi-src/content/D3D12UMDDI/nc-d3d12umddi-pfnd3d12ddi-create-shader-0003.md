---
UID: NC.d3d12umddi.PFND3D12DDI_CREATE_SHADER_0003
title: PFND3D12DDI_CREATE_SHADER_0003
author: windows-driver-content
description: 
ms.assetid: e1f9e059-1de3-407e-8e5a-c9c7f26ab6c7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PFND3D12DDI_CREATE_SHADER_0003 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CREATE_SHADER_0003 Pfnd3d12ddiCreateShader0003; 

// Definition

VOID Pfnd3d12ddiCreateShader0003 
(
	 D3D12DDI_HDEVICE
	CONST UINT *pShaderCode
	 D3D12DDI_HROOTSIGNATURE
	 D3D12DDI_HSHADER
	CONST D3D12DDIARG_STAGE_IO_SIGNATURES *
	 D3D12DDI_CREATE_SHADER_FLAGS
)
{...}

PFND3D12DDI_CREATE_SHADER_0003 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *pShaderCode: 
### -param D3D12DDI_HROOTSIGNATURE: 
### -param D3D12DDI_HSHADER: 
### -param *: 
### -param D3D12DDI_CREATE_SHADER_FLAGS: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also