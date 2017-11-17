---
UID: NC.wdm.PDEVICE_NOTIFY_CALLBACK2
title: PDEVICE_NOTIFY_CALLBACK2
author: windows-driver-content
description: 
ms.assetid: ddfb566f-a40d-4f1c-9412-1fa99bf1dc66
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

# PDEVICE_NOTIFY_CALLBACK2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEVICE_NOTIFY_CALLBACK2 PdeviceNotifyCallback2; 

// Definition

VOID PdeviceNotifyCallback2 
(
	PVOID NotificationContext
	ULONG NotifyCode
)
{...}

PDEVICE_NOTIFY_CALLBACK2 


```

## -parameters

### -param NotificationContext: 
### -param NotifyCode: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also