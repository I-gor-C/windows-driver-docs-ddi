---
UID: NS.ndis._NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES
title: NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES
author: windows-driver-content
description: An NDIS miniport driver sets up an NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure to define the general miniport driver attributes that are associated with a miniport adapter.
old-location: netvista\ndis_miniport_adapter_general_attributes.htm
old-project: netvista
ms.assetid: 5423d073-02a5-468b-b91e-713ac67a5253
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES, NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES, *PNDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES
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
req.irql: See Remarks section
req.iface: 
---

# NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure



## -description
<p>An NDIS miniport driver sets up an <b>NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</b> structure to define the
  general miniport driver attributes that are associated with a miniport adapter.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES {
  NDIS_OBJECT_HEADER               Header;
  ULONG                            Flags;
  NDIS_MEDIUM                      MediaType;
  NDIS_PHYSICAL_MEDIUM             PhysicalMediumType;
  ULONG                            MtuSize;
  ULONG64                          MaxXmitLinkSpeed;
  ULONG64                          XmitLinkSpeed;
  ULONG64                          MaxRcvLinkSpeed;
  ULONG64                          RcvLinkSpeed;
  NDIS_MEDIA_CONNECT_STATE         MediaConnectState;
  NDIS_MEDIA_DUPLEX_STATE          MediaDuplexState;
  ULONG                            LookaheadSize;
  PNDIS_PNP_CAPABILITIES           PowerManagementCapabilities;
  ULONG                            MacOptions;
  ULONG                            SupportedPacketFilters;
  ULONG                            MaxMulticastListSize;
  USHORT                           MacAddressLength;
  UCHAR                            PermanentMacAddress[NDIS_MAX_PHYS_ADDRESS_LENGTH];
  UCHAR                            CurrentMacAddress[NDIS_MAX_PHYS_ADDRESS_LENGTH];
  PNDIS_RECEIVE_SCALE_CAPABILITIES RecvScaleCapabilities;
  NET_IF_ACCESS_TYPE               AccessType;
  NET_IF_DIRECTION_TYPE            DirectionType;
  NET_IF_CONNECTION_TYPE           ConnectionType;
  NET_IFTYPE                       IfType;
  BOOLEAN                          IfConnectorPresent;
  ULONG                            SupportedStatistics;
  ULONG                            SupportedPauseFunctions;
  ULONG                            DataBackFillSize;
  ULONG                            ContextBackFillSize;
  PNDIS_OID                        SupportedOidList;
  ULONG                            SupportedOidListLength;
  ULONG                            AutoNegotiationFlags;
#if (NDIS_SUPPORT_NDIS620)
  PNDIS_PM_CAPABILITIES            PowerManagementCapabilitiesEx;
#endif 
} NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES, *PNDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to <b>NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</b>.
     </p>
<p>To indicate the version of the <b>NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</b> structure, set the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES_REVISION_2"></a><a id="ndis_miniport_adapter_general_attributes_revision_2"></a>NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES_REVISION_2

<dd>
<p>Added the 
        <b>PowerManagementCapabilitiesEx</b> member for NDIS 6.2.</p>
<p>Set the <b>Size</b> member to <b>NDIS_SIZEOF_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES_REVISION_2</b>.</p>
</dd>

### -field <a id="NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES_REVISION_1"></a><a id="ndis_miniport_adapter_general_attributes_revision_1"></a>NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES_REVISION_1

<dd>
<p>Original version for NDIS 6.0 and NDIS 6,1.</p>
<p>Set the 
        <b>Size</b> member to
        <b>NDIS_SIZEOF_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES_REVISION_1</b>.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>MediaType</b>

<dd>
<p>The 
     <b>NdisMedium<i>Xxx</i></b> type that the miniport adapter supports. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565910">NDIS_MEDIUM</a>.</p>
</dd>

### -field <b>PhysicalMediumType</b>

<dd>
<p>The physical medium type for the miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569621">OID_GEN_PHYSICAL_MEDIUM</a>
</p>
</dd>

