---
UID: NC.d3dumddi.PFND3DDDI_CREATEHWQUEUECB
title: PFND3DDDI_CREATEHWQUEUECB
author: windows-driver-content
description: A callback to create a new hardware queue.
old-location: display\pfnd3dddi_createhwqueuecb.htm
ms.assetid: 1BA2E4DD-3E91-4D2E-AA90-9C85D53EE9E3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3DDDI_CREATEHWQUEUECB
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_CREATEHWQUEUECB callback



## -description
<p>A callback to create a new hardware queue</p>


## -prototype

````
_Check_return_ HRESULT APIENTRY CALLBACK PFND3DDDI_CREATEHWQUEUECB(
  _In_    HANDLE                        hDevice,
  _Inout_ D3DDDICB_CREATEHWQUEUE *const createHwQueue
);
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the device.</p>
</dd>

### -param <i>createHwQueue</i> [in, out]

<dd>
<p>A pointer to the structure holding information on creating the hardware queue.</p>
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