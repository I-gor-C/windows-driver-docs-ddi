---
UID: NS.1394._IRB_REQ_ISOCH_FREE_BANDWIDTH
title: IRB_REQ_ISOCH_FREE_BANDWIDTH
author: windows-driver-content
description: This structure contains the fields necessary in order for the Bus driver to carry out an IsochFreeBandwidth request.
old-location: ieee\irb_req_isoch_free_bandwidth.htm
ms.assetid: 1401F3B5-4F3F-47C1-88F9-96AFCCF2AA7E
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
req.alt-api: IRB_REQ_ISOCH_FREE_BANDWIDTH
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
ms.keywords: IRB_REQ_ISOCH_FREE_BANDWIDTH, IRB_REQ_ISOCH_FREE_BANDWIDTH
---

# IRB_REQ_ISOCH_FREE_BANDWIDTH structure



## -description
<p>This structure contains the fields necessary in order for the Bus driver to carry out an <b>IsochFreeBandwidth</b> request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_FREE_BANDWIDTH {
  HANDLE hBandwidth;
} IRB_REQ_ISOCH_FREE_BANDWIDTH;
````


## -struct-fields
<dl>

### -field <b>hBandwidth</b>

<dd>
<p>Specifies the bandwidth handle to release. </p>
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