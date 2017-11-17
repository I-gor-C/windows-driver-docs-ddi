---
UID: NC.bthsdpddi.PBYTESWAPUINT128
title: PBYTESWAPUINT128
author: windows-driver-content
description: 
ms.assetid: 50360c73-84eb-4395-89f0-bf8a810c23f5
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

# PBYTESWAPUINT128 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBYTESWAPUINT128 Pbyteswapuint128; 

// Definition

void Pbyteswapuint128 
(
	PSDP_ULARGE_INTEGER_16 pInUint128
	PSDP_ULARGE_INTEGER_16 pOutUint128
)
{...}

PBYTESWAPUINT128 


```

## -parameters

### -param pInUint128: 
### -param pOutUint128: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also