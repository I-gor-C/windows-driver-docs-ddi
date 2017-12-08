---
UID: NS.d3dkmdt._D3DKMDT_GAMMA_RAMP
title: D3DKMDT_GAMMA_RAMP
author: windows-driver-content
description: The D3DKMDT_GAMMA_RAMP structure contains descriptive information about a gamma lookup table and a pointer to the lookup table.
old-location: display\d3dkmdt_gamma_ramp.htm
old-project: display
ms.assetid: 3a875a1e-ef4f-4851-9329-f1fd2aca261f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_GAMMA_RAMP,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_GAMMA_RAMP
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
req.irql: 
req.iface: 
---

# D3DKMDT_GAMMA_RAMP structure



## -description
<p>The D3DKMDT_GAMMA_RAMP structure contains descriptive information about a gamma lookup table and a pointer to the lookup table.</p>


## -syntax

````
typedef struct _D3DKMDT_GAMMA_RAMP {
  D3DDDI_GAMMARAMP_TYPE Type;
  SIZE_T                DataSize;
  union {
    D3DDDI_GAMMA_RAMP_RGB256x3x16   *pRgb256x3x16;
    D3DDDI_GAMMA_RAMP_DXGI_1        *pDxgi1;
    D3DDDI_3x4_COLORSPACE_TRANSFORM *p3x4;
    VOID                            *pRaw;
  } Data;
} D3DKMDT_GAMMA_RAMP;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-gammaramp-type.md">D3DDDI_GAMMARAMP_TYPE</a> enumerator that specifies the format of the lookup table. </p>
</dd>

### -field DataSize

<dd>
<p>The size, in bytes, of the lookup table pointed to by <i>Data</i>.</p>
</dd>

### -field Data

<dd>
<p>[in] A union that contains one of the following ways to access the lookup table data depending on the value in the Type member:</p>
<dl>

### -field pRgb256x3x16

<dd>
<p>If <b>Type</b> is equal to D3DDDI_GAMMARAMP_RGB256x3x16, this member is a pointer to a <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-gamma-ramp-rgb256x3x16.md">D3DDDI_GAMMA_RAMP_RGB256x3x16</a> structure that contains the lookup table. </p>
</dd>

### -field pDxgi1

<dd>
<p>If <b>Type</b> is equal to D3DDDI_GAMMARAMP_DXGI_1, this member is a pointer to a <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-gamma-ramp-dxgi-1.md">D3DDDI_GAMMA_RAMP_DXGI_1</a> structure that contains the lookup table. </p>
</dd>

### -field p3x4

<dd>
<p>Pointer to a D3DDDI_3x4_COLORSPACE_TRANSFORM which describes the 3 by 4 matrix colorspace transform to be applied.</p>
</dd>

### -field pRaw

<dd>
<p>This member provides an alternative way to access the lookup table data. For example, for copying the lookup table, VOID* might be more convenient than D3DDDI_GAMMA_RAMP_RGB256x3x16.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>GammaRamp</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path.md">D3DKMDT_VIDPN_PRESENT_PATH</a> structure is a D3DKMDT_GAMMA_RAMP structure.</p>

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