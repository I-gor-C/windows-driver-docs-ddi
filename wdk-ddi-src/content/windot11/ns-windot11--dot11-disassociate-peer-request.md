---
UID: NS.windot11._DOT11_DISASSOCIATE_PEER_REQUEST
title: DOT11_DISASSOCIATE_PEER_REQUEST
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_disassociate_peer_request.htm
old-project: netvista
ms.assetid: aa47c030-dcd4-451b-8a4b-03ac566bb394
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_DISASSOCIATE_PEER_REQUEST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating
   system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_DISASSOCIATE_PEER_REQUEST
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

# DOT11_DISASSOCIATE_PEER_REQUEST structure



## -description

## -syntax

````
typedef struct _DOT11_DISASSOCIATE_PEER_REQUEST {
  NDIS_OBJECT_HEADER Header;
  DOT11_MAC_ADDRESS  PeerMacAddr;
  USHORT             usReason;
} DOT11_DISASSOCIATE_PEER_REQUEST, *PDOT11_DISASSOCIATE_PEER_REQUEST;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_DISASSOCIATE_PEER_REQUEST structure. This member is
     formatted as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a>Type

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a>Revision

<dd>
<p>This member must be set to DOT11_DISASSOCIATE_PEER_REQUEST_REVISION_1.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a>Size

<dd>
<p>This member must be set to 
       <b>sizeof</b>(DOT11_DISASSOCIATE_PEER_REQUEST).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>PeerMacAddr</b>

<dd>
<p>The media access control (MAC) address of the peer station that the 802.11 station is to
     disassociate from. If 
     <b>PeerMacAddr</b> has a value of 0xFF, the 802.11 station must disassociate from all
     associated stations. When 
     <b>PeerMacAddr</b> is a unicast address, the 802.11 station must disassociate from a
     specific station.</p>
</dd>

### -field <b>usReason</b>

<dd>
<p>A USHORT value that specifies the reason code field in the disassociation frame that is sent by
     the 802.11 miniport driver.</p>
</dd>
</dl>

## -remarks
<p>This structure is used with 
    <a href="netvista.oid_dot11_disassociate_peer_request">
    OID_DOT11_DISASSOCIATE_PEER_REQUEST</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating
   system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.oid_dot11_disassociate_peer_request">
   OID_DOT11_DISASSOCIATE_PEER_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_DISASSOCIATE_PEER_REQUEST structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
