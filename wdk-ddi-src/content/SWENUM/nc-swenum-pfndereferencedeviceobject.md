---
UID: NC.swenum.PFNDEREFERENCEDEVICEOBJECT
title: PFNDEREFERENCEDEVICEOBJECT
author: windows-driver-content
description: 
ms.assetid: 11817736-91f6-4012-8aec-67a8e384d4c2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: swenum.h
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

# PFNDEREFERENCEDEVICEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNDEREFERENCEDEVICEOBJECT Pfndereferencedeviceobject; 

// Definition

VOID Pfndereferencedeviceobject 
(
	PVOID Context
)
{...}

PFNDEREFERENCEDEVICEOBJECT 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also