### -field <b>MtuSize</b>

<dd>
<p>The maximum transfer unit (MTU) size. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569598">OID_GEN_MAXIMUM_FRAME_SIZE</a>.</p>
</dd>

### -field <b>MaxXmitLinkSpeed</b>

<dd>
<p>The maximum transmit link speed of the adapter in bits per second. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569602">OID_GEN_MAX_LINK_SPEED</a>.</p>
</dd>

### -field <b>XmitLinkSpeed</b>

<dd>
<p>The current transmit link speed of the adapter in bits per second. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>.</p>
</dd>

### -field <b>MaxRcvLinkSpeed</b>

<dd>
<p>The maximum receive link speed of the adapter in bits per second. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569602">OID_GEN_MAX_LINK_SPEED</a>.</p>
</dd>

### -field <b>RcvLinkSpeed</b>

<dd>
<p>The current receive link speed of the adapter in bits per second. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>.</p>
</dd>

### -field <b>MediaConnectState</b>

<dd>
<p>The media connect state for the miniport adapter. For more information, see 
     <a href="netvista.oid_gen_media_connect_status_ex">
     OID_GEN_MEDIA_CONNECT_STATUS_EX</a>.</p>
</dd>

### -field <b>MediaDuplexState</b>

<dd>
<p>The media duplex state for the miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569606">OID_GEN_MEDIA_DUPLEX_STATE</a>.</p>
</dd>

### -field <b>LookaheadSize</b>

<dd>
<p>The lookahead size for the miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569574">OID_GEN_CURRENT_LOOKAHEAD</a>.</p>
</dd>

### -field <b>PowerManagementCapabilities</b>

<dd>
<p>The Plug and Play (PnP) capabilities of the miniport adapter. For more information about PnP
     capabilities, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569774">OID_PNP_CAPABILITIES</a>. If the miniport
     adapter is not power management-aware, the miniport driver should set 
     <b>PowerManagementCapabilities</b> to <b>NULL</b>. NDIS 6.20 and later drivers must use the 
     <b>PowerManagementCapabilitiesEx</b> member instead.</p>
</dd>

### -field <b>MacOptions</b>

<dd>
<p>The MAC options for the miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569597">OID_GEN_MAC_OPTIONS</a>.</p>
</dd>

### -field <b>SupportedPacketFilters</b>

<dd>
<p>The packet filter flags for the miniport adapter. For more information, see 
     <a href="netvista.oid_gen_supported_packet_filters">
     OID_GEN_SUPPORTED_PACKET_FILTERS</a>.</p>
</dd>

### -field <b>MaxMulticastListSize</b>

<dd>
<p>The multicast address list size for the miniport adapter. For more information, see 
     <a href="netvista.oid_802_3_maximum_list_size">
     OID_802_3_MAXIMUM_LIST_SIZE</a>.</p>
</dd>

### -field <b>MacAddressLength</b>

<dd>
<p>The MAC address length, in bytes. The MAC address length is specific to the type of media.</p>
</dd>

### -field <b>PermanentMacAddress</b>

<dd>
<p>The permanent MAC address. For example, the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569074">OID_802_3_PERMANENT_ADDRESS</a> OID
     specifies the permanent MAC address for IEEE 802.3 drivers.</p>
</dd>

### -field <b>CurrentMacAddress</b>

<dd>
<p>The current MAC address. For example, the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569069">OID_802_3_CURRENT_ADDRESS</a> OID
     specifies the current MAC address for IEEE 802.3 drivers.</p>
</dd>

### -field <b>RecvScaleCapabilities</b>

<dd>
<p>The receive side scaling (RSS) capabilities of the NIC. If the miniport adapter does not support
     the RSS feature, set 
     <b>RecvScaleCapabilities</b> to <b>NULL</b>. For more information about RSS, see 
     <a href="netvista.oid_gen_receive_scale_capabilities">
     OID_GEN_RECEIVE_SCALE_CAPABILITIES</a>.</p>
</dd>

### -field <b>AccessType</b>

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568739">NET_IF_ACCESS_TYPE</a> NDIS network interface
     access type.</p>
