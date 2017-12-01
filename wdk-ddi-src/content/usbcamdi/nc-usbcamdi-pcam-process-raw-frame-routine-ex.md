---
UID: NC.usbcamdi.PCAM_PROCESS_RAW_FRAME_ROUTINE_EX
title: PCAM_PROCESS_RAW_FRAME_ROUTINE_EX
author: windows-driver-content
description: A camera minidriver's CamProcessRawVideoFrameEx callback function decodes a raw video frame.
old-location: stream\camprocessrawvideoframeex.htm
old-project: stream
ms.assetid: 07b0d1ea-c099-474e-8dc8-cddec44836e2
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
req.alt-api: CamProcessRawVideoFrameEx
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PCAM_PROCESS_RAW_FRAME_ROUTINE_EX callback



## -description
<p>A camera minidriver's <b>CamProcessRawVideoFrameEx</b> callback function decodes a raw video frame.</p>


## -prototype

````
PCAM_PROCESS_RAW_FRAME_ROUTINE_EX CamProcessRawVideoFrameEx;

NTSTATUS CamProcessRawVideoFrameEx(
   PDEVICE_OBJECT BusDeviceObject,
   PVOID          DeviceContext,
   PVOID          FrameContext,
   PVOID          FrameBuffer,
   ULONG          FrameLength,
   PVOID          RawFrameBuffer,
   ULONG          RawFrameLength,
   ULONG          NumberOfPackets,
   PULONG         BytesReturned,
   ULONG          ActualRawFrameLength,
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

### -param <i>FrameContext</i> 

<dd>
<p>Pointer to the minidriver's frame context.</p>
</dd>

### -param <i>FrameBuffer</i> 

<dd>
<p>Pointer to the buffer that receives the final processed video frame. See the Remarks section for more information about how USBCAMD uses this parameter.</p>
</dd>

### -param <i>FrameLength</i> 

<dd>
<p>Specifies the length of the frame buffer (from the original read request) in bytes.</p>
</dd>

### -param <i>RawFrameBuffer</i> 

<dd>
<p>Pointer to the buffer containing the received USB packets. See the Remarks section for more information about how USBCAMD uses this parameter.</p>
</dd>

### -param <i>RawFrameLength</i> 

<dd>
<p>Specifies the length of <i>RawFrameBuffer</i> in bytes.</p>
</dd>

### -param <i>NumberOfPackets</i> 

<dd>
<p>Specifies the number of USB packets received into <i>RawFrameBuffer</i>.</p>
</dd>

### -param <i>BytesReturned</i> 

<dd>
<p>Pointer to the number of bytes transferred. The minidriver must set this to zero if it encounters any errors during processing, as described in <a href="NULL">Data Flow Using Isochronous Pipes</a>. See the Remarks section for more information about how USBCAMD uses this parameter.</p>
</dd>

### -param <i>ActualRawFrameLength</i> 

<dd>
<p>Contains the length of the actual buffer received from the camera. This value is specified in bytes.</p>
</dd>

### -param <i>StreamNumber</i> 

<dd>
<p>Indicates the stream number with which this frame is associated with.</p>
</dd>
</dl>

## -returns
<p><b>CamProcessRawVideoFrameEx</b> returns STATUS_SUCCESS or an appropriate error code.</p>

## -remarks
<p>Before USBCAMD calls the minidriver's <b>CamProcessRawVideoFrameEx</b> callback, it sets the first DWORD in the buffer pointed to by the <i>FrameBuffer</i> parameter to the value <i>0xdeadbeef.</i> After calling the minidriver's <b>CamProcessRawVideoFrameEx</b> callback USBCAMD checks the first DWORD in the buffer pointed to by the <i>FrameBuffer</i> parameter for the value <i>0xdeadbeef</i> to determine if <b>CamProcessRawVideoFrameEx</b> successfully copied the video frame from the buffer pointed to by the <i>RawFrameBuffer</i> parameter into the buffer pointed to by the <i>FrameBuffer</i> parameter.</p>

<p>This function is not called if either one of the following bits are set in the <i>CamControlFlag</i> argument passed to the <a href="..\usbcamdi\nf-usbcamdi-usbcamd-initializenewinterface.md">USBCAMD_InitializeNewInterface</a> function:</p>

<p>USBCAMD_CamControlFlag_NoVideoRawProcessing</p>

<p>USBCAMD_CamControlFlag_NoStillRawProcessing</p>

<p>USBCAMD clears the stream header options flag before passing the raw frame to the minidriver. The default flag is key frames only. The camera minidriver should set the stream header option flags appropriately if it needs to indicate anything other than key frames.</p>

<p>The original USBCAMD does not call <b>CamProcessRawVideoFrameEx</b>.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>