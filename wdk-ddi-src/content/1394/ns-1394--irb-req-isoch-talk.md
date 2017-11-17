---
UID: NS.1394._IRB_REQ_ISOCH_TALK
title: IRB_REQ_ISOCH_TALK
author: windows-driver-content
description: This structure contains the field necessary to carry out a IsochTalk request.
old-location: ieee\irb_req_isoch_talk.htm
ms.assetid: B42852F3-BF64-44F8-8D9C-361D623CE35A
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
ms.keywords: IRB_REQ_ISOCH_TALK, IRB_REQ_ISOCH_TALK
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

### -field <b>hResource</b>

<dd>
<p>Specifies the resource handle to use for this operation. Resources are acquired through the REQUEST_ISOCH_ALLOCATE_RESOURCES request.</p>
</dd>

### -field <b>fulFlags</b>

<dd>
<p>Reserved. Drivers should set this to zero.</p>
</dd>

### -field <b>StartTime</b>

<dd>
<p>Specifies the cycle time to begin operation. This member is used only if the driver specified the RESOURCE_SYNCH_ON_TIME flag when it allocated the resource handle passed in <b>u.IsochTalk.hResource</b>. (The timing resolution is per isochronous cycle, so the <b>CycleOffset</b> member of <b>StartTime</b> is not used.)</p>
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