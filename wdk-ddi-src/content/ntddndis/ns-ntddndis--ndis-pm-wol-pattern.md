---
UID: NS.ntddndis._NDIS_PM_WOL_PATTERN
title: NDIS_PM_WOL_PATTERN
author: windows-driver-content
description: The NDIS_PM_WOL_PATTERN structure defines a wake-on-LAN (WOL) pattern.
old-location: netvista\ndis_pm_wol_pattern.htm
old-project: netvista
ms.assetid: 2ca1fdbe-efd3-4607-aab1-751e6d5d025b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_PM_WOL_PATTERN, NDIS_PM_WOL_PATTERN, *PNDIS_PM_WOL_PATTERN
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
req.alt-api: NDIS_PM_WOL_PATTERN
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

# NDIS_PM_WOL_PATTERN structure



## -description
<p>The <b>NDIS_PM_WOL_PATTERN</b> structure defines a wake-on-LAN (WOL) pattern.</p>


## -syntax

````
typedef struct _NDIS_PM_WOL_PATTERN {
  NDIS_OBJECT_HEADER     Header;
  ULONG                  Flags;
  ULONG                  Priority;
  NDIS_PM_WOL_PACKET     WoLPacketType;
  NDIS_PM_COUNTED_STRING FriendlyName;
  ULONG                  PatternId;
  ULONG                  NextWoLPatternOffset;
  union _WOL_PATTERN {
    struct _IPV4_TCP_SYN_WOL_PACKET_PARAMETERS {
      ULONG  Flags;
      UCHAR  IPv4SourceAddress[4];
      UCHAR  IPv4DestAddress[4];
      USHORT TCPSourcePortNumber;
      USHORT TCPDestPortNumber;
    } IPv4TcpSynParameters;
    struct _IPV6_TCP_SYN_WOL_PACKET_PARAMETERS {
      ULONG  Flags;
      UCHAR  IPv6SourceAddress[16];
      UCHAR  IPv6DestAddress[16];
      USHORT TCPSourcePortNumber;
      USHORT TCPDestPortNumber;
    } IPv6TcpSynParameters;
    struct _EAPOL_REQUEST_ID_MESSAGE_WOL_PACKET_PARAMETERS {
      ULONG Flags;
    } EapolRequestIdMessageParameters;
    struct _WOL_BITMAP_PATTERN {
      ULONG Flags;
      ULONG MaskOffset;
      ULONG MaskSize;
      ULONG PatternOffset;
      ULONG PatternSize;
    } WoLBitMapPattern;
  } WoLPattern;
} NDIS_PM_WOL_PATTERN, *PNDIS_PM_WOL_PATTERN;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the <b>NDIS_PM_WOL_PATTERN</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_PM_WOL_PATTERN</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field NDIS_PM_WOL_PATTERN_REVISION_2

<dd>
<p>Revisions made to  the <a href="..\ntddndis\ne-ntddndis--ndis-pm-wol-packet.md">NDIS_PM_WOL_PACKET</a> enumeration for NDIS 6.30.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_PM_WOL_PATTERN_REVISION_2.</p>
</dd>

### -field NDIS_PM_WOL_PATTERN_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_PM_WOL_PATTERN_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field Flags

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field Priority

<dd>
<p>A ULONG value that contains the priority of the WOL pattern. If an overlying driver adds a higher
     priority WOL pattern when there are no resources that are available for more WOL patterns, NDIS might remove a
     lower priority WOL pattern to free resources. Miniport drivers should ignore this member. A protocol
     driver can specify any priority that is within the predefined range. The following values are
     predefined:
     </p>
<p></p>
<dl>

### -field NDIS_PM_WOL_PRIORITY_LOWEST

<dd>
<p>Specifies the lowest priority WOL pattern.</p>
</dd>

### -field NDIS_PM_WOL_PRIORITY_NORMAL

<dd>
<p>Specifies a normal priority WOL pattern.</p>
</dd>

### -field NDIS_PM_WOL_PRIORITY_HIGHEST

<dd>
<p>Specifies the highest priority WOL pattern.</p>
</dd>
</dl>
</dd>

### -field WoLPacketType

<dd>
<p>An 
     <a href="..\ntddndis\ne-ntddndis--ndis-pm-wol-packet.md">NDIS_PM_WOL_PACKET</a> enumeration value that
     specifies the type of the WOL packet.</p>
</dd>

### -field FriendlyName

<dd>
<p>An 
     <a href="..\ntddndis\ns-ntddndis--ndis-pm-counted-string.md">NDIS_PM_COUNTED_STRING</a> structure
     that contains the user-readable description of the WOL packet.</p>
</dd>

### -field PatternId

<dd>
<p>A ULONG value that contains an NDIS-provided value that identifies the WOL pattern. Before NDIS
     sends the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569764">OID_PM_ADD_WOL_PATTERN</a> OID request down
     to the underlying NDIS drivers or completes the request to the overlying driver, NDIS sets 
     <b>PatternId</b> to a value that is unique among the WOL patterns on a network adapter.</p>
</dd>

### -field NextWoLPatternOffset

