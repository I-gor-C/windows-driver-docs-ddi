---
UID: NS.ntddndis._NDIS_TCP_LARGE_SEND_OFFLOAD_V2
title: NDIS_TCP_LARGE_SEND_OFFLOAD_V2
author: windows-driver-content
description: The NDIS_TCP_LARGE_SEND_OFFLOAD_V2 structure provides large send offload version 2 (LSOV2) information in the NDIS_OFFLOAD structure.
old-location: netvista\ndis_tcp_large_send_offload_v2.htm
old-project: netvista
ms.assetid: e53e5771-a3ca-4867-a0ac-65adb66e574c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_TCP_LARGE_SEND_OFFLOAD_V2, NDIS_TCP_LARGE_SEND_OFFLOAD_V2, *PNDIS_TCP_LARGE_SEND_OFFLOAD_V2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_TCP_LARGE_SEND_OFFLOAD_V2
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

# NDIS_TCP_LARGE_SEND_OFFLOAD_V2 structure



## -description
<p>The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_V2</b> structure provides large send offload version 2 (LSOV2)
  information in the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a> structure.</p>


## -syntax

````
typedef struct _NDIS_TCP_LARGE_SEND_OFFLOAD_V2 {
  struct {
    ULONG Encapsulation;
    ULONG MaxOffLoadSize;
    ULONG MinSegmentCount;
  } IPv4;
  struct {
    ULONG Encapsulation;
    ULONG MaxOffLoadSize;
    ULONG MinSegmentCount;
    ULONG IpExtensionHeadersSupported  :2;
    ULONG TcpOptionsSupported  :2;
  } IPv6;
} NDIS_TCP_LARGE_SEND_OFFLOAD_V2, *PNDIS_TCP_LARGE_SEND_OFFLOAD_V2;
````


## -struct-fields
<dl>

### -field <b>IPv4</b>

<dd>
<p>A structure within <b>NDIS_TCP_LARGE_SEND_OFFLOAD_V2</b> that specifies IPv4 information and that
     contains the following members:
     </p>
<dl>

### -field <b>Encapsulation</b>

<dd>
<p>Encapsulation settings for IPv4. For more information about this member, see the following
       Remarks section.</p>
</dd>

### -field <b>MaxOffLoadSize</b>

<dd>
<p>The maximum bytes of user data that the transport can pass to the miniport driver in a single
       packet. The transport will not pass a packet to the miniport driver that contains more user data bytes
       than 
       <b>MaxOffLoadSize</b> specifies. If such a packet must be transmitted, the transport itself segments
       the packet into smaller packets.</p>
</dd>

### -field <b>MinSegmentCount</b>

<dd>
<p>The minimum number of segments that a large TCP packet must be divisible by before the transport
       can offload it to the hardware for segmentation. The transport will not offload a large packet to the
       miniport driver for segmentation unless the miniport driver can create at least as many segments as 
       <b>MinSegmentCount</b> specifies from the packet. If a large TCP packet does not meet the
       minimum-segment requirement, the TCP/IP transport itself segments the packet into smaller
       packets.</p>
</dd>
</dl>
</dd>

### -field <b>IPv6</b>

<dd>
<p>A structure within <b>NDIS_TCP_LARGE_SEND_OFFLOAD_V2</b> that specifies IPv6 information and that
     contains the following members:
     </p>
<dl>

### -field <b>Encapsulation</b>

<dd>
<p>Encapsulation settings for IPv6. For more information about this member, see the following
       Remarks section.</p>
</dd>

### -field <b>MaxOffLoadSize</b>

<dd>
<p>The maximum bytes of user data that the transport can pass to the miniport driver in a single
       packet. The transport will not pass a packet to the miniport driver that contains more user data bytes
       than 
       <b>MaxOffLoadSize</b> specifies. If such a packet must be transmitted, the transport itself segments
       the packet into smaller packets.</p>
</dd>

### -field <b>MinSegmentCount</b>

<dd>
<p>The minimum number of segments that a large TCP packet must be divisible by before the transport
       can offload it to a NIC for segmentation. The transport will not offload a large packet to the
       miniport driver for segmentation unless the miniport driver can create at least as many segments as 
       <b>MinSegmentCount</b> specifies from the packet. If a large TCP packet does not meet the
       minimum-segment requirement, the TCP/IP transport itself segments the packet into smaller
       packets.</p>
</dd>

### -field <b>IpExtensionHeadersSupported</b>

<dd>
<p>A ULONG value that a miniport driver sets to indicate that the miniport adapter can segment a
       large TCP packet whose IP header contains IPv6 extension headers.</p>
</dd>

### -field <b>TcpOptionsSupported</b>

<dd>
<p>A ULONG value that a miniport driver sets to indicate that the miniport driver can segment a
       large TCP packet whose TCP header contains TCP options or to indicate that this capability is enabled
       or disabled.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_V2</b> structure is used in the 
    <b>LsoV2</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a> structure. The
    <b>NDIS_TCP_LARGE_SEND_OFFLOAD_V2</b> structure specifies current or supported services that a miniport adapter
    provides for segmenting large TCP packets into smaller packets. NDIS also provides large send offload
    version 1 (LSOV1), which is an earlier version of LSOV2. For more information about LSOV1, see 
    <a href="..\ntddndis\ns-ntddndis--ndis-tcp-large-send-offload-v1.md">
    NDIS_TCP_LARGE_SEND_OFFLOAD_V1</a>.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a> is used in the 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-offload-attributes.md">
    NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES</a> structure, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a> structure, 
    <a href="..\ndis\ns-ndis--ndis-filter-attach-parameters.md">
    NDIS_FILTER_ATTACH_PARAMETERS</a> structure, 
    <a href="netvista.oid_tcp_offload_current_config">
    OID_TCP_OFFLOAD_CURRENT_CONFIG</a> OID, and the 
    <a href="netvista.ndis_status_task_offload_current_config">
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</a> status indication.</p>

