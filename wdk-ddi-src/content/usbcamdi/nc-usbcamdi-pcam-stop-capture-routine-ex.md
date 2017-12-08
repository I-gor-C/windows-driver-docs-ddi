---
UID: NC.usbcamdi.PCAM_STOP_CAPTURE_ROUTINE_EX
title: PCAM_STOP_CAPTURE_ROUTINE_EX
author: windows-driver-content
description: A camera minidriver's CamStopCaptureEx callback function performs any processing after the stream is stopped.
old-location: stream\camstopcaptureex.htm
old-project: stream
ms.assetid: b8b6e3f0-f5c8-449f-9001-3182b3547d8d
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
req.alt-api: CamStopCaptureEx
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

# PCAM_STOP_CAPTURE_ROUTINE_EX callback



## -description
<p>A camera minidriver's <b>CamStopCaptureEx</b> callback function performs any processing after the stream is stopped.</p>


## -prototype

````
PCAM_STOP_CAPTURE_ROUTINE_EX CamStopCaptureEx;

NTSTATUS CamStopCaptureEx(
   PDEVICE_OBJECT BusDeviceObject,
   PVOID          DeviceContext,
   ULONG          StreamNumber
)
{ ... }
````


## -parameters
<dl>

### -param BusDeviceObject 

<dd>
<p>Pointer to the camera minidriver's device object created by the USB hub.</p>
</dd>

### -param DeviceContext 

<dd>
<p>Pointer to the camera minidriver's device context.</p>
</dd>

### -param StreamNumber 

<dd>
<p>Indicates the stream number.</p>
</dd>
</dl>

## -returns
<p><b>CamStopCaptureEx</b> returns STATUS_SUCCESS or an appropriate error code. This return value is the completion code for the read IRP.</p>

## -remarks
<p>USBCAMD calls the minidriver's <b>CamStopCaptureEx</b> callback function immediately after the isochronous video stream is stopped. Typically, a camera minidriver selects an alternate setting within the USB video streaming interface that uses no additional bandwidth.</p>

<p>The original USBCAMD does not call <b>CamStopCaptureEx</b>.</p>

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