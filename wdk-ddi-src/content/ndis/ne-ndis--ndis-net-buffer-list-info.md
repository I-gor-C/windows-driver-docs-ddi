---
UID: NE.ndis._NDIS_NET_BUFFER_LIST_INFO
title: NDIS_NET_BUFFER_LIST_INFO
author: windows-driver-content
description: The NDIS_NET_BUFFER_LIST_INFO enumeration identifies information that is common to all NET_BUFFER structures in a NET_BUFFER_LIST structure.
old-location: netvista\ndis_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 79327b2b-e97b-42dc-8d15-9d774c424cae
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NET_BUFFER_LIST_INFO
req.alt-loc: ndis.h
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

# NDIS_NET_BUFFER_LIST_INFO enumeration



## -description
<p>The <b>NDIS_NET_BUFFER_LIST_INFO</b> enumeration identifies information that is common to all 
  <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures in a 
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
typedef enum _NDIS_NET_BUFFER_LIST_INFO { 
  TcpIpChecksumNetBufferListInfo,
  TcpOffloadBytesTransferred                    = TcpIpChecksumNetBufferListInfo,
  IPsecOffloadV1NetBufferListInfo,
#if (NDIS_SUPPORT_NDIS61)
  IPsecOffloadV2NetBufferListInfo               = IPsecOffloadV1NetBufferListInfo,
#endif 
  TcpLargeSendNetBufferListInfo,
  TcpReceiveNoPush                              = TcpLargeSendNetBufferListInfo,
  ClassificationHandleNetBufferListInfo,
  Ieee8021QNetBufferListInfo,
  NetBufferListCancelId,
  MediaSpecificInformation,
  NetBufferListFrameType,
  NetBufferListProtocolId                       = NetBufferListFrameType,
  NetBufferListHashValue,
  NetBufferListHashInfo,
  WfpNetBufferListInfo,
#if (NDIS_SUPPORT_NDIS61)
  IPsecOffloadV2TunnelNetBufferListInfo,
  IPsecOffloadV2HeaderNetBufferListInfo,
#endif 
#if (NDIS_SUPPORT_NDIS620)
  NetBufferListCorrelationId,
  NetBufferListFilteringInfo,
  MediaSpecificInformationEx,
  NblOriginalInterfaceIfIndex,
  NblReAuthWfpFlowContext                       = NblOriginalInterfaceIfIndex,
  TcpReceiveBytesTransferred,
#if (NDIS_SUPPORT_NDIS630)
#if (_AMD64_) || (_ARM64_)
  SwitchForwardingReserved,
  SwitchForwardingDetail,
  VirtualSubnetInfo,
#endif 
  IMReserved,
  TcpRecvSegCoalesceInfo,
  RscTcpTimestampDelta,
  TcpSendOffloadsSupplementalNetBufferListInfo  = RscTcpTimestampDelta,
#endif 
#endif 
#if NDIS_WRAPPER == 1
  NetBufferListInfoReserved1,
  NetBufferListInfoReserved2,
#endif 
  MaxNetBufferListInfo
} NDIS_NET_BUFFER_LIST_INFO, *PNDIS_NET_BUFFER_LIST_INFO;
````


## -enum-fields
<dl>

### -field <a id="TcpIpChecksumNetBufferListInfo"></a><a id="tcpipchecksumnetbufferlistinfo"></a><a id="TCPIPCHECKSUMNETBUFFERLISTINFO"></a><b>TcpIpChecksumNetBufferListInfo</b>

<dd>
<p>Identifies checksum information that is used in offloading checksum tasks from the TCP/IP protocol
     to a miniport driver. When 
     <b>TcpIpChecksumNetBufferListInfo</b> is specified, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro returns an 
     <a href="..\ndis\ns-ndis--ndis-tcp-ip-checksum-net-buffer-list-info.md">
     NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</a> structure. This structure contains a union that allows
     the checksum information to be accessed as a single <b>PVOID</b> value or as bit fields.</p>
</dd>

