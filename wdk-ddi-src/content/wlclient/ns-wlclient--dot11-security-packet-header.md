---
UID: NS.wlclient._DOT11_SECURITY_PACKET_HEADER
title: DOT11_SECURITY_PACKET_HEADER
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_security_packet_header.htm
old-project: netvista
ms.assetid: 3a880137-58a6-4b89-8384-a92c37f289a2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_SECURITY_PACKET_HEADER, DOT11_SECURITY_PACKET_HEADER, *PDOT11_SECURITY_PACKET_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wlclient.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_SECURITY_PACKET_HEADER
req.alt-loc: wlclient.h
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

# DOT11_SECURITY_PACKET_HEADER structure



## -description

## -syntax

````
typedef struct _DOT11_SECURITY_PACKET_HEADER {
  DOT11_MAC_ADDRESS PeerMac;
  USHORT            usEtherType;
  UCHAR             Data[1];
} DOT11_SECURITY_PACKET_HEADER, *PDOT11_SECURITY_PACKET_HEADER;
````


## -struct-fields
<dl>

### -field <b>PeerMac</b>

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff548681">DOT11_MAC_ADDRESS</a> type that defines the
     MAC address of the peer node.</p>
</dd>

### -field <b>usEtherType</b>

<dd>
<p>The value of the 
     <a href="netvista.ieee_ethertype_handling">IEEE EtherType</a> in big-endian byte
     order.</p>
</dd>

### -field <b>Data</b>

<dd>
<p>The contents of the security packet, excluding the 801.11 MAC header.</p>
</dd>
</dl>

## -remarks


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
<dt>Wlclient.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548681">DOT11_MAC_ADDRESS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_SECURITY_PACKET_HEADER structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
