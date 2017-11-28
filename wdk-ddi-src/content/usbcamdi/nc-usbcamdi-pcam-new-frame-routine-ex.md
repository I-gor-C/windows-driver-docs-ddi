---
UID: NC.usbcamdi.PCAM_NEW_FRAME_ROUTINE_EX
title: PCAM_NEW_FRAME_ROUTINE_EX
author: windows-driver-content
description: A camera minidriver's CamNewVideoFrameEx callback function initializes a new video frame context structure.
old-location: stream\camnewvideoframeex.htm
old-project: stream
ms.assetid: 739e434e-9621-4927-bf1d-2e7c3b2828d7
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
req.alt-api: CamNewVideoFrameEx
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
req.irql: DISPATCH_LEVEL (See Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# PCAM_NEW_FRAME_ROUTINE_EX callback



## -description
<p>A camera minidriver's <b>CamNewVideoFrameEx</b> callback function initializes a new video frame context structure.</p>


## -prototype

````
PCAM_NEW_FRAME_ROUTINE_EX CamNewVideoFrameEx;

VOID CamNewVideoFrameEx(
   PVOID  DeviceContext,
   PVOID  FrameContext,
   ULONG  StreamNumber,
   PULONG FrameLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceContext</i> 

<dd>
<p>Specifies the minidriver device context.</p>
</dd>

### -param <i>FrameContext</i> 

<dd>
<p>Specifies the frame context to be initialized.</p>
</dd>

### -param <i>StreamNumber</i> 

<dd>
<p>Indicates the stream associated with this new frame.</p>
</dd>

### -param <i>FrameLength</i> 

<dd>
<p>Pointer to the raw frame buffer length. The length is expressed in bytes. The camera minidriver may decrease this value if it does not require a buffer transfer on the USB bus of the specified size. The camera minidriver should not increase this value.</p>
</dd>
</dl>

## -returns
<p><b>CamNewVideoFrameEx</b> does not return a value.</p>

## -remarks
<p>USBCAMD calls the camera minidriver's <b>CamNewVideoFrameEx</b> callback function at IRQL = DISPATCH_LEVEL.</p>

<p>The original USBCAMD does not call <b>CamNewVideoFrameEx</b>.</p>

<p>This function is optional.</p>

<p>USBCAMD calls the camera minidriver's <b>CamNewVideoFrameEx</b> callback function at IRQL = DISPATCH_LEVEL.</p>

<p>The original USBCAMD does not call <b>CamNewVideoFrameEx</b>.</p>

<p>This function is optional.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL (See Remarks section)</p>
</td>
</tr>
</table>