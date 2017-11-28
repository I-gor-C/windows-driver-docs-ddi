---
UID: NC.usbcamdi.PCAM_START_CAPTURE_ROUTINE_EX
title: PCAM_START_CAPTURE_ROUTINE_EX
author: windows-driver-content
description: A camera minidriver's CamStartCaptureEx callback function selects the appropriate alternate setting within the USB video streaming interface and prepares the device to stream.
old-location: stream\camstartcaptureex.htm
old-project: stream
ms.assetid: ab2222ed-3166-4984-b76c-5499879f91d5
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: CamStartCaptureEx
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

# PCAM_START_CAPTURE_ROUTINE_EX callback



## -description
<p>A camera minidriver's <b>CamStartCaptureEx</b> callback function selects the appropriate alternate setting within the USB video streaming interface and prepares the device to stream.</p>


## -prototype

````
PCAM_START_CAPTURE_ROUTINE_EX CamStartCaptureEx;

NTSTATUS CamStartCaptureEx(
   PDEVICE_OBJECT BusDeviceObject,
   PVOID          DeviceContext,
   ULONG          StreamNumber
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

### -param <i>StreamNumber</i> 

<dd>
<p>Indicates the stream number.</p>
</dd>
</dl>

## -returns
<p><b>CamStartCaptureEx</b> returns STATUS_SUCCESS or an appropriate error code. This return value is the completion code for the read IRP.</p>

## -remarks
<p>The original USBCAMD does not call <b>CamStartCaptureEx</b>.</p>

<p>This function is required.</p>

<p>The original USBCAMD does not call <b>CamStartCaptureEx</b>.</p>

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