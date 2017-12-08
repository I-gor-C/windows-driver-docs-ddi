---
UID: NS.d3d10umddi.D3D10_DDI_BOX
title: D3D10_DDI_BOX
author: windows-driver-content
description: The D3D10_DDI_BOX structure describes a volume.
old-location: display\d3d10_ddi_box.htm
old-project: display
ms.assetid: b09ea915-070d-4ebb-a40d-d60add5df3d8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10_DDI_BOX, D3D10_DDI_BOX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_DDI_BOX
req.alt-loc: d3d10umddi.h
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

# D3D10_DDI_BOX structure



## -description
<p>The D3D10_DDI_BOX structure describes a volume.</p>


## -syntax

````
typedef struct D3D10_DDI_BOX {
  LONG left;
  LONG top;
  LONG front;
  LONG right;
  LONG bottom;
  LONG back;
} D3D10_DDI_BOX;
````


## -struct-fields
<dl>

### -field left

<dd>
<p>[in] The position of the left side of the box on the x-axis.</p>
</dd>

### -field top

<dd>
<p>[in] The position of the top of the box on the y-axis.</p>
</dd>

### -field front

<dd>
<p>
      [in] The position of the front of the box on the z-axis.
     </p>
</dd>

### -field right

<dd>
<p>[in] The position of the right side of the box on the x-axis. Note that the width of the volume equals the value in the <b>right</b> member minus the value in the <b>left</b> member (that is, width = right – left). </p>
</dd>

### -field bottom

<dd>
<p>[in] The position of the bottom of the box on the y-axis. Note that the height of the volume equals the value in the <b>bottom</b> member minus the value in the <b>top</b> member (that is, height = bottom – top). </p>
</dd>

### -field back

<dd>
<p>[in] The position of the back of the box on the z-axis. Note that the depth of the volume equals the value in the <b>back</b> member minus the value in the <b>front</b> member (that is, depth = back – front). </p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-resourcecopyregion.md">ResourceCopyRegion</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_BOX structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
