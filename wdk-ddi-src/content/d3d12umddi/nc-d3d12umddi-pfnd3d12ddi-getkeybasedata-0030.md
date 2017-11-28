---
UID: NC.d3d12umddi.PFND3D12DDI_GETKEYBASEDATA_0030
title: PFND3D12DDI_GETKEYBASEDATA_0030
author: windows-driver-content
description: Used to get key base data.
old-location: display\pfnd3d12ddi_getkeybasedata_0030.htm
old-project: display
ms.assetid: D4F893E9-6B7B-4E35-A92F-B31FFD55A2C0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3D12DDI_GETKEYBASEDATA_0030
req.alt-loc: d3d12umddi.h
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

# PFND3D12DDI_GETKEYBASEDATA_0030 callback



## -description
<p>Used to get key base data.</p>


## -prototype

````
HRESULT APIENTRY* PFND3D12DDI_GETKEYBASEDATA_0030(
              D3D12DDI_HDEVICE             hDrvDevice,
              D3D12DDI_HCRYPTOSESSION_0030 hDrvCryptoSession,
  _In_  const VOID                         *pKeyInputData,
              UINT                         KeyInputDataSize,
  _Out_       VOID                         *pKeyBaseData,
              UINT                         KeyBaseDataSize
);
````


## -parameters
<dl>

### -param <i>hDrvDevice</i> 

<dd>
<p>The device being processed.</p>
</dd>

### -param <i>hDrvCryptoSession</i> 

<dd>
<p>The crypto session.</p>
</dd>

### -param <i>pKeyInputData</i> [in]

<dd>
<p>A pointer to key input data.</p>
</dd>

### -param <i>KeyInputDataSize</i> 

<dd>
<p>The size of the key input data.</p>
</dd>

### -param <i>pKeyBaseData</i> [out]

<dd>
<p>A pointer to key base data.</p>
</dd>

### -param <i>KeyBaseDataSize</i> 

<dd>
<p>The size of the key base data.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>