---
UID : NS:netdma._NET_DMA_DESCRIPTOR
title : _NET_DMA_DESCRIPTOR
author : windows-driver-content
description : The NET_DMA_DESCRIPTOR structure specifies the DMA transfer information for each entry in a linked list of DMA descriptors.
old-location : netvista\net_dma_descriptor.htm
old-project : netvista
ms.assetid : 0465a8d7-1cdd-4647-9b78-557256f60c05
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NET_DMA_DESCRIPTOR, *PNET_DMA_DESCRIPTOR, NET_DMA_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : netdma.h
req.include-header : Netdma.h
req.target-type : Windows
req.target-min-winverclnt : Supported for NetDMA 2.0 drivers in Windows Server 2008. (Added NextSourceAddress,   NextDestinationAddress, DCAContext32, DCAContext16, and DCAContext8 members.) Supported for NetDMA 1.1   drivers in Windows Server 2008. Supported for NetDMA 1.0 drivers in Windows Server 2008 and Windows   Vista.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NET_DMA_DESCRIPTOR
req.alt-loc : netdma.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PNET_DMA_DESCRIPTOR, NET_DMA_DESCRIPTOR"
---

# _NET_DMA_DESCRIPTOR structure


## Syntax
````
typedef struct _NET_DMA_DESCRIPTOR {
  union {
    ULONG  TransferSize;
    struct {
      ULONG DCAContext  :32;
    } DCAContext32;
    struct {
      ULONG DCAContext  :16;
      ULONG Reserved  :16;
    } DCAContext16;
    struct {
      ULONG DCAContext  :8;
      ULONG Reserved  :24;
    } DCAContext8;
  };
  ULONG            ControlFlags;
  PHYSICAL_ADDRESS SourceAddress;
  PHYSICAL_ADDRESS DestinationAddress;
  PHYSICAL_ADDRESS NextDescriptor;
  union {
    ULONG64          Reserved1;
    PHYSICAL_ADDRESS NextSourceAddress;
  };
  union {
    ULONG64          Reserved2;
    PHYSICAL_ADDRESS NextDestinationAddress;
  };
  ULONG64          UserContext1;
  ULONG64          UserContext2;
} NET_DMA_DESCRIPTOR, *PNET_DMA_DESCRIPTOR;
````

## Members

        
            `ControlFlags`

            A set of flags that specify the operations that the DMA engine should perform for this DMA
     descriptor. This member must contain one or more of the following values (combined with a bitwise OR
     operation):

<table>
<tr>
<th>Unless otherwise noted, descriptions apply to when the bit is set.</th>
<th>Meaning</th>
</tr>
<tr>
        
            `DestinationAddress`

            The physical address of a memory block that is a destination for the DMA transfer.
        
            `NextDescriptor`

            The physical address of the next NET_DMA_DESCRIPTOR structure in the linked list of descriptors.
     If this descriptor is the last descriptor in the list, 
     <b>NextDescriptor</b> is <b>NULL</b>.
        
            `SourceAddress`

            The physical address of a memory block that is a source for the DMA transfer.
        
            `UserContext1`

            A ULONG64 value that is reserved for the NetDMA interface to use.
        
            `UserContext2`

            A ULONG64 value that is reserved for the NetDMA interface to use.

    ## Remarks
        The NET_DMA_DESCRIPTOR structure specifies the source, destination, and control information for a
    single DMA transfer in a linked list of DMA descriptors.

To start a DMA transfer, the NetDMA interface supplies the physical address of a NET_DMA_DESCRIPTOR
    structure at the 
    <i>DescriptorPhysicalAddress</i> parameter of the DMA provider driver's 
    <a href="..\netdma\nc-netdma-dma_start_handler.md">ProviderStartDma</a> function. The 
    <i>DescriptorVirtualAddress</i> parameter contains the virtual address of the descriptor.

The 
    <b>NextDescriptor</b> member of a NET_DMA_DESCRIPTOR structure contains the physical address of the next
    NET_DMA_DESCRIPTOR structure in the linked list of descriptors.

The NetDMA interface calls a DMA provider driver's 
    <a href="..\netdma\nc-netdma-dma_append_handler.md">ProviderAppendDma</a> function to append a
    linked list of DMA descriptors after the last descriptor on a DMA channel.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | netdma.h (include Netdma.h) |

    ## See Also

        <dl>
<dt>
<a href="..\netdma\ns-netdma-_net_dma_channel_parameters.md">NET_DMA_CHANNEL_PARAMETERS</a>
</dt>
<dt>
<a href="..\netdma\nc-netdma-dma_append_handler.md">ProviderAppendDma</a>
</dt>
<dt>
<a href="..\netdma\nc-netdma-dma_start_handler.md">ProviderStartDma</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_DMA_DESCRIPTOR structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>