</dd>

### -field <b>DirectionType</b>

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568742">NET_IF_DIRECTION_TYPE</a> NDIS network
     interface direction type.</p>
</dd>

### -field <b>ConnectionType</b>

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568741">NET_IF_CONNECTION_TYPE</a> NDIS network
     interface connection type.</p>
</dd>

### -field <b>IfType</b>

<dd>
<p>The Internet Assigned Numbers Authority (IANA) interface type. For example,
     IF_TYPE_ETHERNET_CSMACD (6) is the value for 
     <b>IfType</b> that is assigned to any Ethernet-like interface. For a list if interface types, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565767">NDIS Interface Types</a>.</p>
</dd>

### -field <b>IfConnectorPresent</b>

<dd>
<p>A Boolean value that indicates if a connector is present. Set this value to <b>TRUE</b> if there is a
     physical adapter.</p>
</dd>

### -field <b>SupportedStatistics</b>

<dd>
<p>The supported statistics.
     </p>
<div class="alert"><b>Note</b>  NDIS 6.0 drivers must support all statistics and must report them when the drivers
     are queried for 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569640">OID_GEN_STATISTICS</a>.</div>
<div> </div>
<p>The value is the bitwise OR of the following flags:</p>
<p></p>
<dl>

### -field <a id="NDIS_STATISTICS_DIRECTED_FRAMES_RCV_SUPPORTED"></a><a id="ndis_statistics_directed_frames_rcv_supported"></a>NDIS_STATISTICS_DIRECTED_FRAMES_RCV_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCInUcastPkts</b> member is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_MULTICAST_FRAMES_RCV_SUPPORTED"></a><a id="ndis_statistics_multicast_frames_rcv_supported"></a>NDIS_STATISTICS_MULTICAST_FRAMES_RCV_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCInMulticastPkts</b> member of 
       NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_BROADCAST_FRAMES_RCV_SUPPORTED"></a><a id="ndis_statistics_broadcast_frames_rcv_supported"></a>NDIS_STATISTICS_BROADCAST_FRAMES_RCV_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCInBroadcastPkts</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_BYTES_RCV_SUPPORTED"></a><a id="ndis_statistics_bytes_rcv_supported"></a>NDIS_STATISTICS_BYTES_RCV_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCInOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_RCV_DISCARDS_SUPPORTED"></a><a id="ndis_statistics_rcv_discards_supported"></a>NDIS_STATISTICS_RCV_DISCARDS_SUPPORTED

<dd>
<p>The data in the 
       <b>ifInDiscards</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_RCV_ERROR_SUPPORTED"></a><a id="ndis_statistics_rcv_error_supported"></a>NDIS_STATISTICS_RCV_ERROR_SUPPORTED

<dd>
<p>The data in the 
       <b>ifInErrors</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_DIRECTED_FRAMES_XMIT_SUPPORTED"></a><a id="ndis_statistics_directed_frames_xmit_supported"></a>NDIS_STATISTICS_DIRECTED_FRAMES_XMIT_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCOutUcastPkts</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_MULTICAST_FRAMES_XMIT_SUPPORTED"></a><a id="ndis_statistics_multicast_frames_xmit_supported"></a>NDIS_STATISTICS_MULTICAST_FRAMES_XMIT_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCOutMulticastPkts</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_BROADCAST_FRAMES_XMIT_SUPPORTED"></a><a id="ndis_statistics_broadcast_frames_xmit_supported"></a>NDIS_STATISTICS_BROADCAST_FRAMES_XMIT_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCOutBroadcastPkts</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_BYTES_XMIT_SUPPORTED"></a><a id="ndis_statistics_bytes_xmit_supported"></a>NDIS_STATISTICS_BYTES_XMIT_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCOutOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_XMIT_ERROR_SUPPORTED"></a><a id="ndis_statistics_xmit_error_supported"></a>NDIS_STATISTICS_XMIT_ERROR_SUPPORTED

