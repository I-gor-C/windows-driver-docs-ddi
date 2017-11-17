---
UID: NS.vmbuskernelmodeclientlibapi._VMB_CHANNEL_STATE_CHANGE_CALLBACKS
title: VMB_CHANNEL_STATE_CHANGE_CALLBACKS
author: windows-driver-content
description: The VMB_CHANNEL_STATE_CHANGE_CALLBACKS structure contains callback functions that relate to the state changes for a channel.
old-location: netvista\vmb_channel_state_change_callbacks.htm
ms.assetid: 01A9A947-76F0-407C-8480-B2721A9A8A7B
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VMB_CHANNEL_STATE_CHANGE_CALLBACKS
req.alt-loc: VmbusKernelModeClientLibApi.h
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
ms.keywords: VMB_CHANNEL_STATE_CHANGE_CALLBACKS, VMB_CHANNEL_STATE_CHANGE_CALLBACKS, *PVMB_CHANNEL_STATE_CHANGE_CALLBACKS
req.iface: 
req.product: Windows 10 or later.
---

# VMB_CHANNEL_STATE_CHANGE_CALLBACKS structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VMB_CHANNEL_STATE_CHANGE_CALLBACKS</b> structure contains callback functions that relate to the state changes for a channel. </p>


## -syntax

````
typedef struct _VMB_CHANNEL_STATE_CHANGE_CALLBACKS {
  ULONG                        Version;
  ULONG                        Size;
  PFN_VMB_CHANNEL_OPENED       EvtChannelOpened;
  PFN_VMB_CHANNEL_CLOSED       EvtChannelClosed;
  PFN_VMB_CHANNEL_SUSPEND      EvtChannelSuspend;
  PFN_VMB_CHANNEL_STARTED      EvtChannelStarted;
  PFN_VMB_CHANNEL_POST_STARTED EvtChannelPostStarted;
} VMB_CHANNEL_STATE_CHANGE_CALLBACKS, *PVMB_CHANNEL_STATE_CHANGE_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Size of callbacks.</p>
</dd>

### -field <b>EvtChannelOpened</b>

<dd>
<p>The channel opened callback function.</p>
</dd>

### -field <b>EvtChannelClosed</b>

<dd>
<p>The channel closed callback function.</p>
</dd>

### -field <b>EvtChannelSuspend</b>

<dd>
<p>The channel suspended callback funciton. </p>
</dd>

### -field <b>EvtChannelStarted</b>

<dd>
<p>The channel started callback function. </p>
</dd>

### -field <b>EvtChannelPostStarted</b>

<dd>
<p>The channel post started callback function.</p>
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
<dt>VmbusKernelModeClientLibApi.h (include VmbusKernelModeClientLibApi.h)</dt>
</dl>
</td>
</tr>
</table>