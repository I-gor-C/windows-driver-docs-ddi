---
UID: NC.bthsdpddi.PRETRIEVEUINT128
title: PRETRIEVEUINT128
author: windows-driver-content
description: 
ms.assetid: 900eb59f-23e6-4118-bcdf-dd11c83f6347
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: bthsdpddi.h
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

# PRETRIEVEUINT128 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRETRIEVEUINT128 Pretrieveuint128; 

// Definition

void Pretrieveuint128 
(
	PUCHAR Stream
	PSDP_ULARGE_INTEGER_16 pUint128
)
{...}

PRETRIEVEUINT128 


```

## -parameters

### -param Stream: 
### -param pUint128: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also