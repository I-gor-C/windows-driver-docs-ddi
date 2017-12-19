---
UID: NC.usbcamdi.PCAM_INITIALIZE_ROUTINE
title: PCAM_INITIALIZE_ROUTINE
author: windows-driver-content
description: A camera minidriver's CamInitialize callback function initializes the device.
old-location: stream\caminitialize.htm
old-project: stream
ms.assetid: a39f78b7-f749-40b8-952a-5442608b0f1f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _USB_BUS_INTERFACE_USBDI_V3, *PUSB_BUS_INTERFACE_USBDI_V3, PUSB_BUS_INTERFACE_USBDI_V3, USB_BUS_INTERFACE_USBDI_V3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CamInitialize
req.alt-loc: usbcamdi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# PCAM_INITIALIZE_ROUTINE callback



## -description
A camera minidriver's <b>CamInitialize</b> callback function initializes the device.



## -prototype

````
PCAM_INITIALIZE_ROUTINE CamInitialize;

NTSTATUS CamInitialize(
   PDEVICE_OBJECT BusDeviceObject,
   PVOID          DeviceContext
)
{ ... }
````


## -parameters

### -param BusDeviceObject 

Pointer to the camera minidriver's device object created by the USB hub.


### -param DeviceContext 

Pointer to the camera minidriver's device context.


## -returns
<b>CamInitialize</b> returns STATUS_SUCCESS or an appropriate error code. 


## -remarks
USBCAMD calls the camera minidriver's <b>CamInitialize</b> callback function the first time the device is used.

<b>CamInitialize</b> is called by both the original USBCAMD and USBCAMD2.

This function is required.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>