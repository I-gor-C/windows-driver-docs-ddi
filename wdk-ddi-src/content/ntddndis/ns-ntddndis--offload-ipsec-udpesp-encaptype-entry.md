---
UID: NS.ntddndis._OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY
title: OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY
author: windows-driver-content
description: The OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY structure specifies the UDP-ESP encapsulation type and destination port of a parser entry.
old-location: netvista\offload_ipsec_udpesp_encaptype_entry.htm
old-project: netvista
ms.assetid: a1e5ae2e-b183-4ccc-8413-1359c4e8a6bc
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY, OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY, *POFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY
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

# OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY structure



## -description
<p>The OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY structure specifies the UDP-ESP encapsulation type and
  destination port of a parser entry.</p>


## -syntax

````
typedef struct _OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY {
  UDP_ENCAP_TYPE UdpEncapType;
  USHORT         DstEncapPort;
} OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY, *POFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY;
````


## -struct-fields
<dl>

### -field <b>UdpEncapType</b>

<dd>
<p>The UDP-ESP encapsulation type for packets protected by the security associations (SAs) that are
     being offloaded:
     </p>
<p></p>
<dl>

### -field <a id="IPSEC_UDPESP_ENCAPTYPE_IKE"></a><a id="ipsec_udpesp_encaptype_ike"></a><b>IPSEC_UDPESP_ENCAPTYPE_IKE</b>

<dd>
<p>This value is reserved.</p>
</dd>

### -field <a id="IPSEC_UDPESP_E_NCAPTYPE_OTHER"></a><a id="ipsec_udpesp_e_ncaptype_other"></a><b>IPSEC_UDPESP_E\NCAPTYPE_OTHER</b>

<dd>
<p>UDP encapsulation for packets on port 4500. For more information, see 
       <a href="https://msdn.microsoft.com/86556307-d877-4ee6-bf7f-82160a0b9078">UDP-ESP Encapsulation
       Types</a>.</p>
</dd>
</dl>
</dd>

### -field <b>DstEncapPort</b>

<dd>
<p>For an inbound SA (Flags = OFFLOAD_INBOUND_SA), specifies the destination port that the NIC should
     look for in the UDP header of inbound packets that it processes on the SAs being offloaded. The NIC
     should ignore this member for an outbound SA (
     <b>Flags</b> = 
     <b>OFFLOAD_OUTBOUND_SA</b>). 
     <b>DstEncapPort</b> should always specify port 4500.</p>
</dd>
</dl>

## -remarks
<p>The OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY structure is used with the 
    <a href="..\ntddndis\ns-ntddndis--offload-ipsec-add-udpesp-sa.md">
    OFFLOAD_IPSEC_ADD_UDPESP_SA</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--offload-ipsec-add-udpesp-sa.md">OFFLOAD_IPSEC_ADD_UDPESP_SA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20OFFLOAD_IPSEC_UDPESP_ENCAPTYPE_ENTRY structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
