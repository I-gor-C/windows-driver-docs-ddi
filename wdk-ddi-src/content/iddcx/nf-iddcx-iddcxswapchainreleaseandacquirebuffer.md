---
UID: NF.iddcx.IddCxSwapChainReleaseAndAcquireBuffer
title: IddCxSwapChainReleaseAndAcquireBuffer
author: windows-driver-content
description: An OS callback function the driver calls when it wants to release the current buffer in the swap chain and acquire a new one.
old-location: display\iddcxswapchainreleaseandacquirebuffer.htm
old-project: display
ms.assetid: f9b0cf3f-cbb6-4b44-81c1-b60ae525ec17
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IddCxSwapChainReleaseAndAcquireBuffer
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
req.alt-api: IddCxSwapChainReleaseAndAcquireBuffer
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

# IddCxSwapChainReleaseAndAcquireBuffer function



## -description
<p>

                An OS callback function the driver calls when it wants to release the current buffer in the swap chain and acquire a new one</p>


## -syntax

````
HRESULT IddCxSwapChainReleaseAndAcquireBuffer(
  _In_  IDDCX_SWAPCHAIN                    SwapChainObject,
  _Out_ IDARG_OUT_RELEASEANDACQUIREBUFFER* pOutArgs
);
````


## -parameters
<dl>

### -param <i>SwapChainObject</i> [in]

<dd>
<p>The swap-chain object passed to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt761861">EVT_IDD_CX_MONITOR_ASSIGN_SWAPCHAIN</a> call.</p>
</dd>

### -param <i>pOutArgs</i> [out]

<dd>
<p>Output arguments of function</p>
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