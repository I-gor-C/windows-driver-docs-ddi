---
UID: NS.d3dumddi._D3DDDIARG_CREATEPIXELSHADER
title: D3DDDIARG_CREATEPIXELSHADER
author: windows-driver-content
description: The D3DDDIARG_CREATEPIXELSHADER structure specifies a shader handle to associate with pixel shader code.
old-location: display\d3dddiarg_createpixelshader.htm
ms.assetid: dc7baff1-7e74-4666-805b-33b524c89c1d
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
req.alt-api: D3DDDIARG_CREATEPIXELSHADER
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
ms.keywords: D3DDDIARG_CREATEPIXELSHADER, D3DDDIARG_CREATEPIXELSHADER
req.iface: 
---

# D3DDDIARG_CREATEPIXELSHADER structure



## -description
<p>The D3DDDIARG_CREATEPIXELSHADER structure specifies a shader handle to associate with pixel shader code.</p>


## -syntax

````
typedef struct _D3DDDIARG_CREATEPIXELSHADER {
  UINT   CodeSize;
  HANDLE ShaderHandle;
} D3DDDIARG_CREATEPIXELSHADER;
````


## -struct-fields
<dl>

### -field <b>CodeSize</b>

<dd>
<p>[in] The size, in bytes, of the pixel shader code that is passed in the <i>pCode</i> parameter in a call to the user-mode display driver's <a href="https://msdn.microsoft.com/b80a1823-6d91-440f-89e4-f7248579cc8f">CreatePixelShader</a> function.</p>
</dd>

### -field <b>ShaderHandle</b>

<dd>
<p>[out] A handle to the pixel shader code.</p>
</dd>
</dl>

## -remarks
<p>For more information about programming shader assemblers, see <a href="https://msdn.microsoft.com/c858766c-b414-4971-b4d9-23ec94aca8ea">Processing Shader Codes</a>.</p>

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
<a href="https://msdn.microsoft.com/b80a1823-6d91-440f-89e4-f7248579cc8f">CreatePixelShader</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CREATEPIXELSHADER structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
