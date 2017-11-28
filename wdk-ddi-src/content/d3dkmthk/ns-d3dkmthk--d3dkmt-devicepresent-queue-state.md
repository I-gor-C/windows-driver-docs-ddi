---
UID: NS.d3dkmthk._D3DKMT_DEVICEPRESENT_QUEUE_STATE
title: D3DKMT_DEVICEPRESENT_QUEUE_STATE
author: windows-driver-content
description: A structure that holds information on the queue state of a hardware device.
old-location: display\d3dkmt_devicepresent_queue_state.htm
old-project: display
ms.assetid: 0DB9F0ED-D0A9-4A8A-8E27-BC50DEDB0BD5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_DEVICEPRESENT_QUEUE_STATE, D3DKMT_DEVICEPRESENT_QUEUE_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_DEVICEPRESENT_QUEUE_STATE
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
req.iface: 
---

# D3DKMT_DEVICEPRESENT_QUEUE_STATE structure



## -description
<p>A structure that holds information on the queue state of a hardware device.</p>


## -syntax

````
typedef struct _D3DKMT_DEVICEPRESENT_QUEUE_STATE {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  BOOLEAN                        bQueuedPresentLimitReached;
} D3DKMT_DEVICEPRESENT_QUEUE_STATE;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>Indicates the present source id.</p>
</dd>

### -field <b>bQueuedPresentLimitReached</b>

<dd>
<p>Indicates whether the queued present limit has been reached.</p>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>