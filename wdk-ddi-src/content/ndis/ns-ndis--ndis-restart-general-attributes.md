---
UID: NS.ndis._NDIS_RESTART_GENERAL_ATTRIBUTES
title: NDIS_RESTART_GENERAL_ATTRIBUTES
author: windows-driver-content
description: The NDIS_RESTART_GENERAL_ATTRIBUTES structure defines the general restart attributes that are associated with a miniport adapter.
old-location: netvista\ndis_restart_general_attributes.htm
old-project: netvista
ms.assetid: f67bd2fe-4553-4b1a-8d39-26777bcc60e0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_RESTART_GENERAL_ATTRIBUTES, NDIS_RESTART_GENERAL_ATTRIBUTES, *PNDIS_RESTART_GENERAL_ATTRIBUTES
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
req.alt-api: NDIS_RESTART_GENERAL_ATTRIBUTES
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

# NDIS_RESTART_GENERAL_ATTRIBUTES structure



## -description
<p>The <b>NDIS_RESTART_GENERAL_ATTRIBUTES</b> structure defines the general restart attributes that are
  associated with a miniport adapter.</p>


## -syntax

````
typedef struct _NDIS_RESTART_GENERAL_ATTRIBUTES {
  NDIS_OBJECT_HEADER               Header;
  ULONG                            MtuSize;
  ULONG64                          MaxXmitLinkSpeed;
  ULONG64                          MaxRcvLinkSpeed;
  ULONG                            LookaheadSize;
  ULONG                            MacOptions;
  ULONG                            SupportedPacketFilters;
  ULONG                            MaxMulticastListSize;
  PNDIS_RECEIVE_SCALE_CAPABILITIES RecvScaleCapabilities;
  NET_IF_ACCESS_TYPE               AccessType;
  ULONG                            Flags;
  NET_IF_CONNECTION_TYPE           ConnectionType;
  ULONG                            SupportedStatistics;
  ULONG                            DataBackFillSize;
  ULONG                            ContextBackFillSize;
  PNDIS_OID                        SupportedOidList;
  ULONG                            SupportedOidListLength;
#if (NDIS_SUPPORT_NDIS620)
  ULONG                            MaxLookaheadSizeAccessed;
#endif 
} NDIS_RESTART_GENERAL_ATTRIBUTES, *PNDIS_RESTART_GENERAL_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RESTART_GENERAL_ATTRIBUTES</b> structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to <b>NDIS_OBJECT_TYPE_RESTART_GENERIC_ATTRIBUTES</b>. 
     </p>
<p>To indicate the version of the <b>NDIS_RESTART_GENERAL_ATTRIBUTES</b> structure, NDIS sets the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_RESTART_GENERAL_ATTRIBUTES_REVISION_2"></a><a id="ndis_restart_general_attributes_revision_2"></a>NDIS_RESTART_GENERAL_ATTRIBUTES_REVISION_2

<dd>
<p>Added the 
       <b>MaxLookaheadSizeAccessed</b> member for NDIS 6.2. 
       </p>
<p>NDIS sets the 
       <b>Size</b> member to <b>NDIS_SIZEOF_RESTART_GENERAL_ATTRIBUTES_REVISION_2</b>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="NDIS_RESTART_GENERAL_ATTRIBUTES_REVISION_1"></a><a id="ndis_restart_general_attributes_revision_1"></a>NDIS_RESTART_GENERAL_ATTRIBUTES_REVISION_1

<dd>
<p>Original version for NDIS 6.0 and NDIS 6.1.
       </p>
<p>NDIS sets the 
       <b>Size</b> member to <b>NDIS_SIZEOF_RESTART_GENERAL_ATTRIBUTES_REVISION_1</b>.</p>
</dd>
</dl>
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

### -field <b>MaxRcvLinkSpeed</b>

<dd>
<p>The maximum receive link speed of the adapter in bits per second. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569602">OID_GEN_MAX_LINK_SPEED</a>.</p>
</dd>

### -field <b>LookaheadSize</b>

<dd>
<p>The lookahead size for the miniport adapter. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569574">OID_GEN_CURRENT_LOOKAHEAD</a>.</p>
</dd>