<dd>
<p>A ULONG value that contains an offset, in bytes. The 
     <b>NextWoLPatternOffset</b> member of each NDIS_PM_WOL_PATTERN structure in a list is set to the offset
     (from the beginning of the OID request 
     <b>InformationBuffer</b>) of the next NDIS_PM_WOL_PATTERN structure in the list. If 
     <b>NextWoLPatternOffset</b> is zero, the current structure is the last structure in the list.</p>
</dd>

### -field WoLPattern

<dd>
<p>A union that contains the following member structures.</p>
<dl>

### -field IPv4TcpSynParameters

<dd>
<p>A structure that contains IPv4 TCP SYN information. This structure contains the following
      members:</p>
<dl>

### -field Flags

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field IPv4SourceAddress

<dd>
<p>The IPv4 source address in the TCP SYN packet.</p>
</dd>

### -field IPv4DestAddress

<dd>
<p>The IPv4 destination address in the TCP SYN packet.</p>
</dd>

### -field TCPSourcePortNumber

<dd>
<p>The TCP source port number in the TCP SYN packet.</p>
</dd>

### -field TCPDestPortNumber

<dd>
<p>The TCP destination port number in the TCP SYN packet.</p>
</dd>
</dl>
</dd>

### -field IPv6TcpSynParameters

<dd>
<p>A structure that contains IPv6 TCP SYN information. This structure contains the following
      members:</p>
<dl>

### -field Flags

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field IPv6SourceAddress

<dd>
<p>The IPv6 source address in the TCP SYN packet.</p>
</dd>

### -field IPv6DestAddress

<dd>
<p>The IPv6 destination address in the TCP SYN packet.</p>
</dd>

### -field TCPSourcePortNumber

<dd>
<p>The TCP source port in the TCP SYN packet.</p>
</dd>

### -field TCPDestPortNumber

<dd>
<p>The TCP destination port in the TCP SYN packet.</p>
</dd>
</dl>
</dd>

### -field EapolRequestIdMessageParameters

<dd>
<p>A structure that contains 802.1X EAPOL request identity message parameters. This structure
      contains the following members:</p>
<dl>

### -field Flags

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>
</dl>
</dd>

### -field WoLBitMapPattern

<dd>
<p>A structure that specifies a WOL bitmap pattern. For more information about bitmap patterns, see
      the Remarks section. The structure has the following members:</p>
<dl>

### -field Flags

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field MaskOffset

<dd>
<p>The offset, in bytes, for a mask buffer from the beginning of the NDIS_PM_WOL_PATTERN
        structure.</p>
<p>The mask specifies which bytes in incoming packets should be matched against the bitmap pattern.
        Each bit in the bitmask corresponds to a byte in the pattern. If a bit is zero, the corresponding
        byte in the incoming packet should not be pattern-matched. If the bit is one, the network adapter compares the
        byte to the incoming packet with the byte specified in the pattern.</p>
</dd>

### -field MaskSize

<dd>
<p>The size, in bytes, of the mask.</p>
</dd>

### -field PatternOffset

<dd>
<p>The offset, in bytes, for a pattern buffer from the beginning of the NDIS_PM_WOL_PATTERN
       structure.</p>
</dd>

### -field PatternSize

<dd>
<p>The size, in bytes, of the pattern.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The NDIS_PM_WOL_PATTERN structure is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569764">OID_PM_ADD_WOL_PATTERN</a> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569772">OID_PM_WOL_PATTERN_LIST</a> OID
    requests.</p>

<p>An upper-layer driver can specify a generic WOL pattern with the 
    <b>WoLBitMapPattern</b> member. A bitmap pattern is specified as a sequence of
    bytes and a mask bitmap. Each bit in the mask corresponds to a byte in the pattern, and specifies whether
    the corresponding byte in the incoming packet should be matched against the corresponding byte in the
    pattern. If all the bytes compared by the network adapter match, the packet is a match and the network adapter should generate a
    wake-up event.</p>

<p>An upper-layer driver can specify a zero-filled, or 
    <i>unspecified</i>, IPv4 address and TCP port values in the 
    <b>IPv4TcpSynParameters</b> member structure. If the NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_ENABLED flag is
    set in the 
    <b>EnabledWoLPacketPatterns</b> member of the NDIS_PM_PARAMETERS, the network adapter must use the unspecified address
    or port value to match any source or destination IPv4 address or TCP port value in the IPv4 TCP SYN
    packet.</p>

<p>Similarly, an upper layer driver can specify an unspecified
     IPv6 address and TCP port values in the 
    <b>IPv6TcpSynParameters</b> member structure. If the NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_ENABLED flag is
    set in the 
    <b>EnabledWoLPacketPatterns</b> member of the NDIS_PM_PARAMETERS, the network adapter must use the unspecified address
    or port value to match any source or destination IPv6 address or TCP port value in the IPv4 TCP SYN
    packet.</p>

<p>The upper layer driver sets the NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_ENABLED and
    NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_ENABLED flags by issuing a set request of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569768">OID_PM_PARAMETERS</a> OID.</p>

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
<a href="..\ntddndis\ne-ntddndis--ndis-pm-wol-packet.md">NDIS_PM_WOL_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569764">OID_PM_ADD_WOL_PATTERN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569772">OID_PM_WOL_PATTERN_LIST</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-pm-counted-string.md">NDIS_PM_COUNTED_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_WOL_PATTERN structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
