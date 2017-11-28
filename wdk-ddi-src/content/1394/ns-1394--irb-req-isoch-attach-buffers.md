---
UID: NS.1394._IRB_REQ_ISOCH_ATTACH_BUFFERS
title: IRB_REQ_ISOCH_ATTACH_BUFFERS
author: windows-driver-content
description: This structure contains the fields required for the 1394 bus driver to carry out a IsochAttachBuffers request.
old-location: ieee\irb_req_isoch_attach_buffers.htm
old-project: IEEE
ms.assetid: 7EA6E82C-D803-48CD-9955-CF576BF978CA
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_ISOCH_ATTACH_BUFFERS, IRB_REQ_ISOCH_ATTACH_BUFFERS
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
req.alt-api: IRB_REQ_ISOCH_ATTACH_BUFFERS
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

# IRB_REQ_ISOCH_ATTACH_BUFFERS structure



## -description
<p>This structure contains the fields required for the 1394 bus driver to carry out a IsochAttachBuffers request.</p>


## -syntax

````
typedef struct _IRB_REQ_ISOCH_ATTACH_BUFFERS {
  HANDLE            hResource;
  ULONG             nNumberOfDescriptors;
  PISOCH_DESCRIPTOR pIsochDescriptor;
} IRB_REQ_ISOCH_ATTACH_BUFFERS;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>Specifies the resource handle to attach buffers to.</p>
</dd>

### -field <b>nNumberOfDescriptors</b>

<dd>
<p>Specifies the number of elements in the <b>pIsochDescriptor</b> array.</p>
</dd>

### -field <b>pIsochDescriptor</b>

<dd>
<p>Points to an array of ISOCH_DESCRIPTOR structures that describe the buffers to be attached, and the parameters that specify how each buffer is to be used.</p>
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