### -field <b>MacOptions</b>

<dd>
<p>The medium access control (MAC) options for the miniport adapter. For more information, see 
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
<p>The maximum multicast address list size for the miniport adapter. For more information, see 
     <a href="netvista.oid_802_3_maximum_list_size">
     OID_802_3_MAXIMUM_LIST_SIZE</a>.</p>
</dd>

### -field <b>RecvScaleCapabilities</b>

<dd>
<p>The receive side scaling (RSS) capabilities of the NIC. If the miniport adapter does not support
     the RSS feature, NDIS sets 
     <b>RecvScaleCapabilities</b> to a pointer to an 
     <a href="..\ntddndis\ns-ntddndis--ndis-receive-scale-capabilities.md">
     NDIS_RECEIVE_SCALE_CAPABILITIES</a> structure that is filled with zeros. For more information about
     RSS, see 
     <a href="netvista.oid_gen_receive_scale_capabilities">
     OID_GEN_RECEIVE_SCALE_CAPABILITIES</a>.</p>
</dd>

### -field <b>AccessType</b>

<dd>
<p>A 
     <a href="netvista.net_if_access_type">NET_IF_ACCESS_TYPE</a> NDIS network interface
     access type.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>ConnectionType</b>

<dd>
<p>A 
     <a href="netvista.net_if_connection_type">NET_IF_CONNECTION_TYPE</a> NDIS network
     interface connection type.</p>
</dd>

### -field <b>SupportedStatistics</b>

<dd>
<p>The supported statistics. For more information, see the 
     <b>SupportedStatistics</b> member of the 
     <a href="..\ndis\ns-ndis--ndis-miniport-adapter-general-attributes.md">
     NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a> structure.</p>
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
<p>The size, in bytes, of the OID list that is specified in the 
     <b>SupportedOidList</b> member.</p>
</dd>

### -field <b>MaxLookaheadSizeAccessed</b>

<dd>
<p>A ULONG value for the maximum size, in bytes, of the lookahead size requirement for receive
     queues. A miniport adapter that supports lookahead in VM queues splits a received packet at an offset
     equal to or greater than the requested lookahead size and DMAs the lookahead data and the post-lookahead
     data to separate shared memory segments.</p>
</dd>
</dl>

## -remarks
<p>NDIS passes an NDIS_RESTART_GENERAL_ATTRIBUTES structure to drivers during restart operations. For
    example, when NDIS calls a miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a> function, NDIS passes a
    pointer to an 
    <a href="..\ndis\ns-ndis--ndis-restart-attributes.md">NDIS_RESTART_ATTRIBUTES</a> structure to
    the miniport driver in the 
    <b>RestartAttributes</b> member of the 
    <a href="..\ndis\ns-ndis--ndis-miniport-restart-parameters.md">
    NDIS_MINIPORT_RESTART_PARAMETERS</a> structure.</p>

<p>If the 
    <b>Oid</b> member in the NDIS_RESTART_ATTRIBUTES structure is 
    <a href="netvista.oid_gen_miniport_restart_attributes">
    OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a>, the 
    <b>Data</b> member of NDIS_RESTART_ATTRIBUTES contains an NDIS_RESTART_GENERAL_ATTRIBUTES structure.</p>

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
<a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-general-attributes.md">
   NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-restart-parameters.md">
   NDIS_MINIPORT_RESTART_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-receive-scale-capabilities.md">
   NDIS_RECEIVE_SCALE_CAPABILITIES</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-restart-attributes.md">NDIS_RESTART_ATTRIBUTES</a>
</dt>
<dt>
<a href="netvista.net_if_access_type">NET_IF_ACCESS_TYPE</a>
</dt>
<dt>
<a href="netvista.net_if_connection_type">NET_IF_CONNECTION_TYPE</a>
</dt>
<dt>
<a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569072">OID_802_3_MAXIMUM_LIST_SIZE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569574">OID_GEN_CURRENT_LOOKAHEAD</a>
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
<a href="netvista.oid_gen_miniport_restart_attributes">
   OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RESTART_GENERAL_ATTRIBUTES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
