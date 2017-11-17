---
UID: NS.windot11.DOT11_ENCAP_ENTRY
title: DOT11_ENCAP_ENTRY
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_encap_entry.htm
ms.assetid: d17547c5-47a3-4d10-b27f-6a3bbf7aad03
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_ENCAP_ENTRY
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
ms.keywords: DOT11_ENCAP_ENTRY, DOT11_ENCAP_ENTRY, *PDOT11_ENCAP_ENTRY
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_ENCAP_ENTRY structure



## -description

## -syntax

````
typedef struct DOT11_ENCAP_ENTRY {
  USHORT usEtherType;
  USHORT usEncapType;
} DOT11_ENCAP_ENTRY, *PDOT11_ENCAP_ENTRY;
````


## -struct-fields
<dl>

### -field <b>usEtherType</b>

<dd>
<p>The value of the IEEE EtherType in big-endian byte order. 
     </p>
<p>If the 
     <b>usEtherType</b> member is zero, the encapsulation that is specified by the 
     <b>usEncapType</b> member applies to all EtherType values. If the miniport driver sets 
     <b>usEtherType</b> to zero for an entry, it must be the only entry in the EtherType encapsulation
     list.</p>
</dd>

### -field <b>usEncapType</b>

<dd>
<p>The type of encapsulation that is performed on the EtherType specified by the 
     <b>usEtherType</b> member. The 
     <b>usEncapType</b> member can have one of the following values: 
     </p>
<p></p>
<dl>

### -field <a id="DOT11_ENCAP_RFC_1042"></a><a id="dot11_encap_rfc_1042"></a>DOT11_ENCAP_RFC_1042

<dd>
<p>The encapsulation that is defined through IETF RFC 1042.</p>
</dd>

### -field <a id="DOT11_ENCAP_802_IH"></a><a id="dot11_encap_802_ih"></a>DOT11_ENCAP_802_IH

<dd>
<p>The encapsulation that is defined through the IEEE 802.1h-1997 standard.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The miniport driver returns an encapsulation list when it makes an 
    <a href="netvista.ndis_status_dot11_association_completion">
    NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION</a> indication. The encapsulation list specified in the
    indication applies to the association with an access point (AP) in an infrastructure basic service set
    (BSS) network.</p>

<p>For more information about 802.11 packet payload encapsulation, see 
    <a href="NULL">802.11 Payload Encapsulation</a>.</p>

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
<a href="https://msdn.microsoft.com/770962e3-0339-46f8-a789-7c9bbf9e058f">
   DOT11_ASSOCIATION_COMPLETION_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_association_completion">
   NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_ENCAP_ENTRY structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