### -field <a id="TcpOffloadBytesTransferred"></a><a id="tcpoffloadbytestransferred"></a><a id="TCPOFFLOADBYTESTRANSFERRED"></a><b>TcpOffloadBytesTransferred</b>

<dd>
<p>Identifies a <b>ULONG</b> value that is the number of data bytes that were transferred in a TCP chimney
     offload send, receive, or disconnect operation.</p>
</dd>

### -field <a id="IPsecOffloadV1NetBufferListInfo"></a><a id="ipsecoffloadv1netbufferlistinfo"></a><a id="IPSECOFFLOADV1NETBUFFERLISTINFO"></a><b>IPsecOffloadV1NetBufferListInfo</b>

<dd>
<p>Identifies Internet Protocol security (IPsec) information that is used in offloading IPsec tasks
     from the TCP/IP protocol to a miniport driver. When 
     <b>IPsecOffloadV1NetBufferListInfo</b> is specified, <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> returns an 
     <a href="..\ndis\ns-ndis--ndis-ipsec-offload-v1-net-buffer-list-info.md">
     NDIS_IPSEC_OFFLOAD_V1_NET_BUFFER_LIST_INFO</a> structure.</p>
</dd>

### -field <a id="IPsecOffloadV2NetBufferListInfo"></a><a id="ipsecoffloadv2netbufferlistinfo"></a><a id="IPSECOFFLOADV2NETBUFFERLISTINFO"></a><b>IPsecOffloadV2NetBufferListInfo</b>

<dd>
<p>Specifies Internet protocol security offload version 2 (IPsecV2) information that is used in
      offloading IPsec tasks from the TCP/IP protocol to a miniport driver. When you specify 
      <b>IPsecOffloadV2NetBufferListInfo</b>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> returns an 
      <a href="..\ndis\ns-ndis--ndis-ipsec-offload-v2-net-buffer-list-info.md">
      NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO</a> structure.</p>
</dd>

### -field <a id="TcpLargeSendNetBufferListInfo"></a><a id="tcplargesendnetbufferlistinfo"></a><a id="TCPLARGESENDNETBUFFERLISTINFO"></a><b>TcpLargeSendNetBufferListInfo</b>

<dd>
<p>Identifies information that is used in offloading the segmentation of a large TCP packet from the
     TCP/IP protocol to a miniport adapter for large send offload version 1 (LSOV1) and large send offload
     version 2 (LSOV2). When 
     <b>TcpLargeSendNetBufferListInfo</b> is specified, <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> returns an 
     <a href="..\ndis\ns-ndis--ndis-tcp-large-send-offload-net-buffer-list-info.md">
     NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</a> structure. This structure contains a union that
     enables the information to be accessed as a single PVOID value or as bit fields.
     </p>
<p>Before passing a large TCP packet to a miniport driver for segmentation, the TCP/IP protocol writes
     the values in the 
     <b>LsoV1Transmit</b> member of the <a href="..\ndis\ns-ndis--ndis-tcp-large-send-offload-net-buffer-list-info.md">
     NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</a> structure for LSOV1
     or the 
     <b>LsoV2Transmit</b> member for LSOV2. Before completing the send of a large TCP packet that it has
     segmented into smaller packets, a miniport driver writes the values in the 
     <b>LsoV1TransmitComplete</b> member of the <b>
     NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure for
     LSOV1 or the 
     <b>LsoV2TransmitComplete</b> member for LSOV2. For LSOV1, the value that the miniport driver writes
     includes the total number of TCP payload bytes that the miniport driver sent in the packets that it
     segmented from the large TCP packet.</p>
</dd>

### -field <a id="TcpReceiveNoPush"></a><a id="tcpreceivenopush"></a><a id="TCPRECEIVENOPUSH"></a><b>TcpReceiveNoPush</b>

<dd>
<p>Identifies a <b>Boolean</b> value that represents the push mode of a TCP chimney offload receive request.
     If <b>TRUE</b>, the receive request is in non-push mode. Otherwise, the receive request is in push mode.</p>
</dd>

