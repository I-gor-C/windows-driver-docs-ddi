---
UID: NC.ntifs.PRELEASE_FROM_READ_AHEAD
title: PRELEASE_FROM_READ_AHEAD
author: windows-driver-content
description: 
ms.assetid: 1d054a58-cb91-41c9-aa91-bcf534361d63
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PRELEASE_FROM_READ_AHEAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRELEASE_FROM_READ_AHEAD PreleaseFromReadAhead; 

// Definition

VOID PreleaseFromReadAhead 
(
	PVOID Context
)
{...}

PRELEASE_FROM_READ_AHEAD 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also