---
UID: NS.ntddndis._NDIS_PORT
title: NDIS_PORT
author: windows-driver-content
description: The NDIS_PORT structure specifies the characteristics of an NDIS port and a pointer to the next element in a linked list of ports.
old-location: netvista\ndis_port.htm
old-project: netvista
ms.assetid: aef1b7b2-73d3-49ad-a3f2-c06fa1f34839
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PORT,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PORT
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

# NDIS_PORT structure



## -description
<p>The NDIS_PORT structure specifies the characteristics of an NDIS port and a pointer to the next
  element in a linked list of ports.</p>


## -syntax

````
typedef struct _NDIS_PORT {
  PNDIS_PORT                Next;
  PVOID                     NdisReserved;
  PVOID                     MiniportReserved;
  PVOID                     ProtocolReserved;
  NDIS_PORT_CHARACTERISTICS PortCharacteristics;
} NDIS_PORT, *PNDIS_PORT;
````


## -struct-fields
<dl>

### -field <b>Next</b>

<dd>
<p>A pointer to the next port in the linked list of ports.</p>
</dd>

### -field <b>NdisReserved</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>MiniportReserved</b>

<dd>
<p>Reserved for miniport drivers.</p>
</dd>

### -field <b>ProtocolReserved</b>

<dd>
<p>Reserved for protocol drivers.</p>
</dd>

### -field <b>PortCharacteristics</b>

<dd>
<p>An 
     <a href="..\ntddndis\ns-ntddndis--ndis-port-characteristics.md">
     NDIS_PORT_CHARACTERISTICS</a> structure that specifies the characteristics of the port.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_PORT structure is used to create a linked list of ports. Such a linked list is used in port
    activation (<b>NetEventPortActivation</b>) Plug and Play (PnP) events.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
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
<a href="..\ntddndis\ns-ntddndis--ndis-port-characteristics.md">NDIS_PORT_CHARACTERISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PORT structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
