---
UID: NS.iddcx.IDARG_IN_SETSWAPCHAIN~r1
title: IDARG_IN_SETSWAPCHAIN
author: windows-driver-content
description: Gives information used to set the indirect swapchain.
old-location: display\idarg_in_setswapchain.htm
old-project: display
ms.assetid: 5b3a4a43-e8d4-4edf-87f3-dd3e6bb7e9dc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_SETSWAPCHAIN,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDARG_IN_SETSWAPCHAIN
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDARG_IN_SETSWAPCHAIN structure



## -description
<p>
                 Gives information used to set the indirect swapchain.
             </p>


## -syntax

````
typedef struct IDARG_IN_SETSWAPCHAIN {
  IDDCX_SWAPCHAIN hSwapChain;
  HANDLE          hNextSurfaceAvailable;
  LUID            RenderAdapterLuid;
} IDARG_IN_SETSWAPCHAIN, *IDARG_IN_SETSWAPCHAIN;
````


## -struct-fields
<dl>

### -field <b>hSwapChain</b>

<dd>
<p>
                     [in] Handle to indirect swapchain that will be used to pass the desktop image to the driver for processing, transmission and display.</p>
</dd>

### -field <b>hNextSurfaceAvailable</b>

<dd>
<p>
                     [in] Handle to auto reset event that is signaled when the new image to encode is ready.</p>
</dd>

### -field <b>RenderAdapterLuid</b>

<dd>
<p>
                     [In] LUID of the adapter where the desktop image was rendered.</p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>