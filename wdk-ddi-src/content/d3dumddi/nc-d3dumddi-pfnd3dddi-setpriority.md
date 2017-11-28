---
UID: NC.d3dumddi.PFND3DDDI_SETPRIORITY
title: PFND3DDDI_SETPRIORITY
author: windows-driver-content
description: The SetPriority function sets the eviction-from-memory priority for a managed texture.
old-location: display\setpriority.htm
old-project: display
ms.assetid: 61ac2d28-7aed-4796-8d09-591db936013b
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
req.alt-api: SetPriority
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

# PFND3DDDI_SETPRIORITY callback



## -description
<p>The <i>SetPriority</i> function sets the eviction-from-memory priority for a managed texture.</p>


## -prototype

````
PFND3DDDI_SETPRIORITY SetPriority;

__checkReturn HRESULT APIENTRY SetPriority(
  _In_       HANDLE                hDevice,
  _In_ const D3DDDIARG_SETPRIORITY *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543345">D3DDDIARG_SETPRIORITY</a> structure that specifies the priority level to set for the managed texture.</p>
</dd>
</dl>

## -returns
<p><i>SetPriority</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The priority level is successfully set.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

## -remarks
<p>The Microsoft Direct3D runtime calls <i>SetPriority</i> to set the priority level for a resource. The user-mode display driver should translate the resource handle that is supplied in the <b>hResource</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543345">D3DDDIARG_SETPRIORITY</a> structure that is pointed to by <i>pData</i> to an allocation handle. After the driver makes this translation, the driver should pass the resulting handle in a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setprioritycb.md">pfnSetPriorityCb</a> function.</p>

<p>The Microsoft Direct3D runtime calls <i>SetPriority</i> to set the priority level for a resource. The user-mode display driver should translate the resource handle that is supplied in the <b>hResource</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543345">D3DDDIARG_SETPRIORITY</a> structure that is pointed to by <i>pData</i> to an allocation handle. After the driver makes this translation, the driver should pass the resulting handle in a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setprioritycb.md">pfnSetPriorityCb</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543345">D3DDDIARG_SETPRIORITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setprioritycb.md">pfnSetPriorityCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETPRIORITY callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
