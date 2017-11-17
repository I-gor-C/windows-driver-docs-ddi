---
UID: NC.ntifs.PFLUSH_TO_LSN
title: PFLUSH_TO_LSN
author: windows-driver-content
description: 
ms.assetid: 863c74df-d761-495f-9b64-0330f62c8c43
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

# PFLUSH_TO_LSN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLUSH_TO_LSN PflushToLsn; 

// Definition

VOID PflushToLsn 
(
	PVOID LogHandle
	LARGE_INTEGER Lsn
)
{...}

PFLUSH_TO_LSN 


```

## -parameters

### -param LogHandle: 
### -param Lsn: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also