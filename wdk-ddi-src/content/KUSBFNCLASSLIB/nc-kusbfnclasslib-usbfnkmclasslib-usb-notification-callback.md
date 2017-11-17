---
UID: NC.kusbfnclasslib.USBFNKMCLASSLIB_USB_NOTIFICATION_CALLBACK
title: USBFNKMCLASSLIB_USB_NOTIFICATION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 2504a3a1-f2c5-41f9-a383-20f85e080b2f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: kusbfnclasslib.h
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

# USBFNKMCLASSLIB_USB_NOTIFICATION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

USBFNKMCLASSLIB_USB_NOTIFICATION_CALLBACK UsbfnkmclasslibUsbNotificationCallback; 

// Definition

VOID UsbfnkmclasslibUsbNotificationCallback 
(
	WDFDEVICE Device
	USBFN_NOTIFICATION Notification
	NTSTATUS Status
)
{...}

USBFNKMCLASSLIB_USB_NOTIFICATION_CALLBACK 


```

## -parameters

### -param Device: 
### -param Notification: 
### -param Status: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also