---
UID: NS.1394._IRB_REQ_ISOCH_DETACH_BUFFERS
title: IRB_REQ_ISOCH_DETACH_BUFFERS
author: windows-driver-content
description: This structure contains the fields required to carry out a IsochDetachBuffers request.
old-location: ieee\irb_req_isoch_detach_buffers.htm
old-project: IEEE
ms.assetid: 60ED83BD-4AFA-432F-B918-9006815C8D47
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: IRB_REQ_ISOCH_DETACH_BUFFERS, IRB_REQ_ISOCH_DETACH_BUFFERS
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
req.alt-api: IRB_REQ_ISOCH_DETACH_BUFFERS
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

# IRB_REQ_ISOCH_DETACH_BUFFERS structure



## -description
<p>This structure contains the fields required to carry out a IsochDetachBuffers request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_DETACH_BUFFERS {
  HANDLE            hResource;
  ULONG             nNumberOfDescriptors;
  PISOCH_DESCRIPTOR pIsochDescriptor;
} IRB_REQ_ISOCH_DETACH_BUFFERS;
````


## -struct-fields
<dl>

### -field hResource

<dd>
<p>Specifies the resource handle to detach buffers from.</p>
</dd>

### -field nNumberOfDescriptors

<dd>
<p>Specifies the number of elements in the <b>pIsochDescriptor</b> array.</p>
</dd>

### -field pIsochDescriptor

<dd>
<p>Points to an array of ISOCH_DESCRIPTOR structures that describe the buffers to be detached. The device driver should use the same ISOCH_DESCRIPTOR structure for a buffer that it used to attach the buffer.</p>
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