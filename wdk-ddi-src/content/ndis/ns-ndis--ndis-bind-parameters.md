---
UID: NS.ndis._NDIS_BIND_PARAMETERS
title: NDIS_BIND_PARAMETERS
author: windows-driver-content
description: NDIS initializes an NDIS_BIND_PARAMETERS structure with information that defines the characteristics of a binding and passes it to a protocol driver.
old-location: netvista\ndis_bind_parameters.htm
old-project: netvista
ms.assetid: 0a4866a8-a2f2-447b-8aa9-73203b7fc4bb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_BIND_PARAMETERS, NDIS_BIND_PARAMETERS, *PNDIS_BIND_PARAMETERS
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
req.alt-api: NDIS_BIND_PARAMETERS
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

# NDIS_BIND_PARAMETERS structure



## -description
<p>NDIS initializes an <b>NDIS_BIND_PARAMETERS</b> structure with information that defines the characteristics
  of a binding and passes it to a protocol driver.</p>


## -syntax

````
typedef struct _NDIS_BIND_PARAMETERS {
  NDIS_OBJECT_HEADER                Header;
  PNDIS_STRING                      ProtocolSection;
  PNDIS_STRING                      AdapterName;
  PDEVICE_OBJECT                    PhysicalDeviceObject;
  NDIS_MEDIUM                       MediaType;
  ULONG                             MtuSize;
  ULONG64                           MaxXmitLinkSpeed;
  ULONG64                           XmitLinkSpeed;
  ULONG64                           MaxRcvLinkSpeed;
  ULONG64                           RcvLinkSpeed;
  NDIS_MEDIA_CONNECT_STATE          MediaConnectState;
  NDIS_MEDIA_DUPLEX_STATE           MediaDuplexState;
  ULONG                             LookaheadSize;
  PNDIS_PNP_CAPABILITIES            PowerManagementCapabilities;
  ULONG                             SupportedPacketFilters;
  ULONG                             MaxMulticastListSize;
  USHORT                            MacAddressLength;
  UCHAR                             CurrentMacAddress[NDIS_MAX_PHYS_ADDRESS_LENGTH];
  NDIS_PHYSICAL_MEDIUM              PhysicalMediumType;
  PNDIS_RECEIVE_SCALE_CAPABILITIES  RcvScaleCapabilities;
  NET_LUID                          BoundIfNetluid;
  NET_IFINDEX                       BoundIfIndex;
  NET_LUID                          LowestIfNetluid;
  NET_IFINDEX                       LowestIfIndex;
  NET_IF_ACCESS_TYPE                AccessType;
  NET_IF_DIRECTION_TYPE             DirectionType;
  NET_IF_CONNECTION_TYPE            ConnectionType;
  NET_IFTYPE                        IfType;
  BOOLEAN                           IfConnectorPresent;
  PNDIS_PORT                        ActivePorts;
  ULONG                             DataBackFillSize;
  ULONG                             ContextBackFillSize;
  ULONG                             MacOptions;
  NET_IF_COMPARTMENT_ID             CompartmentId;
  PNDIS_OFFLOAD                     DefaultOffloadConfiguration;
  PNDIS_TCP_CONNECTION_OFFLOAD      TcpConnectionOffloadCapabilities;
  PNDIS_STRING                      BoundAdapterName;
#if (NDIS_SUPPORT_NDIS61)
  PNDIS_HD_SPLIT_CURRENT_CONFIG     HDSplitCurrentConfig;
#endif 
#if (NDIS_SUPPORT_NDIS620)
  PNDIS_RECEIVE_FILTER_CAPABILITIES ReceiveFilterCapabilities;
  PNDIS_PM_CAPABILITIES             PowerManagementCapabilitiesEx;
  PNDIS_NIC_SWITCH_CAPABILITIES     NicSwitchCapabilities;
#endif 
#if (NDIS_SUPPORT_NDIS630)
  BOOLEAN                           NDKEnabled;
  PNDIS_NDK_CAPABILITIES            NDKCapabilities;
  PNDIS_SRIOV_CAPABILITIES          SriovCapabilities;
  PNDIS_NIC_SWITCH_INFO_ARRAY       NicSwitchArray;
#endif 
} NDIS_BIND_PARAMETERS, *PNDIS_BIND_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_BIND_PARAMETERS</b> structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_BIND_PARAMETERS.
     </p>
