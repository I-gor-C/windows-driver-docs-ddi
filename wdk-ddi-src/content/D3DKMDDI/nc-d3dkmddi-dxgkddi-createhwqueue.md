---
UID: NC.d3dkmddi.DXGKDDI_CREATEHWQUEUE
title: DXGKDDI_CREATEHWQUEUE
author: windows-driver-content
description: 
ms.assetid: 7bc46fe1-bb28-4566-86a8-9f190c2ab0c6
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

# DXGKDDI_CREATEHWQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CREATEHWQUEUE DxgkddiCreatehwqueue; 

// Definition

NTSTATUS DxgkddiCreatehwqueue 
(
	IN_CONST_HANDLE hHwContext
	INOUT_PDXGKARG_CREATEHWQUEUE pCreateHwQueue
)
{...}

DXGKDDI_CREATEHWQUEUE PDXGKDDI_CREATEHWQUEUE


```

## -parameters

### -param hHwContext: 
### -param pCreateHwQueue: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also