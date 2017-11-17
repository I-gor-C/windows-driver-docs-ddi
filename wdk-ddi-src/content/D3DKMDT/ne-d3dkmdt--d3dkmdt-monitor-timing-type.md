---
UID: NE.d3dkmdt._D3DKMDT_MONITOR_TIMING_TYPE
title: D3DKMDT_MONITOR_TIMING_TYPE
author: windows-driver-content
description: The D3DKMDT_MONITOR_TIMING_TYPE enumeration is reserved for system use. Do not use it in your driver.
old-location: display\d3dkmdt_monitor_timing_type.htm
ms.assetid: fb8a2c29-f41b-4701-bbc2-f0a8e6dadc11
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_TIMING_TYPE
req.alt-loc: d3dkmdt.h
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# D3DKMDT_MONITOR_TIMING_TYPE enumeration



## -description
<p>The D3DKMDT_MONITOR_TIMING_TYPE enumeration is reserved for system use. Do not use it in your driver.</p>


## -syntax

````
typedef enum _D3DKMDT_MONITOR_TIMING_TYPE { 
  D3DKMDT_MTT_UNINITIALIZED          = 0,
  D3DKMDT_MTT_ESTABLISHED            = 1,
  D3DKMDT_MTT_STANDARD               = 2,
  D3DKMDT_MTT_EXTRASTANDARD          = 3,
  D3DKMDT_MTT_DETAILED               = 4,
  D3DKMDT_MTT_DEFAULTMONITORPROFILE  = 5,
  D3DKMDT_MTT_DRIVER                 = 6
} D3DKMDT_MONITOR_TIMING_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_MTT_UNINITIALIZED"></a><a id="d3dkmdt_mtt_uninitialized"></a><b>D3DKMDT_MTT_UNINITIALIZED</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="D3DKMDT_MTT_ESTABLISHED"></a><a id="d3dkmdt_mtt_established"></a><b>D3DKMDT_MTT_ESTABLISHED</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="D3DKMDT_MTT_STANDARD"></a><a id="d3dkmdt_mtt_standard"></a><b>D3DKMDT_MTT_STANDARD</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="D3DKMDT_MTT_EXTRASTANDARD"></a><a id="d3dkmdt_mtt_extrastandard"></a><b>D3DKMDT_MTT_EXTRASTANDARD</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="D3DKMDT_MTT_DETAILED"></a><a id="d3dkmdt_mtt_detailed"></a><b>D3DKMDT_MTT_DETAILED</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="D3DKMDT_MTT_DEFAULTMONITORPROFILE"></a><a id="d3dkmdt_mtt_defaultmonitorprofile"></a><b>D3DKMDT_MTT_DEFAULTMONITORPROFILE</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="D3DKMDT_MTT_DRIVER"></a><a id="d3dkmdt_mtt_driver"></a><b>D3DKMDT_MTT_DRIVER</b>

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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>