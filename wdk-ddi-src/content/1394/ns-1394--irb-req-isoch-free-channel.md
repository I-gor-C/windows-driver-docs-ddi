---
UID: NS.1394._IRB_REQ_ISOCH_FREE_CHANNEL
title: IRB_REQ_ISOCH_FREE_CHANNEL
author: windows-driver-content
description: This structure contains the fields required to carry out a IsochFreeChannel request.
old-location: ieee\irb_req_isoch_free_channel.htm
old-project: IEEE
ms.assetid: 949D165B-1F42-40EA-B050-38847E14B968
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_ISOCH_FREE_CHANNEL, IRB_REQ_ISOCH_FREE_CHANNEL
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
req.alt-api: IRB_REQ_ISOCH_FREE_CHANNEL
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

# IRB_REQ_ISOCH_FREE_CHANNEL structure



## -description
<p>This structure contains the fields required to carry out a IsochFreeChannel request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_FREE_CHANNEL {
  ULONG nChannel;
} IRB_REQ_ISOCH_FREE_CHANNEL;
````


## -struct-fields
<dl>

### -field <b>nChannel</b>

<dd>
<p>Specifies which allocated channel to release.</p>
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