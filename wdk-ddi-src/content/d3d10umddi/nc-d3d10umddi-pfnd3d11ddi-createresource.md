---
UID: NC.d3d10umddi.PFND3D11DDI_CREATERESOURCE
title: PFND3D11DDI_CREATERESOURCE
author: windows-driver-content
description: Creates a resource.
old-location: display\createresource_d3d11_.htm
old-project: display
ms.assetid: 2dff9d2e-c497-422f-824b-a7101904fd67
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateResource(D3D11) is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CreateResource
req.alt-loc: d3d10umddi.h
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

# PFND3D11DDI_CREATERESOURCE callback



## -description
<p>Creates a resource.</p>


## -prototype

````
PFND3D11DDI_CREATERESOURCE CreateResource;

VOID APIENTRY CreateResource(
  _In_       D3D10DDI_HDEVICE           hDevice,
  _In_ const D3D11DDIARG_CREATERESOURCE *pCreateResource,
  _In_       D3D10DDI_HRESOURCE         hResource,
  _In_       D3D10DDI_HRTRESOURCE       hRTResource
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pCreateResource</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a> structure that describes the parameters that the user-mode display driver uses to create a resource. </p>
</dd>

### -param <i>hResource</i> [in]

<dd>
<p> A handle to the driver's private data for the resource. The driver returns the size, in bytes, of the memory region that the Microsoft Direct3D runtime must allocate for the private data from a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivateresourcesize.md">CalcPrivateResourceSize(D3D11)</a> function. The handle is  just a pointer to a region of memory, the size of which the driver requested. The driver uses this region of memory to store internal data structures that are related to its resource object. </p>
</dd>

### -param <i>hRTResource</i> [in]

<dd>
<p> A handle to the resource that the driver will use when it calls back into the Direct3D runtime. </p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see Remarks.</p>

## -remarks
<p>The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function. The driver can also pass DXGI_DDI_ERR_UNSUPPORTED in a call to <b>pfnSetErrorCb</b>. For more information about passing DXGI_DDI_ERR_UNSUPPORTED, see the Remarks section of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a> reference page. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyresource.md">DestroyResource(D3D10)</a> function to destroy the handle that the <i>hResource</i> parameter specifies.</p>

<p>The runtime validates all parameters against the parameters that an application sent to create the resource. Therefore, the driver should not receive invalid combinations.</p>

<p>If the application does not require the contents of the resource to persist across presentations, the runtime sets the D3D10_DDI_RESOURCE_MISC_DISCARD_ON_PRESENT flag of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542004">D3D10_DDI_RESOURCE_MISC_FLAG</a> enumeration in the <b>MiscFlags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a> structure that the <i>pCreateResource</i> parameter points to. Presentation occurs when the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff569179">PresentDXGI</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a> (with the <b>Present</b> flag set in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557451">DXGI_DDI_ARG_BLT_FLAGS</a> structure) function is called. The runtime uses the D3D10_DDI_RESOURCE_MISC_DISCARD_ON_PRESENT flag to create swap-chain back buffers when an application uses the DXGI_SWAP_EFFECT_DISCARD value to request swap chains. </p>

<p>Starting in Windows 8, if the driver must create a stereo back buffer, it must set members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a> structure pointed to by <i>pCreateResource</i> as follows:</p>

<p>Additionally, to support stereo presentation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a> function must allow any values for the <b>DstSubresource</b> and <b>SrcSubresource</b> members of  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557447">DXGI_DDI_ARG_BLT</a> structure that are within the range of the source and destination resources.</p>

<p>For Windows Display Driver Model (WDDM) 1.3 and later drivers, the Microsoft Direct3D runtime supplies a restricted set of input values used by this function. For a list of all restricted values, see <a href="https://msdn.microsoft.com/F9AAE489-EC45-4EE6-875E-E084BB3054EE">Direct3D rendering performance improvements</a>.</p>

<p>The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function. The driver can also pass DXGI_DDI_ERR_UNSUPPORTED in a call to <b>pfnSetErrorCb</b>. For more information about passing DXGI_DDI_ERR_UNSUPPORTED, see the Remarks section of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a> reference page. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyresource.md">DestroyResource(D3D10)</a> function to destroy the handle that the <i>hResource</i> parameter specifies.</p>

<p>The runtime validates all parameters against the parameters that an application sent to create the resource. Therefore, the driver should not receive invalid combinations.</p>

<p>If the application does not require the contents of the resource to persist across presentations, the runtime sets the D3D10_DDI_RESOURCE_MISC_DISCARD_ON_PRESENT flag of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542004">D3D10_DDI_RESOURCE_MISC_FLAG</a> enumeration in the <b>MiscFlags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a> structure that the <i>pCreateResource</i> parameter points to. Presentation occurs when the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff569179">PresentDXGI</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a> (with the <b>Present</b> flag set in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557451">DXGI_DDI_ARG_BLT_FLAGS</a> structure) function is called. The runtime uses the D3D10_DDI_RESOURCE_MISC_DISCARD_ON_PRESENT flag to create swap-chain back buffers when an application uses the DXGI_SWAP_EFFECT_DISCARD value to request swap chains. </p>

<p>Starting in Windows 8, if the driver must create a stereo back buffer, it must set members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a> structure pointed to by <i>pCreateResource</i> as follows:</p>

<p>Additionally, to support stereo presentation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a> function must allow any values for the <b>DstSubresource</b> and <b>SrcSubresource</b> members of  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557447">DXGI_DDI_ARG_BLT</a> structure that are within the range of the source and destination resources.</p>

<p>For Windows Display Driver Model (WDDM) 1.3 and later drivers, the Microsoft Direct3D runtime supplies a restricted set of input values used by this function. For a list of all restricted values, see <a href="https://msdn.microsoft.com/F9AAE489-EC45-4EE6-875E-E084BB3054EE">Direct3D rendering performance improvements</a>.</p>

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
<p>CreateResource(D3D11) is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538252">BltDXGI</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-calcprivateresourcesize.md">CalcPrivateResourceSize(D3D11)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542004">D3D10_DDI_RESOURCE_MISC_FLAG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-destroyresource.md">DestroyResource(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557447">DXGI_DDI_ARG_BLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557451">DXGI_DDI_ARG_BLT_FLAGS</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569179">PresentDXGI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_CREATERESOURCE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
