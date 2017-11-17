---
UID: NC.d3d12umddi.PFND3D12DDI_IA_SET_INDEX_BUFFER
title: PFND3D12DDI_IA_SET_INDEX_BUFFER
author: windows-driver-content
description: 
ms.assetid: d6363250-3ec4-4cb8-abf8-ea83a29f1989
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

# PFND3D12DDI_IA_SET_INDEX_BUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_IA_SET_INDEX_BUFFER Pfnd3d12ddiIaSetIndexBuffer; 

// Definition

VOID Pfnd3d12ddiIaSetIndexBuffer 
(
	 D3D12DDI_HCOMMANDLIST
	CONST D3D12DDI_INDEX_BUFFER_VIEW *pDesc
)
{...}

PFND3D12DDI_IA_SET_INDEX_BUFFER 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param *pDesc: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also