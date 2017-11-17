---
UID: NC.poclass.DEVICE_PASSIVE_COOLING
title: DEVICE_PASSIVE_COOLING
author: windows-driver-content
description: 
ms.assetid: b938125d-83cb-4e95-89e8-d3825c0e38d6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: poclass.h
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

# DEVICE_PASSIVE_COOLING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DEVICE_PASSIVE_COOLING DevicePassiveCooling; 

// Definition

VOID DevicePassiveCooling 
(
	PVOID Context
	ULONG Percentage
)
{...}

DEVICE_PASSIVE_COOLING PDEVICE_PASSIVE_COOLING


```

## -parameters

### -param Context: 
### -param Percentage: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also