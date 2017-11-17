---
UID: NS.d3dumddi._D3DDDIARG_SETPIXELSHADERCONST
title: D3DDDIARG_SETPIXELSHADERCONST
author: windows-driver-content
description: The D3DDDIARG_SETPIXELSHADERCONST structure describes how to set the pixel shader constant registers.
old-location: display\d3dddiarg_setpixelshaderconst.htm
ms.assetid: 1c8cbbdc-ac2e-462e-9d5c-484305a41302
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
req.alt-api: D3DDDIARG_SETPIXELSHADERCONST
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
ms.keywords: D3DDDIARG_SETPIXELSHADERCONST, D3DDDIARG_SETPIXELSHADERCONST
req.iface: 
---

# D3DDDIARG_SETPIXELSHADERCONST structure



## -description
<p>The D3DDDIARG_SETPIXELSHADERCONST structure describes how to set the pixel shader constant registers. </p>


## -syntax

````
typedef struct _D3DDDIARG_SETPIXELSHADERCONST {
  UINT Register;
  UINT Count;
} D3DDDIARG_SETPIXELSHADERCONST;
````


## -struct-fields
<dl>

### -field <b>Register</b>

<dd>
<p>[in] The index of the first pixel shader constant register whose value is set.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>[in] The number of constant registers to set and, therefore, the number of values in the array that is passed in the <i>pRegisters</i> parameter in the call to the user-mode display driver's <a href="https://msdn.microsoft.com/02710936-28df-4c8f-aa1e-bdff01155608">SetPixelShaderConst</a>, <a href="https://msdn.microsoft.com/fafc046e-0595-4901-bfb1-70bd980388bc">SetPixelShaderConstI</a>, or <a href="https://msdn.microsoft.com/6f7c8932-9332-4ff2-89ab-2f9a66783326">SetPixelShaderConstB</a> function.</p>
</dd>
</dl>

## -remarks
<p>The <b>Count</b> member specifies the following values, depending on the structure type that is used in the call to the <a href="https://msdn.microsoft.com/02710936-28df-4c8f-aa1e-bdff01155608">SetPixelShaderConst</a>, <a href="https://msdn.microsoft.com/fafc046e-0595-4901-bfb1-70bd980388bc">SetPixelShaderConstI</a>, or <a href="https://msdn.microsoft.com/6f7c8932-9332-4ff2-89ab-2f9a66783326">SetPixelShaderConstB</a> function: </p>

<p>Four-element, single-precision float vectors for the D3DDDIARG_SETPIXELSHADERCONST structure in the <a href="https://msdn.microsoft.com/02710936-28df-4c8f-aa1e-bdff01155608">SetPixelShaderConst</a> call.</p>

<p>Four-integer vectors for the D3DDDIARG_SETPIXELSHADERCONSTI structure in the <a href="https://msdn.microsoft.com/fafc046e-0595-4901-bfb1-70bd980388bc">SetPixelShaderConstI</a> call.</p>

<p>Boolean values for the D3DDDIARG_SETPIXELSHADERCONSTB structure in the <a href="https://msdn.microsoft.com/6f7c8932-9332-4ff2-89ab-2f9a66783326">SetPixelShaderConstB</a> call.</p>

<p>The preceding structures are identical, as the following definitions show:</p>

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
<a href="https://msdn.microsoft.com/02710936-28df-4c8f-aa1e-bdff01155608">SetPixelShaderConst</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6f7c8932-9332-4ff2-89ab-2f9a66783326">SetPixelShaderConstB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fafc046e-0595-4901-bfb1-70bd980388bc">SetPixelShaderConstI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_SETPIXELSHADERCONST structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
