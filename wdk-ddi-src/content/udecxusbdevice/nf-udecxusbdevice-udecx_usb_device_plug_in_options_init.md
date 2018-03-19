---
UID: NF:udecxusbdevice.UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT
title: UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT function
author: windows-driver-content
description: Initializes a UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure.
old-location: buses\udecx_usb_device_plug_in_options_init.htm
old-project: usbref
ms.assetid: 3188E2EE-E011-476D-9DDC-1DF61ECF9413
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT, UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT function [Buses], buses.udecx_usb_device_plug_in_options_init, udecxusbdevice/UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Udecxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Udecxstub.lib
-	Udecxstub.dll
api_name:
-	UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT
product: Windows
targetos: Windows
req.typenames: UDECX_USB_DEVICE_WAKE_SETTING, *PUDECX_USB_DEVICE_WAKE_SETTING
req.product: Windows 10 or later.
---


# UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT function
Initializes a <a href="..\udecxusbdevice\ns-udecxusbdevice-_udecx_usb_device_plug_in_options.md">UDECX_USB_DEVICE_PLUG_IN_OPTIONS</a> structure.

## Syntax

````
FORCEINLINE void UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT(
  _Out_ PUDECX_USB_DEVICE_PLUG_IN_OPTIONS Options
);
````

## Parameters

`Options`

A pointer to a <a href="..\udecxusbdevice\ns-udecxusbdevice-_udecx_usb_device_plug_in_options.md">UDECX_USB_DEVICE_PLUG_IN_OPTIONS</a> structure to initialize.


## Return Value

This function does not return a value.

## Remarks

The method initializes <b>Usb20PortNumber</b> and <b>Usb30PortNumber</b>  to 0. This indicates a request for  automatic port number selection.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.15 |
| **Header** | udecxusbdevice.h (include Udecx.h) |
| **Library** | Udecxstub.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceplugin.md">UdecxUsbDevicePlugIn</a>