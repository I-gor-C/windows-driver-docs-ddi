---
UID: NC.dispmprt.DXGKDDI_SETVIRTUALFUNCTIONPOWERSTATE
title: DXGKDDI_SETVIRTUALFUNCTIONPOWERSTATE
author: windows-driver-content
description: 
ms.assetid: 57a7f9f8-c9b4-48f6-b3bd-c89b27a7245b
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

# DXGKDDI_SETVIRTUALFUNCTIONPOWERSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETVIRTUALFUNCTIONPOWERSTATE DxgkddiSetvirtualfunctionpowerstate; 

// Definition

NTSTATUS DxgkddiSetvirtualfunctionpowerstate 
(
	HANDLE Context
	DXGKARG_SETVIRTUALFUNCTIONPOWERSTATE * pArgs
)
{...}

DXGKDDI_SETVIRTUALFUNCTIONPOWERSTATE PDXGKDDI_SETVIRTUALFUNCTIONPOWERSTATE


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