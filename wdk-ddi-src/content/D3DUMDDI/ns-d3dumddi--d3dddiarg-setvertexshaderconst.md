---
UID: NS.d3dumddi._D3DDDIARG_SETVERTEXSHADERCONST
title: D3DDDIARG_SETVERTEXSHADERCONST
author: windows-driver-content
description: The D3DDDIARG_SETVERTEXSHADERCONST structure describes how to set vertex shader constant registers.
old-location: display\d3dddiarg_setvertexshaderconst.htm
ms.assetid: ac3c4609-094d-4003-a5ee-b609f7ec13e1
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
req.alt-api: D3DDDIARG_SETVERTEXSHADERCONST
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
ms.keywords: D3DDDIARG_SETVERTEXSHADERCONST, D3DDDIARG_SETVERTEXSHADERCONST
req.iface: 
---

# D3DDDIARG_SETVERTEXSHADERCONST structure



## -description
<p>The D3DDDIARG_SETVERTEXSHADERCONST structure describes how to set vertex shader constant registers. </p>


## -syntax

````
typedef struct _D3DDDIARG_SETVERTEXSHADERCONST {
  UINT Register;
  UINT Count;
} D3DDDIARG_SETVERTEXSHADERCONST;
````


## -struct-fields
<dl>

### -field <b>Register</b>

<dd>
<p>[in] The index of the first vertex shader constant register whose value is set.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>[in] The number of constant registers to set and, therefore, the number of values in the array that is passed in the <i>pRegisters</i> parameter in the call to the user-mode display driver's <a href="https://msdn.microsoft.com/2dbde343-b10a-4357-a2b7-d6b1b1b868f2">SetVertexShaderConst</a>, <a href="https://msdn.microsoft.com/c245cfbd-0368-4a49-96a7-ac4cd14e2f5a">SetVertexShaderConstI</a>, or <a href="https://msdn.microsoft.com/41ca823e-4370-4cba-9129-067e25a43a69">SetVertexShaderConstB</a> function.</p>
</dd>
</dl>

## -remarks
<p>The <b>Count</b> member specifies the following values, depending on the structure type that is used in the call to the <a href="https://msdn.microsoft.com/2dbde343-b10a-4357-a2b7-d6b1b1b868f2">SetVertexShaderConst</a>, <a href="https://msdn.microsoft.com/c245cfbd-0368-4a49-96a7-ac4cd14e2f5a">SetVertexShaderConstI</a>, or <a href="https://msdn.microsoft.com/41ca823e-4370-4cba-9129-067e25a43a69">SetVertexShaderConstB</a> function: </p>

<p>Four-element, single-precision float vectors for the D3DDDIARG_SETVERTEXSHADERCONST structure in the <a href="https://msdn.microsoft.com/2dbde343-b10a-4357-a2b7-d6b1b1b868f2">SetVertexShaderConst</a> call.</p>

<p>Four-integer vectors for the D3DDDIARG_SETVERTEXSHADERCONSTI structure in the <a href="https://msdn.microsoft.com/c245cfbd-0368-4a49-96a7-ac4cd14e2f5a">SetVertexShaderConstI</a> call.</p>

<p>Boolean values for the D3DDDIARG_SETVERTEXSHADERCONSTB structure in the <a href="https://msdn.microsoft.com/41ca823e-4370-4cba-9129-067e25a43a69">SetVertexShaderConstB</a> call.</p>

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
<a href="https://msdn.microsoft.com/2dbde343-b10a-4357-a2b7-d6b1b1b868f2">SetVertexShaderConst</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/41ca823e-4370-4cba-9129-067e25a43a69">SetVertexShaderConstB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c245cfbd-0368-4a49-96a7-ac4cd14e2f5a">SetVertexShaderConstI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_SETVERTEXSHADERCONST structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
