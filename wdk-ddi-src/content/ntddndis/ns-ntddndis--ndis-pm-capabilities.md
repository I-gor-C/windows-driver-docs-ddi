---
UID: NS.ntddndis._NDIS_PM_CAPABILITIES
title: NDIS_PM_CAPABILITIES
author: windows-driver-content
description: The NDIS_PM_CAPABILITIES structure specifies power management capabilities of a network adapter.
old-location: netvista\ndis_pm_capabilities.htm
ms.assetid: 713c8ecc-e0a5-480a-9c53-e331aeaeb38e
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ntddndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PM_CAPABILITIES
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
ms.keywords: NDIS_PM_CAPABILITIES, NDIS_PM_CAPABILITIES, *PNDIS_PM_CAPABILITIES
req.iface: 
---

# NDIS_PM_CAPABILITIES structure



## -description
<p>The <b>NDIS_PM_CAPABILITIES</b> structure specifies power management capabilities of a network adapter.</p>


## -syntax

````
typedef struct _NDIS_PM_CAPABILITIES {
  NDIS_OBJECT_HEADER      Header;
  ULONG                   Flags;
  ULONG                   SupportedWoLPacketPatterns;
  ULONG                   NumTotalWoLPatterns;
  ULONG                   MaxWoLPatternSize;
  ULONG                   MaxWoLPatternOffset;
  ULONG                   MaxWoLPacketSaveBuffer;
  ULONG                   SupportedProtocolOffloads;
  ULONG                   NumArpOffloadIPv4Addresses;
  ULONG                   NumNSOffloadIPv6Addresses;
  NDIS_DEVICE_POWER_STATE MinMagicPacketWakeUp;
  NDIS_DEVICE_POWER_STATE MinPatternWakeUp;
  NDIS_DEVICE_POWER_STATE MinLinkChangeWakeUp;
#if (NDIS_SUPPORT_NDIS630)
  ULONG                   SupportedWakeUpEvents;
  ULONG                   MediaSpecificWakeUpEvents;
#endif 
} NDIS_PM_CAPABILITIES, *PNDIS_PM_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_PM_CAPABILITIES</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_PM_CAPABILITIES</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_PM_CAPABILITIES_REVISION_2"></a><a id="ndis_pm_capabilities_revision_2"></a>NDIS_PM_CAPABILITIES_REVISION_2

<dd>
<p>Added various changes for NDIS 6.30.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_PM_CAPABILITIES_REVISION_2.</p>
</dd>

### -field <a id="NDIS_PM_CAPABILITIES_REVISION_1"></a><a id="ndis_pm_capabilities_revision_1"></a>NDIS_PM_CAPABILITIES_REVISION_1

<dd>
<p>Original version for NDIS 6.20.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_PM_CAPABILITIES_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. For NDIS 6.20, this member is reserved for NDIS.</p>
<p>Starting with NDIS 6.30, the following flags are defined:</p>
<p></p>
<dl>

### -field <a id="NDIS_PM_WAKE_PACKET_INDICATION_SUPPORTED"></a><a id="ndis_pm_wake_packet_indication_supported"></a>NDIS_PM_WAKE_PACKET_INDICATION_SUPPORTED

<dd>
<p>If this flag is set, the network adapter must be able to save the received packet that caused the adapter to generate a wake-up event.</p>
<p>If this flag is set, the miniport driver must be able to do the following with this packet after the network adapter transitions to a full-power state:</p>
<ul>
<li>
<p>The miniport driver must be able to indicate the packet by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff563598">NdisMIndicateReceiveNetBufferLists</a>.

</p>
</li>
<li>
<p>The miniport driver must be able to issue an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439808">NDIS_STATUS_PM_WAKE_REASON</a> status indication and must pass the packet with the indication.

</p>
</li>
</ul>
<p>For more information about this power management capability, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439831">NDIS Wake Reason Status Indications</a>.</p>
</dd>

### -field <a id="NDIS_PM_SELECTIVE_SUSPEND_SUPPORTED"></a><a id="ndis_pm_selective_suspend_supported"></a>NDIS_PM_SELECTIVE_SUSPEND_SUPPORTED

