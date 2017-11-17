---
UID: NC.d3dkmddi.DXGKDDI_PATCH
title: DXGKDDI_PATCH
author: windows-driver-content
description: 
ms.assetid: de9ba2d8-618c-4f53-ad7c-2f1e141c652b
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

# DXGKDDI_PATCH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_PATCH DxgkddiPatch; 

// Definition

NTSTATUS DxgkddiPatch 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_PATCH pPatch
)
{...}

DXGKDDI_PATCH PDXGKDDI_PATCH


```

## -parameters

### -param hAdapter: 
### -param pPatch: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also