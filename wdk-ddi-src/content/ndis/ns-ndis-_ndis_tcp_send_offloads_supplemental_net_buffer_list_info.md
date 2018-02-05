---
UID : NS:ndis._NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
title : "_NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO"
author : windows-driver-content
description : The NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure contains additional out-of-band information for encapsulated packets.
old-location : netvista\ndis_tcp_send_offloads_supplemental_net_buffer_list_info.htm
old-project : netvista
ms.assetid : 6688CF73-7048-4709-A50D-1D5DB17C8538
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure [Network Drivers Starting with Windows Vista], PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, ndis/PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, *PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, netvista.ndis_tcp_send_offloads_supplemental_net_buffer_list_info, PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure pointer [Network Drivers Starting with Windows Vista], ndis/NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndis.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.30 and later.
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
req.irql : See Remarks section
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO"
---

# _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure
The <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> structure contains additional out-of-band information for encapsulated packets. For more information, see <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/jj991956">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a> (NVGRE-TO).

## Syntax
````
typedef struct _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO {
  union {
    struct {
      ULONG IsEncapsulatedPacket  :1;
      ULONG EncapsulatedPacketOffsetsValid  :1;
      ULONG InnerFrameOffset  :8;
      ULONG TransportIpHeaderRelativeOffset  :6;
      ULONG TcpHeaderRelativeOffset  :10;
      ULONG IsInnerIPv6  :1;
      ULONG TcpOptionsPresent  :1;
      ULONG Reserved  :4;
    } EncapsulatedPacketOffsets;
    PVOID Value;
  };
} NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, *PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO;
````

## Members


## Remarks
The members of <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> are meaningful if and only if <b>TcpIpChecksumNetBufferListInfo</b> or <b>TcpLargeSendNetBufferListInfo</b> is specified in the <a href="..\ndis\ne-ndis-_ndis_net_buffer_list_info.md">NDIS_NET_BUFFER_LIST_INFO</a> structure.

If the <b>IsEncapsulatedPacket</b> member is <b>TRUE</b> and the <b>TcpIpChecksumNetBufferListInfo</b> out-of-band (OOB) information is valid, this indicates that NVGRE support is required and the NIC must compute the checksum for the tunnel (outer) IP header, the transport (inner) IP header, and the TCP or UDP header if one of them is present. An NVGRE packet will only be offloaded if the packet conforms to miniport-advertised capabilities. For example, a packet containing a UDP header will not be offloaded if the miniport did not advertise UDP Tx checksum offload support in its base capabilities. For more information, see <a href="https://msdn.microsoft.com/5fb2f379-c357-4ec3-b103-bdbe23fcc033">Offloading Checksum Tasks</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ndis.h |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/jj991956">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>

<a href="..\ndis\ne-ndis-_ndis_net_buffer_list_info.md">NDIS_NET_BUFFER_LIST_INFO</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_encapsulated_packet_task_offload.md">NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD</a>

<a href="https://msdn.microsoft.com/5fb2f379-c357-4ec3-b103-bdbe23fcc033">Offloading Checksum Tasks</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>