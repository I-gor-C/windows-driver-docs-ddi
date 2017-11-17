---
UID: NC.ufxclient.UFX_DEVICE_EVENT_COMPLETE
title: UFX_DEVICE_EVENT_COMPLETE
author: windows-driver-content
description: 
ms.assetid: c017481f-e0b3-46cd-ab06-69735217fac2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ufxclient.h
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

# UFX_DEVICE_EVENT_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_DEVICE_EVENT_COMPLETE UfxDeviceEventComplete; 

// Definition

VOID UfxDeviceEventComplete 
(
	PUFX_GLOBALS 
	UFXDEVICE 
	NTSTATUS 
)
{...}

UFX_DEVICE_EVENT_COMPLETE PFN_UFX_DEVICE_EVENT_COMPLETE


```

## -parameters

### -param : 
### -param : 
### -param : 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also