---
UID: NC.ks.PFNREFERENCEDEVICEOBJECT
title: PFNREFERENCEDEVICEOBJECT
author: windows-driver-content
description: 
ms.assetid: 1d8d4585-98e7-48e3-9eee-f8b2b3698d8b
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

# PFNREFERENCEDEVICEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNREFERENCEDEVICEOBJECT Pfnreferencedeviceobject; 

// Definition

VOID Pfnreferencedeviceobject 
(
	PVOID Context
)
{...}

PFNREFERENCEDEVICEOBJECT 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also