---
UID: NC.ntddk.pHalVectorToIDTEntry
title: pHalVectorToIDTEntry
author: windows-driver-content
description: 
ms.assetid: ca86e486-49d9-4a81-9f34-6a95941eed17
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

# pHalVectorToIDTEntry callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalVectorToIDTEntry Phalvectortoidtentry; 

// Definition

UCHAR Phalvectortoidtentry 
(
	ULONG Vector
)
{...}

pHalVectorToIDTEntry 


```

## -parameters

### -param Vector: 



## -returns

Returns UCHAR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also