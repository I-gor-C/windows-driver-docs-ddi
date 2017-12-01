---
UID: NS.ntddndis._NDIS_PM_PROTOCOL_OFFLOAD
title: NDIS_PM_PROTOCOL_OFFLOAD
author: windows-driver-content
description: The NDIS_PM_PROTOCOL_OFFLOAD structure specifies parameters for a low power protocol offload to a network adapter.
old-location: netvista\ndis_pm_protocol_offload.htm
old-project: netvista
ms.assetid: 1ae68e5c-f9ea-4454-b015-82e3af0f7ccd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PM_PROTOCOL_OFFLOAD, NDIS_PM_PROTOCOL_OFFLOAD, *PNDIS_PM_PROTOCOL_OFFLOAD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ntddndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PM_PROTOCOL_OFFLOAD
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

# NDIS_PM_PROTOCOL_OFFLOAD structure



## -description
<p>The <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure specifies parameters for a low power protocol offload to a
  network adapter.</p>


## -syntax

````
typedef struct _NDIS_PM_PROTOCOL_OFFLOAD {
  NDIS_OBJECT_HEADER                 Header;
  ULONG                              Flags;
  ULONG                              Priority;
  NDIS_PM_PROTOCOL_OFFLOAD_TYPE      ProtocolOffloadType;
  NDIS_PM_COUNTED_STRING             FriendlyName;
  ULONG                              ProtocolOffloadId;
  ULONG                              NextProtocolOffloadOffset;
  union _PROTOCOL_OFFLOAD_PARAMETERS {
    struct _IPV4_ARP_PARAMETERS {
      ULONG Flags;
      UCHAR RemoteIPv4Address[4];
      UCHAR HostIPv4Address[4];
      UCHAR MacAddress[6];
    } IPv4ARPParameters;
    struct _IPV6_NS_PARAMETERS {
      ULONG Flags;
      UCHAR RemoteIPv6Address[16];
      UCHAR SolicitedNodeIPv6Address[16];
      UCHAR MacAddress[6];
      UCHAR TargetIPv6Addresses[2][16];
    } IPv6NSParameters;
    struct _DOT11_RSN_REKEY_PARAMETERS {
      ULONG     Flags;
      UCHAR     KCK[DOT11_RSN_KCK_LENGTH];
      UCHAR     KEK[DOT11_RSN_KEK_LENGTH];
      ULONGLONG KeyReplayCounter;
    } Dot11RSNRekeyParameters;
  } ProtocolOffloadParameters;
} NDIS_PM_PROTOCOL_OFFLOAD, *PNDIS_PM_PROTOCOL_OFFLOAD;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     structure (NDIS_PM_PROTOCOL_OFFLOAD). The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_PM_PROTOCOL_OFFLOAD_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_NDIS_PM_PROTOCOL_OFFLOAD_REVISION_1.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>Priority</b>

<dd>
<p>A ULONG value that contains the priority of the protocol offload. If an overlying driver adds a
     higher priority protocol offload when there are no resources that are available for more protocol offloads, NDIS
     might remove a lower priority protocol offload to free resources. Miniport drivers should ignore this
     member. Protocol drivers can provide any value within the predefined range. The following values are
     predefined:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_LOWEST"></a><a id="ndis_pm_protocol_offload_priority_lowest"></a>NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_LOWEST

<dd>
<p>Specifies the lowest priority protocol offload.</p>
</dd>

### -field <a id="NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_NORMAL"></a><a id="ndis_pm_protocol_offload_priority_normal"></a>NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_NORMAL

<dd>
<p>Specifies a normal priority protocol offload.</p>
</dd>

### -field <a id="NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_HIGHEST"></a><a id="ndis_pm_protocol_offload_priority_highest"></a>NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_HIGHEST

<dd>
<p>Specifies the highest priority protocol offload.</p>
</dd>
</dl>
</dd>

### -field <b>ProtocolOffloadType</b>

<dd>
<p>An 
     <a href="..\ntddndis\ne-ntddndis--ndis-pm-protocol-offload-type.md">
     NDIS_PM_PROTOCOL_OFFLOAD_TYPE</a> value that contains the type of protocol offload.</p>
</dd>

### -field <b>FriendlyName</b>

<dd>
<p>An 
     <a href="..\ntddndis\ns-ntddndis--ndis-pm-counted-string.md">NDIS_PM_COUNTED_STRING</a> structure
     that contains the user-readable description of the low power protocol offload.</p>
</dd>

### -field <b>ProtocolOffloadId</b>

<dd>
<p>A ULONG value that contains an NDIS-provided value that identifies the offloaded protocol. Before
     NDIS sends the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569763">OID_PM_ADD_PROTOCOL_OFFLOAD</a> OID
     request down to the underlying NDIS drivers or completes the request to the overlying driver, NDIS sets 
     <b>ProtocolOffloadId</b> to a value that is unique among the protocol offloads on a network adapter.</p>
</dd>

### -field <b>NextProtocolOffloadOffset</b>