<dd>
<p>If this flag is set, the miniport driver supports NDIS selective suspend for network adapters. </p>
<p>For more information about this power management capability, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451659">NDIS Selective Suspend</a>.</p>
</dd>
</dl>
</dd>

### -field <b>SupportedWoLPacketPatterns</b>

<dd>
<p>A ULONG value that contains a bitwise OR of flags that specify the wake-on-LAN (WOL) patterns that
     a network adapter supports. Miniport drivers use these flags to advertise packet based WOL patterns that a network adapter
     supports. 
     </p>
<p>For more information about this member, see the Remarks section. For more information about WOL
     patterns, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a>.</p>
<p></p>
<dl>

### -field <a id="NDIS_PM_WOL_BITMAP_PATTERN_SUPPORTED"></a><a id="ndis_pm_wol_bitmap_pattern_supported"></a>NDIS_PM_WOL_BITMAP_PATTERN_SUPPORTED

<dd>
<p>The network adapter can generate a wake-up event when it receives a packet that matches a
       configured bitmap pattern.</p>
</dd>

### -field <a id="NDIS_PM_WOL_MAGIC_PACKET_SUPPORTED"></a><a id="ndis_pm_wol_magic_packet_supported"></a>NDIS_PM_WOL_MAGIC_PACKET_SUPPORTED

<dd>
<p>The network adapter can generate a wake-up event when it receives a WOL magic packet. A 
       <i>magic packet</i> contains within its payload a string of six bytes with a value of 0xFF, followed
       immediately by 16 contiguous copies of the receiving network adapter's Ethernet address.</p>
</dd>

### -field <a id="NDIS_PM_WOL_IPV4_TCP_SYN_SUPPORTED"></a><a id="ndis_pm_wol_ipv4_tcp_syn_supported"></a>NDIS_PM_WOL_IPV4_TCP_SYN_SUPPORTED

<dd>
<p>The network adapter can generate a wake-up event when it receives an IPv4 TCP SYN packet.
       Remote hosts send TCP SYN packets to initiate a TCP connection to the local computer.</p>
</dd>

### -field <a id="NDIS_PM_WOL_IPV6_TCP_SYN_SUPPORTED"></a><a id="ndis_pm_wol_ipv6_tcp_syn_supported"></a>NDIS_PM_WOL_IPV6_TCP_SYN_SUPPORTED

<dd>
<p>The network adapter can generate a wake-up event when it receives an IPv6 TCP SYN
       packet.</p>
</dd>

### -field <a id="NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_SUPPORTED"></a><a id="ndis_pm_wol_ipv4_dest_addr_wildcard_supported"></a>NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_SUPPORTED

<dd>
<p>If this flag is set, the network adapter supports as 
        <i>wildcard values</i> any zero-filled, or 
        <i>unspecified</i>, values for IPv4 addresses and TCP/UDP ports in a WOL pattern.
        In this way, the wildcard value matches any IPv4 address and any port value of the incoming packet in
        the location that is specified by the WOL pattern.</p>
<p>When a network adapter supports an IPv4 based wake on LAN packet pattern, such as an IPv4 TCP SYN
        pattern, it must support the generation of a wake-up event if the IPv4 addresses and port values of
        the incoming packet match the ones that are specified in the wake-up pattern.</p>
<p>However, if the NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_SUPPORTED flag is set, the network adapter
        can also generate a wake-up event if the following pattern matching conditions are true:</p>
<ul>
<li>
<p>Any value from the incoming packet in the location that is specified by the WOL pattern is a match, if
          the WOL pattern for that location contains a wildcard value.</p>
</li>
<li>
<p>A value from the incoming packet in the location that is specified by the WOL pattern is a match if the
          WOL pattern for that location contains a nonzero value that equals the packet's value.</p>
</li>
</ul>
<p>The miniport driver must restrict wake-up events to the specified IPv4 addresses and ports unless
        an overlying driver enables this capability.</p>
<div class="alert"><b>Note</b>  Wildcard values that are enabled by this flag can include unspecified IPv4
        source and destination addresses, as well as unspecified source and destination ports.</div>
<div> </div>
</dd>

### -field <a id="NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_SUPPORTED"></a><a id="ndis_pm_wol_ipv6_dest_addr_wildcard_supported"></a>NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_SUPPORTED

