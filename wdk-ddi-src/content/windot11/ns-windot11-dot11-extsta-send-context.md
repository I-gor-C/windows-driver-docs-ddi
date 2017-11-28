---
UID: NS.windot11.DOT11_EXTSTA_SEND_CONTEXT
title: DOT11_EXTSTA_SEND_CONTEXT
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_extsta_send_context.htm
old-project: netvista
ms.assetid: 0a4af7dc-0210-42b6-b15b-a0f885664da9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_EXTSTA_SEND_CONTEXT, DOT11_EXTSTA_SEND_CONTEXT, *PDOT11_EXTSTA_SEND_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_EXTSTA_SEND_CONTEXT
req.alt-loc: windot11.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_EXTSTA_SEND_CONTEXT structure



## -description

## -syntax

````
typedef struct DOT11_EXTSTA_SEND_CONTEXT {
  NDIS_OBJECT_HEADER Header;
  USHORT             usExemptionActionType;
  ULONG              uPhyId;
  ULONG              uDelayedSleepValue;
  PVOID              pvMediaSpecificInfo;
  ULONG              uSendFlags;
} DOT11_EXTSTA_SEND_CONTEXT, *PDOT11_EXTSTA_SEND_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_EXTSTA_SEND_CONTEXT structure. This member is formatted
     as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a><b>Type</b>

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a><b>Revision</b>

<dd>
<p>This member must be set to DOT11_EXTSTA_SEND_CONTEXT_REVISION_1.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a><b>Size</b>

<dd>
<p>This member must be set to 
       sizeof(DOT11_EXTSTA_SEND_CONTEXT).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>usExemptionActionType</b>

<dd>
<p>The type of encryption exemption for the packet. The following exemption types are defined:
     </p>
<p></p>
<dl>

### -field <a id="DOT11_EXEMPT_NO_EXEMPTION"></a><a id="dot11_exempt_no_exemption"></a>DOT11_EXEMPT_NO_EXEMPTION

<dd>
<p>The packet is not exempt from any cipher operations performed by the 802.11 station.</p>
</dd>

### -field <a id="DOT11_EXEMPT_ALWAYS"></a><a id="dot11_exempt_always"></a>DOT11_EXEMPT_ALWAYS

<dd>
<p>The packet is exempt from any cipher operations performed by the 802.11 station. The 802.11
       station must transmit the packet unencrypted.</p>
</dd>

### -field <a id="DOT11_EXEMPT_ON_KEY_MAPPING_KEY_UNAVAILABLE"></a><a id="dot11_exempt_on_key_mapping_key_unavailable"></a>DOT11_EXEMPT_ON_KEY_MAPPING_KEY_UNAVAILABLE

<dd>
<p>The packet is exempt from any cipher operations performed by the 802.11 station only if the
       station does not have a key-mapping key for the packet's destination media access control (MAC)
       address. For more information about key-mapping keys, see 
       <a href="NULL">802.11 Cipher Key Types</a>.</p>
</dd>
</dl>
</dd>

### -field <b>uPhyId</b>

<dd>
<p>The identifier (ID) of a PHY type on the 802.11 station. The 802.11 station must use the specified
     PHY to transmit the packet.
     </p>
<p>The value of 
     <b>uPhyId</b> must be one of the following:</p>
<ul>
<li>
<p>The value of an entry in the list of active PHY types defined by the 
       <b>msDot11ActivePhyList</b> MIB object. The miniport driver sets this MIB object to the list of PHYs
       that have been activated for use over the current basic service set (BSS) network connection. For more
       information about the 
       <b>msDot11ActivePhyList</b> MIB object, see 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff569102">OID_DOT11_ACTIVE_PHY_LIST</a>.</p>
</li>
<li>
<p>The value of DOT11_PHY_ID_ANY, in which case the 802.11 station can use any PHY from the list of
       active PHYs defined by the 
       <b>msDot11ActivePhyList</b> MIB object.</p>
</li>
</ul>
<p>The miniport driver must fail the send request if the PHY specified by 
     <b>uPhyId</b> is either not supported or has been disabled through a proprietary mechanism implemented by
     the independent hardware vendor (IHV). In this situation, the miniport driver sets the 
     <b>Status</b> member of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure to
     NDIS_STATUS_UNSUPPORTED_MEDIA and calls 
     <a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
     NdisMSendNetBufferListsComplete</a> to complete the send request.</p>
</dd>

### -field <b>uDelayedSleepValue</b>

<dd>
<p>The time, in microseconds, before a response to the packet is expected. The 
     <b>uDelayedSleepValue</b> member is only valid when all of the following are true:
     </p>
<ul>
<li>
<p>The packet is a media access control (MAC) service data unit (MSDU) packet.</p>
</li>
<li>
<p>The 802.11 station is operating in a power save (PS) mode. In this situation, the Extensible
       Station (ExtSTA) 
       <b>msDot11PowerSavingLevel</b> management information base (MIB) object has any value except
       DOT11_POWER_SAVING_NO_POWER_SAVING. For more information about the 
       <b>msDot11PowerSavingLevel</b> MIB value, see 
       <a href="netvista.oid_dot11_power_mgmt_request">
       OID_DOT11_POWER_MGMT_REQUEST</a>.</p>
</li>
</ul>
<p>The 802.11 station uses the value of 
     <b>uDelayedSleepValue</b> to optimize network performance while operating in a PS mode. For example,
     depending upon the PS mode, the 802.11 station might keep the radio turned on after the transmission of
     the packet if 
     <b>uDelayedSleepValue</b> is small. By doing so, the network latency will be reduced for receiving the
     response.</p>
</dd>

### -field <b>pvMediaSpecificInfo</b>

<dd>
<p>A pointer to a buffer that contains media-specific information. This member should be <b>NULL</b> when
     the 802.11 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that this
     structure is associated with comes from the native 802.11 framework itself (including any
     NET_BUFFER_LIST structures that come from an IHV extension).
     </p>
<p>Otherwise, 
     <b>pvMediaSpecificInfo</b> points to the out-of-band (OOB) data that is associated with the 
     <b>MediaSpecificInformation</b> entry at the 
     <b>NetBufferListInfo</b> member of the original 802.3 NET_BUFFER_LIST structure. 
     <b>pvMediaSpecificInfo</b> allows the miniport driver to access the media-specific information from an
     IHV-specific 802.3 protocol driver.</p>
</dd>

### -field <b>uSendFlags</b>

<dd>
<p>A set of flags that define send attributes. Currently, there are no flags defined. This member
     should be zero.</p>
</dd>
</dl>

## -remarks
<p>The miniport driver performs a send operation when its 
    <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
    MiniportSendNetBufferLists</a> is called. Each packet passed to the driver through this function is
    defined by a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure, which contains
    Native 802.11 out-of-band (OOB) data. The OOB data contains media-specific parameters that the 802.11
    station uses when transmitting the packet.</p>

<p>The miniport driver accesses the Native 802.11 OOB data through the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro with the
    following parameters:</p>

<p>The 
      <i>_NBL</i> parameter, which is passed the pointer to the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure used for the
      received 802.11 packet.</p>

<p>The _
      <i>id</i> parameter, which is passed the identifier (ID) value of 
      <b>MediaSpecificInformation</b>.</p>

<p>For more information about Native 802.11 send operations, see 
    <a href="netvista.native_802_11_send_operations">Native 802.11 Send
    Operations</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">MiniportSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
   NdisMSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569102">OID_DOT11_ACTIVE_PHY_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569402">OID_DOT11_POWER_MGMT_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_EXTSTA_SEND_CONTEXT structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
