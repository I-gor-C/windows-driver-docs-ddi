---
UID: NC.d3d12umddi.PFND3D12DDI_SET_ROOT_32BIT_CONSTANT
title: PFND3D12DDI_SET_ROOT_32BIT_CONSTANT
author: windows-driver-content
description: 
ms.assetid: 3e78f195-31ce-43ad-8af5-17247efaf530
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

# PFND3D12DDI_SET_ROOT_32BIT_CONSTANT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SET_ROOT_32BIT_CONSTANT Pfnd3d12ddiSetRoot32BitConstant; 

// Definition

VOID Pfnd3d12ddiSetRoot32BitConstant 
(
	 D3D12DDI_HCOMMANDLIST
	UINT RootParameterIndex
	UINT SrcData
	UINT DestOffsetIn32BitValues
)
{...}

PFND3D12DDI_SET_ROOT_32BIT_CONSTANT 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param RootParameterIndex: 
### -param SrcData: 
### -param DestOffsetIn32BitValues: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also