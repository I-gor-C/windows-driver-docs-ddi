---
UID: NS:ndis._NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
title: "_NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO"
author: windows-driver-content
description: The NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure contains additional out-of-band information for encapsulated packets.
old-location: netvista\ndis_tcp_send_offloads_supplemental_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 6688CF73-7048-4709-A50D-1D5DB17C8538
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure [Network Drivers Starting with Windows Vista], PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure pointer [Network Drivers Starting with Windows Vista], _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, ndis/NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, ndis/PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, netvista.ndis_tcp_send_offloads_supplemental_net_buffer_list_info"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ndis.h
api_name:
-	NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
product: Windows
targetos: Windows
req.typenames: NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, *PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
---

# _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure
The <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> structure contains additional out-of-band information for encapsulated packets. For more information, see <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/jj991956">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a> (NVGRE-TO).

## Syntax
```
typedef struct _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO {
  union {
    struct {
      ULONG  : 1  IsEncapsulatedPacket;
      ULONG  : 1  EncapsulatedPacketOffsetsValid;
      ULONG  : 8  InnerFrameOffset;
      ULONG  : 6  TransportIpHeaderRelativeOffset;
      ULONG  : 10 TcpHeaderRelativeOffset;
      ULONG  : 1  IsInnerIPv6;
      ULONG  : 1  TcpOptionsPresent;
      ULONG  : 4  Reserved;
    } EncapsulatedPacketOffsets;
    PVOID Value;
  };
} NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, *PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO;
```

## Members


## Remarks
The members of <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> are meaningful if and only if <b>TcpIpChecksumNetBufferListInfo</b> or <b>TcpLargeSendNetBufferListInfo</b> is specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566569">NDIS_NET_BUFFER_LIST_INFO</a> structure.

If the <b>IsEncapsulatedPacket</b> member is <b>TRUE</b> and the <b>TcpIpChecksumNetBufferListInfo</b> out-of-band (OOB) information is valid, this indicates that NVGRE support is required and the NIC must compute the checksum for the tunnel (outer) IP header, the transport (inner) IP header, and the TCP or UDP header if one of them is present. An NVGRE packet will only be offloaded if the packet conforms to miniport-advertised capabilities. For example, a packet containing a UDP header will not be offloaded if the miniport did not advertise UDP Tx checksum offload support in its base capabilities. For more information, see <a href="https://msdn.microsoft.com/5fb2f379-c357-4ec3-b103-bdbe23fcc033">Offloading Checksum Tasks</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ndis.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/jj991956">NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566569">NDIS_NET_BUFFER_LIST_INFO</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/jj991956">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>



<a href="https://msdn.microsoft.com/5fb2f379-c357-4ec3-b103-bdbe23fcc033">Offloading Checksum Tasks</a>