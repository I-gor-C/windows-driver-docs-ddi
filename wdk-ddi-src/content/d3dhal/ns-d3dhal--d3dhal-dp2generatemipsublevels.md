---
UID: NS.d3dhal._D3DHAL_DP2GENERATEMIPSUBLEVELS
title: D3DHAL_DP2GENERATEMIPSUBLEVELS
author: windows-driver-content
description: DirectX 9.0 and later versions only. The D3DHAL_DP2GENERATEMIPSUBLEVELS structure is used to inform the driver to automatically generate the sublevels of a given MIP-map texture using a given filter type.
old-location: display\d3dhal_dp2generatemipsublevels.htm
ms.assetid: 7952cf0f-8a05-4d82-9669-db3db504d22d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2GENERATEMIPSUBLEVELS
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
ms.keywords: D3DHAL_DP2GENERATEMIPSUBLEVELS, D3DHAL_DP2GENERATEMIPSUBLEVELS
req.iface: 
---

# D3DHAL_DP2GENERATEMIPSUBLEVELS structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>The D3DHAL_DP2GENERATEMIPSUBLEVELS structure is used to inform the driver to automatically generate the sublevels of a given MIP-map texture using a given filter type.</p>


## -syntax

````
typedef struct _D3DHAL_DP2GENERATEMIPSUBLEVELS {
  DWORD                hSurface;
  D3DTEXTUREFILTERTYPE Filter;
} D3DHAL_DP2GENERATEMIPSUBLEVELS, *LPD3DHAL_DP2GENERATEMIPSUBLEVELS;
````


## -struct-fields
<dl>

### -field <b>hSurface</b>

<dd>
<p>Specifies the surface handle used in the generation.</p>
</dd>

### -field <b>Filter</b>

<dd>
<p>Specifies the filter type used in the generation.</p>
</dd>
</dl>

## -remarks
<p>To generate the sublevels of a MIP-map texture, the driver receives a D3DDP2OP_GENERATEMIPSUBLEVELS command along with a D3DHAL_DP2GENERATEMIPSUBLEVELS structure. For more information about automatically generating the sublevels of MIP-map textures, see <a href="https://msdn.microsoft.com/fbfb0d1b-468d-4e7f-865e-bdc7d19f5516">Generating Sublevels of MIP Map Textures</a>.</p>

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
<dt>D3DDP2OP_GENERATEMIPSUBLEVELS</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2GENERATEMIPSUBLEVELS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
