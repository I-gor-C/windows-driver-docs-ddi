---
UID: NF.iddcx.IddCxSwapChainGetDirtyRects
title: IddCxSwapChainGetDirtyRects
author: windows-driver-content
description: An OS callback function the driver calls when it wants retrieve the dirty rects for the current frame.
old-location: display\iddcxswapchaingetdirtyrects.htm
old-project: display
ms.assetid: 4ffe3c46-f729-4088-b69e-f39bc00f40a6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IddCxSwapChainGetDirtyRects
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IddCxSwapChainGetDirtyRects
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

# IddCxSwapChainGetDirtyRects function



## -description
<p>

                An OS callback function the driver calls when it wants retrieve the dirty rects for the current frame</p>


## -syntax

````
HRESULT IddCxSwapChainGetDirtyRects(
  _In_        IDDCX_SWAPCHAIN          SwapChainObject,
  _In_  const IDARG_IN_GETDIRTYRECTS*  pInArgs,
  _Out_       IDARG_OUT_GETDIRTYRECTS* pOutArgs
);
````


## -parameters
<dl>

### -param SwapChainObject [in]

<dd>
<p>The swap-chain object whose current frame is being queried.</p>
</dd>

### -param pInArgs [in]

<dd>
<p>Input arguments of the function</p>
</dd>

### -param pOutArgs [out]

<dd>
<p>Output  arguments of the function</p>
</dd>
</dl>

## -returns
<p>
(NTSTATUS) The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.
                    </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>_Must_inspect_result_</p>
</td>
</tr>
</table>