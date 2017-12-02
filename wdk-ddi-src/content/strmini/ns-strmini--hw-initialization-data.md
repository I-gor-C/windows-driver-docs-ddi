---
UID: NS.strmini._HW_INITIALIZATION_DATA
title: HW_INITIALIZATION_DATA
author: windows-driver-content
description: The HW_INITIALIZATION_DATA structure specifies the basic information the class driver needs to begin initializing the minidriver.
old-location: stream\hw_initialization_data.htm
old-project: stream
ms.assetid: 5be9ba51-bd6c-4650-9c48-f89267a2ac16
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: HW_INITIALIZATION_DATA, HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA
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
req.alt-api: HW_INITIALIZATION_DATA
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

# HW_INITIALIZATION_DATA structure



## -description
<p>The HW_INITIALIZATION_DATA structure specifies the basic information the class driver needs to begin initializing the minidriver. The minidriver passes an HW_INITIALIZATION_DATA structure to the class driver when it registers itself by calling <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>.</p>


## -syntax

````
typedef struct _HW_INITIALIZATION_DATA {
  ULONG                       HwInitializationDataSize;
  PHW_INTERRUPT               HwInterrupt;
  PHW_RECEIVE_DEVICE_SRB      HwReceivePacket;
  PHW_CANCEL_SRB              HwCancelPacket;
  PHW_REQUEST_TIMEOUT_HANDLER HwRequestTimeoutHandler;
  ULONG                       DeviceExtensionSize;
  ULONG                       PerRequestExtensionSize;
  ULONG                       PerStreamExtensionSize;
  ULONG                       FilterInstanceExtensionSize;
  BOOLEAN                     BusMasterDMA;
  BOOLEAN                     Dma24BitAddresses;
  ULONG                       BufferAlignment;
  BOOLEAN                     TurnOffSynchronization;
  ULONG                       DmaBufferSize;
  ULONG                       Reserved[2];
} HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA;
````


## -struct-fields
<dl>

### -field HwInitializationDataSize

<dd>
<p>Specifies the size of this data structure, in bytes.</p>
</dd>

### -field HwInterrupt

<dd>
<p>Points to the minidriver's <a href="stream.strminiinterrupt">StrMiniInterrupt</a> routine.</p>
</dd>

### -field HwReceivePacket

<dd>
<p>Points to the minidriver's <a href="stream.strminireceivedevicepacket">StrMiniReceiveDevicePacket</a> routine.</p>
</dd>

### -field HwCancelPacket

<dd>
<p>Points to the minidriver's <a href="stream.strminicancelpacket">StrMiniCancelPacket</a> routine.</p>
</dd>

### -field HwRequestTimeoutHandler

<dd>
<p>Points to the minidriver's <a href="stream.strminirequesttimeout">StrMiniRequestTimeout</a> routine.</p>
</dd>

### -field DeviceExtensionSize

<dd>
<p>Specifies the size in bytes of the buffer the class driver should allocate for the minidriver's device extension. The minidriver may use this buffer to record private information. The class driver passes pointers to this buffer in the <b>HwDeviceExtension</b> member of <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>, <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a>, <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a>, and <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -field PerRequestExtensionSize

<dd>
<p>Specifies the size in bytes of the buffer the class driver should allocate for the buffer pointed to by <b>SRBExtension</b> member of <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a> structures it passes to the minidriver. The class driver will allocate one buffer for each HW_STREAM_REQUEST_BLOCK.</p>
</dd>

### -field PerStreamExtensionSize

<dd>
<p>Specifies the size in bytes of the buffer the class driver should allocate for the buffer pointed to by the <b>HwStreamExtension</b> member of a stream's <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>. The class driver will allocate one buffer for each stream.</p>
</dd>

### -field FilterInstanceExtensionSize

<dd>
<p>Specifies the size in bytes of the buffer the class extension should allocate for the buffer pointed to by the <b>HwInstanceExtension</b> member of <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a> structures it passes to the minidriver. The class driver allocates one buffer for each instance of the minidriver.</p>
</dd>

### -field BusMasterDMA

<dd>
<p>If <b>TRUE</b>, the device can perform direct bus-master DMA to the minidriver's DMA buffer.</p>
</dd>

### -field Dma24BitAddresses

<dd>
<p>Minidrivers should set this to <b>TRUE</b> if the DMA hardware the devices uses can access only the lower 24 bits of the address space.</p>
</dd>

### -field BufferAlignment

<dd>
<p>Specifies the alignment requirement, in bytes, for DMA buffers. For example, a value of 4 indicates the DMA buffers should be aligned on 4-byte boundaries.</p>
</dd>

### -field TurnOffSynchronization

<dd>
<p>If <b>TRUE</b>, the minidriver will handle its own synchronization; otherwise the class driver handles synchronization. Most minidrivers should set this value to <b>FALSE</b>. See <a href="https://msdn.microsoft.com/2f560e7a-4717-4b3f-9513-e34fcb2b5e6c">Minidriver Synchronization</a> in the <i>Streaming Minidriver Design Guide</i> for more information.</p>
</dd>

### -field DmaBufferSize

<dd>
<p>Specifies the size in bytes of the DMA buffer the class driver should allocate for the minidriver. The minidriver gets a pointer to this buffer by calling <a href="..\strmini\nf-strmini-streamclassgetdmabuffer.md">StreamClassGetDmaBuffer</a>. The class driver allocates contiguous nonpageable memory that will not be available to the operating system, or to other drivers, so this value should be as small as possible.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use. Minidrivers should ignore this member.</p>
</dd>
</dl>

## -remarks


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