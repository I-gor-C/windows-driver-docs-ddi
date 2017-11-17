---
UID: NC.d3d12umddi.PFND3D12DDI_PRESENT_0028
title: PFND3D12DDI_PRESENT_0028
author: windows-driver-content
description: 
ms.assetid: 73c76a92-a925-40e4-b4ca-90e1026d9876
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

# PFND3D12DDI_PRESENT_0028 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_PRESENT_0028 Pfnd3d12ddiPresent0028; 

// Definition

VOID Pfnd3d12ddiPresent0028 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HCOMMANDQUEUE
	CONST D3D12DDIARG_PRESENT_0001 *
	D3D12DDI_PRESENT_0028 *
)
{...}

PFND3D12DDI_PRESENT_0028 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HCOMMANDQUEUE: 
### -param *: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also