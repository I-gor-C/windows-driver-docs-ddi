---
UID: NC.bthsdpddi.PGETNEXTELEMENT
title: PGETNEXTELEMENT
author: windows-driver-content
description: 
ms.assetid: eea98614-333c-4e2f-8a56-5b77495dc494
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

# PGETNEXTELEMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGETNEXTELEMENT Pgetnextelement; 

// Definition

VOID Pgetnextelement 
(
	PUCHAR Stream
	ULONG StreamSize
	PUCHAR CurrentElement
	PUCHAR *NextElement
	PULONG NextElementSize
)
{...}

PGETNEXTELEMENT 


```

## -parameters

### -param Stream: 
### -param StreamSize: 
### -param CurrentElement: 
### -param *NextElement: 
### -param NextElementSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also