<dd>
<p>If this flag is set, the network adapter supports as 
        <i>wildcard values</i> any zero-filled, or 
        <i>unspecified</i>, values for IPv6 addresses and TCP/UDP ports in a WOL pattern.
        In this way, the wildcard value matches any IPv6 address and any port value of the incoming packet in
        the location that is specified by the WOL pattern.</p>
<p>When a network adapter supports an IPv6 based wake on LAN packet pattern, such as an IPv6 TCP SYN
        pattern, it must support the generation of a wake-up event if the IPv6 addresses and port values of
        the incoming packet match the ones that are specified in the wake-up pattern.</p>
<p>However, if the NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_SUPPORTED flag is set, the network adapter
        can also generate a wake-up event if the following pattern matching conditions are true:</p>
<ul>
<li>
<p>Any value from the incoming packet in the location that is specified by the WOL pattern is a match, if
          the WOL pattern for that location contains a wildcard value.</p>
</li>
<li>
<p>A value from the incoming packet in the location that is specified by the WOL pattern is a match if the
          WOL pattern for that location contains a nonzero value that equals the packet's value.</p>
</li>
</ul>
<p>The miniport driver must restrict wake-up events to the specified IPv6 addresses and ports unless
        an overlying driver enables this capability.</p>
<div class="alert"><b>Note</b>  Wildcard values that are enabled by this flag can include unspecified IPv6
        source and destination addresses, as well as unspecified source and destination ports.</div>
<div> </div>
</dd>

### -field <a id="NDIS_PM_WOL_EAPOL_REQUEST_ID_MESSAGE_SUPPORTED"></a><a id="ndis_pm_wol_eapol_request_id_message_supported"></a>NDIS_PM_WOL_EAPOL_REQUEST_ID_MESSAGE_SUPPORTED

<dd>
<p>The network adapter can generate a wake-up event when it receives an EAPOL request identifier
       message.</p>
</dd>
</dl>
</dd>

### -field <b>NumTotalWoLPatterns</b>

<dd>
<p>A <b>ULONG</b> value that contains the total number of WOL patterns that a network adapter supports. This is the sum of "number of
      supported WOL protocol patterns" and "number of supported WOL bitmap patterns."</p>
<p>For example, if  your driver supports 8 flexible bitmap patterns, IPv4 TCP SYN (via preset filter), and magic packet, then you would report 9 in NumTotalWoLPatterns. (8 bitmaps + 1 IPv4 TCP SYN = 9)</p>
<div class="alert"><b>Note</b>  The total number of WOL patterns does not include the magic packet wake-up
      pattern.</div>
<div> </div>
<p>For more information about WOL
     protocol patterns, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a>.</p>
</dd>

### -field <b>MaxWoLPatternSize</b>

<dd>
<p>A ULONG value that contains the maximum number of bytes that can be compared with a
     pattern.</p>
</dd>

### -field <b>MaxWoLPatternOffset</b>

<dd>
<p>A ULONG value that contains the number of bytes in a packet that can be examined, starting at
     the beginning of the MAC header.</p>
</dd>

### -field <b>MaxWoLPacketSaveBuffer</b>

<dd>
<p>A ULONG value that contains the number of bytes of a WOL packet that a miniport driver can save to
     a buffer and indicate up the driver stack. This value must be less than or equal to the size, in bytes, of the maximum transmission unit (MTU)  for the network media. The driver reports the MTU size through OID query requests of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569598">OID_GEN_MAXIMUM_FRAME_SIZE</a>.</p>
<div class="alert"><b>Note</b>  This member is ignored in NDIS 6.20 and earlier versions of NDIS. Starting with NDIS 6.30, this member must contain a nonzero value if the NDIS_PM_WAKE_PACKET_INDICATION_SUPPORTED flag is set in the <b>Flags</b> member.</div>
<div> </div>
</dd>

### -field <b>SupportedProtocolOffloads</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags that specify the protocol offload features that
     a network adapter supports. Miniport drivers use these flags to report the low power protocol offload capabilities
     of a network adapter. 
     </p>
<p></p>
<dl>

