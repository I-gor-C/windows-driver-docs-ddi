---
UID: NC.wdm.PUNREGISTER_FOR_DEVICE_NOTIFICATIONS2
title: PUNREGISTER_FOR_DEVICE_NOTIFICATIONS2
author: windows-driver-content
description: 
ms.assetid: 2db93879-8b1d-4430-93b7-00287ffcf35a
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

# PUNREGISTER_FOR_DEVICE_NOTIFICATIONS2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUNREGISTER_FOR_DEVICE_NOTIFICATIONS2 PunregisterForDeviceNotifications2; 

// Definition

VOID PunregisterForDeviceNotifications2 
(
	PVOID Context
)
{...}

PUNREGISTER_FOR_DEVICE_NOTIFICATIONS2 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also