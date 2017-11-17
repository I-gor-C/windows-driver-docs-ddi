---
UID: NF.iddcx.IddCxSwapChainGetMoveRegions
title: IddCxSwapChainGetMoveRegions
author: windows-driver-content
description: n OS callback function the driver calls when it wants retrieve the move regions for the current frame.
old-location: display\iddcxswapchaingetmoveregions.htm
ms.assetid: ae8257a6-4d4c-446e-b144-1adfe0a28e50
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IddCxSwapChainGetMoveRegions
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
ms.keywords: IddCxSwapChainGetMoveRegions
req.iface: 
---

# IddCxSwapChainGetMoveRegions function



## -description
<p>

                n OS callback function the driver calls when it wants retrieve the move regions for the current frame</p>


## -syntax

````
HRESULT IddCxSwapChainGetMoveRegions(
  _In_        IDDCX_SWAPCHAIN           SwapChainObject,
  _In_  const IDARG_IN_GETMOVEREGIONS*  pInArgs,
  _Out_       IDARG_OUT_GETMOVEREGIONS* pOutArgs
);
````


## -parameters
<dl>

### -param <i>SwapChainObject</i> [in]

<dd>
<p>The swap-chain object whose current frame is being queried.</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>Input arguments of the function</p>
</dd>

### -param <i>pOutArgs</i> [out]

<dd>
<p>Output arguments of the function</p>
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