### -field <a id="NDIS_PM_PROTOCOL_OFFLOAD_ARP_SUPPORTED"></a><a id="ndis_pm_protocol_offload_arp_supported"></a>NDIS_PM_PROTOCOL_OFFLOAD_ARP_SUPPORTED

<dd>
<p>If this bit is set, the network adapter can respond to IPv4 ARP packets while it is in a low
       power state
       </p>
<p>For more information about the ARP protocol, see RFC 826.</p>
</dd>

### -field <a id="NDIS_PM_PROTOCOL_OFFLOAD_NS_SUPPORTED"></a><a id="ndis_pm_protocol_offload_ns_supported"></a>NDIS_PM_PROTOCOL_OFFLOAD_NS_SUPPORTED

<dd>
<p>If this bit is set, the network adapter can respond to IPv6 Neighbor Solicitation (NS) packets
       while it is in a low power state. 
       </p>
<p>For more information about IPv6 NS messages, see <a href="http://go.microsoft.com/fwlink/p/?linkid=268370">RFC 4861</a>.</p>
</dd>

### -field <a id="NDIS_PM_PROTOCOL_OFFLOAD_80211_RSN_REKEY_SUPPORTED"></a><a id="ndis_pm_protocol_offload_80211_rsn_rekey_supported"></a>NDIS_PM_PROTOCOL_OFFLOAD_80211_RSN_REKEY_SUPPORTED

<dd>
<p>The network adapter can respond to IEEE 802.11i Robust Security Network (RSN) re-key requests
       while it is in a low power state.</p>
</dd>
</dl>
</dd>

### -field <b>NumArpOffloadIPv4Addresses</b>

<dd>
<p>A <b>ULONG</b> value that contains the number of IPv4 addresses that the adapter supports for ARP
     offload.</p>
</dd>

### -field <b>NumNSOffloadIPv6Addresses</b>

<dd>
<p>A <b>ULONG</b> value that contains the number of IPv6 NS offload requests that the adapter supports. This should be at least 2.</p>
<div class="alert"><b>Note</b>  Despite its name, the <b>NumNSOffloadIPv6Addresses</b> contains the number of supported requests, not addresses.</div>
<div> </div>
</dd>

### -field <b>MinMagicPacketWakeUp</b>

<dd>
<p>Specifies the lowest device power state from which a network adapter can signal a wake-up event on receipt of
     a magic packet. A 
     <i>magic packet</i> contains within its payload a string of six bytes with a value of 0xFF, followed
     immediately by 16 contiguous copies of the receiving network adapter's MAC address.
     </p>
<div class="alert"><b>Note</b>  Device power states are specified by a value of D<i>x</i>, where D0 is the highest device power state and D3 is the lowest device power state.</div>
<div> </div>
<p>The device power state is specified as one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/gg602135">NDIS_DEVICE_POWER_STATE</a> values:</p>
<p></p>
<dl>

### -field <a id="_________NdisDeviceStateUnspecified________"></a><a id="_________ndisdevicestateunspecified________"></a><a id="_________NDISDEVICESTATEUNSPECIFIED________"></a>
        NdisDeviceStateUnspecified
       

<dd>
<p>The network adapter does not support magic packet wake-ups.</p>
<div class="alert"><b>Note</b>  If the <b>MinMagicPacketWakeUp</b> member is set to this value, the NDIS_PM_WOL_MAGIC_PACKET_SUPPORTED flag must not be set in the <b>SupportedWoLPacketPatterns</b> member.</div>
<div> </div>
</dd>

### -field <a id="_________NdisDeviceStateD0________"></a><a id="_________ndisdevicestated0________"></a><a id="_________NDISDEVICESTATED0________"></a>
        NdisDeviceStateD0
       

<dd>
<p>The network adapter can signal a magic packet wake-up from device power state D0. Because D0 is the fully
       powered state, this does not cause a wake-up, but can be used as a run-time event.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.20, signaling a magic packet wake-up from NdisDeviceStateD0 is no longer supported.</div>
<div> </div>
</dd>

### -field <a id="_________NdisDeviceStateD1________"></a><a id="_________ndisdevicestated1________"></a><a id="_________NDISDEVICESTATED1________"></a>
        NdisDeviceStateD1
       

<dd>
<p>The network adapter can signal a magic packet wake-up from a device power state of D1.</p>
</dd>

