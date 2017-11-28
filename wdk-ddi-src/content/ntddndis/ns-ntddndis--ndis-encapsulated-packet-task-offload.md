---
UID: NS.ntddndis._NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD
title: NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD
author: windows-driver-content
description: The NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD structure contains the offload support state for Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload (NVGRE-TO).
old-location: netvista\ndis_encapsulated_packet_task_offload.htm
old-project: netvista
ms.assetid: EA13DADC-ED00-435D-BEA7-B6E52A86031A
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD, NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD, *PNDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD
req.alt-loc: ntddndis.h
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

# NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD structure



## -description
<p>The <b>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD</b> structure contains the offload support state for <a href="NULL">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a> (NVGRE-TO). This structure is used in the <b>EncapsulatedPacketTaskOffloadGre</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a> structure.</p>


## -syntax

````
typedef struct _NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD {
  ULONG TransmitChecksumOffloadSupported  :4;
  ULONG ReceiveChecksumOffloadSupported  :4;
  ULONG LsoV2Supported  :4;
  ULONG RssSupported  :4;
  ULONG VmqSupported  :4;
  ULONG MaxHeaderSizeSupported;
} NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD, *PNDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD;
````


## -struct-fields
<dl>

### -field <b>TransmitChecksumOffloadSupported</b>

<dd>
<p>Task offload settings for transmit checksum.</p>
</dd>

### -field <b>ReceiveChecksumOffloadSupported</b>

<dd>
<p>Task offload settings for receive checksum.</p>
</dd>

### -field <b>LsoV2Supported</b>

<dd>
<p>Task offload settings for large send offload version 2 (LSOv2).</p>
</dd>

### -field <b>RssSupported</b>

<dd>
<p>Task offload settings for receive side scaling (RSS).</p>
</dd>

### -field <b>VmqSupported</b>

<dd>
<p>Task offload settings for virtual machine queue (VMQ).</p>
</dd>

### -field <b>MaxHeaderSizeSupported</b>

<dd>
<p>This member should be set to the maximum header size from the beginning of the packet to the beginning of the inner TCP or UDP payload (the last byte of TCP or UDP inner header) that the NIC must support for all of these task offloads. The protocol driver is expected to not offload processing of a packet whose combined encapsulation headers exceed this size. </p>
<div class="alert"><b>Note</b>  256 bytes is a good default value that should cover all possible cases.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>In the initial capability advertisement and in <a href="https://msdn.microsoft.com/library/windows/hardware/ff567424">NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567425">NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES</a> status indications, the <b>TransmitChecksumOffloadSupported</b>, <b>ReceiveChecksumOffloadSupported</b>, <b>LsoV2Supported</b>, <b>RssSupported</b>, and <b>VmqSupported</b> members can be set to a bitwise OR of the following flags:</p>

<p>
<p></p>
<table>
<tr>
<th>Term</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_NOT_SUPPORTED"></a><a id="ndis_encapsulated_packet_task_offload_not_supported"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_NOT_SUPPORTED</p>
</td>
<td width="60%">
<p>Specifies that the miniport adapter does not support the corresponding task offload feature that the member specifies.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV4"></a><a id="ndis_encapsulated_packet_task_offload_inner_ipv4"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV4</p>
</td>
<td width="60%">
<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the inner IP header of an encapsulated packet is IPv4.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV4"></a><a id="ndis_encapsulated_packet_task_offload_outer_ipv4"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV4</p>
</td>
<td width="60%">
<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the outer IP header of an encapsulated packet is IPv4.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV6"></a><a id="ndis_encapsulated_packet_task_offload_inner_ipv6"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV6</p>
</td>
<td width="60%">
<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the inner IP header of an encapsulated packet is IPv6.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV6"></a><a id="ndis_encapsulated_packet_task_offload_outer_ipv6"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV6</p>
</td>
<td width="60%">
<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the outer IP header of an encapsulated packet is IPv6.</p>
</td>
</tr>
</table>
<p> </p>
</p>

<p></p>

<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_NOT_SUPPORTED"></a><a id="ndis_encapsulated_packet_task_offload_not_supported"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_NOT_SUPPORTED</p>

<p>Specifies that the miniport adapter does not support the corresponding task offload feature that the member specifies.</p>

<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV4"></a><a id="ndis_encapsulated_packet_task_offload_inner_ipv4"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV4</p>

<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the inner IP header of an encapsulated packet is IPv4.</p>

<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV4"></a><a id="ndis_encapsulated_packet_task_offload_outer_ipv4"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV4</p>

<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the outer IP header of an encapsulated packet is IPv4.</p>

<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV6"></a><a id="ndis_encapsulated_packet_task_offload_inner_ipv6"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV6</p>

<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the inner IP header of an encapsulated packet is IPv6.</p>

<p><a id="NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV6"></a><a id="ndis_encapsulated_packet_task_offload_outer_ipv6"></a>NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV6</p>

<p>Specifies that the miniport adapter supports the corresponding task offload feature that the member specifies where the outer IP header of an encapsulated packet is IPv6.</p>

<p> </p>

<p>As an example, if a miniport adapter and driver only support an  IPv6 header as outer IP header but not as inner IP header, it will set <b>TransmitChecksumOffloadSupported</b>, <b>ReceiveChecksumOffloadSupported</b>, <b>LsoV2Supported</b>, <b>RssSupported</b>, and <b>VmqSupported</b> to the value of the bitwise OR of NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_INNER_IPV4, NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV4 and NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD_OUTER_IPV6.</p>

<p>Regarding IP options and TCP options, the following assumption was made for encapsulated packets:<ul>
<li>If the NIC specifies <b>IpOptions</b> and <b>TcpOptions</b> support in normal checksum offload and LSOv2 advertisement, it must support the option processing for encapsulated packets if <a href="NULL">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a> is supported. This means it will support both inner and outer IP options and TCP options inside the encapsulated packets. There is no separate capability advertisement for these specific to only NVGRE Task Offload.</li>
</ul>
</p>

<p>It is possible for a protocol driver to offload "mixed mode" packets which means packets in which the inner and outer IP header versions are different. For example, a packet could have outer IP header as IPv6 and the inner IP header as IPv4.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a>
</dt>
<dt>
<a href="NULL">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
