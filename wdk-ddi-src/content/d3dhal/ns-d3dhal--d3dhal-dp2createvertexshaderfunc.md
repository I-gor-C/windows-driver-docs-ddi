---
UID: NS.d3dhal._D3DHAL_DP2CREATEVERTEXSHADERFUNC
title: D3DHAL_DP2CREATEVERTEXSHADERFUNC
author: windows-driver-content
description: DirectX 9.0 and later versions only. The D3DHAL_DP2CREATEVERTEXSHADERFUNC structure is used to create a vertex shader code object when a D3DDP2OP_CREATEVERTEXSHADERFUNC opcode is received by D3dDrawPrimitives2.
old-location: display\d3dhal_dp2createvertexshaderfunc.htm
old-project: display
ms.assetid: 2b7456e5-a6fa-42bf-aace-21d555c3e821
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2CREATEVERTEXSHADERFUNC, D3DHAL_DP2CREATEVERTEXSHADERFUNC
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
req.alt-api: D3DHAL_DP2CREATEVERTEXSHADERFUNC
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

# D3DHAL_DP2CREATEVERTEXSHADERFUNC structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>The D3DHAL_DP2CREATEVERTEXSHADERFUNC structure is used to create a vertex shader code object when a D3DDP2OP_CREATEVERTEXSHADERFUNC opcode is received by <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>.</p>


## -syntax

````
typedef struct _D3DHAL_DP2CREATEVERTEXSHADERFUNC {
  DWORD dwHandle;
  DWORD dwSize;
} D3DHAL_DP2CREATEVERTEXSHADERFUNC, *LPD3DHAL_DP2CREATEVERTEXSHADERFUNC;
````


## -struct-fields
<dl>

### -field dwHandle

<dd>
<p>Specifies the handle to the vertex shader code that is assigned by the runtime. This value is guaranteed to be subzero.</p>
</dd>

### -field dwSize

<dd>
<p>Specifies the shader code size in bytes.</p>
</dd>
</dl>

## -remarks
<p>When the runtime calls the driver's <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> function with this token, the driver should validate the given shader code and report success or failure accordingly. </p>

<p>Vertex shader code follows D3DHAL_DP2CREATEVERTEXSHADERFUNC in the command stream. See <a href="display.direct3d_driver_shader_codes">Direct3D Driver Shader Codes</a> for information about the format of individual shader code and the tokens that comprise each shader code. </p>

<p>The DirectX 9.0 runtime sets <b>dwHandle</b> to zero to indicate a fixed function pipeline.</p>

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
<dt>D3DDP2OP_CREATEVERTEXSHADERFUNC</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2createvertexshaderdecl.md">D3DHAL_DP2CREATEVERTEXSHADERDECL</a>
</dt>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--d3dhal-dp2vertexshader.md">D3DHAL_DP2VERTEXSHADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2CREATEVERTEXSHADERFUNC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