### -field <a id="ClassificationHandleNetBufferListInfo"></a><a id="classificationhandlenetbufferlistinfo"></a><a id="CLASSIFICATIONHANDLENETBUFFERLISTINFO"></a><b>ClassificationHandleNetBufferListInfo</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <a id="Ieee8021QNetBufferListInfo"></a><a id="ieee8021qnetbufferlistinfo"></a><a id="IEEE8021QNETBUFFERLISTINFO"></a><b>Ieee8021QNetBufferListInfo</b>

<dd>
<p>Identifies 802.1Q information about a packet. When 
     <b>Ieee8021QNetBufferListInfo</b> is specified, 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> returns the 
     <b>Value</b> member of an 
     <a href="..\ndis\ns-ndis--ndis-net-buffer-list-8021q-info.md">
     NDIS_NET_BUFFER_LIST_8021Q_INFO</a> structure. This structure can specify 802.1p priority and VLAN
     identifier information. 802.1p priority information is used to establish packet priority in shared-media
     802 networks. Miniport drivers that support the 802.1Q tag in hardware must use the
     <b>
     NDIS_NET_BUFFER_LIST_8021Q_INFO</b> structure for transmit and receive operations.</p>
</dd>

### -field <a id="NetBufferListCancelId"></a><a id="netbufferlistcancelid"></a><a id="NETBUFFERLISTCANCELID"></a><b>NetBufferListCancelId</b>

<dd>
<p>Identifies a <b>ULONG_PTR</b> value that is a cancellation identifier for the 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure. To cancel the
     pending transmission of a marked <b>NET_BUFFER_LIST</b> structure, a protocol driver passes the packet's
     cancellation identifier to 
     <a href="..\ndis\nf-ndis-ndiscancelsendnetbufferlists.md">
     NdisCancelSendNetBufferLists</a>. Drivers must call 
     <a href="..\ndis\nf-ndis-ndisgeneratepartialcancelid.md">
     NdisGeneratePartialCancelId</a> to obtain a value that the driver must use as the high-order byte of a
     cancellation identifier.</p>
</dd>

### -field <a id="MediaSpecificInformation"></a><a id="mediaspecificinformation"></a><a id="MEDIASPECIFICINFORMATION"></a><b>MediaSpecificInformation</b>

<dd>
<p>Identifies a PVOID value that is the address of a driver-allocated buffer. This buffer contains
     any media-specific out-of-band data that accompanies the 
     <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures that are associated with
     the <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure. If a protocol driver allocated the out-of-band data, it configured the
     data for a send operation. If a miniport driver allocated the data, it configured the data for a receive
     indication.</p>
</dd>

### -field <a id="NetBufferListFrameType"></a><a id="netbufferlistframetype"></a><a id="NETBUFFERLISTFRAMETYPE"></a><b>NetBufferListFrameType</b>

<dd>
<p>Identifies a <b>USHORT</b> value that is the frame type of the received Ethernet packets.</p>
</dd>

### -field <a id="NetBufferListProtocolId"></a><a id="netbufferlistprotocolid"></a><a id="NETBUFFERLISTPROTOCOLID"></a><b>NetBufferListProtocolId</b>

<dd>
<p>Identifies a <b>UCHAR</b> value that is a protocol identifier as one of the following values: 
     </p>
<p></p>
<dl>

### -field <a id="NDIS_PROTOCOL_ID_DEFAULT"></a><a id="ndis_protocol_id_default"></a>NDIS_PROTOCOL_ID_DEFAULT

<dd>
<p>A default protocol driver identifier.</p>
</dd>

### -field <a id="NDIS_PROTOCOL_ID_TCP_IP"></a><a id="ndis_protocol_id_tcp_ip"></a>NDIS_PROTOCOL_ID_TCP_IP

<dd>
<p>The TCP/IP protocol.</p>
</dd>

### -field <a id="NDIS_PROTOCOL_ID_IPX"></a><a id="ndis_protocol_id_ipx"></a>NDIS_PROTOCOL_ID_IPX

<dd>
<p>The IPX protocol.</p>
</dd>

### -field <a id="NDIS_PROTOCOL_ID_NBF"></a><a id="ndis_protocol_id_nbf"></a>NDIS_PROTOCOL_ID_NBF