<dd>
<p>The data in the 
       <b>ifOutErrors</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_XMIT_DISCARDS_SUPPORTED"></a><a id="ndis_statistics_xmit_discards_supported"></a>NDIS_STATISTICS_XMIT_DISCARDS_SUPPORTED

<dd>
<p>The data in the 
       <b>ifOutDiscards</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_DIRECTED_BYTES_RCV_SUPPORTED"></a><a id="ndis_statistics_directed_bytes_rcv_supported"></a>NDIS_STATISTICS_DIRECTED_BYTES_RCV_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCInUcastOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_MULTICAST_BYTES_RCV_SUPPORTED"></a><a id="ndis_statistics_multicast_bytes_rcv_supported"></a>NDIS_STATISTICS_MULTICAST_BYTES_RCV_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCInMulticastOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_BROADCAST_BYTES_RCV_SUPPORTED"></a><a id="ndis_statistics_broadcast_bytes_rcv_supported"></a>NDIS_STATISTICS_BROADCAST_BYTES_RCV_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCInBroadcastOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_DIRECTED_BYTES_XMIT_SUPPORTED"></a><a id="ndis_statistics_directed_bytes_xmit_supported"></a>NDIS_STATISTICS_DIRECTED_BYTES_XMIT_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCOutUcastOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_MULTICAST_BYTES_XMIT_SUPPORTED"></a><a id="ndis_statistics_multicast_bytes_xmit_supported"></a>NDIS_STATISTICS_MULTICAST_BYTES_XMIT_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCOutMulticastOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>

### -field <a id="NDIS_STATISTICS_BROADCAST_BYTES_XMIT_SUPPORTED"></a><a id="ndis_statistics_broadcast_bytes_xmit_supported"></a>NDIS_STATISTICS_BROADCAST_BYTES_XMIT_SUPPORTED

<dd>
<p>The data in the 
       <b>ifHCOutBroadcastOctets</b> member of NDIS_STATISTICS_INFO is valid.</p>
</dd>
</dl>
</dd>

### -field <b>SupportedPauseFunctions</b>

<dd>
<p>Support for the IEEE 802.3 pause frames as one of the following pause functions:
     </p>
<p></p>
<dl>

### -field <a id="NdisPauseFunctionsUnsupported"></a><a id="ndispausefunctionsunsupported"></a><a id="NDISPAUSEFUNCTIONSUNSUPPORTED"></a><b>NdisPauseFunctionsUnsupported</b>

<dd>
<p>Indicates that the adapter or link partner does not support pause frames.</p>
</dd>

### -field <a id="NdisPauseFunctionsSendOnly"></a><a id="ndispausefunctionssendonly"></a><a id="NDISPAUSEFUNCTIONSSENDONLY"></a><b>NdisPauseFunctionsSendOnly</b>

<dd>
<p>Indicates that the adapter and link partner only support sending pause frames from the adapter
       to the link partner.</p>
</dd>

### -field <a id="NdisPauseFunctionsReceiveOnly"></a><a id="ndispausefunctionsreceiveonly"></a><a id="NDISPAUSEFUNCTIONSRECEIVEONLY"></a><b>NdisPauseFunctionsReceiveOnly</b>

<dd>
<p>Indicates that the adapter and link partner only support sending pause frames from the link
       partner to the adapter</p>
</dd>

### -field <a id="NdisPauseFunctionsSendAndReceive"></a><a id="ndispausefunctionssendandreceive"></a><a id="NDISPAUSEFUNCTIONSSENDANDRECEIVE"></a><b>NdisPauseFunctionsSendAndReceive</b>

<dd>
<p>Indicates that the adapter and link partner support sending and receiving pause frames in both
       transint and receive directions.</p>
</dd>

### -field <a id="NdisPauseFunctionsUnknown"></a><a id="ndispausefunctionsunknown"></a><a id="NDISPAUSEFUNCTIONSUNKNOWN"></a><b>NdisPauseFunctionsUnknown</b>

<dd>
<p>Indicates that pause frame negotiation is in progress. The pause frame support that the link
       partner provides is unknown.</p>
</dd>
</dl>
</dd>

