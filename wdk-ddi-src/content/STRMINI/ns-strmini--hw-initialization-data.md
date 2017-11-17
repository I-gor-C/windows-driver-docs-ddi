---
UID: NS.strmini._HW_INITIALIZATION_DATA
title: HW_INITIALIZATION_DATA
author: windows-driver-content
description: The HW_INITIALIZATION_DATA structure specifies the basic information the class driver needs to begin initializing the minidriver.
old-location: stream\hw_initialization_data.htm
ms.assetid: 5be9ba51-bd6c-4650-9c48-f89267a2ac16
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
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
ms.keywords: HW_INITIALIZATION_DATA, HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA
req.iface: 
req.product: Windows 10 or later.
---

# HW_INITIALIZATION_DATA structure



## -description
<p>The HW_INITIALIZATION_DATA structure specifies the basic information the class driver needs to begin initializing the minidriver. The minidriver passes an HW_INITIALIZATION_DATA structure to the class driver when it registers itself by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>.</p>


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

### -field <b>HwInitializationDataSize</b>

<dd>
<p>Specifies the size of this data structure, in bytes.</p>
</dd>

### -field <b>HwInterrupt</b>

<dd>
<p>Points to the minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568459">StrMiniInterrupt</a> routine.</p>
</dd>

### -field <b>HwReceivePacket</b>

<dd>
<p>Points to the minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568463">StrMiniReceiveDevicePacket</a> routine.</p>
</dd>

### -field <b>HwCancelPacket</b>

<dd>
<p>Points to the minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568448">StrMiniCancelPacket</a> routine.</p>
</dd>

### -field <b>HwRequestTimeoutHandler</b>

<dd>
<p>Points to the minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568473">StrMiniRequestTimeout</a> routine.</p>
</dd>

### -field <b>DeviceExtensionSize</b>

<dd>
<p>Specifies the size in bytes of the buffer the class driver should allocate for the minidriver's device extension. The minidriver may use this buffer to record private information. The class driver passes pointers to this buffer in the <b>HwDeviceExtension</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559706">HW_TIME_CONTEXT</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.</p>
</dd>

### -field <b>PerRequestExtensionSize</b>

<dd>
<p>Specifies the size in bytes of the buffer the class driver should allocate for the buffer pointed to by <b>SRBExtension</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a> structures it passes to the minidriver. The class driver will allocate one buffer for each HW_STREAM_REQUEST_BLOCK.</p>
</dd>

### -field <b>PerStreamExtensionSize</b>

<dd>
<p>Specifies the size in bytes of the buffer the class driver should allocate for the buffer pointed to by the <b>HwStreamExtension</b> member of a stream's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559697">HW_STREAM_OBJECT</a>. The class driver will allocate one buffer for each stream.</p>
</dd>

### -field <b>FilterInstanceExtensionSize</b>

<dd>
<p>Specifies the size in bytes of the buffer the class extension should allocate for the buffer pointed to by the <b>HwInstanceExtension</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559702">HW_STREAM_REQUEST_BLOCK</a> structures it passes to the minidriver. The class driver allocates one buffer for each instance of the minidriver.</p>
</dd>

### -field <b>BusMasterDMA</b>

<dd>
<p>If <b>TRUE</b>, the device can perform direct bus-master DMA to the minidriver's DMA buffer.</p>
</dd>

### -field <b>Dma24BitAddresses</b>

<dd>
<p>Minidrivers should set this to <b>TRUE</b> if the DMA hardware the devices uses can access only the lower 24 bits of the address space.</p>
</dd>

### -field <b>BufferAlignment</b>

<dd>
<p>Specifies the alignment requirement, in bytes, for DMA buffers. For example, a value of 4 indicates the DMA buffers should be aligned on 4-byte boundaries.</p>
</dd>

### -field <b>TurnOffSynchronization</b>

<dd>
<p>If <b>TRUE</b>, the minidriver will handle its own synchronization; otherwise the class driver handles synchronization. Most minidrivers should set this value to <b>FALSE</b>. See <a href="NULL">Minidriver Synchronization</a> in the <i>Streaming Minidriver Design Guide</i> for more information.</p>
</dd>

### -field <b>DmaBufferSize</b>

<dd>
<p>Specifies the size in bytes of the DMA buffer the class driver should allocate for the minidriver. The minidriver gets a pointer to this buffer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff568243">StreamClassGetDmaBuffer</a>. The class driver allocates contiguous nonpageable memory that will not be available to the operating system, or to other drivers, so this value should be as small as possible.</p>
</dd>

### -field <b>Reserved</b>

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