<dd>
<p>The NetBEUI protocol.</p>
</dd>
</dl>
</dd>

### -field <a id="NetBufferListHashValue"></a><a id="netbufferlisthashvalue"></a><a id="NETBUFFERLISTHASHVALUE"></a><b>NetBufferListHashValue</b>

<dd>
<p>On the receive path, 
     <b>NetBufferListHashValue</b> identifies a <b>ULONG</b> value that is the RSS hash value that a NIC calculated,
     if any. 
     </p>
<p>On the transmit path, 
     <b>NetBufferListHashValue</b> identifies a <b>ULONG</b> value that is the RSS hash value that TCP/IP calculated,
     if any. In this case, all <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures in a <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure that TCP/IP submitted
     belong to the same UDP or TCP connection. Therefore, this hash value applies to all <b>NET_BUFFER</b>
     structures that are in the <b>NET_BUFFER_LIST</b> structure.</p>
<p>For more information, see 
     <a href="netvista.indicating_rss_receive_data">Indicating RSS Receive
     Data</a>.</p>
</dd>

### -field <a id="NetBufferListHashInfo"></a><a id="netbufferlisthashinfo"></a><a id="NETBUFFERLISTHASHINFO"></a><b>NetBufferListHashInfo</b>

<dd>
<p>Identifies a <b>ULONG</b> value that is the RSS hash information, which includes the hash function and
     hash type. For more information, see 
     <a href="netvista.indicating_rss_receive_data">Indicating RSS Receive
     Data</a>.</p>
</dd>

### -field <a id="WfpNetBufferListInfo"></a><a id="wfpnetbufferlistinfo"></a><a id="WFPNETBUFFERLISTINFO"></a><b>WfpNetBufferListInfo</b>

<dd>
<p>Reserved for use by the Windows Filtering Platform (WFP). No drivers, including WFP callout
     drivers, can store information by using this value.</p>
</dd>

### -field <a id="IPsecOffloadV2TunnelNetBufferListInfo"></a><a id="ipsecoffloadv2tunnelnetbufferlistinfo"></a><a id="IPSECOFFLOADV2TUNNELNETBUFFERLISTINFO"></a><b>IPsecOffloadV2TunnelNetBufferListInfo</b>

<dd>
<p>Specifies IPsecV2 tunnel information that is used in offloading IPsec tasks from the TCP/IP protocol
      to a miniport driver. When you specify 
      <b>IPsecOffloadV2TunnelNetBufferListInfo</b>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> returns an 
      <a href="..\ndis\ns-ndis--ndis-ipsec-offload-v2-tunnel-net-buffer-list-info.md">
      NDIS_IPSEC_OFFLOAD_V2_TUNNEL_NET_BUFFER_LIST_INFO</a> structure.</p>
</dd>

### -field <a id="IPsecOffloadV2HeaderNetBufferListInfo"></a><a id="ipsecoffloadv2headernetbufferlistinfo"></a><a id="IPSECOFFLOADV2HEADERNETBUFFERLISTINFO"></a><b>IPsecOffloadV2HeaderNetBufferListInfo</b>

<dd>
<p>Specifies IPsecV2 header information that is used in offloading IPsec tasks from the TCP/IP protocol
      to a miniport driver. When you specify <b>IPsecOffloadV2HeaderNetBufferListInfo</b>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> returns an 
      <a href="..\ndis\ns-ndis--ndis-ipsec-offload-v2-header-net-buffer-list-info.md">
      NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO</a> structure.</p>
</dd>

### -field <a id="NetBufferListCorrelationId"></a><a id="netbufferlistcorrelationid"></a><a id="NETBUFFERLISTCORRELATIONID"></a><b>NetBufferListCorrelationId</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <a id="NetBufferListFilteringInfo"></a><a id="netbufferlistfilteringinfo"></a><a id="NETBUFFERLISTFILTERINGINFO"></a><b>NetBufferListFilteringInfo</b>

