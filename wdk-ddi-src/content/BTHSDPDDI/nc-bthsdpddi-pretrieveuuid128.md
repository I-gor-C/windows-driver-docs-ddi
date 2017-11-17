---
UID: NC.bthsdpddi.PRETRIEVEUUID128
title: PRETRIEVEUUID128
author: windows-driver-content
description: 
ms.assetid: ec77c078-28e4-4da8-aece-05e67075c0df
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

# PRETRIEVEUUID128 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRETRIEVEUUID128 Pretrieveuuid128; 

// Definition

void Pretrieveuuid128 
(
	PUCHAR Stream
	GUID *uuid128
)
{...}

PRETRIEVEUUID128 


```

## -parameters

### -param Stream: 
### -param *uuid128: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also