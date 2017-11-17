---
UID: NC.dispmprt.DXGKDDI_RESUMEVIRTUALGPU
title: DXGKDDI_RESUMEVIRTUALGPU
author: windows-driver-content
description: 
ms.assetid: 5a97a025-46e4-4622-9631-21c0f1ea77fb
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

# DXGKDDI_RESUMEVIRTUALGPU callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_RESUMEVIRTUALGPU DxgkddiResumevirtualgpu; 

// Definition

NTSTATUS DxgkddiResumevirtualgpu 
(
	HANDLE Context
	DXGKARG_RESUMEVIRTUALGPU * pArgs
)
{...}

DXGKDDI_RESUMEVIRTUALGPU PDXGKDDI_RESUMEVIRTUALGPU


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