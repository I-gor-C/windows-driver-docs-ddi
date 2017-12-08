---
UID: NS.ndis._NET_IF_INFORMATION
title: NET_IF_INFORMATION
author: windows-driver-content
description: The NET_IF_INFORMATION structure provides NDIS with information about a registered network interface.
old-location: netvista\net_if_information.htm
old-project: netvista
ms.assetid: 5508650c-473c-4710-869e-053481e83f1b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NET_IF_INFORMATION, NET_IF_INFORMATION, *PNET_IF_INFORMATION
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
req.alt-api: NET_IF_INFORMATION
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

# NET_IF_INFORMATION structure



## -description
<p>The NET_IF_INFORMATION structure provides NDIS with information about a registered network
  interface.</p>


## -syntax

````
typedef struct _NET_IF_INFORMATION {
  NDIS_OBJECT_HEADER     Header;
  ULONG                  Flags;
  NET_PHYSICAL_LOCATION  PhysicalLocation;
  ULONG                  WanTunnelType;
  ULONG                  PortNumber;
  NET_IF_ACCESS_TYPE     AccessType;
  NET_IF_DIRECTION_TYPE  DirectionType;
  NET_IF_CONNECTION_TYPE ConnectionType;
  BOOLEAN                ifConnectorPresent;
  USHORT                 PhysAddressLength;
  USHORT                 PhysAddressOffset;
  USHORT                 PermanentPhysAddressOffset;
  USHORT                 FriendlyNameLength;
  USHORT                 FriendlyNameOffset;
  GUID                   InterfaceGuid;
  NET_IF_NETWORK_GUID    NetworkGuid;
  ULONG                  SupportedStatistics;
  NDIS_MEDIUM            MediaType;
  NDIS_PHYSICAL_MEDIUM   PhysicalMediumType;
} NET_IF_INFORMATION, *PNET_IF_INFORMATION;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     interface information structure (NET_IF_INFORMATION). The provider sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_OBJECT_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_NET_IF_INFORMATION_REVISION_1.</p>
</dd>

### -field Flags

<dd>
<p>Flags that provide information about the interface that this structure describes. These flags are
     combined with a bitwise OR operation. If none of the flags applies, set this member to zero. The
     following flag values are defined:
     </p>
<p></p>
<dl>

### -field NIIF_HARDWARE_INTERFACE

<dd>
<p>Set if the network interface is for hardware.</p>
</dd>

### -field NIIF_FILTER_INTERFACE

<dd>
<p>Set if the network interface is for a filter module.</p>
</dd>

### -field NIIF_NDIS_RESERVED1

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field NIIF_NDIS_RESERVED2

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field NIIF_NDIS_RESERVED3

<dd>
<p>Reserved for NDIS.</p>
</dd>
</dl>
</dd>

### -field PhysicalLocation

<dd>
<p>The physical location for the hardware that is associated with an interface specified in a 
     <a href="netvista.net_physical_location">
     NET_PHYSICAL_LOCATION</a> structure.</p>
</dd>

### -field WanTunnelType

<dd>
<p>The tunnelIfEncapsMethod (from 
     RFC 2667) for WAN devices. If the WAN tunnel type is unknown, set this
     member to NIIF_WAN_TUNNEL_TYPE_UNKNOWN.</p>
</dd>

### -field PortNumber

<dd>
<p>The NDIS port number for the interface.</p>
</dd>

### -field AccessType

<dd>
<p>A 
     <a href="netvista.net_if_access_type">NET_IF_ACCESS_TYPE</a> NDIS network interface
     access type.</p>
</dd>

### -field DirectionType

<dd>
<p>A 
     <a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a> NDIS network
     interface direction type.</p>
</dd>

### -field ConnectionType

<dd>
<p>A 
     <a href="netvista.net_if_connection_type">NET_IF_CONNECTION_TYPE</a> NDIS network
     interface connection type.</p>
</dd>

### -field ifConnectorPresent

<dd>
<p>A Boolean value that indicates if a connector is present. Set this value to <b>TRUE</b> if there is a
     physical adapter or <b>FALSE</b> if there is no physical adapter.</p>
</dd>

### -field PhysAddressLength

<dd>
<p>The length, in bytes, of the physical address or MAC address. This length is the length of the
     byte arrays that are located at the offsets that the 
     <b>PhysAddressOffset</b> and 
     <b>PermanentPhysAddressOffset</b> members specify.</p>
