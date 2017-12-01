---
UID: NS.netdma._NET_DMA_CHANNEL_PARAMETERS
title: NET_DMA_CHANNEL_PARAMETERS
author: windows-driver-content
description: The NET_DMA_CHANNEL_PARAMETERS structure specifies the configuration parameters that a DMA provider driver should use to configure a DMA channel.
old-location: netvista\net_dma_channel_parameters.htm
old-project: netvista
ms.assetid: 0d09a9e9-06c5-4026-9053-ac74a59509cc
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NET_DMA_CHANNEL_PARAMETERS, NET_DMA_CHANNEL_PARAMETERS, *PNET_DMA_CHANNEL_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_DMA_CHANNEL_PARAMETERS
req.alt-loc: netdma.h
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

# NET_DMA_CHANNEL_PARAMETERS structure



## -description

## -syntax

````
typedef struct _NET_DMA_CHANNEL_PARAMETERS {
  USHORT           Revision;
  USHORT           Size;
  ULONG            Flags;
  PVOID            CompletionVirtualAddress;
  PHYSICAL_ADDRESS CompletionPhysicalAddress;
  ULONG            ProcessorAffinityMask;
  ULONG            ChannelPriority;
  ULONG            CpuNumber;
#if NTDDI_VERSION >= NTDDI_WIN7
  GROUP_AFFINITY   ProcessorAffinityMaskEx;
#endif 
} NET_DMA_CHANNEL_PARAMETERS, *PNET_DMA_CHANNEL_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Revision</b>

<dd>
<p>The revision number of this structure. </p>
<p>For Windows 7 and Windows Server 2008 R2 and later, set this member to
     <b>NET_DMA_CHANNEL_PARAMETERS_REVISION_2</b>.</p>
<p>For Windows Vista and Windows Server 2008, set this member to
     <b>NET_DMA_CHANNEL_PARAMETERS_REVISION_1</b>.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure. Set this member to 
     sizeof(<b>NET_DMA_CHANNEL_PARAMETERS</b>).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A set of bits for flags that define DMA channel attributes. Set this member to zero. There are
     currently no flags defined.</p>
</dd>

### -field <b>CompletionVirtualAddress</b>

<dd>
<p>The virtual address of the memory location where the DMA engine can write the DMA transfer
     completion status. This virtual address is associated with the physical address that is specified in the
     
     <b>CompletionPhysicalAddress</b> member.</p>
</dd>

### -field <b>CompletionPhysicalAddress</b>

<dd>
<p>The physical address of the memory location where the DMA engine can write the DMA transfer
     completion status. If the <b>NET_DMA_STATUS_UPDATE_ON_COMPLETION</b> flag is not set in the 
     <b>ControlFlags</b> member of the 
     <a href="..\netdma\ns-netdma--net-dma-descriptor.md">NET_DMA_DESCRIPTOR</a> structure, 
     <b>CompletionPhysicalAddress</b> is not used. Otherwise, the completion status value at the specified
     address is a 64-bit wide combination of the physical address of the most recent DMA descriptor that the
     DMA engine processed and additional status information. 
     </p>
<p>The physical address of the DMA descriptor must be aligned to 64-bit boundaries. Therefore, the lower
     six bits of the address are available for other information. The DMA engine combines the following
     status values with the descriptor address by using a bitwise OR operation:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NetDmaTransferStatusActive"></a><a id="netdmatransferstatusactive"></a><a id="NETDMATRANSFERSTATUSACTIVE"></a><dl>

### -field <b><b>NetDmaTransferStatusActive</b></b>

</dl>
</td>
<td width="60%">
<p>The DMA transfer for the most recent DMA descriptor completed without errors, and the DMA engine
       has more descriptors to process.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NetDmaTransferStatusIdle"></a><a id="netdmatransferstatusidle"></a><a id="NETDMATRANSFERSTATUSIDLE"></a><dl>

### -field <b><b>NetDmaTransferStatusIdle</b></b>

</dl>
</td>
<td width="60%">
<p>The DMA transfer for the last DMA descriptor in the linked list of descriptors completed without
       errors.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NetDmaTransferStatusSuspend"></a><a id="netdmatransferstatussuspend"></a><a id="NETDMATRANSFERSTATUSSUSPEND"></a><dl>

