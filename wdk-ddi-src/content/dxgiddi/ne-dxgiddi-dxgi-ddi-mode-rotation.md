---
UID: NE.dxgiddi.DXGI_DDI_MODE_ROTATION
title: DXGI_DDI_MODE_ROTATION
author: windows-driver-content
description: The DXGI_DDI_MODE_ROTATION enumeration type contains values that identify the orientation of the display.
old-location: display\dxgi_ddi_mode_rotation.htm
old-project: display
ms.assetid: 8cc413c4-e4fe-449b-a66a-c79da01ad3be
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
req.alt-api: DXGI_DDI_MODE_ROTATION
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

# DXGI_DDI_MODE_ROTATION enumeration



## -description
<p>The DXGI_DDI_MODE_ROTATION enumeration type contains values that identify the orientation of the display.</p>


## -syntax

````
typedef enum DXGI_DDI_MODE_ROTATION { 
  DXGI_DDI_MODE_ROTATION_UNSPECIFIED  = 0,
  DXGI_DDI_MODE_ROTATION_IDENTITY     = 1,
  DXGI_DDI_MODE_ROTATION_ROTATE90     = 2,
  DXGI_DDI_MODE_ROTATION_ROTATE180    = 3,
  DXGI_DDI_MODE_ROTATION_ROTATE270    = 4
} DXGI_DDI_MODE_ROTATION;
````


## -enum-fields
<dl>

### -field DXGI_DDI_MODE_ROTATION_UNSPECIFIED

<dd>
<p>A DXGI_DDI_MODE_ROTATION-typed variable has not yet been assigned a meaningful value.</p>
</dd>

### -field DXGI_DDI_MODE_ROTATION_IDENTITY

<dd>
<p>The display is not rotated.</p>
</dd>

### -field DXGI_DDI_MODE_ROTATION_ROTATE90

<dd>
<p>The display is rotated 90 degrees.</p>
</dd>

### -field DXGI_DDI_MODE_ROTATION_ROTATE180

<dd>
<p>The display is rotated 180 degrees.</p>
</dd>

### -field DXGI_DDI_MODE_ROTATION_ROTATE270

<dd>
<p>The display is rotated 270 degrees.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_MODE_ROTATION enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