</dd>

### -field PhysAddressOffset

<dd>
<p>The offset of the current physical address, in bytes, from the beginning of this structure. The
     current physical address is an array of bytes. The length of the array is specified in the 
     <b>PhysAddressLength</b> member. The current physical address is the same value that the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569069">OID_802_3_CURRENT_ADDRESS</a> OID
     returns.</p>
</dd>

### -field PermanentPhysAddressOffset

<dd>
<p>The offset of the permanent physical address, in bytes, from the beginning of this structure. The
     permanent physical address is an array of bytes. The length of the array is specified in the 
     <b>PhysAddressLength</b> member. The permanent physical address is the same value that the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569074">OID_802_3_PERMANENT_ADDRESS</a> OID
     returns.</p>
</dd>

### -field FriendlyNameLength

<dd>
<p>The length, in bytes, of the friendly name for the interface that this structure describes. This
     length is the length of the WCHAR array that is located at the offset in the 
     <b>FriendlyNameOffset</b> member.</p>
</dd>

### -field FriendlyNameOffset

<dd>
<p>The offset of the beginning of the friendly name, in bytes, from the beginning of this structure.
     This name should include the name of the manufacturer, the product, and the version of the interface
     hardware and software. The name is specified as an array of WCHAR values. The 
     <b>FriendlyNameLength</b> member specifies the length of the array.</p>
</dd>

### -field InterfaceGuid

<dd>
<p>The GUID that is associated with the interface. The interface provider generates the interface
     GUID for the interface. The provider can call the 
     <a href="..\ntddk\nf-ntddk-exuuidcreate.md">ExUuidCreate</a> routine to create the GUID. The
     interface GUID should be associated with the 
     <a href="netvista.net_luid">NET_LUID</a> value that is assigned to the interface.
     If the provider retains information about the interface in persistent storage, it should save the GUID
     and reuse the GUID when it reregisters the interface after the computer restarts.</p>
</dd>

### -field NetworkGuid

<dd>
<p>The GUID that is associated with the network that the interface belongs to. If the interface
     provider cannot provide the network GUID, it can pass a zero GUID. In this case, NDIS will register the
     interface in the default network of the primary compartment.</p>
</dd>

### -field SupportedStatistics

<dd>
<p>The statistics that the interface supports. For more information, see the 
     <b>SupportedStatistics</b> member of the 
     <a href="..\ndis\ns-ndis--ndis-miniport-adapter-general-attributes.md">
     NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a> structure .</p>
</dd>

### -field MediaType

<dd>
<p>The 
     <b>NdisMedium</b><i>Xxx</i> type that the interface supports. For more information, see 
     <a href="..\ntddndis\ne-ntddndis--ndis-medium.md">NDIS_MEDIUM</a>.</p>
</dd>

### -field PhysicalMediumType

<dd>
<p>The physical medium type for the interface. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569621">OID_GEN_PHYSICAL_MEDIUM</a>
</p>
</dd>
</dl>

## -remarks
<p>A network interface provider initializes a NET_IF_INFORMATION structure to provide NDIS with
    information about a registered interface. To register an interface, a provider passes a pointer to a
    NET_IF_INFORMATION structure to the 
    <a href="..\ndis\nf-ndis-ndisifregisterinterface.md">
    NdisIfRegisterInterface</a> function.</p>

<p>The interface provider should allocate enough memory for the structure and the arrays that the 
    <b>PhysAddressOffset</b>, 
    <b>PermanentPhysAddressOffset</b>, and 
    <b>FriendlyNameOffset</b> members specify. The provider must provide the values for the arrays after the
    structure and set the offset members to identify the location of the arrays.</p>

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
<a href="..\ntddk\nf-ntddk-exuuidcreate.md">ExUuidCreate</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-medium.md">NDIS_MEDIUM</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-general-attributes.md">
   NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisifregisterinterface.md">NdisIfRegisterInterface</a>
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
<a href="netvista.net_luid">NET_LUID</a>
</dt>
<dt>
<a href="netvista.net_physical_location">NET_PHYSICAL_LOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569069">OID_802_3_CURRENT_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569074">OID_802_3_PERMANENT_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569621">OID_GEN_PHYSICAL_MEDIUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569640">OID_GEN_STATISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_IF_INFORMATION structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
