---
UID: NS.d3dkmddi._DXGK_INTERFACESPECIFICDATA
title: DXGK_INTERFACESPECIFICDATA
author: windows-driver-content
description: The DXGK_INTERFACESPECIFICDATA structure is reserved for system use. Do not use it in your driver.
old-location: display\dxgk_interfacespecificdata.htm
old-project: display
ms.assetid: dc9ad39c-4439-4e01-9825-fc1df3c3adc0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_INTERFACESPECIFICDATA, DXGK_INTERFACESPECIFICDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_INTERFACESPECIFICDATA
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_INTERFACESPECIFICDATA structure



## -description
<p>The DXGK_INTERFACESPECIFICDATA structure is reserved for system use. Do not use it in your driver.</p>


## -syntax

````
typedef struct _DXGK_INTERFACESPECIFICDATA {
  HANDLE                     hAdapter;
  DXGKCB_GETHANDLEDATA       pfnGetHandleDataCb;
  DXGKCB_GETHANDLEPARENT     pfnGetHandleParentCb;
  DXGKCB_ENUMHANDLECHILDREN  pfnEnumHandleChildrenCb;
  DXGKCB_NOTIFY_INTERRUPT    pfnNotifyInterruptCb;
  DXGKCB_NOTIFY_DPC          pfnNotifyDpcCb;
  DXGKCB_QUERYVIDPNINTERFACE pfnQueryVidPnInterfaceCb;
  DXGKCB_GETCAPTUREADDRESS   pfnGetCaptureAddressCb;
} DXGK_INTERFACESPECIFICDATA;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pfnGetHandleDataCb</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pfnGetHandleParentCb</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pfnEnumHandleChildrenCb</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pfnNotifyInterruptCb</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pfnNotifyDpcCb</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pfnQueryVidPnInterfaceCb</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pfnGetCaptureAddressCb</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>