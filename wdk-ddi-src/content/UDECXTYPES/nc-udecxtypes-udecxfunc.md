---
UID: NC.udecxtypes.UDECXFUNC
title: UDECXFUNC
author: windows-driver-content
description: 
ms.assetid: 90948541-3348-4421-858f-261bdb2b6d25
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxtypes.h
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

# UDECXFUNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UDECXFUNC Udecxfunc; 

// Definition

VOID Udecxfunc 
(
	 VOID
)
{...}

UDECXFUNC 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also