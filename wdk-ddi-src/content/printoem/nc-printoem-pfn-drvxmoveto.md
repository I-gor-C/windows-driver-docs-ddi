---
UID: NC.printoem.PFN_DrvXMoveTo
title: PFN_DrvXMoveTo
author: windows-driver-content
description: 
ms.assetid: e01db5d4-c5e4-4019-bf0f-49bdbcef2da2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: printoem.h
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

# PFN_DrvXMoveTo callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvXMoveTo PfnDrvxmoveto; 

// Definition

INT PfnDrvxmoveto 
(
	PDEVOBJ pdevobj
	INT x
	DWORD dwFlags
)
{...}

PFN_DrvXMoveTo 


```

## -parameters

### -param pdevobj: 
### -param x: 
### -param dwFlags: 



## -returns

Returns INT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also