---
UID: NS.d3dkmthk._D3DKMT_CREATEHWCONTEXT
title: D3DKMT_CREATEHWCONTEXT
author: windows-driver-content
description: A structure holding information to create a hardware context.
old-location: display\d3dkmt_createhwcontext.htm
old-project: display
ms.assetid: 9B6EA552-B576-45F3-A0BD-7EB721638D7F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATEHWCONTEXT, D3DKMT_CREATEHWCONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATEHWCONTEXT
req.alt-loc: d3dkmthk.h
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
req.iface: 
---

# D3DKMT_CREATEHWCONTEXT structure



## -description
<p>A structure holding information to create a hardware context.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEHWCONTEXT {
  D3DKMT_HANDLE               hDevice;
  UINT                        NodeOrdinal;
  UINT                        EngineAffinity;
  D3DDDI_CREATEHWCONTEXTFLAGS Flags;
  UINT                        PrivateDriverDataSize;
  VOID                        * pPrivateDriverData;
  D3DKMT_HANDLE               hHwContext;
} D3DKMT_CREATEHWCONTEXT;
````


## -struct-fields
<dl>

### -field hDevice

<dd>
<p>Handle to the device owning this context.</p>
</dd>

### -field NodeOrdinal

<dd>
<p>Identifier for the node targetted by this context.
</p>
</dd>

### -field EngineAffinity

<dd>
<p>Engine affinity within the specified node.</p>
</dd>

### -field Flags

<dd>
<p>Context creation flags.
</p>
</dd>

### -field PrivateDriverDataSize

<dd>
<p>Size of private driver data.</p>
</dd>

### -field  pPrivateDriverData

<dd>
<p>Private driver data.</p>
</dd>

### -field hHwContext

<dd>
<p>Handle of the created context.</p>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>