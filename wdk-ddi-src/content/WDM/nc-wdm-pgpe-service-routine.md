---
UID: NC.wdm.PGPE_SERVICE_ROUTINE
title: PGPE_SERVICE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 3af1b78b-7d53-40f8-970c-b82315551abd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PGPE_SERVICE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPE_SERVICE_ROUTINE PgpeServiceRoutine; 

// Definition

BOOLEAN PgpeServiceRoutine 
(
	 PVOID
	 PVOID
)
{...}

PGPE_SERVICE_ROUTINE 


```

## -parameters

### -param PVOID: 
### -param PVOID: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also