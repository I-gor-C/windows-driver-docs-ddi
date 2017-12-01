---
UID: NC.usbcamdi.PCAM_INITIALIZE_ROUTINE
title: PCAM_INITIALIZE_ROUTINE
author: windows-driver-content
description: A camera minidriver's CamInitialize callback function initializes the device.
old-location: stream\caminitialize.htm
old-project: stream
ms.assetid: a39f78b7-f749-40b8-952a-5442608b0f1f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: USBC_FUNCTION_DESCRIPTOR, USBC_FUNCTION_DESCRIPTOR, *PUSBC_FUNCTION_DESCRIPTOR
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
req.iface: 
req.product: Windows 10 or later.
---

# PCAM_INITIALIZE_ROUTINE callback



## -description
<p>A camera minidriver's <b>CamInitialize</b> callback function initializes the device.</p>


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
<dl>

### -param <i>BusDeviceObject</i> 

<dd>
<p>Pointer to the camera minidriver's device object created by the USB hub.</p>
</dd>

### -param <i>DeviceContext</i> 

<dd>
<p>Pointer to the camera minidriver's device context.</p>
</dd>
</dl>

## -returns
<p><b>CamInitialize</b> returns STATUS_SUCCESS or an appropriate error code. </p>

## -remarks
<p>USBCAMD calls the camera minidriver's <b>CamInitialize</b> callback function the first time the device is used.</p>

<p><b>CamInitialize</b> is called by both the original USBCAMD and USBCAMD2.</p>

<p>This function is required.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>