---
UID: NS.ntddndis._NDIS_OFFLOAD
title: NDIS_OFFLOAD
author: windows-driver-content
description: The NDIS_OFFLOAD structure specifies several computational tasks that can be offloaded to the network adapter.
old-location: netvista\ndis_offload.htm
old-project: netvista
ms.assetid: 9d1447f1-aae8-4c27-a27b-e521c0c8ca97
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_OFFLOAD, NDIS_OFFLOAD, *PNDIS_OFFLOAD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista,Supported in NDIS 6.0 and later.
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_OFFLOAD
req.alt-loc: Ntddndis.h
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

# NDIS_OFFLOAD structure



## -description
<p>The NDIS_OFFLOAD structure specifies several computational <a href="netvista.task_offload">tasks that can be offloaded to the network adapter</a>.</p>


## -syntax

````
typedef struct _NDIS_OFFLOAD {
  NDIS_OBJECT_HEADER                    Header;
  NDIS_TCP_IP_CHECKSUM_OFFLOAD          Checksum;
  NDIS_TCP_LARGE_SEND_OFFLOAD_V1        LsoV1;
  NDIS_IPSEC_OFFLOAD_V1                 IPsecV1;
  NDIS_TCP_LARGE_SEND_OFFLOAD_V2        LsoV2;
  ULONG                                 Flags;
#if (NDIS_SUPPORT_NDIS61)
  NDIS_IPSEC_OFFLOAD_V2                 IPsecV2;
#endif 
#if (NDIS_SUPPORT_NDIS630)
  NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD    Rsc;
  NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD EncapsulatedPacketTaskOffloadGre;
#endif 
} NDIS_OFFLOAD, *PNDIS_OFFLOAD;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_OFFLOAD</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_OFFLOAD.
     </p>
<p>Set the <b>Revision</b> and <b>Size</b> members of the <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure as follows:<ul>
<li>For NDIS 6.30 and later drivers:<ul>
<li>Set <b>Revision</b> to NDIS_OFFLOAD_REVISION_3 (NDIS 6.30).</li>
<li>Set <b>Size</b> to NDIS_SIZEOF_NDIS_OFFLOAD_REVISION_3.</li>
</ul>
</li>
<li>For NDIS 6.1 and 6.20 drivers:<ul>
<li>Set <b>Revision</b> to NDIS_OFFLOAD_REVISION_2 (NDIS 6.1).</li>
<li>Set <b>Size</b> to NDIS_SIZEOF_NDIS_OFFLOAD_REVISION_2.</li>
</ul>
</li>
<li>For NDIS 6.0 drivers:<ul>
<li>Set <b>Revision</b> to NDIS_OFFLOAD_REVISION_1 (NDIS 6.0).</li>
<li>Set <b>Size</b> to NDIS_SIZEOF_NDIS_OFFLOAD_REVISION_1.</li>
</ul>
</li>
</ul>
</p>
</dd>

### -field <b>Checksum</b>

<dd>
<p>Checksum offload information in an 
     <a href="..\ntddndis\ns-ntddndis--ndis-tcp-ip-checksum-offload.md">
     NDIS_TCP_IP_CHECKSUM_OFFLOAD</a> structure.</p>
</dd>

### -field <b>LsoV1</b>

<dd>
<p>Large send offload version 1 (LSOV1) information in an 
     <a href="..\ntddndis\ns-ntddndis--ndis-tcp-large-send-offload-v1.md">
     NDIS_TCP_LARGE_SEND_OFFLOAD_V1</a> structure.</p>
</dd>

### -field <b>IPsecV1</b>

<dd>
<p>Internet protocol security (IPsec) offload information in an 
     <a href="..\ntddndis\ns-ntddndis--ndis-ipsec-offload-v1.md">
     NDIS_IPSEC_OFFLOAD_V1</a> structure.</p>
</dd>

### -field <b>LsoV2</b>

<dd>
<p>Large send offload version 2 (LSOV2) offload information in an 
     <a href="..\ntddndis\ns-ntddndis--ndis-tcp-large-send-offload-v2.md">
     NDIS_TCP_LARGE_SEND_OFFLOAD_V2</a> structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR  of flags that specify properties that the network adapter supports. The following flags are defined.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="IPSEC_OFFLOAD_V2_AND_TCP_CHECKSUM_COEXISTENCE"></a><a id="ipsec_offload_v2_and_tcp_checksum_coexistence"></a><dl>

