---
UID: NS.1394._IRB_REQ_ISOCH_STOP
title: IRB_REQ_ISOCH_STOP
author: windows-driver-content
description: This structure contains the field necessary to carry out a IsochStop request.
old-location: ieee\irb_req_isoch_stop.htm
old-project: IEEE
ms.assetid: 1400FAC6-DD4E-4E8E-A0ED-C59B700F0672
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_ISOCH_STOP, IRB_REQ_ISOCH_STOP
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
req.alt-api: IRB_REQ_ISOCH_STOP
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

# IRB_REQ_ISOCH_STOP structure



## -description
<p>This structure contains the field necessary to carry out a IsochStop request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_STOP {
  HANDLE hResource;
  ULONG  fulFlags;
} IRB_REQ_ISOCH_STOP;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>Specifies the resource handle for the channel on which to stop isochronous operations. </p>
</dd>

### -field <b>fulFlags</b>

<dd>
<p>Reserved. Device drivers should set this member to zero.</p>
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