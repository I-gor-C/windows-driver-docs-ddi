---
UID: NS.fwpsk.FWPS_PACKET_LIST_IPSEC_INFORMATION0_
title: FWPS_PACKET_LIST_IPSEC_INFORMATION0_
author: windows-driver-content
description: The FWPS_PACKET_LIST_IPSEC_INFORMATION0 structure defines IPsec information associated with a packet list.Note  FWPS_PACKET_LIST_IPSEC_INFORMATION0 is a specific version of FWPS_PACKET_LIST_IPSEC_INFORMATION.
old-location: netvista\fwps_packet_list_ipsec_information0.htm
old-project: netvista
ms.assetid: bd005dd9-887a-4323-9816-e4a3b96ca53d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FWPS_PACKET_LIST_IPSEC_INFORMATION0_, FWPS_PACKET_LIST_IPSEC_INFORMATION0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_PACKET_LIST_IPSEC_INFORMATION0
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
req.iface: 
---

# FWPS_PACKET_LIST_IPSEC_INFORMATION0_ structure



## -description
<p>The <b>FWPS_PACKET_LIST_IPSEC_INFORMATION0</b> structure defines IPsec information associated with a packet
  list.</p>


## -syntax

````
typedef struct FWPS_PACKET_LIST_IPSEC_INFORMATION0_ {
  union {
    FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0  inbound;
    FWPS_PACKET_LIST_OUTBOUND_IPSEC_INFORMATION0 outbound;
    UINT32                                       flags;
  };
} FWPS_PACKET_LIST_IPSEC_INFORMATION0;
````


## -struct-fields
<dl>

### -field <b>inbound</b>

<dd>
<p>An 
      <a href="netvista.fwps_packet_list_inbound_ipsec_information0">FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0</a> structure that contains IPsec information associated
      with inbound packet data.</p>
</dd>

### -field <b>outbound</b>

<dd>
<p>An 
      <a href="netvista.fwps_packet_list_outbound_ipsec_information0">FWPS_PACKET_LIST_OUTBOUND_IPSEC_INFORMATION0</a> structure that contains IPsec information associated
      with outbound packet data.</p>
</dd>

### -field <b>flags</b>

<dd>
<p>A value that contains a generic representation of the IPsec information associated with the
      packet list.</p>
</dd>
</dl>

## -remarks
<p>A FWPS_PACKET_LIST_IPSEC_INFORMATION0 structure is included as a member of the 
    <a href="netvista.fwps_packet_list_information0">
    FWPS_PACKET_LIST_INFORMATION0</a> structure.</p>

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
<a href="netvista.fwps_packet_list_inbound_ipsec_information0">
   FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0</a>
</dt>
<dt>
<a href="netvista.fwps_packet_list_information0">FWPS_PACKET_LIST_INFORMATION0</a>
</dt>
<dt>
<a href="netvista.fwps_packet_list_outbound_ipsec_information0">
   FWPS_PACKET_LIST_OUTBOUND_IPSEC_INFORMATION0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_PACKET_LIST_IPSEC_INFORMATION0 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
