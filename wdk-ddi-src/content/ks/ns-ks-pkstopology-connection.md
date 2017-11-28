---
UID: NS.ks.PKSTOPOLOGY_CONNECTION
title: PKSTOPOLOGY_CONNECTION
author: windows-driver-content
description: The KSTOPOLOGY_CONNECTION structure describes a single data-path connection inside a kernel streaming filter.
old-location: stream\kstopology_connection.htm
old-project: stream
ms.assetid: 604be66a-bec7-48db-b038-aaaf78043965
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSTOPOLOGY_CONNECTION, KSTOPOLOGY_CONNECTION, *PKSTOPOLOGY_CONNECTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSTOPOLOGY_CONNECTION
req.alt-loc: ks.h
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
---

# PKSTOPOLOGY_CONNECTION structure



## -description
<p>The KSTOPOLOGY_CONNECTION structure describes a single data-path connection inside a kernel streaming filter.</p>


## -syntax

````
typedef struct {
  ULONG FromNode;
  ULONG FromNodePin;
  ULONG ToNode;
  ULONG ToNodePin;
} KSTOPOLOGY_CONNECTION, *PKSTOPOLOGY_CONNECTION;
````


## -struct-fields
<dl>

### -field <b>FromNode</b>

<dd>
<p>Specifies the node ID of the node on the upstream end of the connection. If this end of the connection is an external pin on the filter -- not a logical pin on a node--set this member to the null node-ID value, KSFILTER_NODE.</p>
</dd>

### -field <b>FromNodePin</b>

<dd>
<p>Specifies the pin ID for the upstream end of the connection. If <b>FromNode </b>is KSFILTER_NODE, the pin on this end of the connection is an external pin on the filter. If not, the pin on this end is a logical pin on an internal node.</p>
</dd>

### -field <b>ToNode</b>

<dd>
<p>Specifies the node ID of the node on the downstream end of the connection. If this end of the connection is an external pin on the filter--not a logical pin on a node -- set this member to the null node-ID value, KSFILTER_NODE.</p>
</dd>

### -field <b>ToNodePin</b>

<dd>
<p>Specifies the pin ID for the downstream end of the connection. If <b>ToNode</b> is KSFILTER_NODE, the pin on this end of the connection is an external pin on the filter. If not, the pin on this end is a logical pin on an internal node.</p>
</dd>
</dl>

## -remarks
<p>KSTOPOLOGY_CONNECTION represents a single connection inside a filter, between either external pins, internal nodes, or an external pin and an internal node.</p>

<p>A streaming driver returns an array of KSTOPOLOGY_CONNECTION structures in response to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565802">KSPROPERTY_TOPOLOGY_CONNECTIONS</a> get-property request.</p>

<p>When representing a connection between two external pins, both <b>FromNode</b> and <b>ToNode</b> should be set to KSFILTER_NODE, and the <b>FromNodePin</b> and <b>ToNodePin</b> should be the pin type ID of the respective pins. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566584">KSPROPSETID_Pin</a> for a description of pin type IDs.)</p>

<p>Otherwise, <b>FromNodePin</b> or <b>ToNodePin</b> represent a logical incoming or outgoing pin for the connection. The logical pin numbers are used solely to describe a connection between nodes; they have no existence outside of the KSPROPERTY_TOPOLOGY_CONNECTIONS property.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537688">PCCONNECTION_DESCRIPTOR</a> structure name is an alias for KSTOPOLOGY_CONNECTION.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556501">BdaPropertyTemplateConnections</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537688">PCCONNECTION_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565802">KSPROPERTY_TOPOLOGY_CONNECTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566584">KSPROPSETID_Pin</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566598">KSPROPSETID_Topology</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSTOPOLOGY_CONNECTION structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
