---
UID: NC.d3dumddi.PFND3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATACB
title: PFND3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATACB
author: windows-driver-content
description: pfnGetResourcePresentPrivateDriverDataCb is used to query the resource private data, which is associated with the resource during Present.
old-location: display\pfngetresourcepresentprivatedriverdatacb.htm
old-project: display
ms.assetid: D4F0F272-60DC-4060-9762-3DB49236CE62
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnGetResourcePresentPrivateDriverDataCb
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
req.iface: 
---

# PFND3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATACB callback



## -description
<p><b>pfnGetResourcePresentPrivateDriverDataCb</b> is used to query the resource private data, which is associated with the resource during Present. 
</p>


## -prototype

````
PFND3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATACB pfnGetResourcePresentPrivateDriverDataCb;

HRESULT APIENTRY CALLBACK* pfnGetResourcePresentPrivateDriverDataCb(
  _In_    HANDLE                                     hDevice,
  _Inout_ D3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATA *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device.</p>
</dd>

### -param <i>pData</i> [in, out]

<dd>
<p>A pointer to a <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-getresourcepresentprivatedriverdata.md">D3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATA</a> structure that describes the operation to perform and contains the results.

</p>
</dd>
</dl>

## -returns
<dl>
<dt>S_OK</dt>
</dl><p>The operation completed successfully.</p><dl>
<dt>STATUS_INVALID_BUFFER_SIZE</dt>
</dl><p>The value of <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-getresourcepresentprivatedriverdata.md">D3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATA</a>::<b>PrivateDriverDataSize</b> was zero or was insufficient to hold the data. When control returns to the caller, <b>PrivateDriverDataSize</b> will contain the required buffer size.</p>

<p> </p>

<p>This method may return other <b>HRESULT</b> values.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>