<p>To indicate the version of the NDIS_BIND_PARAMETERS structure, NDIS sets the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_BIND_PARAMETERS_REVISION_4"></a><a id="ndis_bind_parameters_revision_4"></a>NDIS_BIND_PARAMETERS_REVISION_4

<dd>
<p>Added various members for NDIS 6.30.</p>
<p>NDIS sets the 
        <b>Size</b> member to NDIS_SIZEOF_BIND_PARAMETERS_REVISION_4.</p>
</dd>

### -field <a id="NDIS_BIND_PARAMETERS_REVISION_3"></a><a id="ndis_bind_parameters_revision_3"></a>NDIS_BIND_PARAMETERS_REVISION_3

<dd>
<p>Added the 
        <b>ReceiveFilterCapabilities</b>, 
        <b>PowerManagementCapabilitiesEx</b>, and 
        <b>NicSwitchCapabilities</b> members for NDIS 6.20.</p>
<p>NDIS sets the 
        <b>Size</b> member to NDIS_SIZEOF_BIND_PARAMETERS_REVISION_3.</p>
</dd>

### -field <a id="NDIS_BIND_PARAMETERS_REVISION_2"></a><a id="ndis_bind_parameters_revision_2"></a>NDIS_BIND_PARAMETERS_REVISION_2

<dd>
<p>Added the 
        <b>HDSplitCurrentConfig</b> member for NDIS 6.1.</p>
<p>NDIS sets the 
        <b>Size</b> member to NDIS_SIZEOF_BIND_PARAMETERS_REVISION_2.</p>
</dd>

### -field <a id="NDIS_BIND_PARAMETERS_REVISION_1"></a><a id="ndis_bind_parameters_revision_1"></a>NDIS_BIND_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.0.</p>
<p>NDIS sets the 
        <b>Size</b> member to NDIS_SIZEOF_BIND_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>ProtocolSection</b>

<dd>
<p>A pointer to a Unicode string that contains a registry path. The path starts from the protocol
     driver's service key and continues down the registry hierarchy to the miniport adapter name (for
     example, 
     <b>Tcpip\Parameters\Adapters\</b>&lt;
     <i>miniport adapter name</i>&gt;). The miniport adapter name is the name of the
     bottom-most miniport adapter in the driver stack. If there is a MUX intermediate driver in the stack,
     the bottom-most miniport adapter is a virtual miniport. Otherwise, the bottom-most miniport adapter is a
     miniport adapter for a physical device.
     </p>
<p>The protocol driver can use this registry path to read configuration parameters that are specific to
     the binding between the driver and the underlying miniport adapter.</p>
</dd>

### -field <b>AdapterName</b>

<dd>
<p>A pointer to a Unicode string that contains the name of the underlying miniport adapter to which 
     <i>ProtocolBindAdapterEx</i> should bind.</p>
</dd>

### -field <b>PhysicalDeviceObject</b>

<dd>
<p>The physical device object for the underlying miniport adapter.</p>
</dd>

### -field <b>MediaType</b>

<dd>
<p>The 
     <b>NdisMedium</b><i>Xxx</i> type that the underlying miniport adapter supports. For more information
     about 
     <b>NdisMedium</b><i>Xxx</i> types, see 
     <a href="..\ntddndis\ne-ntddndis--ndis-medium.md">NDIS_MEDIUM</a>.</p>
</dd>

### -field <b>MtuSize</b>

<dd>
<p>The maximum transfer unit (MTU) size. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569598">OID_GEN_MAXIMUM_FRAME_SIZE</a>.</p>
</dd>

### -field <b>MaxXmitLinkSpeed</b>

<dd>
<p>The maximum transmit link speed of the underlying adapter in bits per second. For more
     information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569602">OID_GEN_MAX_LINK_SPEED</a>.</p>
</dd>

### -field <b>XmitLinkSpeed</b>

<dd>
<p>The current transmit link speed of the underlying adapter in bits per second. For more
     information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>.</p>
</dd>

### -field <b>MaxRcvLinkSpeed</b>

<dd>
<p>The maximum receive link speed of the underlying adapter in bits per second. For more information,
     see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569602">OID_GEN_MAX_LINK_SPEED</a>.</p>
</dd>

### -field <b>RcvLinkSpeed</b>

<dd>
<p>The current receive link speed of the underlying adapter in bits per second. For more information,
     see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569594">OID_GEN_LINK_SPEED_EX</a>.</p>
</dd>

### -field <b>MediaConnectState</b>

<dd>
<p>The media connect state for the underlying miniport adapter. For more information, see 
     <a href="netvista.oid_gen_media_connect_status_ex">
     OID_GEN_MEDIA_CONNECT_STATUS_EX</a>.</p>
