---
UID: NF.iddcx.IddCxSwapChainSetDevice
title: IddCxSwapChainSetDevice
author: windows-driver-content
description: An OS callback function the driver calls within its SetSwapChain routine to setup the swap-chain with a particular DXGI device.
old-location: display\iddcxswapchainsetdevice.htm
ms.assetid: f1e96d8a-910e-4808-b9a3-e8c530158872
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
req.alt-api: IddCxSwapChainSetDevice
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
ms.keywords: IddCxSwapChainSetDevice
req.iface: 
---

# IddCxSwapChainSetDevice function



## -description
<p>An OS callback function the driver calls within its SetSwapChain routine to setup the swap-chain with a particular DXGI device.

                </p>


## -syntax

````
HRESULT IddCxSwapChainSetDevice(
  _In_ IDDCX_SWAPCHAIN              SwapChainObject,
  _In_ IDARG_IN_SWAPCHAINSETDEVICE* pInArgs
);
````


## -parameters
<dl>

### -param <i>SwapChainObject</i> [in]

<dd>
<p>The swap-chain object that will be setup with a particular DXGI device.</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>Input arguments to the function</p>
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