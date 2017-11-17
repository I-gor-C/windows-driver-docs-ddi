---
UID: NF.d3dkmthk.D3DKMTCreateHwQueue
title: D3DKMTCreateHwQueue
author: windows-driver-content
description: Used to create a new hardware queue.
old-location: display\d3dkmtcreatehwqueue.htm
ms.assetid: FD4E892F-DDC6-449A-B77F-6C7F8240E467
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTCreateHwQueue
req.alt-loc: d3dkmthk.h
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
ms.keywords: D3DKMTCreateHwQueue
req.iface: 
---

# D3DKMTCreateHwQueue function



## -description
<p>Used to create a new hardware queue.</p>


## -syntax

````
NTSTATUS APIENTRY D3DKMTCreateHwQueue(
  _Inout_ D3DKMT_CREATEHWQUEUE *createHwQueue
);
````


## -parameters
<dl>

### -param <i>createHwQueue</i> [in, out]

<dd>
<p>A structure holding the information needed to create a new hardware queue.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if called successfully. </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>