<p>For 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569805">OID_TCP_OFFLOAD_CURRENT_CONFIG</a>,
    the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a> structure specifies the task offload capabilities that a miniport adapter supports. If
    the current offloads capabilities change, a miniport driver reports the new capabilities in an 
    <a href="netvista.ndis_status_task_offload_current_config">
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</a> status indication.</p>

<p>The 
    <b>Encapsulation</b> members of <b>NDIS_TCP_LARGE_SEND_OFFLOAD_V2</b> define the LSOV2 encapsulation settings for
    the miniport adapter.</p>

<p>In response to an 
    <a href="netvista.oid_tcp_offload_current_config">
    OID_TCP_OFFLOAD_CURRENT_CONFIG</a> query request, NDIS provides a bitwise OR of the encapsulation
    flags, which indicate the supported encapsulation settings, in each of the 
    <b>Encapsulation</b> members. Miniport drivers must provide Ethernet encapsulation
    (NDIS_ENCAPSULATION_IEEE_802_3). The other types of encapsulation are optional.</p>

<p>For an 
    <a href="netvista.ndis_status_task_offload_current_config">
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</a> status indication, the miniport driver provides a bitwise
    OR of the encapsulation flags, which indicate the current capabilities, in each of the 
    <b>Encapsulation</b> members.</p>

<p>The following flags are defined for the 
    <b>Encapsulation</b> members:</p>

<p></p><dl>
<dt><a id="NDIS_ENCAPSULATION_NOT_SUPPORTED"></a><a id="ndis_encapsulation_not_supported"></a>NDIS_ENCAPSULATION_NOT_SUPPORTED</dt>
<dd>
<p>Specifies that no encapsulation offload is supported.</p>
</dd>
<dt><a id="NDIS_ENCAPSULATION_NULL"></a><a id="ndis_encapsulation_null"></a>NDIS_ENCAPSULATION_NULL</dt>
<dd>
<p>Specifies NULL encapsulation.</p>
</dd>
<dt><a id="NDIS_ENCAPSULATION_IEEE_802_3"></a><a id="ndis_encapsulation_ieee_802_3"></a>NDIS_ENCAPSULATION_IEEE_802_3</dt>
<dd>
<p>Specifies IEEE 802.3 encapsulation.</p>
</dd>
<dt><a id="NDIS_ENCAPSULATION_IEEE_802_3_P_AND_Q"></a><a id="ndis_encapsulation_ieee_802_3_p_and_q"></a>NDIS_ENCAPSULATION_IEEE_802_3_P_AND_Q</dt>
<dd>
<p>Specifies IEEE 802.3p and IEEE 802.3q encapsulation.</p>
</dd>
<dt><a id="NDIS_ENCAPSULATION_IEEE_802_3_P_AND_Q_IN_OOB"></a><a id="ndis_encapsulation_ieee_802_3_p_and_q_in_oob"></a>NDIS_ENCAPSULATION_IEEE_802_3_P_AND_Q_IN_OOB</dt>
<dd>
<p>Specifies that IEEE 802.3p and IEEE 802.3q encapsulation settings are specified in the 
      <b>NetBufferListInfo</b> member of each 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>
</dd>
<dt><a id="NDIS_ENCAPSULATION_IEEE_LLC_SNAP_ROUTED"></a><a id="ndis_encapsulation_ieee_llc_snap_routed"></a>NDIS_ENCAPSULATION_IEEE_LLC_SNAP_ROUTED</dt>
<dd>
<p>Specifies logical link control (LLC) encapsulation for routed protocols, as described in RFC
      1483. This flag is also used to indicate Ethernet LLC/SNAP encapsulation.</p>
</dd>
</dl><p>Specifies that no encapsulation offload is supported.</p>

<p>Specifies NULL encapsulation.</p>

<p>Specifies IEEE 802.3 encapsulation.</p>

<p>Specifies IEEE 802.3p and IEEE 802.3q encapsulation.</p>

<p>Specifies that IEEE 802.3p and IEEE 802.3q encapsulation settings are specified in the 
      <b>NetBufferListInfo</b> member of each 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>

<p>Specifies logical link control (LLC) encapsulation for routed protocols, as described in RFC
      1483. This flag is also used to indicate Ethernet LLC/SNAP encapsulation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565481">NDIS_FILTER_ATTACH_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-offload-attributes.md">
   NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566599">NDIS_OFFLOAD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="netvista.ndis_status_task_offload_current_config">
   NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-tcp-large-send-offload-v1.md">
   NDIS_TCP_LARGE_SEND_OFFLOAD_V1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569805">OID_TCP_OFFLOAD_CURRENT_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_LARGE_SEND_OFFLOAD_V2 structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
