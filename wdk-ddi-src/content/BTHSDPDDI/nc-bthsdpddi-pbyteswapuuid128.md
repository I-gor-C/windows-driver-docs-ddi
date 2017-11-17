---
UID: NC.bthsdpddi.PBYTESWAPUUID128
title: PBYTESWAPUUID128
author: windows-driver-content
description: 
ms.assetid: 1e301ed1-eafd-42e8-b6ec-1ca8cd5a51ce
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

# PBYTESWAPUUID128 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBYTESWAPUUID128 Pbyteswapuuid128; 

// Definition

void Pbyteswapuuid128 
(
	GUID *pUuidFrom
	GUID *pUuiidTo
)
{...}

PBYTESWAPUUID128 


```

## -parameters

### -param *pUuidFrom: 
### -param *pUuiidTo: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also