<dd>
<p>A ULONG value that contains an offset, in bytes. The 
     <b>NextProtocolOffloadOffset</b> member of each <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure in a list is set to
     the offset (from the beginning of the OID request 
     InformationBuffer) of the next <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure in the list. If 
     <b>NextProtocolOffloadOffset</b> is zero, the current structure is the last structure in the list.</p>
</dd>

### -field <b>ProtocolOffloadParameters</b>

<dd>
<p>A union that contains the following member structures:</p>
<dl>

### -field <b>IPv4ARPParameters</b>

<dd>
<p>A structure that contains IPv4 ARP parameters. This structure contains the following
      members:</p>
<dl>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>RemoteIPv4Address</b>

<dd>
<p>A <b>UCHAR</b> array that contains an optional IPv4 address. This address represents the Source Protocol
        Address (SPA) field of the ARP request.</p>
<p>If the incoming ARP request has an SPA value that matches this IPv4 address, the network adapter sends an ARP
        response when it is in a low power state. If this member is zero, the network adapter should respond to ARP
        requests from any remote IPv4 address.</p>
<p>For more information about the ARP protocol, see RFC 826.</p>
</dd>

### -field <b>HostIPv4Address</b>

<dd>
<p>A <b>UCHAR</b> array that contains the IPv4 address. When it sends the ARP response, the network adapter uses this
       member for the SPA field of the response.</p>
</dd>

### -field <b>MacAddress</b>

<dd>
<p>A <b>UCHAR</b> array that contains a media access control (MAC) address. The network adapter uses this MAC address
       for the Source Hardware Address (SHA) field of the ARP response packet that it generates.
       </p>
<div class="alert"><b>Note</b>  When it sends an ARP response, the network adapter must always use this MAC address in the
       ARP payload. However, it should use the current MAC address of the network adapter as the source address in the
       MAC header.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>IPv6NSParameters</b>

<dd>
<p>A structure that contains IPv6 Neighbor Solicitation (NS) parameters. This structure contains the
      following members:</p>
<dl>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>RemoteIPv6Address</b>

<dd>
<p>A <b>UCHAR</b> array that contains an optional IPv6 address. This address represents the Source Address
        field in the IPv6 header of the NS message.</p>
<p>If the incoming NS message has a Source Address value that matches this IPv6 address, the network adapter
        sends a neighbor advertisement (NA) message when it is in a low power state. If this member is zero,
        the network adapter should respond to NS messages from any remote IPv6 address.</p>
<p>For more information about IPv6 NS and NA messages, see <a href="http://go.microsoft.com/fwlink/p/?linkid=268370">RFC 4861</a>.</p>
</dd>

### -field <b>SolicitedNodeIPv6Address</b>

<dd>
<p>A <b>UCHAR</b> array that contains the solicited node IPv6 address. For more information about this
       type of IPv6 address, see Multicast IPv6 Addresses.</p>
</dd>

### -field <b>MacAddress</b>

<dd>
<p>A <b>UCHAR</b> array that contains the MAC address. When it sends the NA message, the network adapter uses this array
        for the target link-layer address (TLLA) field of the NA message.</p>
<div class="alert"><b>Note</b>  When it sends an NA message, the network adapter must always use this MAC address in the
        TLLA field of the NA message. However, it should use the current MAC address of the network adapter as the source
        address in the MAC header.</div>
<div> </div>
</dd>

### -field <b>TargetIPv6Addresses</b>

<dd>
<p>A <b>UCHAR</b> array that contains one or two IPv6 addresses. If it contains only one address, that address is stored in the first element in the array, and the second element is filled with zeros.</p>
<p>Miniport drivers must consume all addresses in the array.</p>
<p>These addresses represent the Target Address field of an NS message. If one of these addresses
       matches the Target Address field of an incoming NS message, the network adapter sends an NA message in
       response.</p>
</dd>
</dl>
</dd>

### -field <b>Dot11RSNRekeyParameters</b>

<dd>
<p>A structure that contains IEEE 802.11i Robust Security Network (RSN) handshake parameters. This
      structure contains the following members:</p>
<dl>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>KCK</b>

<dd>
<p>A <b>UCHAR</b> array that contains an IEEE 802.11 key confirmation key (KCK).</p>
</dd>

### -field <b>KEK</b>

<dd>
<p>A <b>UCHAR</b> array that contains an IEEE 802.11 key encryption key (KEK).</p>
</dd>

### -field <b>KeyReplayCounter</b>

<dd>
<p>A <b>ULONGLONG</b> value that contains a replay counter.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569763">OID_PM_ADD_PROTOCOL_OFFLOAD</a> and 
    <a href="netvista.oid_pm_protocol_offload_list">
    OID_PM_PROTOCOL_OFFLOAD_LIST</a> OIDs.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.20 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ntddndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-pm-counted-string.md">NDIS_PM_COUNTED_STRING</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis--ndis-pm-protocol-offload-type.md">NDIS_PM_PROTOCOL_OFFLOAD_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569763">OID_PM_ADD_PROTOCOL_OFFLOAD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569769">OID_PM_PROTOCOL_OFFLOAD_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_PROTOCOL_OFFLOAD structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
