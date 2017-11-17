---
UID: NC.usbbusif.PUSB_BUSIFFN_IS_DEVICE_HIGH_SPEED
title: PUSB_BUSIFFN_IS_DEVICE_HIGH_SPEED
author: windows-driver-content
description: 
ms.assetid: 278f4508-30b4-4e9a-b549-6a8bf89bcd13
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbbusif.h
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

# PUSB_BUSIFFN_IS_DEVICE_HIGH_SPEED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUSB_BUSIFFN_IS_DEVICE_HIGH_SPEED PusbBusiffnIsDeviceHighSpeed; 

// Definition

BOOLEAN PusbBusiffnIsDeviceHighSpeed 
(
	PVOID 
)
{...}

PUSB_BUSIFFN_IS_DEVICE_HIGH_SPEED 


```

## -parameters

### -param : 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also