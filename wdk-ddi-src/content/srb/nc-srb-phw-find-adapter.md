---
UID: NC.srb.PHW_FIND_ADAPTER
title: PHW_FIND_ADAPTER
author: windows-driver-content
description: 
ms.assetid: 666d97ec-0201-42e0-b0fa-d5b6872e3199
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: srb.h
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

# PHW_FIND_ADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_FIND_ADAPTER PhwFindAdapter; 

// Definition

ULONG PhwFindAdapter 
(
	PVOID DeviceExtension
	PVOID HwContext
	PVOID BusInformation
	PCHAR ArgumentString
	PPORT_CONFIGURATION_INFORMATION ConfigInfo
	PBOOLEAN Again
)
{...}

PHW_FIND_ADAPTER 


```

## -parameters

### -param DeviceExtension: 
### -param HwContext: 
### -param BusInformation: 
### -param ArgumentString: 
### -param ConfigInfo: 
### -param Again: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also