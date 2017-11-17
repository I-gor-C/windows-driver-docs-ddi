---
UID: NC.ntifs.PQUERY_LOG_USAGE
title: PQUERY_LOG_USAGE
author: windows-driver-content
description: 
ms.assetid: 8a81ba08-4443-4ba9-a500-167e5bdba425
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PQUERY_LOG_USAGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PQUERY_LOG_USAGE PqueryLogUsage; 

// Definition

VOID PqueryLogUsage 
(
	PVOID LogHandle
	PUSHORT PercentageFull
)
{...}

PQUERY_LOG_USAGE 


```

## -parameters

### -param LogHandle: 
### -param PercentageFull: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also