<dd>
<p>Specifies filtering information that is used in the virtual machine queue (VMQ) interface, the single root I/O virtualization (SR-IOV) interface, and NDIS packet coalescing. When you specify 
     <b>NetBufferListFilteringInfo</b>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> returns an 
     <a href="..\ndis\ns-ndis--ndis-net-buffer-list-filtering-info.md">
     NDIS_NET_BUFFER_LIST_FILTERING_INFO</a> structure.</p>
<p>Starting with NDIS 6.20, receive indications made by miniport drivers that support VMQ, SR-IOV, or packet coalesing must include an <a href="..\ndis\ns-ndis--ndis-net-buffer-list-filtering-info.md">NDIS_NET_BUFFER_LIST_FILTERING_INFO</a> structure. The miniport drivers must set the VMQ queue identifier in the 
     <b>QueueId</b> member of the <b>
     NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure.  The driver also sets the <b>FilterId</b> member of the <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure to zero. </p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, the miniport driver that supports SR-IOV or packet coalescing must set the <b>QueueId</b> to <b>NDIS_DEFAULT_RECEIVE_QUEUE_ID</b> and the <b>FilterId</b> member to zero.</div>
<div> </div>
</dd>

### -field <a id="MediaSpecificInformationEx"></a><a id="mediaspecificinformationex"></a><a id="MEDIASPECIFICINFORMATIONEX"></a><b>MediaSpecificInformationEx</b>

<dd>
<p>Identifies a pointer to a driver-allocated 
     <a href="..\ndis\ns-ndis--ndis-nbl-media-specific-information-ex.md">
     NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX</a> structure. This structure identifies any media-specific
     out-of-band data that accompanies the <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structures that are associated with the <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
     structure. NDIS 6.20 and later drivers should use the <b>
     NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX</b> structure
     to specify media specific information. Any driver in an NDIS driver stack can allocate and manage
     media-specific information.</p>
</dd>

### -field <a id="NblOriginalInterfaceIfIndex"></a><a id="nbloriginalinterfaceifindex"></a><a id="NBLORIGINALINTERFACEIFINDEX"></a><b>NblOriginalInterfaceIfIndex</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <a id="NblReAuthWfpFlowContext"></a><a id="nblreauthwfpflowcontext"></a><a id="NBLREAUTHWFPFLOWCONTEXT"></a><b>NblReAuthWfpFlowContext</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <a id="TcpReceiveBytesTransferred"></a><a id="tcpreceivebytestransferred"></a><a id="TCPRECEIVEBYTESTRANSFERRED"></a><b>TcpReceiveBytesTransferred</b>

<dd>
<p>Identifies a <b>ULONG</b> value that is the number of data bytes that were received by the host stack and
     filled in the receive request that is being processed as a TCP chimney offload receive operation.</p>
</dd>

### -field <a id="SwitchForwardingReserved"></a><a id="switchforwardingreserved"></a><a id="SWITCHFORWARDINGRESERVED"></a><b>SwitchForwardingReserved</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <a id="SwitchForwardingDetail"></a><a id="switchforwardingdetail"></a><a id="SWITCHFORWARDINGDETAIL"></a><b>SwitchForwardingDetail</b>

<dd>
<p>Identifies a pointer to a driver-allocated <a href="..\ndis\ns-ndis--ndis-switch-forwarding-detail-net-buffer-list-info.md">NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</a> structure. This  structure specifies the information for forwarding a packet to one or more  ports of a Hyper-V extensible switch. The driver allocates this structure by calling <a href="netvista.AllocateNetBufferListForwardingContext">AllocateNetBufferListForwardingContext</a> and frees the structure by calling <a href="netvista.FreeNetBufferListForwardingContext">FreeNetBufferListForwardingContext</a>.</p>
</dd>

### -field <a id="VirtualSubnetInfo"></a><a id="virtualsubnetinfo"></a><a id="VIRTUALSUBNETINFO"></a><b>VirtualSubnetInfo</b>

<dd>
<p>Identifies a pointer to a driver-allocated <a href="..\ndis\ns-ndis--ndis-net-buffer-list-virtual-subnet-info.md">NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO</a> structure. </p>
</dd>

