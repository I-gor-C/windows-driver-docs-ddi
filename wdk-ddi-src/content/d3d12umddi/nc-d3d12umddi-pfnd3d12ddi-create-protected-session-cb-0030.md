---
UID: NC.d3d12umddi.PFND3D12DDI_CREATE_PROTECTED_SESSION_CB_0030
title: PFND3D12DDI_CREATE_PROTECTED_SESSION_CB_0030
author: windows-driver-content
description: Used to create a protected session state.
old-location: display\pfnd3d12ddi_create_protected_session_cb_0030.htm
old-project: display
ms.assetid: 64E38759-2863-4481-8A89-6E6263CEFE8B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3D12DDI_CREATE_PROTECTED_SESSION_CB_0030
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

# PFND3D12DDI_CREATE_PROTECTED_SESSION_CB_0030 callback



## -description
<p>Used to create a protected session state.</p>


## -prototype

````
HRESULT APIENTRY CALLBACK* PFND3D12DDI_CREATE_PROTECTED_SESSION_CB_0030(
       D3D12DDI_HRTDEVICE                hRTDevice,
       D3D12DDI_HRTPROTECTEDSESSION_0030 hRTProtectedSession,
  _In_ pArgs                             *D3D12DDICB_CREATE_PROTECTED_RESOURCE_SESSION
);
````


## -parameters
<dl>

### -param <i>hRTDevice</i> 

<dd>
<p>The hardware device being processed.</p>
</dd>

### -param <i>hRTProtectedSession</i> 

<dd>
<p>The protected session.</p>
</dd>

### -param <i>D3D12DDICB_CREATE_PROTECTED_RESOURCE_SESSION</i> [in]

<dd>
<p>Used to create a protected resource session</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully.</p>

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
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>