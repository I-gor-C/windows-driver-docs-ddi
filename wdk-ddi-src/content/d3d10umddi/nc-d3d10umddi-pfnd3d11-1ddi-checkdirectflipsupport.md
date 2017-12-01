---
UID: NC.d3d10umddi.PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT
title: PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT
author: windows-driver-content
description: Called by the Desktop Window Manager (DWM) to verify that the user-mode driver supports Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the DWM's managed primary allocations.
old-location: display\checkdirectflipsupport_d3d11_1_.htm
old-project: display
ms.assetid: 2acf84cb-5e51-4aa8-96ce-96abc6ceec8c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CheckDirectFlipSupport(D3D11_1)
req.alt-loc: D3d10umddi.h
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

# PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT callback



## -description
<p>Called by the Desktop Window Manager (DWM) to verify that the user-mode driver supports Direct Flip operations, in which video memory is seamlessly flipped between an application's managed primary allocations and the DWM's managed primary allocations.</p>


## -prototype

````
PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT CheckDirectFlipSupport(D3D11_1);

VOID APIENTRY* CheckDirectFlipSupport(D3D11_1)(
        D3D10DDI_HDEVICE   hDevice,
        D3D10DDI_HRESOURCE hResource1,
        D3D10DDI_HRESOURCE hResource2,
        UINT               CheckDirectFlipFlags,
  _Out_ BOOL               *pSupported
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> 

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>hResource1</i> 

<dd>
<p>A resource in the application's swapchain.</p>
</dd>

### -param <i>hResource2</i> 

<dd>
<p>A resource in the DWM's swapchain.</p>
</dd>

### -param <i>CheckDirectFlipFlags</i> 

<dd>
<p>If this parameter has a value of <b>D3D11_1DDI_CHECK_DIRECT_FLIP_IMMEDIATE</b>, seamless flipping should occur immediately and does not have to be synchronized with a VSync interrupt.</p>
</dd>

### -param <i>pSupported</i> [out]

<dd>
<p>Set to <b>TRUE</b> if the driver can seamlessly flip video memory between  an application's managed primary allocations and the DWM's managed primary allocations. Otherwise, set to <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>This function is called at least once before the DWM attempts to present to a Direct Flip swapchain. It is also called after each mode change occurs, or after the DWM re-creates its own swapchain for any reason.</p>

<p>The user-mode driver should ensure that the managed primary allocations of the application and the DWM have the following compatible resources:</p>

<p>The user-mode driver might need to call the kernel-mode driver to perform these validations. To do this, call the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a> callback function and then call the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandledata.md">DxgkCbGetHandleData</a> function to access the kernel-mode driver's resource allocation data.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d11-1-ddi-check-direct-flip-flags.md">D3D11_1_DDI_CHECK_DIRECT_FLIP_FLAGS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-allocationinfo.md">D3DDDI_ALLOCATIONINFO</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandledata.md">DxgkCbGetHandleData</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-escapecb.md">pfnEscapeCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CHECKDIRECTFLIPSUPPORT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
