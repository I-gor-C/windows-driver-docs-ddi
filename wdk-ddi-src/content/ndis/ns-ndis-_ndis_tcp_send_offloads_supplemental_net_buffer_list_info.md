---
UID: NS.NDIS._NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
title: _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
author: windows-driver-content
description: The NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure contains additional out-of-band information for encapsulated packets.
old-location: netvista\ndis_tcp_send_offloads_supplemental_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 6688CF73-7048-4709-A50D-1D5DB17C8538
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, *PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
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
req.alt-api: NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
req.alt-loc: Ndis.h
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
---

# _NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure



## -description
The <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> structure contains additional out-of-band information for encapsulated packets. For more information, see <a href="netvista.network_virtualization_using_generic_routing_encapsulation__nvgre__task_offload">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a> (NVGRE-TO).



## -syntax

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


## -struct-fields

### -field EncapsulatedPacketOffsets


### -field IsEncapsulatedPacket

If this member is  <b>TRUE</b>, this NBL represents a packet containing an inner Ethernet frame with a transport IP header. It is <b>FALSE</b> for normal packets. When <b>IsEncapsulatedPacket</b> is <b>TRUE</b>, the existing header offset fields, <a href="netvista.ndis_tcp_large_send_offload_net_buffer_list_info">NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</a>.<b>LsoV2Transmit</b>.<b>TcpHeaderOffset</b> and <a href="netvista.ndis_tcp_ip_checksum_net_buffer_list_info">NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</a>.<b>Transmit</b>.<b>TcpHeaderOffset</b>, will not have correct values and must not be used by the NIC or driver. Instead, the miniport driver must use the offsets specified in the other members of this structure.


### -field EncapsulatedPacketOffsetsValid

If this member is <b>TRUE</b>, the <b>InnerFrameOffset</b>, <b>TransportIpHeaderRelativeOffset</b>, and <b>TcpHeaderRelativeOffset</b> members
have valid values.


### -field InnerFrameOffset

Offset from the beginning of the packet to the first byte of the inner Ethernet frame.


### -field TransportIpHeaderRelativeOffset

Offset to the first byte of the inner IP header relative to the <b>InnerFrameOffset</b>.


### -field TcpHeaderRelativeOffset

Offset to the first byte of the inner (transport) header relative to the <b>TransportIpHeaderRelativeOffset</b>. This value is always set to the correct offset, even if the inner frame is not a TCP packet.


### -field IsInnerIPv6

Set by the protocol driver to indicate that the inner IP header in the encapsulated packet contains IPv6 addresses.


### -field TcpOptionsPresent

Set by the protocol driver when the inner TCP header contains TCP options. This allows a miniport driver to optimize the case when there are no options to assume the TCP header length to access the payload.


### -field Reserved

Reserved for future use.

</dd>
</dl>

### -field Value

Reserved for future use.


## -remarks
The members of <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> are meaningful if and only if <b>TcpIpChecksumNetBufferListInfo</b> or <b>TcpLargeSendNetBufferListInfo</b> is specified in the <a href="netvista.ndis_net_buffer_list_info">NDIS_NET_BUFFER_LIST_INFO</a> structure.

If the <b>IsEncapsulatedPacket</b> member is <b>TRUE</b> and the <b>TcpIpChecksumNetBufferListInfo</b> out-of-band (OOB) information is valid, this indicates that NVGRE support is required and the NIC must compute the checksum for the tunnel (outer) IP header, the transport (inner) IP header, and the TCP or UDP header if one of them is present. An NVGRE packet will only be offloaded if the packet conforms to miniport-advertised capabilities. For example, a packet containing a UDP header will not be offloaded if the miniport did not advertise UDP Tx checksum offload support in its base capabilities. For more information, see <a href="netvista.offloading_checksum_tasks">Offloading Checksum Tasks</a>.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.30 and later. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_encapsulated_packet_task_offload">NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD</a>
</dt>
<dt>
<a href="netvista.ndis_net_buffer_list_info">NDIS_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="netvista.network_virtualization_using_generic_routing_encapsulation__nvgre__task_offload">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>
</dt>
<dt>
<a href="netvista.offloading_checksum_tasks">Offloading Checksum Tasks</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

