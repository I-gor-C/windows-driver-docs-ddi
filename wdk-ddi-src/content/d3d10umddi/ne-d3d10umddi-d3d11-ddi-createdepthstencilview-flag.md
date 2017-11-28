---
UID: NE.d3d10umddi.D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG
title: D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG
author: windows-driver-content
description: The D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG enumeration type contains values that identify the type of depth-stencil view to create through a call to the driver's CreateDepthStencilView(D3D11) function.
old-location: display\d3d11_ddi_createdepthstencilview_flag.htm
old-project: display
ms.assetid: 197ba249-f7a4-4c98-914c-ecb8984ffd5d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG
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

# D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG enumeration



## -description
<p>The D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG enumeration type contains values that identify the type of depth-stencil view to create through a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createdepthstencilview.md">CreateDepthStencilView(D3D11)</a> function. </p>


## -syntax

````
typedef enum D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG { 
  D3D11_DDI_CREATE_DSV_READ_ONLY_DEPTH    = 0x01L,
  D3D11_DDI_CREATE_DSV_READ_ONLY_STENCIL  = 0x02L,
  D3D11_DDI_CREATE_DSV_FLAG_MASK          = 0x03L
} D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG;
````


## -enum-fields
<dl>

### -field <a id="D3D11_DDI_CREATE_DSV_READ_ONLY_DEPTH"></a><a id="d3d11_ddi_create_dsv_read_only_depth"></a><b>D3D11_DDI_CREATE_DSV_READ_ONLY_DEPTH</b>

<dd>
<p>The driver should create a read-only depth view. </p>
</dd>

### -field <a id="D3D11_DDI_CREATE_DSV_READ_ONLY_STENCIL"></a><a id="d3d11_ddi_create_dsv_read_only_stencil"></a><b>D3D11_DDI_CREATE_DSV_READ_ONLY_STENCIL</b>

<dd>
<p>The driver should create a read-only stencil view.</p>
</dd>

### -field <a id="D3D11_DDI_CREATE_DSV_FLAG_MASK"></a><a id="d3d11_ddi_create_dsv_flag_mask"></a><b>D3D11_DDI_CREATE_DSV_FLAG_MASK</b>

<dd>
<p>A mask value that indicates the valid bitfields in a bitwise OR combination of the values from this enumeration. </p>
</dd>
</dl>

## -remarks
<p>D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG values are specified in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542048">D3D11DDIARG_CREATEDEPTHSTENCILVIEW</a> structure to indicate the type of depth-stencil view to create.  </p>

<p>D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG values are specified in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542048">D3D11DDIARG_CREATEDEPTHSTENCILVIEW</a> structure to indicate the type of depth-stencil view to create.  </p>

<p>D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG values are specified in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542048">D3D11DDIARG_CREATEDEPTHSTENCILVIEW</a> structure to indicate the type of depth-stencil view to create.  </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG is supported beginning with the Windows 7 operating system. </p>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createdepthstencilview.md">CreateDepthStencilView(D3D11)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542048">D3D11DDIARG_CREATEDEPTHSTENCILVIEW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_DDI_CREATEDEPTHSTENCILVIEW_FLAG enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
