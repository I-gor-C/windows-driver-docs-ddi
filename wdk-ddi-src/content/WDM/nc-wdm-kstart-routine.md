---
UID: NC.wdm.KSTART_ROUTINE
title: KSTART_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 0d26cfdc-a59e-4476-afbc-116a225c8cb2
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

# KSTART_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KSTART_ROUTINE KstartRoutine; 

// Definition

VOID KstartRoutine 
(
	PVOID StartContext
)
{...}

KSTART_ROUTINE PKSTART_ROUTINE


```

## -parameters

### -param StartContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also