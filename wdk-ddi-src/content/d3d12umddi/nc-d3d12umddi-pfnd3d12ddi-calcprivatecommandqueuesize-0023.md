---
UID: NC.d3d12umddi.PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023
title: PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023
author: windows-driver-content
description: The pfnCalcPrivateCommandQueueSize callback function is used to calculate the size of a private command queue.
old-location: display\pfnd3d12ddi_calcprivatecommandqueuesize_0023.htm
old-project: display
ms.assetid: 70A81285-97CD-4526-8EB0-F00908B2D331
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
req.alt-api: pfnCalcPrivateCommandQueueSize
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

# PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023 callback



## -description
<p>The <i>pfnCalcPrivateCommandQueueSize</i> callback function is used to calculate the size of a private command queue. </p>


## -prototype

````
PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023 pfnCalcPrivateCommandQueueSize;

SIZE_T APIENTRY* pfnCalcPrivateCommandQueueSize(
             D3D12DDI_HDEVICE                    hDevice,
  _In_ const D3D12DDIARG_CREATECOMMANDQUEUE_0023 *CreateCommandQueue
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
</dl>

## -returns
<p>The size of the queue.</p>

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