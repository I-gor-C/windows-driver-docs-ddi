---
UID: NS.1394._IRB_REQ_ISOCH_ALLOCATE_CHANNEL
title: IRB_REQ_ISOCH_ALLOCATE_CHANNEL
author: windows-driver-content
description: This structure contains the fields necessary in order for the 1394 bus driver to carry out an IsochAllocateChannel request.
old-location: ieee\irb_req_isoch_allocate_channel.htm
ms.assetid: CE38C189-34C7-40FC-81BE-9688AC9A7420
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
req.alt-api: IRB_REQ_ISOCH_ALLOCATE_CHANNEL
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
ms.keywords: IRB_REQ_ISOCH_ALLOCATE_CHANNEL, IRB_REQ_ISOCH_ALLOCATE_CHANNEL
---

# IRB_REQ_ISOCH_ALLOCATE_CHANNEL structure



## -description
<p>This structure contains the fields necessary in order for the 1394 bus driver to carry out an IsochAllocateChannel request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_ALLOCATE_CHANNEL {
  ULONG         nRequestedChannel;
  ULONG         Channel;
  LARGE_INTEGER ChannelsAvailable;
} IRB_REQ_ISOCH_ALLOCATE_CHANNEL;
````


## -struct-fields
<dl>

### -field <b>nRequestedChannel</b>

<dd>
<p>Specifies the particular channel to allocate, or ISOCH_ANY_CHANNEL for an arbitrary channel. </p>
</dd>

### -field <b>Channel</b>

<dd>
<p>Specifies the channel allocated, if the request succeeds.</p>
</dd>

### -field <b>ChannelsAvailable</b>

<dd>
<p>A bitmap specifying the available channels. The highest order bit (bit 63) specifies channel 0, the next bit (bit 62) specifies channel 1, and so on.</p>
<div class="alert"><b>Note</b>  Drivers should not rely on this information  because another device may allocate or deallocate channels at any time. The bus driver fills in this member, even if the request fails.</div>
<div> </div>
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