---
UID: NC.d3dumddi.PFND3DDDI_SETRENDERSTATE
title: PFND3DDDI_SETRENDERSTATE
author: windows-driver-content
description: The SetRenderState function updates a render state.
old-location: display\setrenderstate.htm
ms.assetid: 22fb67f7-cc28-4f10-950d-1379769ddf89
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetRenderState
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_SETRENDERSTATE callback



## -description
<p>The <i>SetRenderState</i> function updates a render state.</p>


## -prototype

````
PFND3DDDI_SETRENDERSTATE SetRenderState;

__checkReturn HRESULT APIENTRY SetRenderState(
  _In_       HANDLE                hDevice,
  _In_ const D3DDDIARG_RENDERSTATE *pData
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
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543267">D3DDDIARG_RENDERSTATE</a> structure that describes how to update the render state.</p>
</dd>
</dl>

## -returns
<p><i>SetRenderState</i> returns S_OK or an appropriate error result if the render state is not successfully updated.</p>

## -remarks
<p>The Microsoft Direct3D runtime maps <b>BeginScene</b> and <b>EndScene</b> calls from applications to the user-mode display driver's <i>SetRenderState</i> function. When the runtime receives a <b>BeginScene</b> call, it sets the <b>State</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543267">D3DDDIARG_RENDERSTATE</a> structure that is pointed to by <i>pData</i> to D3DRENDERSTATE_SCENECAPTURE and the <b>Value</b> member of D3DDDIARG_RENDERSTATE to <b>TRUE</b> and then calls <i>SetRenderState</i>. When the runtime receives an <b>EndScene</b> call, it sets the <b>State</b> member to D3DRENDERSTATE_SCENECAPTURE and the <b>Value</b> member to <b>FALSE</b> and then calls <i>SetRenderState</i>. In between these calls to <i>SetRenderState</i>, the driver captures geometric data within a frame.</p>

<p>The Microsoft Direct3D runtime maps <b>BeginScene</b> and <b>EndScene</b> calls from applications to the user-mode display driver's <i>SetRenderState</i> function. When the runtime receives a <b>BeginScene</b> call, it sets the <b>State</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543267">D3DDDIARG_RENDERSTATE</a> structure that is pointed to by <i>pData</i> to D3DRENDERSTATE_SCENECAPTURE and the <b>Value</b> member of D3DDDIARG_RENDERSTATE to <b>TRUE</b> and then calls <i>SetRenderState</i>. When the runtime receives an <b>EndScene</b> call, it sets the <b>State</b> member to D3DRENDERSTATE_SCENECAPTURE and the <b>Value</b> member to <b>FALSE</b> and then calls <i>SetRenderState</i>. In between these calls to <i>SetRenderState</i>, the driver captures geometric data within a frame.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543267">D3DDDIARG_RENDERSTATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETRENDERSTATE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
