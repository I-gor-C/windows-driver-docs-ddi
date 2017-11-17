---
UID: NC.d3dumddi.PFND3DDDI_DESTROYHWQUEUECB
title: PFND3DDDI_DESTROYHWQUEUECB
author: windows-driver-content
description: A callback to destroy a hardware queue.
old-location: display\pfnd3dddi_destroyhwqueuecb.htm
ms.assetid: F3578E0E-2249-4BC2-B776-E6356D523059
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
req.alt-api: PFND3DDDI_DESTROYHWQUEUECB
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

# PFND3DDDI_DESTROYHWQUEUECB callback



## -description
<p>A callback to destroy a hardware queue.</p>


## -prototype

````
_Check_return_ HRESULT APIENTRY CALLBACK PFND3DDDI_DESTROYHWQUEUECB(
  _In_ HANDLE                         hDevice,
  _In_ D3DDDICB_DESTROYHWQUEUE *const destroyHwQueue
);
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the device.</p>
</dd>

### -param <i>destroyHwQueue</i> [in]

<dd>
<p>A pointer to the structure holding information to destroy the hardware queue.</p>
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