---
UID: NC.swdevice.SW_DEVICE_CREATE_CALLBACK
title: SW_DEVICE_CREATE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 71fda5c7-b787-4685-8a32-e28569e03a88
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: swdevice.h
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

# SW_DEVICE_CREATE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SW_DEVICE_CREATE_CALLBACK SwDeviceCreateCallback; 

// Definition

VOID SwDeviceCreateCallback 
(
	HSWDEVICE hSwDevice
	HRESULT CreateResult
	PVOID pContext
	PCWSTR pszDeviceInstanceId
)
{...}

SW_DEVICE_CREATE_CALLBACK 


```

## -parameters

### -param hSwDevice: 
### -param CreateResult: 
### -param pContext: 
### -param pszDeviceInstanceId: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also