### -field <a id="_________NdisDeviceStateD2________"></a><a id="_________ndisdevicestated2________"></a><a id="_________NDISDEVICESTATED2________"></a>
        NdisDeviceStateD2
       

<dd>
<p>The network adapter can signal a magic packet wake-up from a device state of D2.</p>
</dd>

### -field <a id="_________NdisDeviceStateD3________"></a><a id="_________ndisdevicestated3________"></a><a id="_________NDISDEVICESTATED3________"></a>
        NdisDeviceStateD3
       

<dd>
<p>The network adapter can signal a magic packet wake-up from a device power state  of D3.</p>
</dd>
</dl>
</dd>

### -field <b>MinPatternWakeUp</b>

<dd>
<p>Specifies the lowest device power state from which a network adapter can signal a wake-up event on receipt of
     a network frame that contains a pattern that is specified by the protocol driver. The power state is
     specified as one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/gg602135">NDIS_DEVICE_POWER_STATE</a> values:
     </p>
<p></p>
<dl>

### -field <a id="_________NdisDeviceStateUnspecified________"></a><a id="_________ndisdevicestateunspecified________"></a><a id="_________NDISDEVICESTATEUNSPECIFIED________"></a>
        NdisDeviceStateUnspecified
       

<dd>
<p>The network adapter does not support pattern-match wake-ups.</p>
<div class="alert"><b>Note</b>  If the <b>MinPatternWakeUp</b> member is set to this value, only the NDIS_PM_WOL_MAGIC_PACKET_SUPPORTED flag can be set in the <b>SupportedWoLPacketPatterns </b> member.</div>
<div> </div>
</dd>

### -field <a id="_________NdisDeviceStateD0________"></a><a id="_________ndisdevicestated0________"></a><a id="_________NDISDEVICESTATED0________"></a>
        NdisDeviceStateD0
       

<dd>
<p>The network adapter can signal a pattern-match wake-up from device power state D0. Because D0 is the fully
       powered state, this does not cause a wake-up but can be used as a run-time event.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.20, signaling a pattern-match wake-up from NdisDeviceStateD0 is no longer supported.</div>
<div> </div>
</dd>

### -field <a id="_________NdisDeviceStateD1________"></a><a id="_________ndisdevicestated1________"></a><a id="_________NDISDEVICESTATED1________"></a>
        NdisDeviceStateD1
       

<dd>
<p>The network adapter can signal a pattern-match wake-up from a device power state of D1.</p>
</dd>

### -field <a id="_________NdisDeviceStateD2________"></a><a id="_________ndisdevicestated2________"></a><a id="_________NDISDEVICESTATED2________"></a>
        NdisDeviceStateD2
       

<dd>
<p>The network adapter can signal a pattern-match wake-up from a device power state of D2.</p>
</dd>

### -field <a id="_________NdisDeviceStateD3________"></a><a id="_________ndisdevicestated3________"></a><a id="_________NDISDEVICESTATED3________"></a>
        NdisDeviceStateD3
       

<dd>
<p>The network adapter can signal a pattern-match wake-up from a device power state of D3.</p>
</dd>
</dl>
</dd>

### -field <b>MinLinkChangeWakeUp</b>

<dd>
<p>Starting with NDIS 6.20, this member specifies the lowest device power state from which a network adapter can signal a wake-up event when the link
     state changes from media disconnected to media connected. </p>
<p>Starting with NDIS 6.30, this member specifies the lowest device power state from which a network adapter can signal    wake-up events. These events are specified in the  <b>SupportedWakeUpEvents</b> member.</p>
<p>The power state is specified as one of the
     following <a href="https://msdn.microsoft.com/library/windows/hardware/gg602135">NDIS_DEVICE_POWER_STATE</a> values:
     </p>
<p></p>
<dl>

### -field <a id="_________NdisDeviceStateUnspecified________"></a><a id="_________ndisdevicestateunspecified________"></a><a id="_________NDISDEVICESTATEUNSPECIFIED________"></a>
        NdisDeviceStateUnspecified
       

