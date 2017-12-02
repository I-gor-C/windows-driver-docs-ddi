---
UID: NC.d3dumddi.PFND3DDDI_UNLOCK
title: PFND3DDDI_UNLOCK
author: windows-driver-content
description: The Unlock function unlocks a resource or a surface within the resource that was previously locked by the Lock function.
old-location: display\unlock.htm
old-project: display
ms.assetid: 23cc9c64-99d4-4602-a1b0-234fe7fcc3da
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Unlock
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

# PFND3DDDI_UNLOCK callback



## -description
<p>The <i>Unlock</i> function unlocks a resource or a surface within the resource that was previously locked by the <i>Lock</i> function.</p>


## -prototype

````
PFND3DDDI_UNLOCK Unlock;

__checkReturn HRESULT APIENTRY Unlock(
  _In_       HANDLE           hDevice,
  _In_ const D3DDDIARG_UNLOCK *pData
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param pData [in]

<dd>
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-unlock.md">D3DDDIARG_UNLOCK</a> structure that describes the resource or surface within the resource to unlock.</p>
</dd>
</dl>

## -returns
<p><i>Unlock</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The resource is successfully unlocked.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><i>Unlock</i> could not allocate the required memory for it to complete.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The resource that <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-unlock.md">D3DDDIARG_UNLOCK</a> describes was not locked by a previous call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> function. </p>

<p> </p>

## -remarks
<p>These comments are analogous to the description in the Remarks section of the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> reference page.</p>

<p>The user-mode display driver must call the Microsoft Direct3D runtime's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlockcb.md">pfnUnlockCb</a> function after <i>Unlock</i> is called. In this <b>pfnUnlockCb</b> call, the user-mode display driver passes an allocation handle. Before calling <b>pfnUnlockCb</b>, the user-mode display driver must first map the surface to an appropriate allocation. </p>

<p>The runtime calls the user-mode display driver's <i>Unlock</i> function to unlock preallocated system memory surfaces as well. The runtime sets the <b>NotifyOnly</b> bit-field flag in the <b>Flags</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-unlock.md">D3DDDIARG_UNLOCK</a> structure that is pointed to by <i>pData</i> to differentiate <i>Unlock</i> calls that unlock preallocated system memory from other <i>Unlock</i> calls. If the user-mode display driver's <i>Lock</i> function called <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lockcb.md">pfnLockCb</a> to lock the system memory allocation that corresponds to the surface, it must also call <b>pfnUnlockCb</b>. Not calling <b>pfnUnlockCb</b>  stops the coordination between the runtime, the user-mode display driver, and the display miniport driver. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-unlock.md">D3DDDIARG_UNLOCK</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lockcb.md">pfnLockCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlockcb.md">pfnUnlockCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_UNLOCK callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
