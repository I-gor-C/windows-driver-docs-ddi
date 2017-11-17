---
UID: NS.ndis._NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
title: NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
author: windows-driver-content
description: The NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure contains additional out-of-band information for encapsulated packets.
old-location: netvista\ndis_tcp_send_offloads_supplemental_net_buffer_list_info.htm
ms.assetid: 6688CF73-7048-4709-A50D-1D5DB17C8538
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO, *PNDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO
req.iface: 
---

# NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure



## -description
<p>The <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> structure contains additional out-of-band information for encapsulated packets. For more information, see <a href="NULL">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a> (NVGRE-TO).</p>


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
<dl>

### -field <b>EncapsulatedPacketOffsets</b>

<dd>
<dl>

### -field <b>IsEncapsulatedPacket</b>

<dd>
<p>If this member is  <b>TRUE</b>, this NBL represents a packet containing an inner Ethernet frame with a transport IP header. It is <b>FALSE</b> for normal packets. When <b>IsEncapsulatedPacket</b> is <b>TRUE</b>, the existing header offset fields, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567882">NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</a>.<b>LsoV2Transmit</b>.<b>TcpHeaderOffset</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567877">NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</a>.<b>Transmit</b>.<b>TcpHeaderOffset</b>, will not have correct values and must not be used by the NIC or driver. Instead, the miniport driver must use the offsets specified in the other members of this structure.</p>
</dd>

### -field <b>EncapsulatedPacketOffsetsValid</b>

<dd>
<p>If this member is <b>TRUE</b>, the <b>InnerFrameOffset</b>, <b>TransportIpHeaderRelativeOffset</b>, and <b>TcpHeaderRelativeOffset</b> members
have valid values.</p>
</dd>

### -field <b>InnerFrameOffset</b>

<dd>
<p>Offset from the beginning of the packet to the first byte of the inner Ethernet frame.</p>
</dd>

### -field <b>TransportIpHeaderRelativeOffset</b>

<dd>
<p>Offset to the first byte of the inner IP header relative to the <b>InnerFrameOffset</b>.</p>
</dd>

### -field <b>TcpHeaderRelativeOffset</b>

<dd>
<p>Offset to the first byte of the inner (transport) header relative to the <b>TransportIpHeaderRelativeOffset</b>. This value is always set to the correct offset, even if the inner frame is not a TCP packet.</p>
</dd>

### -field <b>IsInnerIPv6</b>

<dd>
<p>Set by the protocol driver to indicate that the inner IP header in the encapsulated packet contains IPv6 addresses.</p>
</dd>

### -field <b>TcpOptionsPresent</b>

<dd>
<p>Set by the protocol driver when the inner TCP header contains TCP options. This allows a miniport driver to optimize the case when there are no options to assume the TCP header length to access the payload.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>
</dd>

### -field <b>Value</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>The members of <b>NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</b> are meaningful if and only if <b>TcpIpChecksumNetBufferListInfo</b> or <b>TcpLargeSendNetBufferListInfo</b> is specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566569">NDIS_NET_BUFFER_LIST_INFO</a> structure.</p>

<p>If the <b>IsEncapsulatedPacket</b> member is <b>TRUE</b> and the <b>TcpIpChecksumNetBufferListInfo</b> out-of-band (OOB) information is valid, this indicates that NVGRE support is required and the NIC must compute the checksum for the tunnel (outer) IP header, the transport (inner) IP header, and the TCP or UDP header if one of them is present. An NVGRE packet will only be offloaded if the packet conforms to miniport-advertised capabilities. For example, a packet containing a UDP header will not be offloaded if the miniport did not advertise UDP Tx checksum offload support in its base capabilities. For more information, see <a href="NULL">Offloading Checksum Tasks</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/jj991956">NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566569">NDIS_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="NULL">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>
</dt>
<dt>
<a href="NULL">Offloading Checksum Tasks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
