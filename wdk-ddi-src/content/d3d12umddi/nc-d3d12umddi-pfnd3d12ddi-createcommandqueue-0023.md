---
UID: NC.d3d12umddi.PFND3D12DDI_CREATECOMMANDQUEUE_0023
title: PFND3D12DDI_CREATECOMMANDQUEUE_0023
author: windows-driver-content
description: The pfnCreateCommandQueue callback function is used to create command queue.
old-location: display\pfnd3d12ddi_createcommandqueue_0023.htm
old-project: display
ms.assetid: 1DA52354-2338-4214-8489-B6BFCD6060FB
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnCreateCommandQueue
req.alt-loc: D3d12umddi.h
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

# PFND3D12DDI_CREATECOMMANDQUEUE_0023 callback



## -description
<p>The <i>pfnCreateCommandQueue</i> callback function is used to create command queue. </p>


## -prototype

````
PFND3D12DDI_CREATECOMMANDQUEUE_0023 pfnCreateCommandQueue;

HRESULT APIENTRY* pfnCreateCommandQueue(
             D3D12DDI_HDEVICE                    hDevice,
  _In_ const D3D12DDIARG_CREATECOMMANDQUEUE_0023 *CreateCommandQueue,
             D3D12DDI_HCOMMANDQUEUE              hDrvCommandQueue,
             D3D12DDI_HRTCOMMANDQUEUE            hRTCommandQueue
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> 

<dd>
<p>The handle of a device.</p>
</dd>

### -param <i>CreateCommandQueue</i> [in]

<dd>
<p>An argument used to create a command queue. </p>
</dd>

### -param <i>hDrvCommandQueue</i> 

<dd>
<p>The handle of a command queue.</p>
</dd>

### -param <i>hRTCommandQueue</i> 

<dd>
<p>The handle of the command queue for the driver to use when it calls back into the runtime.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>Access this callback function by using a device functions core structure, such as the <b>D3D12DDI_DEVICE_FUNCS_CORE_0003</b> structure.</p>

<p>Access this callback function by using a device functions core structure, such as the <b>D3D12DDI_DEVICE_FUNCS_CORE_0003</b> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>