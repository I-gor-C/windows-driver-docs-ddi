---
UID: NC.d3dumddi.PFND3DDDI_RESOLVESHAREDRESOURCE
title: PFND3DDDI_RESOLVESHAREDRESOURCE
author: windows-driver-content
description: The ResolveSharedResource function informs a user-mode display driver that ownership of a shared surface changed or that a surface is being used for GDI interoperation.
old-location: display\resolvesharedresource.htm
old-project: display
ms.assetid: 8ad9130e-bade-4fd2-b345-b6361fd001ef
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: ResolveSharedResource is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ResolveSharedResource
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

# PFND3DDDI_RESOLVESHAREDRESOURCE callback



## -description
<p>The <i>ResolveSharedResource</i> function informs a user-mode display driver that ownership of a shared surface changed or that a surface is being used for GDI interoperation. </p>


## -prototype

````
PFND3DDDI_RESOLVESHAREDRESOURCE ResolveSharedResource;

__checkReturn HRESULT APIENTRY ResolveSharedResource(
  _In_       HANDLE                          hDevice,
  _In_ const D3DDDIARG_RESOLVESHAREDRESOURCE *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (that is, the graphics context) that is associated with the shared surface or GDI interoperable surface. </p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543274">D3DDDIARG_RESOLVESHAREDRESOURCE</a> structure that contains a handle to the surface. </p>
</dd>
</dl>

## -returns
<p><i>ResolveSharedResource</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The resource is successfully resolved.</p><dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl><p>The driver detects that the graphics adapter was removed. Therefore, the driver did not complete the operation. If the driver never notices the adapter-removal condition, the driver is not required to return this error code. </p>

<p> </p>

## -remarks
<p>The Direct3D runtime calls <i>ResolveSharedResource</i> when an application calls one of the following functions:</p>

<p><b>IDXGIKeyedMutex::ReleaseSynch</b> on a synchronized shared surface </p>

<p><b>IDXGISurface1::GetDC</b> for a GDI interoperable surface </p>

<p>The runtime calls the driver's <i>ResolveSharedResource</i> function every time a shared surface owner changes or when a surface is used for GDI interoperation. The runtime supplies <i>ResolveSharedResource</i> with handles to the display device--via the <i>hDevice</i> parameter-- and the surface--via the <i>pData</i> parameter.</p>

<p>The driver implements <i>ResolveSharedResource</i> to appropriately manage resources for multiple GPU scenarios. Each resource might be divided across memory for multiple GPUs to render on. The driver can implement <i>ResolveSharedResource</i> to remerge each resource so that the new resource owner has the merged resource. The driver must flush any partially built command buffers that might modify the resource.</p>

<p>The Direct3D runtime calls <i>ResolveSharedResource</i> when an application calls one of the following functions:</p>

<p><b>IDXGIKeyedMutex::ReleaseSynch</b> on a synchronized shared surface </p>

<p><b>IDXGISurface1::GetDC</b> for a GDI interoperable surface </p>

<p>The runtime calls the driver's <i>ResolveSharedResource</i> function every time a shared surface owner changes or when a surface is used for GDI interoperation. The runtime supplies <i>ResolveSharedResource</i> with handles to the display device--via the <i>hDevice</i> parameter-- and the surface--via the <i>pData</i> parameter.</p>

<p>The driver implements <i>ResolveSharedResource</i> to appropriately manage resources for multiple GPU scenarios. Each resource might be divided across memory for multiple GPUs to render on. The driver can implement <i>ResolveSharedResource</i> to remerge each resource so that the new resource owner has the merged resource. The driver must flush any partially built command buffers that might modify the resource.</p>

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
<p><i>ResolveSharedResource</i> is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543274">D3DDDIARG_RESOLVESHAREDRESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_RESOLVESHAREDRESOURCE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
