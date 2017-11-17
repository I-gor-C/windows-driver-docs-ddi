---
UID: NC.ntddk.pHalEndOfBoot
title: pHalEndOfBoot
author: windows-driver-content
description: 
ms.assetid: 6ee6e297-bad2-4a0c-b069-d13739d38562
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pHalEndOfBoot callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalEndOfBoot Phalendofboot; 

// Definition

VOID Phalendofboot 
(
	 VOID
)
{...}

pHalEndOfBoot 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also