---
UID: NS.d3dumddi.D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS
title: D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS
author: windows-driver-content
description: Used by the user-mode display driver to specify a group of overlay plane capabilities.
old-location: display\d3dddi_multiplane_overlay_group_caps.htm
old-project: display
ms.assetid: 6909579F-5387-4A35-B65B-EF77CC50DCC4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS, D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS
req.alt-loc: D3dumddi.h
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

# D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS structure



## -description
<p>Used by the user-mode display driver to specify a group of overlay plane capabilities.</p>


## -syntax

````
typedef struct D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS {
  UINT  NumPlanes;
  float MaxStretchFactor;
  float MaxShrinkFactor;
  UINT  OverlayCaps;
} D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS;
````


## -struct-fields
<dl>

### -field <b>NumPlanes</b>

<dd>
<p>Specifies the number of overlay planes that are supported by the overlay planes within the capability group.</p>
</dd>

### -field <b>MaxStretchFactor</b>

<dd>
<p>Specifies the maximum stretch factor that is supported by the overlay planes within the capability group.</p>
<p>The stretch factor is the ratio of the final, stretched overlay plane size to the original size. For example, if the original overlay plane is 100 x 100 pixels, a value of 2.5 means that it can be stretched to 250 x 250 pixels.</p>
<p>It's not guaranteed that this stretch factor can be applied in all scenarios. For example, it might be possible to stretch only one overlay plane out of several using this factor.</p>
</dd>

### -field <b>MaxShrinkFactor</b>

<dd>
<p>Specifies the maximum shrink factor that is supported by the overlay planes within the capability group.</p>
<p>The shrink factor is the ratio of the final, shrunk overlay plane size to the original size. For example, if the original overlay plane is 100 x 100 pixels, a value of 0.25 means that it can be shrunk to 25 x 25 pixels.</p>
<p>It's not guaranteed that this shrink factor can be applied in all scenarios. For example, it might be possible to shrink only one overlay plane out of several using this factor.</p>
</dd>

### -field <b>OverlayCaps</b>

<dd>
<p>The overlay capabilities, given as a bitwise <b>OR</b> of values from the <a href="..\d3dumddi\ne-d3dumddi--d3dddi-multiplane-overlay-feature-caps.md">D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS</a> enumeration.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ne-d3dumddi--d3dddi-multiplane-overlay-feature-caps.md">D3DDDI_MULTIPLANE_OVERLAY_FEATURE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_MULTIPLANE_OVERLAY_GROUP_CAPS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
