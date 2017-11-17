---
UID: NC.ks.PFNKSITEMFREECALLBACK
title: PFNKSITEMFREECALLBACK
author: windows-driver-content
description: 
ms.assetid: f18db7a9-2184-4928-bee4-9b0492b30bc0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSITEMFREECALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSITEMFREECALLBACK Pfnksitemfreecallback; 

// Definition

VOID Pfnksitemfreecallback 
(
	PKSOBJECT_CREATE_ITEM CreateItem
)
{...}

PFNKSITEMFREECALLBACK 


```

## -parameters

### -param CreateItem: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also