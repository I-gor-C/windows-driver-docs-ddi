---
UID: NC.d3dumddi.PFND3DDDI_CREATEHWCONTEXTCB
title: PFND3DDDI_CREATEHWCONTEXTCB
author: windows-driver-content
description: A callback to create a new hardware context.
old-location: display\pfnd3dddi_createhwcontextcb.htm
old-project: display
ms.assetid: 989682F3-340E-4F64-BF2D-771D58066EB2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3DDDI_CREATEHWCONTEXTCB
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_CREATEHWCONTEXTCB callback



## -description
<p>A callback to create a new hardware context.</p>


## -prototype

````
_Check_return_ HRESULT APIENTRY CALLBACK PFND3DDDI_CREATEHWCONTEXTCB(
  _In_    HANDLE                          hDevice,
  _Inout_ D3DDDICB_CREATEHWCONTEXT *const createHwContext
);
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p>A handle to the device.</p>
</dd>

### -param createHwContext [in, out]

<dd>
<p>A pointer to the structure holding information on creating the hardware context.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The call was successfully completed.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h</dt>
</dl>
</td>
</tr>
</table>