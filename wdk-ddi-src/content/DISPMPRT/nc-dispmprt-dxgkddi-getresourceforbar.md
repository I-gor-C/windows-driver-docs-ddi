---
UID: NC.dispmprt.DXGKDDI_GETRESOURCEFORBAR
title: DXGKDDI_GETRESOURCEFORBAR
author: windows-driver-content
description: 
ms.assetid: 9f6c1475-0f70-4728-b640-08af83df3e31
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

# DXGKDDI_GETRESOURCEFORBAR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_GETRESOURCEFORBAR DxgkddiGetresourceforbar; 

// Definition

NTSTATUS DxgkddiGetresourceforbar 
(
	HANDLE Context
	DXGKARG_GETRESOURCEFORBAR * pArgs
)
{...}

DXGKDDI_GETRESOURCEFORBAR PDXGKDDI_GETRESOURCEFORBAR


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