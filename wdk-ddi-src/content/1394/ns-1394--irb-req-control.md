---
UID: NS.1394._IRB_REQ_CONTROL
title: IRB_REQ_CONTROL
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 bus driver to carry out a control request.
old-location: ieee\irb_req_control.htm
old-project: IEEE
ms.assetid: F0ABD318-AC63-40D5-B94E-BD6FEA1A57AC
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: IRB_REQ_CONTROL, IRB_REQ_CONTROL
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
req.alt-api: IRB_REQ_CONTROL
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

# IRB_REQ_CONTROL structure



## -description
<p>This structure contains the fields necessary for the 1394 bus driver to carry out a control request.</p>


## -syntax

````
typedef struct _IRB_REQ_CONTROL {
  ULONG ulIoControlCode;
  PMDL  pInBuffer;
  ULONG ulInBufferLength;
  PMDL  pOutBuffer;
  ULONG ulOutBufferLength;
  ULONG BytesReturned;
} IRB_REQ_CONTROL;
````


## -struct-fields
<dl>

### -field ulIoControlCode

<dd>
<p>Specifies the control code used in this request. Vendors should make these control codes unique, so that they do not overlap.</p>
</dd>

### -field pInBuffer

<dd>
<p>Points to an MDL that describes the input buffer. The input buffer contains user-defined information.</p>
</dd>

### -field ulInBufferLength

<dd>
<p>Specifies the length of the input buffer.</p>
</dd>

### -field pOutBuffer

<dd>
<p>Points to an MDL that describes the output buffer. The output buffer contains user-defined information.</p>
</dd>

### -field ulOutBufferLength

<dd>
<p>Specifies the length of the output buffer.</p>
</dd>

### -field BytesReturned

<dd>
<p>Specifies the number of bytes returned.</p>
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