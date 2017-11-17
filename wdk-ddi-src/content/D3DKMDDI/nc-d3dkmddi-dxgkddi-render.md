---
UID: NC.d3dkmddi.DXGKDDI_RENDER
title: DXGKDDI_RENDER
author: windows-driver-content
description: 
ms.assetid: 3f089d64-f5f8-4ef9-8021-46a40b7735ff
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

# DXGKDDI_RENDER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_RENDER DxgkddiRender; 

// Definition

NTSTATUS DxgkddiRender 
(
	IN_CONST_HANDLE hContext
	INOUT_PDXGKARG_RENDER pRender
)
{...}

DXGKDDI_RENDER PDXGKDDI_RENDER


```

## -parameters

### -param hContext: 
### -param pRender: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also