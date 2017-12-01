---
UID: NE.dxgiddi.DXGI_DDI_MODE_SCALING
title: DXGI_DDI_MODE_SCALING
author: windows-driver-content
description: The DXGI_DDI_MODE_SCALING enumeration type contains values that identify the scaling support for a display.
old-location: display\dxgi_ddi_mode_scaling.htm
old-project: display
ms.assetid: dfe37343-18a6-46f2-b23f-52fc0ca2f800
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DxApiGetVersion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MODE_SCALING
req.alt-loc: dxgiddi.h
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

# DXGI_DDI_MODE_SCALING enumeration



## -description
<p>The DXGI_DDI_MODE_SCALING enumeration type contains values that identify the scaling support for a display.</p>


## -syntax

````
typedef enum DXGI_DDI_MODE_SCALING { 
  DXGI_DDI_MODE_SCALING_UNSPECIFIED  = 0,
  DXGI_DDI_MODE_SCALING_STRETCHED    = 1,
  DXGI_DDI_MODE_SCALING_CENTERED     = 2
} DXGI_DDI_MODE_SCALING;
````


## -enum-fields
<dl>

### -field <a id="DXGI_DDI_MODE_SCALING_UNSPECIFIED"></a><a id="dxgi_ddi_mode_scaling_unspecified"></a><b>DXGI_DDI_MODE_SCALING_UNSPECIFIED</b>

<dd>
<p>A DXGI_DDI_MODE_SCALING-typed variable has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="DXGI_DDI_MODE_SCALING_STRETCHED"></a><a id="dxgi_ddi_mode_scaling_stretched"></a><b>DXGI_DDI_MODE_SCALING_STRETCHED</b>

<dd>
<p>Stretched content can be displayed. </p>
</dd>

### -field <a id="DXGI_DDI_MODE_SCALING_CENTERED"></a><a id="dxgi_ddi_mode_scaling_centered"></a><b>DXGI_DDI_MODE_SCALING_CENTERED</b>

<dd>
<p>Centered content can be displayed. </p>
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
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-mode-desc.md">DXGI_DDI_MODE_DESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_MODE_SCALING enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
