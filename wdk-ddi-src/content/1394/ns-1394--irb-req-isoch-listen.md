---
UID: NS.1394._IRB_REQ_ISOCH_LISTEN
title: IRB_REQ_ISOCH_LISTEN
author: windows-driver-content
description: This structure contains the fields necessary to carry out a ReqIsochListen request.
old-location: ieee\irb_req_isoch_listen.htm
old-project: IEEE
ms.assetid: 9B0590F4-E9B3-4999-99BD-BDB1EA413FF4
ms.author: windowsdriverdev
ms.date: 10/23/2017
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

### -field <b>hResource</b>

<dd>
<p>Specifies the resource handle to use in reading data.</p>
</dd>

### -field <b>fulFlags</b>

<dd>
<p>Reserved. Device drivers must set this to zero.</p>
</dd>

### -field <b>StartTime</b>

<dd>
<p>Specifies the cycle time to begin reading data. This member is used only if the driver specified the RESOURCE_SYNCH_ON_TIME flag when it allocated the resource handle passed in <b>u.IsochListen.hResource</b>. (The timing resolution is per isochronous cycle, so the <b>CycleOffset</b> member of <b>StartTime</b> is not used.)</p>
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