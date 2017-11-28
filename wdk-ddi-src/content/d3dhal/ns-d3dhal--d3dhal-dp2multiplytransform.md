---
UID: NS.d3dhal._D3DHAL_DP2MULTIPLYTRANSFORM
title: D3DHAL_DP2MULTIPLYTRANSFORM
author: windows-driver-content
description: DirectX 8.0 and later versions only. The D3DHAL_DP2MULTIPLYTRANSFORM structure is used to modify the transform matrix for D3dDrawPrimitives2.
old-location: display\d3dhal_dp2multiplytransform.htm
old-project: display
ms.assetid: 3c7c0d40-a51e-4656-b262-233f0af8db0f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2MULTIPLYTRANSFORM, D3DHAL_DP2MULTIPLYTRANSFORM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2MULTIPLYTRANSFORM
req.alt-loc: d3dhal.h
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

# D3DHAL_DP2MULTIPLYTRANSFORM structure



## -description
<p>
   DirectX 8.0 and later versions only.
   </p>
<p>The D3DHAL_DP2MULTIPLYTRANSFORM structure is used to modify the transform matrix for <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>.</p>


## -syntax

````
typedef struct _D3DHAL_DP2MULTIPLYTRANSFORM {
  D3DTRANSFORMSTATETYPE xfrmType;
  D3DMATRIX             matrix;
} D3DHAL_DP2MULTIPLYTRANSFORM, *LPD3DHAL_DP2MULTIPLYTRANSFORM;
````


## -struct-fields
<dl>

### -field <b>xfrmType</b>

<dd>
<p>Specifies the current transform being modified.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DTRANSFORMSTATE_PROJECTION</p>
</td>
<td>
<p>Specifies the current projection transformation.</p>
</td>
</tr>
<tr>
<td>
<p>D3DTRANSFORMSTATE_VIEW</p>
</td>
<td>
<p>Specifies the current view transformation.</p>
</td>
</tr>
<tr>
<td>
<p>D3DTRANSFORMSTATE_WORLD</p>
</td>
<td>
<p>Specifies the current world transformation.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>matrix</b>

<dd>
<p>Specifies the matrix used to modify the current transform.</p>
</dd>
</dl>

## -remarks
<p>This structure is used with hardware transform and lighting and is used by the Direct3D runtime to inform the driver about modifications to the various transformation matrices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545823">D3DHAL_DP2SETTRANSFORM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2MULTIPLYTRANSFORM structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
