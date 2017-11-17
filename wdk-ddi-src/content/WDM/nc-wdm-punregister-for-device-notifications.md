---
UID: NC.wdm.PUNREGISTER_FOR_DEVICE_NOTIFICATIONS
title: PUNREGISTER_FOR_DEVICE_NOTIFICATIONS
author: windows-driver-content
description: 
ms.assetid: 1802cf48-1a15-4b74-b0f2-03c88265a383
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

# PUNREGISTER_FOR_DEVICE_NOTIFICATIONS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUNREGISTER_FOR_DEVICE_NOTIFICATIONS PunregisterForDeviceNotifications; 

// Definition

void PunregisterForDeviceNotifications 
(
)
{...}

PUNREGISTER_FOR_DEVICE_NOTIFICATIONS 


```

## -parameters




## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also