---
UID: NS.d3dumddi._D3DDDIARG_GENERATEMIPSUBLEVELS
title: D3DDDIARG_GENERATEMIPSUBLEVELS
author: windows-driver-content
description: The D3DDDIARG_GENERATEMIPSUBLEVELS structure describes how to generate the sublevels of a MIP-map texture.
old-location: display\d3dddiarg_generatemipsublevels.htm
ms.assetid: 19c08206-cde8-4ec2-bbd1-92eadeecdb90
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_GENERATEMIPSUBLEVELS
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDIARG_GENERATEMIPSUBLEVELS, D3DDDIARG_GENERATEMIPSUBLEVELS
req.iface: 
---

# D3DDDIARG_GENERATEMIPSUBLEVELS structure



## -description
<p>The D3DDDIARG_GENERATEMIPSUBLEVELS structure describes how to generate the sublevels of a MIP-map texture. </p>


## -syntax

````
typedef struct _D3DDDIARG_GENERATEMIPSUBLEVELS {
  HANDLE                  hResource;
  D3DDDITEXTUREFILTERTYPE Filter;
} D3DDDIARG_GENERATEMIPSUBLEVELS;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>[in] A handle to the MIP-map texture surface.</p>
</dd>

### -field <b>Filter</b>

<dd>
<p>[in] A D3DDDITEXTUREFILTERTYPE-typed value that indicates the texture magnification or minification filter type that is used in generating the sublevels of the MIP-map texture. This member can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DDDITEXF_NONE</p>
</td>
<td>
<p>MIP-map filtering is disabled.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDITEXF_POINT</p>
</td>
<td>
<p>Point filtering. The texel with coordinates that are nearest to the required pixel value is used. The texture filter to be used between MIP-map levels is nearest-point MIP-map filtering.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDITEXF_LINEAR</p>
</td>
<td>
<p>Bilinear-interpolation filtering. A weighted average of a 2x2 area of texels that surround the required pixel is used. The texture filter to use between MIP-map levels is trilinear MIP-map interpolation. </p>
</td>
</tr>
<tr>
<td>
<p>D3DDDITEXF_ANISOTROPIC</p>
</td>
<td>
<p>Anisotropic texture filtering. This filtering compensates for distortion that is caused by the difference in angle between the texture polygon and the plane of the screen.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDITEXF_PYRAMIDALQUAD</p>
</td>
<td>
<p>Four-sample tent filtering.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDITEXF_GAUSSIANQUAD</p>
</td>
<td>
<p>Four-sample Gaussian filtering.</p>
</td>
</tr>
</table>
<p> </p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/86567fc1-cf66-4709-a6e1-6b24408df963">GenerateMipSubLevels</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_GENERATEMIPSUBLEVELS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
