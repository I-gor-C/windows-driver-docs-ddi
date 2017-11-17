---
UID: NC.extsfns.EXT_DECODE_ERROR
title: EXT_DECODE_ERROR
author: windows-driver-content
description: 
ms.assetid: 2f1d4e5f-b9e1-4f92-b13c-80e06253c438
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# EXT_DECODE_ERROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_DECODE_ERROR ExtDecodeError; 

// Definition

VOID ExtDecodeError 
(
	PDEBUG_DECODE_ERROR pDecodeError
)
{...}

EXT_DECODE_ERROR 


```

## -parameters

### -param pDecodeError: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also