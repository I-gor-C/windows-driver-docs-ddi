---
UID: NS.1394._IRB_REQ_ISOCH_LISTEN
title: IRB_REQ_ISOCH_LISTEN
author: windows-driver-content
description: This structure contains the fields necessary to carry out a ReqIsochListen request.
old-location: ieee\irb_req_isoch_listen.htm
old-project: IEEE
ms.assetid: 9B0590F4-E9B3-4999-99BD-BDB1EA413FF4
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: IRB_REQ_ISOCH_LISTEN, IRB_REQ_ISOCH_LISTEN
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
req.alt-api: IRB_REQ_ISOCH_LISTEN
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

# IRB_REQ_ISOCH_LISTEN structure



## -description
<p>This structure contains the fields necessary to carry out a ReqIsochListen request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_LISTEN {
  HANDLE     hResource;
  ULONG      fulFlags;
  CYCLE_TIME StartTime;
} IRB_REQ_ISOCH_LISTEN;
````


## -struct-fields
<dl>

### -field hResource

<dd>
<p>Specifies the resource handle to use in reading data.</p>
</dd>

### -field fulFlags

<dd>
<p>Reserved. Device drivers must set this to zero.</p>
</dd>

### -field StartTime

<dd>
<p>Specifies the cycle time to begin reading data. This member is used only if the driver specified the RESOURCE_SYNCH_ON_TIME flag when it allocated the resource handle passed in <b>u.IsochListen.hResource</b>. (The timing resolution is per isochronous cycle, so the <b>CycleOffset</b> member of <b>StartTime</b> is not used.)</p>
</dd>
</dl>

## -remarks
<p>The bus driver completes this request once it has successfully scheduled the isochronous listen operation. It does not wait for the data transfer to finish, or even begin, before it completes the request.</p>

<p>Listening on a channel may begin immediately, or it may be synchronized to an event. If the driver set the RESOURCE_SYNCH_ON_TIME flag on the REQUEST_ISOCH_ALLOCATE_RESOURCES request that returned the resource handle, then the listen begins on the cycle count specified in <b>StartTime</b>. Additional synchronization options may be set for each buffer within that buffer's ISOCH_DESCRIPTOR structure.</p>

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