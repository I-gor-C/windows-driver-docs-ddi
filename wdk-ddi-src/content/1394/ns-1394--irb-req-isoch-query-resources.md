---
UID: NS.1394._IRB_REQ_ISOCH_QUERY_RESOURCES
title: IRB_REQ_ISOCH_QUERY_RESOURCES
author: windows-driver-content
description: This structure contains the fields necessary to carry out a IsochQueryResources request.
old-location: ieee\irb_req_isoch_query_resources.htm
ms.assetid: B9CDFB62-32CF-497A-BF0F-1E4FBCA36E82
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_ISOCH_QUERY_RESOURCES
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
ms.keywords: IRB_REQ_ISOCH_QUERY_RESOURCES, IRB_REQ_ISOCH_QUERY_RESOURCES
---

# IRB_REQ_ISOCH_QUERY_RESOURCES structure



## -description
<p>This structure contains the fields necessary to carry out a IsochQueryResources request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_QUERY_RESOURCES {
  ULONG         fulSpeed;
  ULONG         BytesPerFrameAvailable;
  LARGE_INTEGER ChannelsAvailable;
} IRB_REQ_ISOCH_QUERY_RESOURCES;
````


## -struct-fields
<dl>

### -field <b>fulSpeed</b>

<dd>
<p>Specifies the speed flag to use in allocating bandwidth. The possible speed values are SPEED_FLAGS_xxx, where xxx is the approximate transfer rate in megabits per second. Existing hardware supports transfer rates of 100, 200, and 400 MBps.</p>
<table>
<tr>
<th>Transfer Rate</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_100</p>
</td>
<td>
<p>100 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_200</p>
</td>
<td>
<p>200 Mb/s</p>
</td>
</tr>
<tr>
<td>
<p>SPEED_FLAGS_400</p>
</td>
<td>
<p>400 Mb/s</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>BytesPerFrameAvailable</b>

<dd>
<p>On success, specifies the returned available bandwidth as expressed in bytes per isochronous frame. </p>
</dd>

### -field <b>ChannelsAvailable</b>

<dd>
<p>On success, points to a bitmap of available channels.</p>
<p> The highest order bit (bit 63) specifies channel 0, the next bit (bit 62) specifies channel 1, and so on.</p>
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