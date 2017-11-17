---
UID: NC.wdm.REQUEST_POWER_COMPLETE
title: REQUEST_POWER_COMPLETE
author: windows-driver-content
description: 
ms.assetid: ef83e9bb-94c5-4628-9570-71b967e15ce7
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

# REQUEST_POWER_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

REQUEST_POWER_COMPLETE RequestPowerComplete; 

// Definition

_IRQL_requires_same_ VOID RequestPowerComplete 
(
	PDEVICE_OBJECT DeviceObject
	UCHAR MinorFunction
	POWER_STATE PowerState
	PVOID Context
	PIO_STATUS_BLOCK IoStatus
)
{...}

REQUEST_POWER_COMPLETE PREQUEST_POWER_COMPLETE


```

## -parameters

### -param DeviceObject: 
### -param MinorFunction: 
### -param PowerState: 
### -param Context: 
### -param IoStatus: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also