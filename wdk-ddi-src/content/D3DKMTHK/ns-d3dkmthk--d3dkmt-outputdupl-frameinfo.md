---
UID: NS.d3dkmthk._D3DKMT_OUTPUTDUPL_FRAMEINFO
title: D3DKMT_OUTPUTDUPL_FRAMEINFO
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_frameinfo.htm
ms.assetid: e35389b2-52aa-4481-a5d7-6c45c795885f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTPUTDUPL_FRAMEINFO
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_OUTPUTDUPL_FRAMEINFO, D3DKMT_OUTPUTDUPL_FRAMEINFO
req.iface: 
---

# D3DKMT_OUTPUTDUPL_FRAMEINFO structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPL_FRAMEINFO {
  LARGE_INTEGER                      LastPresentTime;
  LARGE_INTEGER                      LastMouseUpdateTime;
  UINT                               AccumulatedFrames;
  BOOL                               RectsCoalesced;
  BOOL                               ProtectedContentMaskedOut;
  D3DKMT_OUTPUTDUPL_POINTER_POSITION PointerPosition;
  UINT                               TotalMetadataBufferSize;
  UINT                               PointerShapeBufferSize;
} D3DKMT_OUTPUTDUPL_FRAMEINFO;
````


## -struct-fields
<dl>

### -field <b>LastPresentTime</b>

<dd></dd>

### -field <b>LastMouseUpdateTime</b>

<dd></dd>

### -field <b>AccumulatedFrames</b>

<dd></dd>

### -field <b>RectsCoalesced</b>

<dd></dd>

### -field <b>ProtectedContentMaskedOut</b>

<dd></dd>

### -field <b>PointerPosition</b>

<dd></dd>

### -field <b>TotalMetadataBufferSize</b>

<dd></dd>

### -field <b>PointerShapeBufferSize</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>