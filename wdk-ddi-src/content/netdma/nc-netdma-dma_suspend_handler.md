---
UID : NC:netdma.DMA_SUSPEND_HANDLER
title : DMA_SUSPEND_HANDLER
author : windows-driver-content
description : The ProviderSuspendDma function suspends the DMA transfers that are currently in progress on a DMA channel.
old-location : netvista\providersuspenddma.htm
old-project : netvista
ms.assetid : b020b0c6-eb69-44d0-a374-b39eb2f536f1
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.providersuspenddma, ProviderSuspendDma callback function [Network Drivers Starting with Windows Vista], ProviderSuspendDma, DMA_SUSPEND_HANDLER, DMA_SUSPEND_HANDLER, netdma/ProviderSuspendDma, netdma_ref_f194d9b0-083c-46a1-9e39-aa33c62af512.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : netdma.h
req.include-header : Netdma.h
req.target-type : Windows
req.target-min-winverclnt : Supported for NetDMA 1.0 drivers in Windows Vista.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<= DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PMIRACAST_DRIVER_INTERFACE, MIRACAST_DRIVER_INTERFACE"
---


# DMA_SUSPEND_HANDLER callback function
<div class="alert"><b>Note</b>  The NetDMA interface is not supported 

in Windows 8 and later.</div><div> </div>The 
  <i>ProviderSuspendDma</i> function suspends the DMA transfers that are currently in progress on a DMA
  channel.

## Syntax

```
DMA_SUSPEND_HANDLER DmaSuspendHandler;

NTSTATUS DmaSuspendHandler(
  PVOID ProviderChannelContext,
  PPHYSICAL_ADDRESS *pLastDescriptor
)
{...}
```

## Parameters

`ProviderChannelContext`

A pointer that identifies a DMA channel's context area. The DMA provider returned this handle to
     NetDMA at the location that is specified in the 
     <i>pProviderChannelContext</i> parameter of the 
     <mshelp:link keywords="netvista.providerallocatedmachannel" tabindex="0"><b>
     ProviderAllocateDmaChannel</b></mshelp:link> function.

`*pLastDescriptor`




## Return Value

<i>ProviderSuspendDma</i> returns one of the following status values:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The operation completed successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>
</td>
<td width="60%">
The operation failed for unspecified reasons.

</td>
</tr>
</table>

## Remarks

The 
    <i>ProviderSuspendDma</i> function is an optional function for NetDMA providers. The NetDMA interface can
    call the 
    <i>ProviderSuspendDma</i> function, if any, to temporarily suspend any DMA transfers that are in progress
    on a DMA channel.

The DMA provider completes the transfer of the current DMA descriptor before it returns from 
    <i>ProviderSuspendDma</i>. If completion status reporting is enabled, the DMA engine writes the 
    <b>NetDmaTransferStatusSuspend</b> status in the address that is specified in the 
    <b>CompletionVirtualAddress</b> and 
    <b>CompletionPhysicalAddress</b> members in the 
    <mshelp:link keywords="netvista.net_dma_channel_parameters" tabindex="0"><b>
    NET_DMA_CHANNEL_PARAMETERS</b></mshelp:link> structure.

While the DMA transfers are suspended, the NetDMA interface can modify the DMA descriptor linked list
    (for example, to insert or delete descriptors).

The NetDMA interface calls the 
    <a href="..\netdma\nc-netdma-dma_resume_handler.md">ProviderResumeDma</a> function to resume DMA
    operations that were suspended by calling 
    <i>ProviderSuspendDma</i>.

NetDMA calls 
    <i>ProviderSuspendDma</i> at IRQL &lt;= DISPATCH_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | netdma.h (include Netdma.h) |
| **Library** |  |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** |  |

## See Also

<a href="..\netdma\ns-netdma-_net_dma_channel_parameters.md">NET_DMA_CHANNEL_PARAMETERS</a>

<a href="..\netdma\nc-netdma-dma_resume_handler.md">ProviderResumeDma</a>

<a href="..\netdma\nc-netdma-dma_channel_allocate_handler.md">ProviderAllocateDmaChannel</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DMA_SUSPEND_HANDLER callback function%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>