<dd>
<p>The network adapter does not support link change wake-ups.</p>
<div class="alert"><b>Note</b>  If the <b>MinLinkChangeWakeUp</b> member is set to this value, the<b>SupportedWakeUpEvents</b> member must be set to zero.</div>
<div> </div>
</dd>

### -field <a id="_________NdisDeviceStateD0________"></a><a id="_________ndisdevicestated0________"></a><a id="_________NDISDEVICESTATED0________"></a>
        NdisDeviceStateD0
       

<dd>
<p>The network adapter can signal a link change wake-up from device power state D0. Because D0 is the fully
       powered state, this does not cause a wake-up but can be used as a run-time event.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.20, signaling a link change wake-up from NdisDeviceStateD0 is no longer supported.</div>
<div> </div>
</dd>

### -field <a id="_________NdisDeviceStateD1________"></a><a id="_________ndisdevicestated1________"></a><a id="_________NDISDEVICESTATED1________"></a>
        NdisDeviceStateD1
       

<dd>
<p>The network adapter can signal a link change wake-up from a device power state of D1.</p>
</dd>

### -field <a id="_________NdisDeviceStateD2________"></a><a id="_________ndisdevicestated2________"></a><a id="_________NDISDEVICESTATED2________"></a>
        NdisDeviceStateD2
       

<dd>
<p>The network adapter can signal a link change wake-up from a device power state of D2.</p>
</dd>

### -field <a id="_________NdisDeviceStateD3________"></a><a id="_________ndisdevicestated3________"></a><a id="_________NDISDEVICESTATED3________"></a>
        NdisDeviceStateD3
       

<dd>
<p>The network adapter can signal a link change wake-up from a device power state of D3.</p>
</dd>
</dl>
</dd>

### -field <b>SupportedWakeUpEvents</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. These flags specify the   media-independent wake-up events that a network adapter supports. 
     These events are not specific to media type.</p>
<p>Starting with NDIS 6.30, the following flags are defined:</p>
<p></p>
<dl>

### -field <a id="NDIS_PM_WAKE_ON_MEDIA_CONNECT_SUPPORTED"></a><a id="ndis_pm_wake_on_media_connect_supported"></a>NDIS_PM_WAKE_ON_MEDIA_CONNECT_SUPPORTED

<dd>
<p>If this flag is set, the network adapter can generate a wake-up event when it becomes connected to the networking interface.</p>
</dd>

### -field <a id="NDIS_PM_WAKE_ON_MEDIA_DISCONNECT_SUPPORTED"></a><a id="ndis_pm_wake_on_media_disconnect_supported"></a>NDIS_PM_WAKE_ON_MEDIA_DISCONNECT_SUPPORTED

<dd>
<p>If this flag is set, the network adapter can generate a wake-up event when it becomes disconnected to the networking interface.</p>
</dd>
</dl>
</dd>

### -field <b>MediaSpecificWakeUpEvents</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. These flags specify the media-specific wake-up events that a network adapter supports. 
     </p>
<p>Starting with NDIS 6.30, the following flags are defined:</p>
<p></p>
<dl>

### -field <a id="NDIS_WLAN_WAKE_ON_NLO_DISCOVERY_SUPPORTED"></a><a id="ndis_wlan_wake_on_nlo_discovery_supported"></a>NDIS_WLAN_WAKE_ON_NLO_DISCOVERY_SUPPORTED

<dd>
<p>If this flag is set, the 802.11 network adapter can generate a wake-up event if it detects a service set identifier (SSID) that was specified through a network list offload (NLO). </p>
<p>For more information about NLO, see <a href="NULL">Wi-Fi Network List Offload</a>.</p>
</dd>

### -field <a id="NDIS_WLAN_WAKE_ON_AP_ASSOCIATION_LOST_SUPPORTED"></a><a id="ndis_wlan_wake_on_ap_association_lost_supported"></a>NDIS_WLAN_WAKE_ON_AP_ASSOCIATION_LOST_SUPPORTED

<dd>
<p>If this flag is set, the 802.11 network adapter can generate a wake-up event if it disassociates with the access point (AP).</p>
</dd>

### -field <a id="NDIS_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR_SUPPORTED"></a><a id="ndis_wlan_wake_on_gtk_handshake_error_supported"></a>NDIS_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR_SUPPORTED

