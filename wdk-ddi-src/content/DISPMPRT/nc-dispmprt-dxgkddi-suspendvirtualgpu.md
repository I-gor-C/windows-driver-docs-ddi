---
UID: NC.dispmprt.DXGKDDI_SUSPENDVIRTUALGPU
title: DXGKDDI_SUSPENDVIRTUALGPU
author: windows-driver-content
description: 
ms.assetid: cd71bbcc-bf52-4b66-86b9-5893b2a483b0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
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

# DXGKDDI_SUSPENDVIRTUALGPU callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SUSPENDVIRTUALGPU DxgkddiSuspendvirtualgpu; 

// Definition

NTSTATUS DxgkddiSuspendvirtualgpu 
(
	HANDLE Context
	DXGKARG_SUSPENDVIRTUALGPU * pArgs
)
{...}

DXGKDDI_SUSPENDVIRTUALGPU PDXGKDDI_SUSPENDVIRTUALGPU


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also