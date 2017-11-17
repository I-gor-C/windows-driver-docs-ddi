---
UID: NC.strmini.PHW_PRIORITY_ROUTINE
title: PHW_PRIORITY_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 717b1a5d-e9e9-4a88-afa1-541db3009172
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: strmini.h
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

# PHW_PRIORITY_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_PRIORITY_ROUTINE PhwPriorityRoutine; 

// Definition

VOID PhwPriorityRoutine 
(
	IN PVOID Context
)
{...}

PHW_PRIORITY_ROUTINE 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also