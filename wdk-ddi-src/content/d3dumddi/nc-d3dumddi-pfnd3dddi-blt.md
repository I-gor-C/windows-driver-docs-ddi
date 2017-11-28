---
UID: NC.d3dumddi.PFND3DDDI_BLT
title: PFND3DDDI_BLT
author: windows-driver-content
description: The Blt function copies the contents of a source surface to a destination surface.
old-location: display\blt.htm
old-project: display
ms.assetid: e87576c6-0173-4d8e-bbaf-b82e2907140a
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
req.alt-api: Blt
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

# PFND3DDDI_BLT callback



## -description
<p>The <b>Blt</b> function copies the contents of a source surface to a destination surface.</p>


## -prototype

````
PFND3DDDI_BLT Blt;

__checkReturn HRESULT APIENTRY Blt(
  _In_       HANDLE        hDevice,
  _In_ const D3DDDIARG_BLT *pData
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
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a> structure that describes the parameters of the bit-block transfer (bitblt).</p>
</dd>
</dl>

## -returns
<p><b>Blt</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The bitblt for the resource is successfully performed.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-blt.md">Blt</a> could not allocate the required memory for it to complete.</p>

<p> </p>

## -remarks
<p>The Microsoft Direct3D runtime calls the user-mode display driver's <b>Blt</b> function to copy the contents of a source surface to a destination surface. After mapping the surface references to allocation references, the user-mode display driver should issue the appropriate hardware commands. If either the source or destination allocation is in system memory, the user-mode display driver might be required to synchronize (that is, call the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a> function) if the outstanding hardware command stream contains references to the system-memory allocation. If both the source and destination allocations are in system memory, the driver should synchronize as necessary but should not copy the contents of the source surface. The Direct3D runtime copies the contents after the call to <b>pfnRenderCb</b> returns. </p>

<p>The user-mode display driver must handle the following conditions that might occur during a copy operation:</p>

<p>The destination and source surfaces are part of the same resource (that is, the <b>hSrcResource</b> and <b>hDstResource</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a> specify handles to the same resource).</p>

<p>The source and destination rectangles overlap (that is, the coordinates of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structures in the <b>SrcRect</b> and <b>DstRect</b> members of D3DDDIARG_BLT overlap).</p>

<p>The user-mode display driver must handle all of the bitblt to and from video memory, including bitblt from video memory to system memory. If the user-mode display driver cannot use the graphics processing unit (GPU) to issue a bitblt from video memory to system memory, the user-mode display driver can copy the data by using the CPU.</p>

<p>The user-mode display driver must support colorkeying only with formats that were introduced before Microsoft DirectX 8.0. For formats that were introduced in DirectX 8.0 and later runtimes, colorkeying support is not required.</p>

<p>The type of bitblt to perform is indicated through the bit-field flags that are specified in the <b>Flags</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a>. Video memory to video memory bitblts can include colorkeying, stretching, mirroring, and linear-to-sRGB format conversion. System memory to video memory bitblts can include stretching and linear-to-sRGB format conversion; however, these types of bitblts never include mirroring or colorkeying. All video memory to system memory bitblts and system memory to system memory bitblts are straight copies only; that is, these types of bitblts never include stretching, mirroring, colorkeying, or linear-to-sRGB format conversion. For more information about sRGB format, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a> website.</p>

<p>For more information about rules that the <b>Blt</b> function must follow when converting depth-stencil values, see <a href="https://msdn.microsoft.com/b83d4e6d-5645-49ab-bbb0-c694f1410cba">Copying Depth-Stencil Values</a>.</p>

<p>The Direct3D runtime can call the user-mode display driver's <b>Blt</b> function to copy the contents of any source surface type (such as, offscreen-plain type, render-target type, or texture type) to any other destination surface type. </p>

<p>The Microsoft Direct3D runtime calls the user-mode display driver's <b>Blt</b> function to copy the contents of a source surface to a destination surface. After mapping the surface references to allocation references, the user-mode display driver should issue the appropriate hardware commands. If either the source or destination allocation is in system memory, the user-mode display driver might be required to synchronize (that is, call the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a> function) if the outstanding hardware command stream contains references to the system-memory allocation. If both the source and destination allocations are in system memory, the driver should synchronize as necessary but should not copy the contents of the source surface. The Direct3D runtime copies the contents after the call to <b>pfnRenderCb</b> returns. </p>

<p>The user-mode display driver must handle the following conditions that might occur during a copy operation:</p>

<p>The destination and source surfaces are part of the same resource (that is, the <b>hSrcResource</b> and <b>hDstResource</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a> specify handles to the same resource).</p>

<p>The source and destination rectangles overlap (that is, the coordinates of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structures in the <b>SrcRect</b> and <b>DstRect</b> members of D3DDDIARG_BLT overlap).</p>

<p>The user-mode display driver must handle all of the bitblt to and from video memory, including bitblt from video memory to system memory. If the user-mode display driver cannot use the graphics processing unit (GPU) to issue a bitblt from video memory to system memory, the user-mode display driver can copy the data by using the CPU.</p>

<p>The user-mode display driver must support colorkeying only with formats that were introduced before Microsoft DirectX 8.0. For formats that were introduced in DirectX 8.0 and later runtimes, colorkeying support is not required.</p>

<p>The type of bitblt to perform is indicated through the bit-field flags that are specified in the <b>Flags</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a>. Video memory to video memory bitblts can include colorkeying, stretching, mirroring, and linear-to-sRGB format conversion. System memory to video memory bitblts can include stretching and linear-to-sRGB format conversion; however, these types of bitblts never include mirroring or colorkeying. All video memory to system memory bitblts and system memory to system memory bitblts are straight copies only; that is, these types of bitblts never include stretching, mirroring, colorkeying, or linear-to-sRGB format conversion. For more information about sRGB format, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a> website.</p>

<p>For more information about rules that the <b>Blt</b> function must follow when converting depth-stencil values, see <a href="https://msdn.microsoft.com/b83d4e6d-5645-49ab-bbb0-c694f1410cba">Copying Depth-Stencil Values</a>.</p>

<p>The Direct3D runtime can call the user-mode display driver's <b>Blt</b> function to copy the contents of any source surface type (such as, offscreen-plain type, render-target type, or texture type) to any other destination surface type. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_BLT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