### -field <b><b>NetDmaTransferStatusSuspend</b></b>

</dl>
</td>
<td width="60%">
<p>The DMA transfer for the most recent DMA descriptor completed without errors, and DMA transfers
       are suspended because the NetDMA interface called the 
       <a href="..\netdma\nc-netdma-dma-suspend-handler.md">ProviderSuspendDma</a> function. The DMA
       engine will restart the transfer after the NetDMA interface calls the 
       <a href="..\netdma\nc-netdma-dma-resume-handler.md">ProviderResumeDma</a> function.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NetDmaTransferStatusHalted"></a><a id="netdmatransferstatushalted"></a><a id="NETDMATRANSFERSTATUSHALTED"></a><dl>

### -field <b><b>NetDmaTransferStatusHalted</b></b>

</dl>
</td>
<td width="60%">
<p>The DMA transfer for the most recent DMA transfer was aborted because of errors or because the
       NetDMA interface called the 
       <a href="..\netdma\nc-netdma-dma-abort-handler.md">ProviderAbortDma</a> function.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NetDmaTransferStatusArmed"></a><a id="netdmatransferstatusarmed"></a><a id="NETDMATRANSFERSTATUSARMED"></a><dl>

### -field <b><b>NetDmaTransferStatusArmed</b></b>

</dl>
</td>
<td width="60%">
<p>The DMA transfer for the first descriptor has not completed and the completed descriptor address
       is not valid.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ProcessorAffinityMask</b>

<dd>
<p>A bitmap that indicates CPUs that are available for use with this DMA channel. Each bit in 
     <b>ProcessorAffinityMask</b> identifies a CPU. For example, setting bit 0 indicates CPU 0 can be used,
     setting bit 1 indicates CPU 1 can be used, and so on.</p>
</dd>

### -field <b>ChannelPriority</b>

<dd>
<p>A DMA channel priority value that represents the priority for the DMA channel relative to other
     DMA channels on the same DMA engine. A lower priority setting indicates a lower priority DMA channel. If
     this value indicates a higher priority than the hardware supports, the highest value that the hardware
     supports should be used. The Windows Vista NetDMA interface sets this member to zero.</p>
</dd>

### -field <b>CpuNumber</b>

<dd>
<p>The CPU number that is associated with the DMA channel. The DMA provider driver sets the value
     before it returns from the 
     
     <a href="..\netdma\nc-netdma-dma-channel-allocate-handler.md">ProviderAllocateDmaChannel</a> function. The DMA engine uses this CPU for interrupt DPCs that are
     associated with the DMA channel. If the DMA engine and computer configuration support MSI-X, the
     interrupt should also be associated with the indicated CPU number, unless there was no MSI-X interrupt
     available for the indicated CPU.</p>
</dd>

### -field <b>ProcessorAffinityMaskEx</b>

<dd>
<p>The group number and a bitmap of the CPUs that this DMA channel could be associated with.</p>
</dd>
</dl>

## -remarks
<p>Before using a DMA channel, the NetDMA interface calls the 
    
    <a href="..\netdma\nc-netdma-dma-channel-allocate-handler.md">ProviderAllocateDmaChannel</a> function of the DMA provider driver to allocate and initialize the DMA
    channel.</p>

<p>The NetDMA interface supplies a <b>NET_DMA_CHANNEL_PARAMETERS</b> structure at the 
    <i>ChannelParameters</i> parameter of 
    <a href="..\netdma\nc-netdma-dma-channel-allocate-handler.md">ProviderAllocateDmaChannel</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdma.h (include Netdma.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netdma\ns-netdma--net-dma-descriptor.md">NET_DMA_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\netdma\nc-netdma-dma-abort-handler.md">ProviderAbortDma</a>
</dt>
<dt>
<a href="..\netdma\nc-netdma-dma-channel-allocate-handler.md">ProviderAllocateDmaChannel</a>
</dt>
<dt>
<a href="..\netdma\nc-netdma-dma-resume-handler.md">ProviderResumeDma</a>
</dt>
<dt>
<a href="..\netdma\nc-netdma-dma-suspend-handler.md">ProviderSuspendDma</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_DMA_CHANNEL_PARAMETERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
