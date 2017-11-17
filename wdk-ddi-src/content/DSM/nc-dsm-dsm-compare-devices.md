---
UID: NC.dsm.DSM_COMPARE_DEVICES
title: DSM_COMPARE_DEVICES
author: windows-driver-content
description: 
ms.assetid: 9e09aee3-1564-4415-90a0-8892f9ce524c
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

# DSM_COMPARE_DEVICES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_COMPARE_DEVICES DsmCompareDevices; 

// Definition

BOOLEAN DsmCompareDevices 
(
	IN PVOID DsmContext
	IN PVOID DsmId1
	IN PVOID DsmId2
)
{...}

DSM_COMPARE_DEVICES 


```

## -parameters

### -param DsmContext: 
### -param DsmId1: 
### -param DsmId2: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also