</dd>

### -field <b>MediaDuplexState</b>

<dd>
<p>The media duplex state for the underlying miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569606">OID_GEN_MEDIA_DUPLEX_STATE</a>.</p>
</dd>

### -field <b>LookaheadSize</b>

<dd>
<p>The lookahead size for the underlying miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569574">OID_GEN_CURRENT_LOOKAHEAD</a>.</p>
</dd>

### -field <b>PowerManagementCapabilities</b>

<dd>
<p>The Plug and Play capabilities of the underlying miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569774">OID_PNP_CAPABILITIES</a>. NDIS 6.20 and
     later drivers must use the 
     <b>PowerManagementCapabilitiesEx</b> member instead.</p>
</dd>

### -field <b>SupportedPacketFilters</b>

<dd>
<p>A set of flags that identify the types of network packets that the underlying miniport adapter can
     filter. For more information, see 
     <a href="netvista.oid_gen_supported_packet_filters">
     OID_GEN_SUPPORTED_PACKET_FILTERS</a>.</p>
</dd>

### -field <b>MaxMulticastListSize</b>

<dd>
<p>The multicast address list size for the underlying miniport adapter. For more information, see 
     <a href="netvista.oid_802_3_maximum_list_size">
     OID_802_3_MAXIMUM_LIST_SIZE</a>.</p>
</dd>

### -field <b>MacAddressLength</b>

<dd>
<p>The MAC address length, in bytes. The MAC address length is specific to the type of media.</p>
</dd>

### -field <b>CurrentMacAddress</b>

<dd>
<p>The current MAC address. For example, the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569069">OID_802_3_CURRENT_ADDRESS</a> OID
     specifies the current MAC address for IEEE 802.3 drivers.</p>
</dd>

### -field <b>PhysicalMediumType</b>

<dd>
<p>The physical medium type for the miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569621">OID_GEN_PHYSICAL_MEDIUM</a>.</p>
</dd>

### -field <b>RcvScaleCapabilities</b>

<dd>
<p>The <a href="netvista.ndis_receive_side_scaling2">receive side scaling (RSS)</a> capabilities of the NIC. For more information, see 
     <a href="netvista.oid_gen_receive_scale_capabilities">
     OID_GEN_RECEIVE_SCALE_CAPABILITIES</a>.</p>
</dd>

### -field <b>BoundIfNetluid</b>

<dd>
<p>The NDIS 
     <a href="netvista.net_luid">NET_LUID</a> value, that is also the network interface
     name (
     <i>ifName</i> in RFC 2863), of the highest level interface that is stacked on the
     miniport adapter. That is, if there are virtual miniports or filter modules that are installed over the
     miniport adapter, this is the NET_LUID value of the highest level virtual miniport or filter
     module.</p>
</dd>

### -field <b>BoundIfIndex</b>

<dd>
<p>The NDIS network interface index of the highest level interface that is stacked on the miniport
     adapter. That is, if there are virtual miniports or filter modules that are installed over the miniport
     adapter, this is the ifIndex of the highest level virtual miniport or filter module.</p>
</dd>

### -field <b>LowestIfNetluid</b>

<dd>
<p>The NDIS 
     <a href="netvista.net_luid">NET_LUID</a> value, that is also the network interface
     name (
     <i>ifName</i> in RFC 2863), of the lowest level interface on a binding. That is, the
     NDIS network interface of the miniport adapter at the bottom of a filter stack.</p>
</dd>

### -field <b>LowestIfIndex</b>

<dd>
<p>The NDIS network interface index of lowest level interface on a binding. That is, the NDIS network
     interface of the miniport adapter at the bottom of a filter stack.</p>
</dd>

### -field <b>AccessType</b>

<dd>
<p>A 
     <a href="netvista.net_if_access_type">NET_IF_ACCESS_TYPE</a> NDIS network interface
     access type.</p>
</dd>

### -field <b>DirectionType</b>

<dd>
<p>A 
     <a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a> NDIS network
     interface direction type.</p>
</dd>

### -field <b>ConnectionType</b>

<dd>
<p>The NDIS network interface connection type. Use <b>NET_IF_CONNECTION_DEDICATED</b> for a typical Ethernet
     adapter. The following valuse are valid:
     </p>
<p></p>
<dl>

### -field <a id="NET_IF_CONNECTION_DEDICATED"></a><a id="net_if_connection_dedicated"></a>NET_IF_CONNECTION_DEDICATED

