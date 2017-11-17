---
UID: NC.dispmprt.DXGKDDI_DESTROYVIRTUALGPU
title: DXGKDDI_DESTROYVIRTUALGPU
author: windows-driver-content
description: 
ms.assetid: 4a8f7a1c-cbd1-4e02-9444-57660a09448e
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

# DXGKDDI_DESTROYVIRTUALGPU callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_DESTROYVIRTUALGPU DxgkddiDestroyvirtualgpu; 

// Definition

NTSTATUS DxgkddiDestroyvirtualgpu 
(
	HANDLE Context
	DXGKARG_DESTROYVIRTUALGPU * pArgs
)
{...}

DXGKDDI_DESTROYVIRTUALGPU PDXGKDDI_DESTROYVIRTUALGPU


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