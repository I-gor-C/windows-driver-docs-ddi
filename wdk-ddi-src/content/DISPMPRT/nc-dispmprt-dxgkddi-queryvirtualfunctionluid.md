---
UID: NC.dispmprt.DXGKDDI_QUERYVIRTUALFUNCTIONLUID
title: DXGKDDI_QUERYVIRTUALFUNCTIONLUID
author: windows-driver-content
description: 
ms.assetid: 238f0e48-2513-475d-bf66-610d92a83ac8
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

# DXGKDDI_QUERYVIRTUALFUNCTIONLUID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_QUERYVIRTUALFUNCTIONLUID DxgkddiQueryvirtualfunctionluid; 

// Definition

VOID DxgkddiQueryvirtualfunctionluid 
(
	HANDLE Context
	DXGKARG_QUERYVIRTUALFUNCTIONLUID * pArgs
)
{...}

DXGKDDI_QUERYVIRTUALFUNCTIONLUID PDXGKDDI_QUERYVIRTUALFUNCTIONLUID


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also