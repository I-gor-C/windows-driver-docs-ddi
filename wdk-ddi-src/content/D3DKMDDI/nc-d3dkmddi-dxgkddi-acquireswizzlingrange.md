---
UID: NC.d3dkmddi.DXGKDDI_ACQUIRESWIZZLINGRANGE
title: DXGKDDI_ACQUIRESWIZZLINGRANGE
author: windows-driver-content
description: 
ms.assetid: 030eccd2-3607-4203-973b-c04289e1670b
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

# DXGKDDI_ACQUIRESWIZZLINGRANGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_ACQUIRESWIZZLINGRANGE DxgkddiAcquireswizzlingrange; 

// Definition

NTSTATUS DxgkddiAcquireswizzlingrange 
(
	IN_CONST_HANDLE hAdapter
	INOUT_PDXGKARG_ACQUIRESWIZZLINGRANGE pAcquireSwizzlingRange
)
{...}

DXGKDDI_ACQUIRESWIZZLINGRANGE PDXGKDDI_ACQUIRESWIZZLINGRANGE


```

## -parameters

### -param hAdapter: 
### -param pAcquireSwizzlingRange: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also