### -field <b>DataBackFillSize</b>

<dd>
<p>The required data backfill size, in bytes, of the driver.</p>
</dd>

### -field <b>ContextBackFillSize</b>

<dd>
<p>The required context backfill size, in bytes, of the driver.</p>
</dd>

### -field <b>SupportedOidList</b>

<dd>
<p>A list of OIDs that the miniport driver supports. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569642">OID_GEN_SUPPORTED_LIST</a>.</p>
</dd>

### -field <b>SupportedOidListLength</b>

<dd>
<p>The size, in bytes, of the OID list at 
     <b>SupportedOidList</b> .</p>
</dd>

### -field <b>AutoNegotiationFlags</b>

<dd>
<p>The auto-negotiation settings for the miniport adapter. This member is created from a bitwise OR
     of the following flags:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED"></a><a id="ndis_link_state_xmit_link_speed_auto_negotiated"></a>NDIS_LINK_STATE_XMIT_LINK_SPEED_AUTO_NEGOTIATED

<dd>
<p>The adapter has auto-negotiated the transmit link speed with the link partner.</p>
</dd>

### -field <a id="NDIS_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED"></a><a id="ndis_link_state_rcv_link_speed_auto_negotiated"></a>NDIS_LINK_STATE_RCV_LINK_SPEED_AUTO_NEGOTIATED

<dd>
<p>The adapter has auto-negotiated the receive link speed with the link partner.</p>
</dd>

### -field <a id="NDIS_LINK_STATE_DUPLEX_AUTO_NEGOTIATED"></a><a id="ndis_link_state_duplex_auto_negotiated"></a>NDIS_LINK_STATE_DUPLEX_AUTO_NEGOTIATED

<dd>
<p>The adapter has auto-negotiated the duplex state with the link partner.</p>
</dd>

### -field <a id="NDIS_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED"></a><a id="ndis_link_state_pause_functions_auto_negotiated"></a>NDIS_LINK_STATE_PAUSE_FUNCTIONS_AUTO_NEGOTIATED

<dd>
<p>The adapter has auto-negotiated the pause functions with the link partner.</p>
</dd>
</dl>
</dd>

### -field <b>PowerManagementCapabilitiesEx</b>

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566748">NDIS_PM_CAPABILITIES</a> structure. This
     structure specifies power management capabilities of the miniport adapter. This member is mandatory for
     NDIS 6.20 and later drivers.</p>
</dd>
</dl>

## -remarks
<p>A miniport driver passes a pointer to an NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure in the 
    <i>MiniportAttributes</i> parameter of the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function. A miniport driver calls 
    <b>NdisMSetMiniportAttributes</b> from its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function
    during initialization. Miniport drivers should set the these attributes after they set the registration
    attributes in the 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">
    NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a> structure and before they set any other attributes.
    Setting these attribute is mandatory. </p>

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
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565910">NDIS_MEDIUM</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">
   NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566748">NDIS_PM_CAPABILITIES</a>
</dt>
<dt>
<a href="netvista.oid_gen_statistics">NDIS_STATISTICS_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568739">NET_IF_ACCESS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568741">NET_IF_CONNECTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568742">NET_IF_DIRECTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569069">OID_802_3_CURRENT_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569072">OID_802_3_MAXIMUM_LIST_SIZE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569074">OID_802_3_PERMANENT_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569574">OID_GEN_CURRENT_LOOKAHEAD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569597">OID_GEN_MAC_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569602">OID_GEN_MAX_LINK_SPEED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569598">OID_GEN_MAXIMUM_FRAME_SIZE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569605">OID_GEN_MEDIA_CONNECT_STATUS_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569606">OID_GEN_MEDIA_DUPLEX_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569621">OID_GEN_PHYSICAL_MEDIUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569640">OID_GEN_STATISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569642">OID_GEN_SUPPORTED_LIST</a>
</dt>
<dt>
<a href="netvista.oid_gen_supported_packet_filters">
   OID_GEN_SUPPORTED_PACKET_FILTERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569774">OID_PNP_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