### -field <a id="IMReserved"></a><a id="imreserved"></a><a id="IMRESERVED"></a><b>IMReserved</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <a id="TcpRecvSegCoalesceInfo"></a><a id="tcprecvsegcoalesceinfo"></a><a id="TCPRECVSEGCOALESCEINFO"></a><b>TcpRecvSegCoalesceInfo</b>

<dd>
<p>Identifies a pointer to a driver-allocated <a href="..\ndis\ns-ndis--ndis-rsc-nbl-info.md">NDIS_RSC_NBL_INFO</a> union containing receive segment coalescing (RSC) counter information. For more information, see the <a href="..\ndis\ns-ndis--ndis-rsc-nbl-info.md">NDIS_RSC_NBL_INFO</a> documentation.</p>
</dd>

### -field <a id="RscTcpTimestampDelta"></a><a id="rsctcptimestampdelta"></a><a id="RSCTCPTIMESTAMPDELTA"></a><b>RscTcpTimestampDelta</b>

<dd>
<p>Identifies a pointer to a driver-allocated <a href="..\ndis\ns-ndis--ndis-rsc-nbl-info.md">NDIS_RSC_NBL_INFO</a> union containing RSC timestamp information. For more information, see the <a href="..\ndis\ns-ndis--ndis-rsc-nbl-info.md">NDIS_RSC_NBL_INFO</a> documentation.</p>
</dd>

### -field <a id="TcpSendOffloadsSupplementalNetBufferListInfo"></a><a id="tcpsendoffloadssupplementalnetbufferlistinfo"></a><a id="TCPSENDOFFLOADSSUPPLEMENTALNETBUFFERLISTINFO"></a><b>TcpSendOffloadsSupplementalNetBufferListInfo</b>

<dd>
<p>Identifies a pointer to a driver-allocated <a href="..\ndis\ns-ndis--ndis-tcp-send-offloads-supplemental-net-buffer-list-info.md">NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO</a> structure containing additional out-of-band information for encapsulated packets.</p>
</dd>

### -field <a id="NetBufferListInfoReserved1"></a><a id="netbufferlistinforeserved1"></a><a id="NETBUFFERLISTINFORESERVED1"></a><b>NetBufferListInfoReserved1</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <a id="NetBufferListInfoReserved2"></a><a id="netbufferlistinforeserved2"></a><a id="NETBUFFERLISTINFORESERVED2"></a><b>NetBufferListInfoReserved2</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <a id="MaxNetBufferListInfo"></a><a id="maxnetbufferlistinfo"></a><a id="MAXNETBUFFERLISTINFO"></a><b>MaxNetBufferListInfo</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.

</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_NET_BUFFER_LIST_INFO</b> enumeration is used in the 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>

<p>Use these enumeration values with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro to set and
    get values in the 
    <b>NetBufferListInfo</b> array in a <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>.</p>

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
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--ndis-ipsec-offload-v1-net-buffer-list-info.md">
   NDIS_IPSEC_OFFLOAD_V1_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-ipsec-offload-v2-header-net-buffer-list-info.md">
   NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-ipsec-offload-v2-net-buffer-list-info.md">
   NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-ipsec-offload-v2-tunnel-net-buffer-list-info.md">
   NDIS_IPSEC_OFFLOAD_V2_TUNNEL_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-nbl-media-specific-information-ex.md">
   NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-net-buffer-list-8021q-info.md">
   NDIS_NET_BUFFER_LIST_8021Q_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-net-buffer-list-filtering-info.md">
   NDIS_NET_BUFFER_LIST_FILTERING_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-net-buffer-list-virtual-subnet-info.md">NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-switch-forwarding-detail-net-buffer-list-info.md">NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-tcp-ip-checksum-net-buffer-list-info.md">
   NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-tcp-large-send-offload-net-buffer-list-info.md">
   NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscancelsendnetbufferlists.md">NdisCancelSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisgeneratepartialcancelid.md">NdisGeneratePartialCancelId</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NET_BUFFER_LIST_INFO enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
