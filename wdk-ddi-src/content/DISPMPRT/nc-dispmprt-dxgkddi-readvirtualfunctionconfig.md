---
UID: NC.dispmprt.DXGKDDI_READVIRTUALFUNCTIONCONFIG
title: DXGKDDI_READVIRTUALFUNCTIONCONFIG
author: windows-driver-content
description: 
ms.assetid: 6b2536c0-1e78-4f00-ab1d-394ba0594f04
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

# DXGKDDI_READVIRTUALFUNCTIONCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_READVIRTUALFUNCTIONCONFIG DxgkddiReadvirtualfunctionconfig; 

// Definition

NTSTATUS DxgkddiReadvirtualfunctionconfig 
(
	HANDLE Context
	DXGKARG_READVIRTUALFUNCTIONCONFIG * pArgs
)
{...}

DXGKDDI_READVIRTUALFUNCTIONCONFIG PDXGKDDI_READVIRTUALFUNCTIONCONFIG


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