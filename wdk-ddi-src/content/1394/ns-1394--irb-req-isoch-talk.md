---
UID: NS.1394._IRB_REQ_ISOCH_TALK
title: IRB_REQ_ISOCH_TALK
author: windows-driver-content
description: This structure contains the field necessary to carry out a IsochTalk request.
old-location: ieee\irb_req_isoch_talk.htm
old-project: IEEE
ms.assetid: B42852F3-BF64-44F8-8D9C-361D623CE35A
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: IRB_REQ_ISOCH_TALK, IRB_REQ_ISOCH_TALK
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
req.alt-api: IRB_REQ_ISOCH_TALK
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

# IRB_REQ_ISOCH_TALK structure



## -description
<p>This structure contains the field necessary to carry out a IsochTalk request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_TALK {
  HANDLE     hResource;
  ULONG      fulFlags;
  CYCLE_TIME StartTime;
} IRB_REQ_ISOCH_TALK;
````


## -struct-fields
<dl>

### -field hResource

<dd>
<p>Specifies the resource handle to use for this operation. Resources are acquired through the REQUEST_ISOCH_ALLOCATE_RESOURCES request.</p>
</dd>

### -field fulFlags

<dd>
<p>Reserved. Drivers should set this to zero.</p>
</dd>

### -field StartTime

<dd>
<p>Specifies the cycle time to begin operation. This member is used only if the driver specified the RESOURCE_SYNCH_ON_TIME flag when it allocated the resource handle passed in <b>u.IsochTalk.hResource</b>. (The timing resolution is per isochronous cycle, so the <b>CycleOffset</b> member of <b>StartTime</b> is not used.)</p>
</dd>
</dl>

## -remarks
<p>Talking on a channel may begin immediately, or it may be synchronized to an event. If the driver set the RESOURCE_SYNCH_ON_TIME flag on the REQUEST_ISOCH_ALLOCATE_RESOURCES request that returned the resource handle, then the write operation begins on the specified cycle count. Additional synchronization options can be set for each buffer in the ISOCH_DESCRIPTOR structure.</p>

<p>If successful, the request returns a STATUS_SUCCESS value. The call returns immediately, and does not wait for any synchronization events. The bus driver calls the callback the driver provides in ISOCH_DESCRIPTOR to signal that it has finished processing an attached buffer.</p>

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