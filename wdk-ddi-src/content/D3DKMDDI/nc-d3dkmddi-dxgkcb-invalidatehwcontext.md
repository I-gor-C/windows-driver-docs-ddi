---
UID: NC.d3dkmddi.DXGKCB_INVALIDATEHWCONTEXT
title: DXGKCB_INVALIDATEHWCONTEXT
author: windows-driver-content
description: 
ms.assetid: b440e8c8-7deb-44d0-bc65-4f02b33a4f17
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

# DXGKCB_INVALIDATEHWCONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKCB_INVALIDATEHWCONTEXT DxgkcbInvalidatehwcontext; 

// Definition

NTSTATUS DxgkcbInvalidatehwcontext 
(
)
{...}

DXGKCB_INVALIDATEHWCONTEXT 


```

## -parameters




## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also