<dd>
<p>Specifies the dedicated connection type. The connection comes up automatically when media sense
       is <b>TRUE</b>. For example, an Ethernet connection is dedicated.</p>
</dd>

### -field <a id="NET_IF_CONNECTION_PASSIVE"></a><a id="net_if_connection_passive"></a>NET_IF_CONNECTION_PASSIVE

<dd>
<p>Specifies the passive connection type. The other end must bring up the connection to the local
       station. For example, the RAS interface is passive.</p>
</dd>

### -field <a id="NET_IF_CONNECTION_DEMAND"></a><a id="net_if_connection_demand"></a>NET_IF_CONNECTION_DEMAND

<dd>
<p>Specifies the demand-dial connection type. A demand-dial connection comes up in response to a
       local action--for example, sending a packet.</p>
</dd>
</dl>
</dd>

### -field <b>IfType</b>

<dd>
<p>The Internet Assigned Numbers Authority (IANA) interface type. For example,
     IF_TYPE_ETHERNET_CSMACD (6) is the value for 
     <b>IfType</b> that is assigned to any Ethernet-like interface. For a list if
     interface types, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565767">NDIS Interface Types</a>.</p>
</dd>

### -field <b>IfConnectorPresent</b>

<dd>
<p>A Boolean value that indicates if a connector is present. NDIS sets this value to <b>TRUE</b> if there is
     a physical adapter.</p>
</dd>

### -field <b>ActivePorts</b>

<dd>
<p>To be determined.</p>
</dd>

### -field <b>DataBackFillSize</b>

<dd>
<p>The required data backfill size, in bytes, of the underlying driver stack.</p>
</dd>

### -field <b>ContextBackFillSize</b>

<dd>
<p>The required context backfill size, in bytes, of the underlying driver stack.</p>
</dd>

### -field <b>MacOptions</b>

<dd>
<p>The MAC options for the miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569597">OID_GEN_MAC_OPTIONS</a>.</p>
</dd>

### -field <b>CompartmentId</b>

<dd>
<p>The compartment to which the underlying interface belongs or one of the following values:
     </p>
<p></p>
<dl>

### -field <a id="NET_IF_COMPARTMENT_ID_UNSPECIFIED"></a><a id="net_if_compartment_id_unspecified"></a>NET_IF_COMPARTMENT_ID_UNSPECIFIED

<dd>
<p>Specifies that the compartment identifier is not used or specified.</p>
</dd>

### -field <a id="NET_IF_COMPARTMENT_ID_PRIMARY"></a><a id="net_if_compartment_id_primary"></a>NET_IF_COMPARTMENT_ID_PRIMARY

<dd>
<p>Specifies the default compartment identifier. Third party interface providers must always
       specify NET_IF_COMPARTMENT_ID_PRIMARY. All other values are reserved for Microsoft internal
       use.</p>
</dd>
</dl>
</dd>

### -field <b>DefaultOffloadConfiguration</b>

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-offload.md">NDIS_OFFLOAD</a> structure. This structure
     specifies the capabilities for a task-offload-capable miniport adapter. For more information, see 
     <a href="netvista.oid_tcp_offload_current_config">
     OID_TCP_OFFLOAD_CURRENT_CONFIG</a>.</p>
</dd>

### -field <b>TcpConnectionOffloadCapabilities</b>

<dd>
<p>A pointer to an 
     <a href="..\ntddndis\ns-ntddndis--ndis-tcp-connection-offload.md">
     NDIS_TCP_CONNECTION_OFFLOAD</a> structure that indicates the current offload capabilities that are
     provided by the underlying miniport adapter.</p>
</dd>

### -field <b>BoundAdapterName</b>

<dd>
<p>A pointer to a Unicode string that contains the name of the highest-level miniport adapter that is
     stacked on the underlying miniport adapter. That is, if there are filter intermediate driver virtual
     miniports that are installed over the miniport adapter, this member is the name of the highest-level
     filter intermediate driver virtual miniport.</p>
</dd>

### -field <b>HDSplitCurrentConfig</b>

<dd>
<p>A pointer to an 
      <a href="..\ntddndis\ns-ntddndis--ndis-hd-split-current-config.md">
      NDIS_HD_SPLIT_CURRENT_CONFIG</a> structure. This structure specifies the current header-data split
      configuration of the underlying miniport adapter. This value can be <b>NULL</b> if the miniport adapter does
      not support header-data split.</p>
</dd>

