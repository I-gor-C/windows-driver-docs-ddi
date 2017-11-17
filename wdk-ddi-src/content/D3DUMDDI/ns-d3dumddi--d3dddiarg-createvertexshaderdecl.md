---
UID: NS.d3dumddi._D3DDDIARG_CREATEVERTEXSHADERDECL
title: D3DDDIARG_CREATEVERTEXSHADERDECL
author: windows-driver-content
description: The D3DDDIARG_CREATEVERTEXSHADERDECL structure specifies a shader handle to associate with the vertex shader declaration.
old-location: display\d3dddiarg_createvertexshaderdecl.htm
ms.assetid: 510f8cda-922e-48de-b95e-daf972e906fa
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
req.alt-api: D3DDDIARG_CREATEVERTEXSHADERDECL
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
ms.keywords: D3DDDIARG_CREATEVERTEXSHADERDECL, D3DDDIARG_CREATEVERTEXSHADERDECL
req.iface: 
---

# D3DDDIARG_CREATEVERTEXSHADERDECL structure



## -description
<p>The D3DDDIARG_CREATEVERTEXSHADERDECL structure specifies a shader handle to associate with the vertex shader declaration.</p>


## -syntax

````
typedef struct _D3DDDIARG_CREATEVERTEXSHADERDECL {
  UINT   NumVertexElements;
  HANDLE ShaderHandle;
} D3DDDIARG_CREATEVERTEXSHADERDECL;
````


## -struct-fields
<dl>

### -field <b>NumVertexElements</b>

<dd>
<p>[in] The number of vertex elements in the array that is passed to the <i>pVertexElements</i> parameter in a call to the user-mode display driver's <a href="https://msdn.microsoft.com/00c53e81-93db-46b8-b65c-c8d62059452a">CreateVertexShaderDecl</a> function.</p>
</dd>

### -field <b>ShaderHandle</b>

<dd>
<p>[out] A handle to the vertex shader declaration.</p>
</dd>
</dl>

## -remarks
<p>The handle value in the <b>ShaderHandle</b> member is guaranteed to be nonzero. </p>

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
<a href="https://msdn.microsoft.com/00c53e81-93db-46b8-b65c-c8d62059452a">CreateVertexShaderDecl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CREATEVERTEXSHADERDECL structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
