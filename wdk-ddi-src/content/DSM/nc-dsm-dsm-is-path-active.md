---
UID: NC.dsm.DSM_IS_PATH_ACTIVE
title: DSM_IS_PATH_ACTIVE
author: windows-driver-content
description: 
ms.assetid: cfd93ca9-8e0d-4176-908e-31136287737e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_IS_PATH_ACTIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_IS_PATH_ACTIVE DsmIsPathActive; 

// Definition

BOOLEAN DsmIsPathActive 
(
	IN PVOID DsmContext
	IN PVOID PathId
	IN PVOID DsmId
)
{...}

DSM_IS_PATH_ACTIVE 


```

## -parameters

### -param DsmContext: 
### -param PathId: 
### -param DsmId: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also