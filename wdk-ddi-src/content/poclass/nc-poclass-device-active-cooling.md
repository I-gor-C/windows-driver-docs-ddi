---
UID: NC.poclass.DEVICE_ACTIVE_COOLING
title: DEVICE_ACTIVE_COOLING
author: windows-driver-content
description: 
ms.assetid: 4874ba68-c79d-4efe-8731-ea2422907465
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

# DEVICE_ACTIVE_COOLING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DEVICE_ACTIVE_COOLING DeviceActiveCooling; 

// Definition

VOID DeviceActiveCooling 
(
	PVOID Context
	BOOLEAN Engaged
)
{...}

DEVICE_ACTIVE_COOLING PDEVICE_ACTIVE_COOLING


```

## -parameters

### -param Context: 
### -param Engaged: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also