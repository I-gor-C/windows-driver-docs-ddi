---
UID: NC.spbcx.SPBFUNC
title: SPBFUNC
author: windows-driver-content
description: 
ms.assetid: 544a64e0-5a24-4506-9474-6fc889c8bb76
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# SPBFUNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SPBFUNC Spbfunc; 

// Definition

VOID Spbfunc 
(
	 VOID
)
{...}

SPBFUNC 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also