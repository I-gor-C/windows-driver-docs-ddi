---
UID: NS.d3dhal._D3DHAL_DP2CREATEPIXELSHADER
title: D3DHAL_DP2CREATEPIXELSHADER
author: windows-driver-content
description: DirectX 8.0 and later versions only. The D3DHAL_DP2CREATEPIXELSHADER structure is used to create a pixel shader when a D3DDP2OP_CREATEPIXELSHADER opcode is received by D3dDrawPrimitives2.
old-location: display\d3dhal_dp2createpixelshader.htm
old-project: display
ms.assetid: aa3a7f17-7210-458f-979b-1da455790e4a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2CREATEPIXELSHADER, D3DHAL_DP2CREATEPIXELSHADER
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
req.alt-api: D3DHAL_DP2CREATEPIXELSHADER
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

# D3DHAL_DP2CREATEPIXELSHADER structure



## -description
<p>
   DirectX 8.0 and later versions only.
   </p>
<p>The D3DHAL_DP2CREATEPIXELSHADER structure is used to create a pixel shader when a D3DDP2OP_CREATEPIXELSHADER opcode is received by <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>.</p>


## -syntax

````
typedef struct _D3DHAL_DP2CREATEPIXELSHADER {
  DWORD dwHandle;
  DWORD dwCodeSize;
} D3DHAL_DP2CREATEPIXELSHADER, *LPD3DHAL_DP2CREATEPIXELSHADER;
````


## -struct-fields
<dl>

### -field dwHandle

<dd>
<p>Specifies the handle to the pixel shader that is assigned by the runtime. This value is guaranteed to be subzero.</p>
</dd>

### -field dwCodeSize

<dd>
<p>Specifies the size, in bytes, of the shader code following this data structure in the DP2 stream.</p>
</dd>
</dl>

## -remarks
<p>The runtime generates a handle for this shader before calling the driver. The shader code itself follows the D3DHAL_DP2CREATEPIXELSHADER in the DP2 stream. See <a href="display.direct3d_driver_shader_codes">Direct3D Driver Shader Codes</a> for information about the format of an individual shader code and the tokens that comprise each shader code. </p>

<p>Before calling the driver, the runtime validates the pixel shader code to ensure that it is legal for the specified shader language version.</p>

<p>It is important to note that the creation of a pixel shader does not imply the setting of the current shader.</p>

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
<dt>D3DDP2OP_CREATEPIXELSHADER</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2pixelshader.md">D3DHAL_DP2PIXELSHADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2CREATEPIXELSHADER structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
