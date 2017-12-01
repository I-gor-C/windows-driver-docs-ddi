---
UID: NS.d3d10umddi.D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW
title: D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW
author: windows-driver-content
description: The D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW structure describes a buffer that is used to create a shader resource view in a call to the CreateShaderResourceView(D3D11) function.
old-location: display\d3d11ddiarg_bufferex_shaderresourceview.htm
old-project: display
ms.assetid: b3585a06-fdb0-4fe9-8d5c-63680039a789
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW, D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW
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

# D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW structure



## -description
<p>The D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW structure describes a buffer that is used to create a shader resource view in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createshaderresourceview.md">CreateShaderResourceView(D3D11)</a> function. </p>


## -syntax

````
typedef struct D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW {
  union {
    UINT FirstElement;
    UINT ElementOffset;
  };
  union {
    UINT NumElements;
    UINT ElementWidth;
  };
  UINT  Flags;
} D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW;
````


## -struct-fields
<dl>

### -field <b>FirstElement</b>

<dd>
<p>[in] The offset, in bytes, to the first element in the buffer. </p>
</dd>

### -field <b>ElementOffset</b>

<dd>
<p>[in] The offset, in bytes, to the first element in the buffer. </p>
</dd>

### -field <b>NumElements</b>

<dd>
<p>[in] The number of elements in the buffer. </p>
</dd>

### -field <b>ElementWidth</b>

<dd>
<p>[in] The width, in elements, in the buffer. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A valid bitwise OR of flag values that describe the buffer. Currently, the Direct3D runtime supports only the D3D11_DDI_BUFFEREX_SRV_FLAG_RAW (0x00000001) flag. If this flag is set, the buffer is in raw format. </p>
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
<p>D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW is supported beginning with the Windows 7 operating system. </p>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivateshaderresourceviewsize.md">CalcPrivateShaderResourceViewSize(D3D11)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createshaderresourceview.md">CreateShaderResourceView(D3D11)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg-createshaderresourceview.md">D3D11DDIARG_CREATESHADERRESOURCEVIEW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDIARG_BUFFEREX_SHADERRESOURCEVIEW structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
