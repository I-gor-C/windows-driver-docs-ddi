---
UID: NC.d3dumddi.PFND3DDDI_DELETEPIXELSHADER
title: PFND3DDDI_DELETEPIXELSHADER
author: windows-driver-content
description: The DeletePixelShader function cleans up driver-side resources that are associated with pixel shader code.
old-location: display\deletepixelshader.htm
old-project: display
ms.assetid: bc987531-d402-4f3b-a4e2-d71fe97f5400
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
req.alt-api: DeletePixelShader
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

# PFND3DDDI_DELETEPIXELSHADER callback



## -description
<p>The <b>DeletePixelShader</b> function cleans up driver-side resources that are associated with pixel shader code.</p>


## -prototype

````
PFND3DDDI_DELETEPIXELSHADER DeletePixelShader;

__checkReturn HRESULT APIENTRY DeletePixelShader(
  _In_ HANDLE hDevice,
  _In_ HANDLE hShaderHandle
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>hShaderHandle</i> [in]

<dd>
<p> A handle to the pixel shader code object.</p>
</dd>
</dl>

## -returns
<p><b>DeletePixelShader</b> returns S_OK or an appropriate error result if the pixel shader code object is not successfully cleaned up.</p>

## -remarks
<p>The <b>DeletePixelShader</b> function notifies the driver about the deletion of the pixel shader code object that the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createpixelshader.md">CreatePixelShader</a> function created. The driver can then clean up any driver-side resources that are associated with the pixel shader code.</p>

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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createpixelshader.md">CreatePixelShader</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DELETEPIXELSHADER callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
