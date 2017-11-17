---
UID: NC.ucmcx.UCMFUNC
title: UCMFUNC
author: windows-driver-content
description: 
ms.assetid: a1ac0815-6163-4542-9886-c994172e4725
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucmcx.h
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

# UCMFUNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UCMFUNC Ucmfunc; 

// Definition

VOID Ucmfunc 
(
	 VOID
)
{...}

UCMFUNC 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also