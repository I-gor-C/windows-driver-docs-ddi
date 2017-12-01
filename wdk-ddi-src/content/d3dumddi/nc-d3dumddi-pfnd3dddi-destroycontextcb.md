---
UID: NC.d3dumddi.PFND3DDDI_DESTROYCONTEXTCB
title: PFND3DDDI_DESTROYCONTEXTCB
author: windows-driver-content
description: The pfnDestroyContextCb function destroys the context that was created through a call to the pfnCreateContextCb function.
old-location: display\pfndestroycontextcb.htm
old-project: display
ms.assetid: 6b65d75b-544b-4153-b821-d59d6f85673d
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
req.alt-api: pfnDestroyContextCb
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

# PFND3DDDI_DESTROYCONTEXTCB callback



## -description
<p>The <b>pfnDestroyContextCb</b> function destroys the context that was created through a call to the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function.</p>


## -prototype

````
PFND3DDDI_DESTROYCONTEXTCB pfnDestroyContextCb;

_checkReturn HRESULT APIENTRY CALLBACK pfnDestroyContextCb(
  _In_       HANDLE                  hDevice,
  _In_ const D3DDDICB_DESTROYCONTEXT *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to a display device (that is, the graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-destroycontext.md">D3DDDICB_DESTROYCONTEXT</a> structure that contains a handle to the context to destroy.</p>
</dd>
</dl>

## -returns
<p><b>pfnDestroyContextCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The context was successfully destroyed.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks
<p>If the specified context has not finished the work that is currently queued to it, the <b>pfnDestroyContextCb</b> function blocks until the context finishes its work and then returns. </p>

<p><b>pfnDestroyContextCb</b> returns an error if the context to destroy currently owns a synchronization object.</p>

<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnDestroyContextCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>

<p>The following code example shows how to destroy the default context for a display device.</p>

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
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-destroycontext.md">D3DDDICB_DESTROYCONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DESTROYCONTEXTCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
