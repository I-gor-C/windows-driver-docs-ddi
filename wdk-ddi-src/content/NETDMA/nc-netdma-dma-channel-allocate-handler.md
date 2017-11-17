---
UID: NC.netdma.DMA_CHANNEL_ALLOCATE_HANDLER
title: DMA_CHANNEL_ALLOCATE_HANDLER
author: windows-driver-content
description: The ProviderAllocateDmaChannel function allocates a DMA channel.
old-location: netvista\providerallocatedmachannel.htm
ms.assetid: 42bc0e08-3d85-424f-aaa4-4df788d3706a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NetDMA 1.0 drivers in Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProviderAllocateDmaChannel
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: MIRACAST_WFD_CONNECTION_STATS, MIRACAST_WFD_CONNECTION_STATS
req.iface: 
---

# DMA_CHANNEL_ALLOCATE_HANDLER callback



## -description

## -prototype

````
DMA_CHANNEL_ALLOCATE_HANDLER ProviderAllocateDmaChannel;

NTSTATUS ProviderAllocateDmaChannel(
  _In_  PVOID                       ProviderContext,
  _In_  PNET_DMA_CHANNEL_PARAMETERS ChannelParameters,
  _In_  PVOID                       NetDmaChannelHandle,
  _Out_ PVOID                       *pProviderChannelContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProviderContext</i> [in]

<dd>
<p>A pointer that identifies a DMA provider's context area. The DMA provider driver passes this
     handle to the NetDMA interface in a call to the 
     <a href="https://msdn.microsoft.com/35d70d0b-c1b9-433f-941d-6cb61ddf0b62">
     NetDmaRegisterProvider</a> function.</p>
</dd>

### -param <i>ChannelParameters</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/0d09a9e9-06c5-4026-9053-ac74a59509cc">
     NET_DMA_CHANNEL_PARAMETERS</a> structure that defines the configuration parameters for the DMA
     channel.</p>
</dd>

### -param <i>NetDmaChannelHandle</i> [in]

<dd>
<p>A handle that identifies the DMA channel. Provider drivers pass this handle to 
     <b>NetDma<i>Xxx</i></b> functions to identify the DMA channel.</p>
</dd>

### -param <i>pProviderChannelContext</i> [out]

<dd>
<p>A pointer to a value that is a pointer to a DMA provider's context area for the DMA channel. The
     DMA provider driver allocates this context area before returning from 
     <i>ProviderAllocateDmaChannel</i>. NetDMA passes the context area pointer to 
     <i>ProviderXxx</i> functions that require a provider channel context.</p>
</dd>
</dl>

## -returns
<p><i>ProviderAllocateDmaChannel</i> returns one of the following status values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>STATUS_RESOURCES</b></dt>
</dl><p>The operation failed because of insufficient resources.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The operation failed for unspecified reasons.</p>

<p> </p>

## -remarks
<p>The NetDMA interface calls a DMA provider driver's 
    <i>ProviderAllocateDmaChannel</i> function to allocate a DMA channel. The NetDMA interface calls 
    <i>ProviderAllocateDmaChannel</i> before it uses a DMA channel.</p>

<p>The DMA provider driver attempts to allocate a DMA channel with an interrupt CPU affinity that matches
    a bit that is specified in the 
    <b>ProcessorAffinityMask</b> member of the 
    <a href="https://msdn.microsoft.com/0d09a9e9-06c5-4026-9053-ac74a59509cc">
    NET_DMA_CHANNEL_PARAMETERS</a> structure at the 
    <i>ChannelParameters</i> parameter. If MSI-X is not supported or MSI-X is supported but a DMA channel with
    a matching interrupt CPU affinity is not available, the DMA provider driver allocates any available DMA
    channel and calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff553278">KeSetTargetProcessorDpc</a> routine to
    set the target CPU of the interrupt DPC to match one of the specified affinity mask bits.</p>

<p>The DMA provider always driver returns the CPU number that it associated with the interrupt DPC for
    the DMA channel to the NetDMA interface in the 
    <b>CpuNumber</b> member of the NET_DMA_CHANNEL_PARAMETERS structure.</p>

<p>The DMA provider driver provides a pointer to a block of driver-allocated context information at the 
    <i>pProviderChannelContext</i> parameter of 
    <i>ProviderAllocateDmaChannel</i>. This context area stores information about the DMA channel. The NetDMA
    interface passes the context information in subsequent calls to 
    <i>ProviderXxx</i> functions that require a DMA channel context.</p>

<p>When the NetDMA interface calls 
    <i>ProviderAllocateDmaChannel</i>, it provides a handle at the 
    <i>NetDmaChannelHandle</i> parameter. The DMA provider driver uses this handle in subsequent calls to 
    <b>NetDma<i>Xxx</i></b> functions that are associated with the DMA channel.</p>

<p>The NetDMA interface calls the 
    <a href="https://msdn.microsoft.com/5bbe432d-f236-46ec-8e78-788bd676b852">ProviderFreeDmaChannel</a> function to
    free a previously allocated DMA channel.</p>

<p>NetDMA calls 
    <i>ProviderAllocateDmaChannel</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>The NetDMA interface calls a DMA provider driver's 
    <i>ProviderAllocateDmaChannel</i> function to allocate a DMA channel. The NetDMA interface calls 
    <i>ProviderAllocateDmaChannel</i> before it uses a DMA channel.</p>

<p>The DMA provider driver attempts to allocate a DMA channel with an interrupt CPU affinity that matches
    a bit that is specified in the 
    <b>ProcessorAffinityMask</b> member of the 
    <a href="https://msdn.microsoft.com/0d09a9e9-06c5-4026-9053-ac74a59509cc">
    NET_DMA_CHANNEL_PARAMETERS</a> structure at the 
    <i>ChannelParameters</i> parameter. If MSI-X is not supported or MSI-X is supported but a DMA channel with
    a matching interrupt CPU affinity is not available, the DMA provider driver allocates any available DMA
    channel and calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff553278">KeSetTargetProcessorDpc</a> routine to
    set the target CPU of the interrupt DPC to match one of the specified affinity mask bits.</p>

<p>The DMA provider always driver returns the CPU number that it associated with the interrupt DPC for
    the DMA channel to the NetDMA interface in the 
    <b>CpuNumber</b> member of the NET_DMA_CHANNEL_PARAMETERS structure.</p>

<p>The DMA provider driver provides a pointer to a block of driver-allocated context information at the 
    <i>pProviderChannelContext</i> parameter of 
    <i>ProviderAllocateDmaChannel</i>. This context area stores information about the DMA channel. The NetDMA
    interface passes the context information in subsequent calls to 
    <i>ProviderXxx</i> functions that require a DMA channel context.</p>

<p>When the NetDMA interface calls 
    <i>ProviderAllocateDmaChannel</i>, it provides a handle at the 
    <i>NetDmaChannelHandle</i> parameter. The DMA provider driver uses this handle in subsequent calls to 
    <b>NetDma<i>Xxx</i></b> functions that are associated with the DMA channel.</p>

<p>The NetDMA interface calls the 
    <a href="https://msdn.microsoft.com/5bbe432d-f236-46ec-8e78-788bd676b852">ProviderFreeDmaChannel</a> function to
    free a previously allocated DMA channel.</p>

<p>NetDMA calls 
    <i>ProviderAllocateDmaChannel</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NetDMA 1.0 drivers in Windows Vista.</p>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553278">KeSetTargetProcessorDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568732">NET_DMA_CHANNEL_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568336">NetDmaRegisterProvider</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5bbe432d-f236-46ec-8e78-788bd676b852">ProviderFreeDmaChannel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DMA_CHANNEL_ALLOCATE_HANDLER callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
