---
UID: NC.dispmprt.DXGKDDI_SETVIRTUALGPUVMBUS
title: DXGKDDI_SETVIRTUALGPUVMBUS
author: windows-driver-content
description: 
ms.assetid: c4255dcb-6744-4973-8ffd-fa7f66f78701
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

# DXGKDDI_SETVIRTUALGPUVMBUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETVIRTUALGPUVMBUS DxgkddiSetvirtualgpuvmbus; 

// Definition

NTSTATUS DxgkddiSetvirtualgpuvmbus 
(
	HANDLE Context
	DXGKARG_SETVIRTUALGPUVMBUS * pArgs
)
{...}

DXGKDDI_SETVIRTUALGPUVMBUS PDXGKDDI_SETVIRTUALGPUVMBUS


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