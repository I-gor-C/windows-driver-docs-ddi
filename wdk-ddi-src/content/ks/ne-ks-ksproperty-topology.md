---
UID: NE.ks.KSPROPERTY_TOPOLOGY
title: KSPROPERTY_TOPOLOGY
author: windows-driver-content
description: .
old-location: stream\ksproperty_topology.htm
old-project: stream
ms.assetid: 9C000B4B-DB21-41E1-9AF0-D3B92EAC070B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_TOPOLOGY
req.alt-loc: Ks.h
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

# KSPROPERTY_TOPOLOGY enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_TOPOLOGY_CATEGORIES,
  KSPROPERTY_TOPOLOGY_NODES,
  KSPROPERTY_TOPOLOGY_CONNECTIONS,
  KSPROPERTY_TOPOLOGY_NAME
} KSPROPERTY_TOPOLOGY;
````


## -enum-fields
<dl>

### -field KSPROPERTY_TOPOLOGY_CATEGORIES

<dd>
<p>Specify to query for the array of functional categories that a driver supports.</p>
</dd>

### -field KSPROPERTY_TOPOLOGY_NODES

<dd>
<p>Specify for a list of the topology nodes and node types GUIDs supported by the filter.</p>
</dd>

### -field KSPROPERTY_TOPOLOGY_CONNECTIONS

<dd>
<p>Specify to query all connections between nodes of a KS filter.</p>
</dd>

### -field KSPROPERTY_TOPOLOGY_NAME

<dd>
<p>Specify to provide the localized Unicode string name of the node.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>