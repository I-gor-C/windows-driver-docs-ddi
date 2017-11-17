---
UID: NC.winppi.EMFPLAYPROC
title: EMFPLAYPROC
author: windows-driver-content
description: 
ms.assetid: 406b1d70-05cd-4818-b1d3-159b2240c355
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: winppi.h
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

# EMFPLAYPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EMFPLAYPROC Emfplayproc; 

// Definition

int Emfplayproc 
(
	 HDC
	 INT
	 HANDLE
)
{...}

EMFPLAYPROC 


```

## -parameters

### -param HDC: 
### -param INT: 
### -param HANDLE: 



## -returns

Returns int that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also