### -field <b>ReceiveFilterCapabilities</b>

<dd>
<p>A pointer to an 
     <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-capabilities.md">
     NDIS_RECEIVE_FILTER_CAPABILITIES</a> structure. This structure specifies the generic filtering
     capabilities that are currently enabled on the underlying miniport adapter. This value can be <b>NULL</b> if the miniport adapter does not
     support receive filtering.</p>
</dd>

### -field <b>PowerManagementCapabilitiesEx</b>

<dd>
<p>A pointer to an 
     <a href="..\ntddndis\ns-ntddndis--ndis-pm-capabilities.md">NDIS_PM_CAPABILITIES</a> structure. This
     structure specifies power management capabilities of the miniport adapter. This member is mandatory for
     NDIS 6.20 and later drivers.</p>
</dd>

### -field <b>NicSwitchCapabilities</b>

<dd>
<p>A pointer to an 
     <a href="..\ntddndis\ns-ntddndis--ndis-nic-switch-capabilities.md">
     NDIS_NIC_SWITCH_CAPABILITIES</a> structure. This structure specifies the NIC switch capabilities of
     the underlying miniport adapter. This value can be <b>NULL</b> if the miniport adapter does not support NIC
     switch features.</p>
</dd>

### -field <b>NDKEnabled</b>

<dd>
<p>NDIS sets this value to <b>TRUE</b> if the network direct kernel provider interface (NDKPI) is currently enabled on the underlying miniport adapter.</p>
</dd>

### -field <b>NDKCapabilities</b>

<dd>
<p>A pointer to an <a href="..\ntddndis\ns-ntddndis--ndis-ndk-capabilities.md">NDIS_NDK_CAPABILITIES</a> structure. This structure specifies the NDKPI capabilities that are currently enabled on the underlying miniport adapter. This value can be <b>NULL</b> if the miniport adapter does not support NDKPI.</p>
</dd>

### -field <b>SriovCapabilities</b>

<dd>
<p>A pointer to an <a href="..\ntddndis\ns-ntddndis--ndis-sriov-capabilities.md">NDIS_SRIOV_CAPABILITIES</a> structure. This structure specifies the single root I/O virtualization (SR-IOV) capabilities that are currently enabled on the underlying miniport adapter. This value can be <b>NULL</b> if the miniport adapter does not support SR-IOV features.</p>
</dd>

### -field <b>NicSwitchArray</b>

<dd>
<p>A pointer to an <a href="..\ntddndis\ns-ntddndis--ndis-nic-switch-info-array.md">NDIS_NIC_SWITCH_INFO_ARRAY</a> structure.  This array enumerates the NIC switches that have been created on the miniport adapter. NIC switches can only be created if SR-IOV is supported and enabled on the adapter. </p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, Windows supports only the default NIC switch on the miniport adapter. Therefore, this array can contain only one element. </div>
<div> </div>
</dd>
</dl>

## -remarks
<p>NDIS passes a pointer to an NDIS_BIND_PARAMETERS structure in the 
    <i>BindParameters</i> parameter of the 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">
    ProtocolBindAdapterEx</a> function.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-hd-split-current-config.md">NDIS_HD_SPLIT_CURRENT_CONFIG</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-medium.md">NDIS_MEDIUM</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-nic-switch-capabilities.md">NDIS_NIC_SWITCH_CAPABILITIES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-nic-switch-info-array.md">NDIS_NIC_SWITCH_INFO_ARRAY</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-offload.md">NDIS_OFFLOAD</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-pm-capabilities.md">NDIS_PM_CAPABILITIES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-capabilities.md">
   NDIS_RECEIVE_FILTER_CAPABILITIES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-sriov-capabilities.md">NDIS_SRIOV_CAPABILITIES</a>
</dt>
<dt>
<a href="netvista.net_if_access_type">NET_IF_ACCESS_TYPE</a>
</dt>
<dt>
<a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a>
</dt>
<dt>
<a href="netvista.net_luid">NET_LUID</a>
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
<a href="netvista.oid_gen_receive_scale_capabilities">
   OID_GEN_RECEIVE_SCALE_CAPABILITIES</a>
</dt>
<dt>
<a href="netvista.oid_gen_supported_packet_filters">
   OID_GEN_SUPPORTED_PACKET_FILTERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-tcp-connection-offload.md">NDIS_TCP_CONNECTION_OFFLOAD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569805">OID_TCP_OFFLOAD_CURRENT_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569774">OID_PNP_CAPABILITIES</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_BIND_PARAMETERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
