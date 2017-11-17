---
UID: NC.d3d12umddi.PFND3D12DDI_BLT
title: PFND3D12DDI_BLT
author: windows-driver-content
description: 
ms.assetid: 27e26081-8ce7-4b30-ae7d-81a35d008291
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

# PFND3D12DDI_BLT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_BLT Pfnd3d12ddiBlt; 

// Definition

VOID Pfnd3d12ddiBlt 
(
	 D3D12DDI_HCOMMANDLIST
	CONST D3D12DDIARG_BLT *
)
{...}

PFND3D12DDI_BLT 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also