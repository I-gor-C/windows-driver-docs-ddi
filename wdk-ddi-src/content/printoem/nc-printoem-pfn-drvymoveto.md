---
UID: NC.printoem.PFN_DrvYMoveTo
title: PFN_DrvYMoveTo
author: windows-driver-content
description: 
ms.assetid: 495ddd8f-317e-4a9a-bf00-bb60c45ec890
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

# PFN_DrvYMoveTo callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvYMoveTo PfnDrvymoveto; 

// Definition

INT PfnDrvymoveto 
(
	PDEVOBJ pdevobj
	INT y
	DWORD dwFlags
)
{...}

PFN_DrvYMoveTo 


```

## -parameters

### -param pdevobj: 
### -param y: 
### -param dwFlags: 



## -returns

Returns INT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also