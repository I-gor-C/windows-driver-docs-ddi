---
UID: NF.d3dkmthk.D3DKMTCreateHwContext
title: D3DKMTCreateHwContext
author: windows-driver-content
description: Used to create a new hardware context.
old-location: display\d3dkmtcreatehwcontext.htm
old-project: display
ms.assetid: 147F46A9-1182-4480-8886-7C39F940EA7D
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTCreateHwContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTCreateHwContext
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

# D3DKMTCreateHwContext function



## -description
<p>Used to create a new hardware context.</p>


## -syntax

````
NTSTATUS D3DKMTCreateHwContext(
  _Inout_ D3DKMT_CREATEHWCONTEXT *createHwContext
);
````


## -parameters
<dl>

### -param createHwContext [in, out]

<dd>
<p>A structure holding the information needed to create a new hardware context.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if called successfully. </p>

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