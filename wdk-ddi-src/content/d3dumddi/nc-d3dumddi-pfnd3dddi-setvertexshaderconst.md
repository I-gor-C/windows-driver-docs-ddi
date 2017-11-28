---
UID: NC.d3dumddi.PFND3DDDI_SETVERTEXSHADERCONST
title: PFND3DDDI_SETVERTEXSHADERCONST
author: windows-driver-content
description: The SetVertexShaderConst function sets one or more vertex shader constant registers with floating-point values.
old-location: display\setvertexshaderconst.htm
old-project: display
ms.assetid: 2dbde343-b10a-4357-a2b7-d6b1b1b868f2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetVertexShaderConst
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
req.iface: 
---

# PFND3DDDI_SETVERTEXSHADERCONST callback



## -description
<p>The <i>SetVertexShaderConst</i> function sets one or more vertex shader constant registers with floating-point values.</p>


## -prototype

````
PFND3DDDI_SETVERTEXSHADERCONST SetVertexShaderConst;

__checkReturn HRESULT APIENTRY SetVertexShaderConst(
  _In_       HANDLE                         hDevice,
  _In_ const D3DDDIARG_SETVERTEXSHADERCONST *pData,
  _In_ const VOID                           *pRegisters
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543368">D3DDDIARG_SETVERTEXSHADERCONST</a> structure that specifies how to set the vertex shader constant registers.</p>
</dd>

### -param <i>pRegisters</i> [in]

<dd>
<p> A pointer to a buffer that contains the floating-point values to copy.</p>
</dd>
</dl>

## -returns
<p><i>SetVertexShaderConst</i> returns S_OK or an appropriate error result if the vertex shader constant registers are not successfully set with floating-point values.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543368">D3DDDIARG_SETVERTEXSHADERCONST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETVERTEXSHADERCONST callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
