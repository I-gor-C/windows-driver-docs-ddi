---
UID: NS.windot11.DOT11_PRIVACY_EXEMPTION
title: DOT11_PRIVACY_EXEMPTION
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_privacy_exemption.htm
old-project: netvista
ms.assetid: ee4499d0-3275-419d-9ab2-89edd77e0374
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_PRIVACY_EXEMPTION, DOT11_PRIVACY_EXEMPTION, *PDOT11_PRIVACY_EXEMPTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_PRIVACY_EXEMPTION
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

# DOT11_PRIVACY_EXEMPTION structure



## -description

## -syntax

````
typedef struct DOT11_PRIVACY_EXEMPTION {
  USHORT usEtherType;
  USHORT usExemptionActionType;
  USHORT usExemptionPacketType;
} DOT11_PRIVACY_EXEMPTION, *PDOT11_PRIVACY_EXEMPTION;
````


## -struct-fields
<dl>

### -field <b>usEtherType</b>

<dd>
<p>The value of the IEEE EtherType in big-endian byte order.</p>
</dd>

### -field <b>usExemptionActionType</b>

<dd>
<p>The type of exemption for the specified EtherType. The following exemption types are defined:
     </p>
<p></p>
<dl>

### -field <a id="DOT11_EXEMPT_ALWAYS"></a><a id="dot11_exempt_always"></a>DOT11_EXEMPT_ALWAYS

<dd>
<p>The 802.11 station must discard the received packet if the Protected Frame subfield of the Frame
       Control field in the 802.11 MAC header is set to one.</p>
</dd>

### -field <a id="DOT11_EXEMPT_ON_KEY_MAPPING_KEY_UNAVAILABLE"></a><a id="dot11_exempt_on_key_mapping_key_unavailable"></a>DOT11_EXEMPT_ON_KEY_MAPPING_KEY_UNAVAILABLE

<dd>
<p>The 802.11 station must discard the received packet if a key-mapping key for the source MAC
       address is available and the Protected Frame subfield of the Frame Control field in the 802.11 MAC
       header is set to zero.</p>
</dd>
</dl>
</dd>

### -field <b>usExemptionPacketType</b>

<dd>
<p>The type of packet that the exemption for the specified EtherType applies to. The following packet
     types are defined:
     </p>
<p></p>
<dl>

### -field <a id="DOT11_EXEMPT_UNICAST"></a><a id="dot11_exempt_unicast"></a>DOT11_EXEMPT_UNICAST

<dd>
<p>Exempt only unicast packets.</p>
</dd>

### -field <a id="DOT11_EXEMPT_MULTICAST"></a><a id="dot11_exempt_multicast"></a>DOT11_EXEMPT_MULTICAST

<dd>
<p>Exempt only multicast or broadcast packets.</p>
</dd>

### -field <a id="DOT11_EXEMPT_BOTH"></a><a id="dot11_exempt_both"></a>DOT11_EXEMPT_BOTH

<dd>
<p>Exempt all packet types.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The 802.11 station's packet exemption list if configured through a set request of 
    <a href="netvista.oid_dot11_privacy_exemption_list">
    OID_DOT11_PRIVACY_EXEMPTION_LIST</a>. For each packet the 802.11 station receives, it will apply the
    decryption exemption specified by the list entry with a 
    <b>usEtherType</b> value that matches the EtherType of the packet.</p>

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
<a href="netvista.oid_dot11_privacy_exemption_list">
   OID_DOT11_PRIVACY_EXEMPTION_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_PRIVACY_EXEMPTION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