### -field <b>IPSEC_OFFLOAD_V2_AND_TCP_CHECKSUM_COEXISTENCE</b>


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>The network adapter supports IPsecV2 and TCP checksums.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="IPSEC_OFFLOAD_V2_AND_UDP_CHECKSUM_COEXISTENCE"></a><a id="ipsec_offload_v2_and_udp_checksum_coexistence"></a><dl>

### -field <b>IPSEC_OFFLOAD_V2_AND_UDP_CHECKSUM_COEXISTENCE</b>


### -field 0x00000004

</dl>
</td>
<td width="60%">
<p>The network adapter supports IPsecV2 and UDP checksums.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>IPsecV2</b>

<dd>
<p>Internet protocol security (IPsec) offload version 2 information in an 
      <a href="..\ntddndis\ns-ntddndis--ndis-ipsec-offload-v2.md">NDIS_IPSEC_OFFLOAD_V2</a> structure.</p>
</dd>

### -field <b>Rsc</b>

<dd>
<p>
<a href="NULL">Receive Segment Coalescing (RSC)</a> offload information in    an <a href="..\ntddndis\ns-ntddndis--ndis-tcp-recv-seg-coalesce-offload.md">NDIS_TCP_RECV_SEG_COALESCE_OFFLOAD</a> structure.</p>
</dd>

### -field <b>EncapsulatedPacketTaskOffloadGre</b>

<dd>
<p>
<a href="NULL">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a> information in an <a href="..\ntddndis\ns-ntddndis--ndis-encapsulated-packet-task-offload.md">NDIS_ENCAPSULATED_PACKET_TASK_OFFLOAD</a> structure. This member should only be set by miniport drivers that support task offloads for NVGRE-formatted packets.<div class="alert"><b>Note</b>  This member is available only in NDIS 6.30 and later. </div>
<div> </div>
</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_OFFLOAD</b> structure is used in the following places:<ul>
<li>The <b>DefaultOffloadConfiguration</b> member of the <a href="..\ndis\ns-ndis--ndis-miniport-adapter-offload-attributes.md">NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES</a> structure</li>
<li>The <b>DefaultOffloadConfiguration</b> member of the <a href="..\ndis\ns-ndis--ndis-bind-parameters.md">NDIS_BIND_PARAMETERS</a> structure</li>
<li>The <b>DefaultOffloadConfiguration</b> member of the <a href="..\ndis\ns-ndis--ndis-filter-attach-parameters.md">NDIS_FILTER_ATTACH_PARAMETERS</a> structure</li>
<li>The <b>InformationBuffer</b> member of the <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> structure (which is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569805">OID_TCP_OFFLOAD_CURRENT_CONFIG</a> OID request)</li>
<li>The <b>StatusBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567424">NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</a> status indication</li>
</ul>
</p>

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
<a href="..\ndis\ns-ndis--ndis-bind-parameters.md">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-filter-attach-parameters.md">NDIS_FILTER_ATTACH_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-ipsec-offload-v1.md">NDIS_IPSEC_OFFLOAD_V1</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-ipsec-offload-v2.md">NDIS_IPSEC_OFFLOAD_V2</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-offload-attributes.md">
   NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-status-indication.md">NDIS_STATUS_INDICATION</a>
</dt>
<dt>
<a href="netvista.ndis_status_task_offload_current_config">
   NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-tcp-ip-checksum-offload.md">NDIS_TCP_IP_CHECKSUM_OFFLOAD</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-tcp-large-send-offload-v1.md">
   NDIS_TCP_LARGE_SEND_OFFLOAD_V1</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-tcp-large-send-offload-v2.md">
   NDIS_TCP_LARGE_SEND_OFFLOAD_V2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569762">OID_OFFLOAD_ENCAPSULATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569805">OID_TCP_OFFLOAD_CURRENT_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569806">OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES</a>
</dt>
<dt>
<a href="NULL">Determining the RSC Capabilities of a Network Adapter</a>
</dt>
<dt>
<a href="NULL">Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload</a>
</dt>
<dt>
<a href="NULL">TCP/IP Task Offload</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OFFLOAD structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
