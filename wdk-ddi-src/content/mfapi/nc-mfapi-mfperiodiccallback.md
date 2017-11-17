---
UID: NC.mfapi.MFPERIODICCALLBACK
title: MFPERIODICCALLBACK
author: windows-driver-content
description: 
ms.assetid: e49e5bf8-dc20-4fcb-b3ef-be067a640df3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mfapi.h
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

# MFPERIODICCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

MFPERIODICCALLBACK Mfperiodiccallback; 

// Definition

void Mfperiodiccallback 
(
	IUnknown *pContext
)
{...}

MFPERIODICCALLBACK 


```

## -parameters

### -param *pContext: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also