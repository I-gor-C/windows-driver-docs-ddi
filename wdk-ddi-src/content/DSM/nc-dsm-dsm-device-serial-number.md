---
UID: NC.dsm.DSM_DEVICE_SERIAL_NUMBER
title: DSM_DEVICE_SERIAL_NUMBER
author: windows-driver-content
description: 
ms.assetid: fd3caa6a-2ec0-490f-8119-c28252c1f35a
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

# DSM_DEVICE_SERIAL_NUMBER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_DEVICE_SERIAL_NUMBER DsmDeviceSerialNumber; 

// Definition

PUCHAR DsmDeviceSerialNumber 
(
	IN PVOID DsmContext
	IN PVOID DsmId
)
{...}

DSM_DEVICE_SERIAL_NUMBER 


```

## -parameters

### -param DsmContext: 
### -param DsmId: 



## -returns

Returns PUCHAR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also