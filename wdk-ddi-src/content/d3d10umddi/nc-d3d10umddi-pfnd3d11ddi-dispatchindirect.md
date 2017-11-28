---
UID: NC.d3d10umddi.PFND3D11DDI_DISPATCHINDIRECT
title: PFND3D11DDI_DISPATCHINDIRECT
author: windows-driver-content
description: The DispatchIndirect function executes the compute shader.
old-location: display\dispatchindirect.htm
old-project: display
ms.assetid: 0c818515-163f-48ba-ad57-f4405672c98f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: DispatchIndirect is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DispatchIndirect
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

# PFND3D11DDI_DISPATCHINDIRECT callback



## -description
<p>The <b>DispatchIndirect</b> function executes the compute shader.</p>


## -prototype

````
PFND3D11DDI_DISPATCHINDIRECT DispatchIndirect;

VOID APIENTRY DispatchIndirect(
  _In_ D3D10DDI_HDEVICE   hDevice,
  _In_ D3D10DDI_HRESOURCE hBufferForArgs,
  _In_ UINT               AlignedByteOffsetForArgs
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>hBufferForArgs</i> [in]

<dd>
<p> A handle to a buffer that contains three UINT values that hold the sizes, in thread groups, of the X, Y, and Z dimensions of the thread-group grid. The buffer contains the following tightly packed structure:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>struct DispatchArgs {
  UINT ThreadGroupCountX; 
  UINT ThreadGroupCountY;
  UINT ThreadGroupCountZ;
}</pre>
</td>
</tr>
</table></span></div>
</dd>

### -param <i>AlignedByteOffsetForArgs</i> [in]

<dd>
<p> The offset, in bytes, into the buffer that <i>hBufferForArgs</i> specifies. <i>AlignedByteOffsetForArgs</i> must be a multiple of 4.</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>The DispatchIndirect function performs the same task as the call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-dispatch.md">Dispatch</a> function. The Direct3D runtime calls the driver's <b>DispatchIndirect</b> function on the display device to execute the compute shader over a number of threads in a grid of thread groups. However, <b>DispatchIndirect</b> obtains the number of thread groups to execute from the contents of the buffer that the <i>hBufferForArgs</i> parameter specifies.  <b>DispatchIndirect</b> reads three UINT values, starting at the byte offset that the <i>AlignedByteOffsetForArgs</i> parameter specifies.</p>

<p>When the Direct3D runtime calls the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function to create the buffer resource that the <i>hBufferForArgs</i> parameter specifies, the runtime must set the D3D11_DDI_RESOURCE_MISC_DRAWINDIRECT_ARGS flag in the <b>MiscFlags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a> structure.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>DispatchIndirect</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

<p>The DispatchIndirect function performs the same task as the call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-dispatch.md">Dispatch</a> function. The Direct3D runtime calls the driver's <b>DispatchIndirect</b> function on the display device to execute the compute shader over a number of threads in a grid of thread groups. However, <b>DispatchIndirect</b> obtains the number of thread groups to execute from the contents of the buffer that the <i>hBufferForArgs</i> parameter specifies.  <b>DispatchIndirect</b> reads three UINT values, starting at the byte offset that the <i>AlignedByteOffsetForArgs</i> parameter specifies.</p>

<p>When the Direct3D runtime calls the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function to create the buffer resource that the <i>hBufferForArgs</i> parameter specifies, the runtime must set the D3D11_DDI_RESOURCE_MISC_DRAWINDIRECT_ARGS flag in the <b>MiscFlags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a> structure.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>DispatchIndirect</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

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
<p>DispatchIndirect is supported beginning with the Windows 7 operating system. </p>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542062">D3D11DDIARG_CREATERESOURCE</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-dispatch.md">Dispatch</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_DISPATCHINDIRECT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
