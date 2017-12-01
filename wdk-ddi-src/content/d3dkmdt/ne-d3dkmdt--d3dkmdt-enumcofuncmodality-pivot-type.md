---
UID: NE.d3dkmdt._D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE
title: D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE
author: windows-driver-content
description: The D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE enumeration indicates the pivot type in a call to DxgkDdiEnumVidPnCofuncModality.
old-location: display\d3dkmdt_enumcofuncmodality_pivot_type.htm
old-project: display
ms.assetid: ba99936a-e76a-4a34-b7cd-762a8f15732c
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
req.alt-api: D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE
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

# D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE enumeration



## -description
<p>The D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE enumeration indicates the pivot type in a call to <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>.</p>


## -syntax

````
typedef enum _D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE { 
  D3DKMDT_EPT_UNINITIALIZED  = 0,
  D3DKMDT_EPT_VIDPNSOURCE    = 1,
  D3DKMDT_EPT_VIDPNTARGET    = 2,
  D3DKMDT_EPT_SCALING        = 3,
  D3DKMDT_EPT_ROTATION       = 4,
  D3DKMDT_EPT_NOPIVOT        = 5
} D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_EPT_UNINITIALIZED"></a><a id="d3dkmdt_ept_uninitialized"></a><b>D3DKMDT_EPT_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_EPT_VIDPNSOURCE"></a><a id="d3dkmdt_ept_vidpnsource"></a><b>D3DKMDT_EPT_VIDPNSOURCE</b>

<dd>
<p>Indicates that a video present source is the pivot of the enumeration.</p>
</dd>

### -field <a id="D3DKMDT_EPT_VIDPNTARGET"></a><a id="d3dkmdt_ept_vidpntarget"></a><b>D3DKMDT_EPT_VIDPNTARGET</b>

<dd>
<p>Indicates that a video present target is the pivot of the enumeration.</p>
</dd>

### -field <a id="D3DKMDT_EPT_SCALING"></a><a id="d3dkmdt_ept_scaling"></a><b>D3DKMDT_EPT_SCALING</b>

<dd>
<p>Indicates that the scaling transformation is the pivot of the enumeration.</p>
</dd>

### -field <a id="D3DKMDT_EPT_ROTATION"></a><a id="d3dkmdt_ept_rotation"></a><b>D3DKMDT_EPT_ROTATION</b>

<dd>
<p>Indicates that the rotatation transformation is the pivot of the enumeration.</p>
</dd>

### -field <a id="D3DKMDT_EPT_NOPIVOT"></a><a id="d3dkmdt_ept_nopivot"></a><b>D3DKMDT_EPT_NOPIVOT</b>

<dd>
<p>Indicates that the enumeration has no pivot.</p>
</dd>
</dl>

## -remarks
<p>The <b>EnumPivotType</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-enumvidpncofuncmodality.md">DXGKARG_ENUMVIDPNCOFUNCMODALITY</a> structure is a D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE value.</p>

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

## -see-also
<dl>
<dt>
<a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