<dd>
<p>If this flag is set, the 802.11 network adapter can generate a wake-up event if it encounters an error during the IEEE 802.11i RSN group transient key (GTK) handshake with the AP.</p>
</dd>

### -field <a id="NDIS_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST_SUPPORTED"></a><a id="ndis_wlan_wake_on_4way_handshake_request_supported"></a>NDIS_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST_SUPPORTED

<dd>
<p>If this flag is set, the 802.11 network adapter can generate a wake-up event if it receives the first frame of the IEEE 802.11i RSN 4-way handshake with the AP. This handshake is performed when the adapter authenticates with the AP.</p>
</dd>

### -field <a id="NDIS_WWAN_WAKE_ON_REGISTER_STATE_SUPPORTED"></a><a id="ndis_wwan_wake_on_register_state_supported"></a>NDIS_WWAN_WAKE_ON_REGISTER_STATE_SUPPORTED

<dd>
<p>If this flag is set, the mobile broadband (MB) network adapter can generate a wake-up event if its registration state to the MB Service has changed.</p>
</dd>

### -field <a id="NDIS_WWAN_WAKE_ON_SMS_RECEIVE_SUPPORTED"></a><a id="ndis_wwan_wake_on_sms_receive_supported"></a>NDIS_WWAN_WAKE_ON_SMS_RECEIVE_SUPPORTED

<dd>
<p>If this flag is set, the MB network adapter can generate a wake-up event if the MB Service has to be notified about the receipt of a Short Message Service (SMS) message. The adapter generates this wake-up event either after the completion of a previously issued <a href="https://msdn.microsoft.com/library/windows/hardware/ff569839">OID_WWAN_SMS_READ</a> query request, or the arrival of a new class-0 (flash/alert) message from the network provider as an event notification.</p>
</dd>

### -field <a id="NDIS_WWAN_WAKE_ON_USSD_RECEIVE_SUPPORTED"></a><a id="ndis_wwan_wake_on_ussd_receive_supported"></a>NDIS_WWAN_WAKE_ON_USSD_RECEIVE_SUPPORTED

<dd>
<p>If this flag is set, the MB network adapter can generate a wake-up event if it receives an Unstructured Supplementary Service Data (USSD) message.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_PM_CAPABILITIES</b> structure is used in the 
    <b>PowerManagementCapabilitiesEx</b> member of the 
    <a href="https://msdn.microsoft.com/5423d073-02a5-468b-b91e-713ac67a5253">
    NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a> structures and in
    the 
    <a href="netvista.ndis_status_pm_capabilities_change">
    NDIS_STATUS_PM_CAPABILITIES_CHANGE</a> status indication.</p>

<p>During miniport initialization, the miniport driver initializes an <b>NDIS_PM_CAPABILITIES</b> structure with
    the power management capabilities of the network adapter hardware. The miniport driver then sets the 
    <b>PowerManagementCapabilitiesEx</b> member of the NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure to
    point to the initialized <b>NDIS_PM_CAPABILITIES</b> structure.</p>

<p>An overlying driver should not try to enable capabilities that a network adapter does not support. To
    allow an overlying driver to determine what capabilities a network adapter provides, NDIS provides the
    capabilities in the 
    <b>PowerManagementCapabilitiesEx</b> member of the NDIS_BIND_PARAMETERS structure.</p>

<p>The 
    <b>SupportedProtocolOffloads</b> member contains flags that specify the protocol offload features that a
    network adapter supports. The network adapter handles these protocols in a low power state. For example, if the network adapter hardware can
    handle IPv4 ARP packets for the driver stack while it is in a low power state, the miniport driver sets
    the NDIS_PM_PROTOCOL_OFFLOAD_ARP_SUPPORTED bit in 
    <b>SupportedProtocolOffloads</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564832">NDIS_BIND_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5423d073-02a5-468b-b91e-713ac67a5253">
   NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563598">NdisMIndicateReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563600">NdisMIndicateStatusEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a>
</dt>
<dt>
<a href="netvista.ndis_status_pm_capabilities_change">
   NDIS_STATUS_PM_CAPABILITIES_CHANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439808">NDIS_STATUS_PM_WAKE_REASON</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_CAPABILITIES structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
