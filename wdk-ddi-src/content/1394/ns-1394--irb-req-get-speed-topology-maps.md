---
UID: NS.1394._IRB_REQ_GET_SPEED_TOPOLOGY_MAPS
title: IRB_REQ_GET_SPEED_TOPOLOGY_MAPS
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 bus driver to carry out a GetSpeedTopologyMaps request.
old-location: ieee\irb_req_get_speed_topology_maps.htm
old-project: IEEE
ms.assetid: 3238BDA7-9C85-405B-B731-DD230B0975F9
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_GET_SPEED_TOPOLOGY_MAPS, IRB_REQ_GET_SPEED_TOPOLOGY_MAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_GET_SPEED_TOPOLOGY_MAPS
req.alt-loc: 1394.h
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
---

# IRB_REQ_GET_SPEED_TOPOLOGY_MAPS structure



## -description
<p>This structure contains the fields necessary for the 1394 bus driver to carry out a GetSpeedTopologyMaps request. </p>


## -syntax

````
typedef struct _IRB_REQ_GET_SPEED_TOPOLOGY_MAPS {
  PSPEED_MAP    SpeedMap;
  PTOPOLOGY_MAP TopologyMap;
} IRB_REQ_GET_SPEED_TOPOLOGY_MAPS;
````


## -struct-fields
<dl>

### -field <b>SpeedMap</b>

<dd>
<p>Points to the SPEED_MAP structure of the bus. This member is filled on completion.</p>
</dd>

### -field <b>TopologyMap</b>

<dd>
<p>Points to the TOPOLOGY_MAP structure of the bus. The topology map will be in big-endian, irrespective of the byte order of the local node. This member is filled on completion.</p>
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
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>