---
UID: NC.d3dkmddi.DXGKDDI_GETROOTPAGETABLESIZE
title: DXGKDDI_GETROOTPAGETABLESIZE
author: windows-driver-content
description: 
ms.assetid: b324f4fb-18a8-4f83-9619-33803e3beb9b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKDDI_GETROOTPAGETABLESIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_GETROOTPAGETABLESIZE DxgkddiGetrootpagetablesize; 

// Definition

SIZE_T DxgkddiGetrootpagetablesize 
(
	IN_CONST_HANDLE hAdapter
	INOUT_PDXGKARG_GETROOTPAGETABLESIZE pArgs
)
{...}

DXGKDDI_GETROOTPAGETABLESIZE PDXGKDDI_GETROOTPAGETABLESIZE


```

## -parameters

### -param hAdapter: 
### -param pArgs: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also