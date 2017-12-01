---
UID: NC.usbcamdi.PCAM_PROCESS_PACKET_ROUTINE_EX
title: PCAM_PROCESS_PACKET_ROUTINE_EX
author: windows-driver-content
description: A camera minidriver's CamProcessUSBPacketEx callback function processes a USB packet.
old-location: stream\camprocessusbpacketex.htm
old-project: stream
ms.assetid: 9f69b2f0-6e55-440f-98ab-35d8faddf933
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
req.alt-api: CamProcessUSBPacketEx
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
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PCAM_PROCESS_PACKET_ROUTINE_EX callback



## -description
<p>A camera minidriver's <b>CamProcessUSBPacketEx</b> callback function processes a USB packet.</p>


## -prototype

````
PCAM_PROCESS_PACKET_ROUTINE_EX CamProcessUSBPacketEx;

ULONG CamProcessUSBPacketEx(
   PDEVICE_OBJECT              BusDeviceObject,
   PVOID                       DeviceContext,
   PVOID                       CurrentFrameContext,
   PUSBD_ISO_PACKET_DESCRIPTOR SyncPacket,
   PVOID                       SyncBuffer,
   PUSBD_ISO_PACKET_DESCRIPTOR DataPacket,
   PVOID                       DataBuffer,
   PBOOLEAN                    FrameComplete,
   PULONG                      PacketFlag,
   PULONG                      ValidDataOffset
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

### -param <i>CurrentFrameContext</i> 

<dd>
<p>Pointer to the camera minidriver's frame context.</p>
</dd>

### -param <i>SyncPacket</i> 

<dd>
<p>Pointer to a <a href="..\usb\ns-usb--usbd-iso-packet-descriptor.md">USBD_ISO_PACKET_DESCRIPTOR</a> structure from the sync pipe. This value is <b>NULL</b> if the interface has only one pipe.</p>
</dd>

### -param <i>SyncBuffer</i> 

<dd>
<p>Pointer to the data for the <i>SyncPacket</i>.</p>
</dd>

### -param <i>DataPacket</i> 

<dd>
<p>Specifies the isochronous packet descriptor from data pipe.</p>
</dd>

### -param <i>DataBuffer</i> 

<dd>
<p>Pointer to <i>DataPacket.</i></p>
</dd>

### -param <i>FrameComplete</i> 

<dd>
<p>Pointer to a BOOLEAN value that the camera minidriver sets to indicate whether this is the first data packet for a new video frame.</p>
</dd>

### -param <i>PacketFlag</i> 

<dd>
<p>Pointer to a value that the minidriver sets to indicate the contents of the current frame. It should be set to one of the following values:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>USBCAMD_PROCESSPACKETEX_DropFrame</p>
</td>
<td>
<p>The current frame is unsalvageable. The read IRP should be recycled.</p>
</td>
</tr>
<tr>
<td>
<p>USBCAMD_PROCESSPACKETEX_NextFrameIsStill</p>
</td>
<td>
<p>The frame is a still image.</p>
</td>
</tr>
<tr>
<td>
<p>USBCAMD_PROCESSPACKETEX_CurrentFrameIsStill</p>
</td>
<td>
<p>The current frame is for the still pin.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>ValidDataOffset</i> 

<dd>
<p>Pointer to a ULONG value that indicates an offset from the beginning of the packet. USBCAMD should start the copy from this offset. This eliminates the extra buffer copy in the case of an in-band signal. If the camera is not using in-band signaling, <i>ValidDataOffset</i> should be set to zero.</p>
</dd>
</dl>

## -returns
<p>This function returns the number of bytes that should be copied.</p>

## -remarks
<p>The minidriver should complete its <b>CamProcessUSBPacketEx</b> function as quickly as possible. Image processing should be deferred to the <a href="stream.camprocessrawvideoframeex">CamProcessRawVideoFrameEx</a> function.</p>

<p>This callback function is used with isochronous pipes only (video or still streaming).</p>

<p>The original USBCAMD does not call <b>CamProcessUSBPacketEx</b>.</p>

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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usb\ns-usb--usbd-iso-packet-descriptor.md">USBD_ISO_PACKET_DESCRIPTOR</a>
</dt>
<dt>
<a href="stream.camprocessrawvideoframeex">CamProcessRawVideoFrameEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20CamProcessUSBPacketEx routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
