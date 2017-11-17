---
UID: NC.d3d12umddi.PFND3D12DDI_DISPATCH
title: PFND3D12DDI_DISPATCH
author: windows-driver-content
description: 
ms.assetid: c6de5815-30d2-48da-8fad-7a41ed5d9d2d
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

# PFND3D12DDI_DISPATCH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DISPATCH Pfnd3d12ddiDispatch; 

// Definition

VOID Pfnd3d12ddiDispatch 
(
	 D3D12DDI_HCOMMANDLIST
	 UINT
	 UINT
	 UINT
)
{...}

PFND3D12DDI_DISPATCH 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param UINT: 
### -param UINT: 
### -param UINT: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also