---
UID: NE.d3dkmdt._D3DKMDT_GTFCOMPLIANCE
title: D3DKMDT_GTFCOMPLIANCE
author: windows-driver-content
description: The D3DKMDT_GTFCOMPLIANCE enumeration is reserved for system use. Do not use it in your driver.
old-location: display\d3dkmdt_gtfcompliance.htm
old-project: display
ms.assetid: f66bee69-206d-4e94-aca8-72f59569ab4a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_GTFCOMPLIANCE
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
req.iface: 
---

# D3DKMDT_GTFCOMPLIANCE enumeration



## -description
<p>The D3DKMDT_GTFCOMPLIANCE enumeration is reserved for system use. Do not use it in your driver.</p>


## -syntax

````
typedef enum _D3DKMDT_GTFCOMPLIANCE { 
  D3DKMDT_GTF_UNINITIALIZED  = 0,
  D3DKMDT_GTF_COMPLIANT      = 1,
  D3DKMDT_GTF_NOTCOMPLIANT   = 2
} D3DKMDT_GTFCOMPLIANCE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_GTF_UNINITIALIZED"></a><a id="d3dkmdt_gtf_uninitialized"></a><b>D3DKMDT_GTF_UNINITIALIZED</b>

<dd></dd>

### -field <a id="D3DKMDT_GTF_COMPLIANT"></a><a id="d3dkmdt_gtf_compliant"></a><b>D3DKMDT_GTF_COMPLIANT</b>

<dd></dd>

### -field <a id="D3DKMDT_GTF_NOTCOMPLIANT"></a><a id="d3dkmdt_gtf_notcompliant"></a><b>D3DKMDT_GTF_NOTCOMPLIANT</b>

<dd></dd>
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