---
UID: NS.fwpsk.FWPS_PACKET_LIST_INFORMATION0_
title: FWPS_PACKET_LIST_INFORMATION0_
author: windows-driver-content
description: The FWPS_PACKET_LIST_INFORMATION0 structure defines information associated with a packet list.Note  FWPS_PACKET_LIST_INFORMATION0 is a specific version of FWPS_PACKET_LIST_INFORMATION.
old-location: netvista\fwps_packet_list_information0.htm
ms.assetid: 1fc6ffb1-c6e9-4bca-9d10-541708fe0086
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_PACKET_LIST_INFORMATION0
req.alt-loc: fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FWPS_PACKET_LIST_INFORMATION0_, FWPS_PACKET_LIST_INFORMATION0
req.iface: 
---

# FWPS_PACKET_LIST_INFORMATION0_ structure



## -description
<p>The <b>FWPS_PACKET_LIST_INFORMATION0</b> structure defines information associated with a packet list.</p>


## -syntax

````
typedef struct FWPS_PACKET_LIST_INFORMATION0_ {
  FWPS_PACKET_LIST_IPSEC_INFORMATION0 ipsecInformation;
  FWPS_PACKET_LIST_FWP_INFORMATION0   fwpInformation;
} FWPS_PACKET_LIST_INFORMATION0;
````


## -struct-fields
<dl>

### -field <b>ipsecInformation</b>

<dd>
<p>An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552414">FWPS_PACKET_LIST_IPSEC_INFORMATION0</a> structure that contains IPsec information associated with the
     packet list.</p>
</dd>

### -field <b>fwpInformation</b>

<dd>
<p>An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552410">FWPS_PACKET_LIST_FWP_INFORMATION0</a> structure that contains Windows Filtering Platform information
     associated with the packet list.</p>
</dd>
</dl>

## -remarks
<p>A callout driver passes a pointer to an FWPS_PACKET_LIST_INFORMATION0 structure to the 
    <a href="https://msdn.microsoft.com/c3391615-963b-4916-9280-ce782269692c">
    FwpsGetPacketListSecurityInformation0</a> function when querying information associated with a packet
    list.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/c3391615-963b-4916-9280-ce782269692c">
   FwpsGetPacketListSecurityInformation0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e2d3faf3-cd3b-4147-8ceb-5b3f0c257939">
   FWPS_PACKET_LIST_FWP_INFORMATION0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/bd005dd9-887a-4323-9816-e4a3b96ca53d">
   FWPS_PACKET_LIST_IPSEC_INFORMATION0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_PACKET_LIST_INFORMATION0 structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
