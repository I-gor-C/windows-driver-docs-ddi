---
UID: NS.dot11wdi._WDI_TXRX_TARGET_CAPABILITIES
title: WDI_TXRX_TARGET_CAPABILITIES
author: windows-driver-content
description: The WDI_TXRX_CAPABILITIES structure defines the target capabilities.
old-location: netvista\wdi_txrx_capabilities.htm
old-project: netvista
ms.assetid: 7a1d3ffd-6f5e-429d-8c2f-a141f98ccad8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDI_TXRX_TARGET_CAPABILITIES, WDI_TXRX_CAPABILITIES, *PWDI_TXRX_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_TXRX_CAPABILITIES
req.alt-loc: dot11wdi.h
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
---

# WDI_TXRX_TARGET_CAPABILITIES structure



## -description
<p>The 
   WDI_TXRX_CAPABILITIES structure defines the target capabilities.</p>


## -syntax

````
typedef struct _WDI_TXRX_CAPABILITIES {
  WDI_INTERCONNECT_TYPE InterconnectType;
  struct {
    BOOLEAN TargetPriorityQueueing;
    UINT16  MaxMemBlocksPerFrame;
    BOOLEAN ExplicitSendCompleteFlagRequired;
    UINT8   bPad;
    UINT16  MinEffectiveSize;
    UINT16  FrameSizeGranularity;
  } TransmitCapabilities;
  struct {
    BOOLEAN RxTxForwarding;
    UINT32  MaxThroughput;
  } ReceiveCapabilities;
} WDI_TXRX_CAPABILITIES, *PWDI_TXRX_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>InterconnectType</b>

<dd>
<p>Interconnect type of the target.</p>
</dd>

### -field <b>TransmitCapabilities</b>

<dd>
<p>Transmit capabilities.</p>
<dl>

### -field <b>TargetPriorityQueueing</b>

<dd>
<p>If true, WDI does not classify Tx frames by Peer and TID, and only provides queuing at a port level.  WDI schedules backlogged port queues using a global DRR.</p>
<p>If false, WDI classifies Tx frames by Peer and TID and utilizes the full scheduler to select TX queues to transfer.</p>
<p>Setting this to false is recommended unless the target is capable of classification and Peer-TID queueing.</p>
</dd>

### -field <b>MaxMemBlocksPerFrame</b>

<dd>
<p>Maximum number of Scatter Gather elements in a frame.  WDI coalesces frames as necessary so that the IHV miniport does not receive a frame that requires more scatter gather elements than specified by this capability.  For best performance, it is suggested that this capability is set higher than the typical frame as the coalescing requires a memory copy.  If this capability is not greater than the maximum frame size divided by page size, WDI may be unable to successfully coalesce the frame and it may be dropped.</p>
</dd>

### -field <b>ExplicitSendCompleteFlagRequired</b>

<dd>
<p>If true, the target/TAL generates a TX send completion indication only for frames that have this flag set in the frame's metadata.</p>
<p>If false, the target/TAL generates a TX send completion indication for all frames</p>
</dd>

### -field <b>bPad</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>MinEffectiveSize</b>

<dd>
<p>When dequeuing frames, the TxMgr treats frames smaller than <b>MinEffectiveSize</b> as having an effective size of <b>MinEffectiveSize</b>.</p>
</dd>

### -field <b>FrameSizeGranularity</b>

<dd>
<p>This value is equal to the granularity of memory allocation per frame.  For the purposes of dequeuing, the TxMgr treats a frame as having an effective size equal to the frame size plus the least amount of padding such that the effective size is an integer multiple of the <b>FrameSizeGranularity</b>.</p>
<p>This value must be set to a power of two.</p>
</dd>
</dl>
</dd>

### -field <b>ReceiveCapabilities</b>

<dd>
<p>Receive capabilities.</p>
<dl>

### -field <b>RxTxForwarding</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>MaxThroughput</b>

<dd>
<p>Specifies the maximum throughput of the device in units of 0.5 Mbps.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>