---
UID: NS.strmini._HW_STREAM_OBJECT~r1
title: HW_STREAM_OBJECT
author: windows-driver-content
description: HW_STREAM_OBJECT describes an instance of a minidriver stream.
old-location: stream\hw_stream_object.htm
old-project: stream
ms.assetid: 0cb2041a-844d-4ddb-9dab-e1c77c28835a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: HW_STREAM_OBJECT, HW_STREAM_OBJECT, *PHW_STREAM_OBJECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HW_STREAM_OBJECT
req.alt-loc: strmini.h
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

# HW_STREAM_OBJECT structure



## -description
<p>HW_STREAM_OBJECT describes an instance of a minidriver stream.</p>


## -syntax

````
typedef struct _HW_STREAM_OBJECT {
  ULONG                          SizeOfThisPacket;
  ULONG                          StreamNumber;
  PVOID                          HwStreamExtension;
  PHW_RECEIVE_STREAM_DATA_SRB    ReceiveDataPacket;
  PHW_RECEIVE_STREAM_CONTROL_SRB ReceiveControlPacket;
  HW_CLOCK_OBJECT                HwClockObject;
  BOOLEAN                        Dma;
  BOOLEAN                        Pio;
  PVOID                          HwDeviceExtension;
  ULONG                          StreamHeaderMediaSpecific;
  ULONG                          StreamHeaderWorkspace;
  BOOLEAN                        Allocator;
  PHW_EVENT_ROUTINE              HwEventRoutine;
  ULONG                          Reserved[2];
} HW_STREAM_OBJECT, *PHW_STREAM_OBJECT;
````


## -struct-fields
<dl>

### -field <b>SizeOfThisPacket</b>

<dd>
<p>Specifies the size, in bytes, of this structure.</p>
</dd>

### -field <b>StreamNumber</b>

<dd>
<p>Specifies the offset of the stream within the minidriver's <a href="..\strmini\ns-strmini--hw-stream-descriptor.md">HW_STREAM_DESCRIPTOR</a> structure.</p>
</dd>

### -field <b>HwStreamExtension</b>

<dd>
<p>Points to the stream extension, a buffer allocated by the class driver for the minidriver to use to hold private information about this stream. The minidriver sets the size of the buffer in the <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself with the stream class driver.</p>
</dd>

### -field <b>ReceiveDataPacket</b>

<dd>
<p>Pointer to the stream's <a href="stream.strminireceivestreamdatapacket">StrMiniReceiveStreamDataPacket</a> routine.</p>
</dd>

### -field <b>ReceiveControlPacket</b>

<dd>
<p>Pointer to the stream's <a href="stream.strminireceivestreamcontrolpacket">StrMiniReceiveStreamControlPacket</a> routine.</p>
</dd>

### -field <b>HwClockObject</b>

<dd>
<p>Contains the stream's clock object. See <a href="..\strmini\ns-strmini--hw-clock-object.md">HW_CLOCK_OBJECT</a> for details.</p>
</dd>

### -field <b>Dma</b>

<dd>
<p>If <b>TRUE</b>, the device uses DMA to transfer data for this stream.</p>
</dd>

### -field <b>Pio</b>

<dd>
<p>If <b>TRUE</b>, the device uses programmed I/O to transfer data for this stream. Note that both the <b>Pio</b> and <b>Dma</b> members may be <b>TRUE</b>.</p>
</dd>

### -field <b>HwDeviceExtension</b>

<dd>
<p>Pointer to the minidriver's device extension. The minidriver may use this buffer to record private information. The minidriver sets the size of this buffer in the <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>. The class driver also passes pointers to this buffer in the <b>HwDeviceExtension</b> member of the <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a>, <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a>, and <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -field <b>StreamHeaderMediaSpecific</b>

<dd>
<p>Specifies the size in bytes of the media-specific, per-stream header extension.</p>
</dd>

### -field <b>StreamHeaderWorkspace</b>

<dd>
<p>Specifies the size of the per-stream-header workspace.</p>
</dd>

### -field <b>Allocator</b>

<dd>
<p>Specifies <b>TRUE</b> if the driver uses allocators. Most minidrivers set this value to <b>FALSE</b>. </p>
</dd>

### -field <b>HwEventRoutine</b>

<dd>
<p>Pointer to the stream's <a href="stream.strminievent">StrMiniEvent</a> routine</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>
</dl>

## -remarks
<p>This structure is created by the class driver to hold information about a particular stream in the minidriver. For each stream-specific request, the class driver passes the HW_STREAM_OBJECT for the stream in the <b>StreamObject</b> member of the stream request block (See <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a>). </p>

<p>When the class driver opens the stream and issues the SRB_OPEN_STREAM request to the minidriver's <a href="stream.strminireceivedevicepacket">StrMiniReceiveDevicePacket</a> routine, the minidriver initializes the stream object.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\strmini\ns-strmini--hw-clock-object.md">HW_CLOCK_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20HW_STREAM_OBJECT structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
