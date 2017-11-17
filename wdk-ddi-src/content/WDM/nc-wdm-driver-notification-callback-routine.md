---
UID: NC.wdm.DRIVER_NOTIFICATION_CALLBACK_ROUTINE
title: DRIVER_NOTIFICATION_CALLBACK_ROUTINE
author: windows-driver-content
description: 
ms.assetid: bb7f2bbd-6980-410c-9dbd-bae5314614eb
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

# DRIVER_NOTIFICATION_CALLBACK_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DRIVER_NOTIFICATION_CALLBACK_ROUTINE DriverNotificationCallbackRoutine; 

// Definition

NTSTATUS DriverNotificationCallbackRoutine 
(
	PVOID NotificationStructure
	PVOID Context
)
{...}

DRIVER_NOTIFICATION_CALLBACK_ROUTINE PDRIVER_NOTIFICATION_CALLBACK_ROUTINE


```

## -parameters

### -param NotificationStructure: 
### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also