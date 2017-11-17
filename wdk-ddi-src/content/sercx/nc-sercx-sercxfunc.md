---
UID: NC.sercx.SERCXFUNC
title: SERCXFUNC
author: windows-driver-content
description: 
ms.assetid: e13dbbad-e190-481f-a207-500d762861ab
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# SERCXFUNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SERCXFUNC Sercxfunc; 

// Definition

VOID Sercxfunc 
(
	 VOID
)
{...}

SERCXFUNC 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also