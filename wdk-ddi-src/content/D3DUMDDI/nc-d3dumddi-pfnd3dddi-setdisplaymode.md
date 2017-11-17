---
UID: NC.d3dumddi.PFND3DDDI_SETDISPLAYMODE
title: PFND3DDDI_SETDISPLAYMODE
author: windows-driver-content
description: The SetDisplayMode function switches to a display mode or primary that is not supported by the GDI desktop.
old-location: display\setdisplaymode.htm
ms.assetid: d0e409fe-1c64-4468-b52e-b0ede39f6601
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
req.alt-api: SetDisplayMode
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

# PFND3DDDI_SETDISPLAYMODE callback



## -description
<p>The <i>SetDisplayMode</i> function switches to a display mode or primary that is not supported by the GDI desktop.</p>


## -prototype

````
PFND3DDDI_SETDISPLAYMODE SetDisplayMode;

__checkReturn HRESULT APIENTRY SetDisplayMode(
  _In_       HANDLE                   hDevice,
  _In_ const D3DDDIARG_SETDISPLAYMODE *pData
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
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543304">D3DDDIARG_SETDISPLAYMODE</a> structure that specifies parameters for setting the display mode.</p>
</dd>
</dl>

## -returns
<p><i>SetDisplayMode</i> returns S_OK or an appropriate error result if the display mode is not successfully set.</p>

## -remarks
<p>The Microsoft Direct3D runtime calls <i>SetDisplayMode</i> to switch to a display mode or primary that is not supported by the GDI desktop. The following list describes examples of such primaries: </p>

<p>Primaries that are created with 10-bits-per-channel (10:10:10:2) display and render target formats (for example, D3DFMT_A2R10G10B10)</p>

<p>Multiple-sampled primaries where the multiple-sampling is performed while scanning-out </p>

<p>Persistent primaries that are used by full-screen Microsoft DirectX version 9.L applications </p>

<p>The Direct3D runtime calls the user-mode display driver's <a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a> function to create the primary to be scanned out. However, the driver should program the hardware to scan out only when its <i>SetDisplayMode</i> function is called. Therefore, the runtime sets the <b>hResource</b> and <b>SubResourceIndex</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543304">D3DDDIARG_SETDISPLAYMODE</a> structure that is pointed to by the <i>pData</i> parameter to the primary that was created through the call to the driver's <i>CreateResource</i> function. The driver should then translate the primary that is represented by <b>hResource</b> and <b>SubResourceIndex</b> to a primary allocation handle. After the driver makes this translation, the driver should pass the resulting handle in a call to the <a href="https://msdn.microsoft.com/a1f58757-809d-4351-8b1a-fd4420981c24">pfnSetDisplayModeCb</a> function, which then initiates a call to the display miniport driver's <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a> function. </p>

<p>The user-mode display driver can set the <b>hPrimaryAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544255">D3DDDICB_SETDISPLAYMODE</a> structure in the call to <b>pfnSetDisplayModeCb</b> to scan out any allocation. However, the allocation must be marked as a primary (that is, the user-mode display driver must have set the <b>Primary</b> bit-field flag in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544364">D3DDDI_ALLOCATIONINFO</a> structure in a call to the <a href="https://msdn.microsoft.com/a61e6c6a-3992-429c-ad8c-5f1a61dc7b8b">pfnAllocateCb</a> function to create the allocation).</p>

<p>The Microsoft Direct3D runtime calls <i>SetDisplayMode</i> to switch to a display mode or primary that is not supported by the GDI desktop. The following list describes examples of such primaries: </p>

<p>Primaries that are created with 10-bits-per-channel (10:10:10:2) display and render target formats (for example, D3DFMT_A2R10G10B10)</p>

<p>Multiple-sampled primaries where the multiple-sampling is performed while scanning-out </p>

<p>Persistent primaries that are used by full-screen Microsoft DirectX version 9.L applications </p>

<p>The Direct3D runtime calls the user-mode display driver's <a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a> function to create the primary to be scanned out. However, the driver should program the hardware to scan out only when its <i>SetDisplayMode</i> function is called. Therefore, the runtime sets the <b>hResource</b> and <b>SubResourceIndex</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543304">D3DDDIARG_SETDISPLAYMODE</a> structure that is pointed to by the <i>pData</i> parameter to the primary that was created through the call to the driver's <i>CreateResource</i> function. The driver should then translate the primary that is represented by <b>hResource</b> and <b>SubResourceIndex</b> to a primary allocation handle. After the driver makes this translation, the driver should pass the resulting handle in a call to the <a href="https://msdn.microsoft.com/a1f58757-809d-4351-8b1a-fd4420981c24">pfnSetDisplayModeCb</a> function, which then initiates a call to the display miniport driver's <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a> function. </p>

<p>The user-mode display driver can set the <b>hPrimaryAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544255">D3DDDICB_SETDISPLAYMODE</a> structure in the call to <b>pfnSetDisplayModeCb</b> to scan out any allocation. However, the allocation must be marked as a primary (that is, the user-mode display driver must have set the <b>Primary</b> bit-field flag in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544364">D3DDDI_ALLOCATIONINFO</a> structure in a call to the <a href="https://msdn.microsoft.com/a61e6c6a-3992-429c-ad8c-5f1a61dc7b8b">pfnAllocateCb</a> function to create the allocation).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543304">D3DDDIARG_SETDISPLAYMODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a1f58757-809d-4351-8b1a-fd4420981c24">pfnSetDisplayModeCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETDISPLAYMODE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
