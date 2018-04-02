---
UID: NF:ucxusbdevice.UcxUsbDeviceRemoteWakeNotification
title: UcxUsbDeviceRemoteWakeNotification function
author: windows-driver-content
description: Notifies UCX that a remote wake signal from the device is received.
old-location: buses\_ucxusbdeviceremotewakenotification.htm
old-project: usbref
ms.assetid: 0C95831F-2E20-461C-8478-9A40C1F063E2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UcxUsbDeviceRemoteWakeNotification, UcxUsbDeviceRemoteWakeNotification method [Buses], buses._ucxusbdeviceremotewakenotification, ucxusbdevice/UcxUsbDeviceRemoteWakeNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	ucxusbdevice.h
api_name:
-	UcxUsbDeviceRemoteWakeNotification
product: Windows
targetos: Windows
req.typenames: UCX_USBDEVICE_CHARACTERISTIC_TYPE
req.product: Windows 10 or later.
---


# UcxUsbDeviceRemoteWakeNotification function
Notifies UCX that a remote wake signal from the device is received.

## Syntax

```
void UcxUsbDeviceRemoteWakeNotification(
  UCXUSBDEVICE UsbDevice,
  ULONG        Interface
);
```

## Parameters

`UsbDevice`

A handle to the USB device object for which the remote wake is received. The client driver retrieved the handle in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a>.

`Interface`

The interface number that sent the remote wake notification.


## Return Value

This method does not return a value.

## Remarks

This function completes the pending remote wake request from the request driver such as the hub driver or usbccgp driver. If no such request is found, this notification is ignored.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10  |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |
| **IRQL** | "<=DISPATCH_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a>