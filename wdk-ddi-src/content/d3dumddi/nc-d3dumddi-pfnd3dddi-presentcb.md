---
UID: NC.d3dumddi.PFND3DDDI_PRESENTCB
title: PFND3DDDI_PRESENTCB
author: windows-driver-content
description: The pfnPresentCb function copies content from a source allocation.
old-location: display\pfnpresentcb.htm
old-project: display
ms.assetid: 460b9be5-5817-4225-9089-f86ad64f4554
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
req.alt-api: pfnPresentCb
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

# PFND3DDDI_PRESENTCB callback



## -description
<p>The <b>pfnPresentCb</b> function copies content from a source allocation.</p>


## -prototype

````
PFND3DDDI_PRESENTCB pfnPresentCb;

__checkReturn HRESULT APIENTRY CALLBACK pfnPresentCb(
  _In_       HANDLE           hDevice,
  _In_ const D3DDDICB_PRESENT *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to a display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544218">D3DDDICB_PRESENT</a> structure that describes the source allocation that content is copied from.</p>
</dd>
</dl>

## -returns
<p><b>pfnPresentCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Content was successfully copied.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><b>pfnPresentCb</b> could not complete because of insufficient memory.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks
<p>The user-mode display driver sets the <b>hContext</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544218">D3DDDICB_PRESENT</a> structure that is pointed to by the <i>pData</i> parameter to a context that it previously created by calling the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function. The user-mode display driver must create at least one context when the Microsoft Direct3D runtime calls the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a> or <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function to create a device. The Direct3D runtime sends the present operation to a created context.
     </p>

<p>
<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnPresentCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>
</p>

<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnPresentCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>

<p>The following code example shows how to color-fill a destination surface.</p>

<p>The user-mode display driver sets the <b>hContext</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544218">D3DDDICB_PRESENT</a> structure that is pointed to by the <i>pData</i> parameter to a context that it previously created by calling the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function. The user-mode display driver must create at least one context when the Microsoft Direct3D runtime calls the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a> or <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function to create a device. The Direct3D runtime sends the present operation to a created context.
     </p>

<p>
<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnPresentCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>
</p>

<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnPresentCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>

<p>The following code example shows how to color-fill a destination surface.</p>

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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544218">D3DDDICB_PRESENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544512">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_PRESENTCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
