---
UID: NC.wdm.PREGISTER_FOR_DEVICE_NOTIFICATIONS2
title: PREGISTER_FOR_DEVICE_NOTIFICATIONS2
author: windows-driver-content
description: 
ms.assetid: 5b14476e-a17c-4441-9578-3469a8eedaad
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

# PREGISTER_FOR_DEVICE_NOTIFICATIONS2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREGISTER_FOR_DEVICE_NOTIFICATIONS2 PregisterForDeviceNotifications2; 

// Definition

NTSTATUS PregisterForDeviceNotifications2 
(
	PVOID Context
	PDEVICE_NOTIFY_CALLBACK2 NotificationHandler
	PVOID NotificationContext
)
{...}

PREGISTER_FOR_DEVICE_NOTIFICATIONS2 


```

## -parameters

### -param Context: 
### -param NotificationHandler: 
### -param NotificationContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also