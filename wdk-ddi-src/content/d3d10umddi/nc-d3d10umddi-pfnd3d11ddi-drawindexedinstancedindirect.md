---
UID: NC.d3d10umddi.PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT
title: PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT
author: windows-driver-content
description: The DrawIndexedInstancedIndirect function draws particular instances of indexed primitives.
old-location: display\drawindexedinstancedindirect.htm
old-project: display
ms.assetid: 3debfb11-4de9-456b-a094-feb2f68e96a5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: DrawIndexedInstancedIndirect is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DrawIndexedInstancedIndirect
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

# PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT callback



## -description
<p>The <b>DrawIndexedInstancedIndirect</b> function draws particular instances of indexed primitives. </p>


## -prototype

````
PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT DrawIndexedInstancedIndirect;

VOID  APIENTRY DrawIndexedInstancedIndirect(
   D3D10DDI_HDEVICE   hDevice,
   D3D10DDI_HRESOURCE hBufferForArgs,
   UINT               AlignedByteOffsetForArgs
)
{ ... }
````


## -parameters
<dl>

### -param hDevice 

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param hBufferForArgs 

<dd>
<p> A handle to a buffer that contains the arguments for <b>DrawIndexedInstancedIndirect</b> to process. The buffer contains the following tightly packed structure:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>struct DrawIndexedInstancedIndirectArgs {
  UINT IndexCountPerInstance; 
  UINT InstanceCount;
  UINT StartIndexLocation;
  INT BaseVertexLocation;
  UINT StartInstanceLocation;
}</pre>
</td>
</tr>
</table></span></div>
<p>For more information about these arguments, see the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawindexedinstanced.md">DrawIndexedInstanced</a> reference page. </p>
</dd>

### -param AlignedByteOffsetForArgs 

<dd>
<p> The offset, in bytes, into the buffer that <i>hBufferForArgs</i> specifies. <i>AlignedByteOffsetForArgs</i> must be a multiple of 4. </p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the Remarks section. </p>

## -remarks
<p>The <b>DrawIndexedInstancedIndirect</b> function performs the same task as the call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawindexedinstanced.md">DrawIndexedInstanced</a> function. However, <b>DrawIndexedInstancedIndirect</b> obtains information about the index primitives from the contents of the buffer that the <i>hBufferForArgs</i> parameter specifies. <b>DrawIndexedInstancedIndirect</b> reads the contents of the buffer, starting at the byte offset that the <i>AlignedByteOffsetForArgs</i> parameter specifies.</p>

<p>When the Direct3D runtime calls the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function to create the buffer resource that the <i>hBufferForArgs</i> parameter specifies, the runtime must set the D3D11_DDI_RESOURCE_MISC_DRAWINDIRECT_ARGS flag in the <b>MiscFlags</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg-createresource.md">D3D11DDIARG_CREATERESOURCE</a> structure.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>DrawIndexedInstancedIndirect</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

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
<p>DrawIndexedInstancedIndirect is supported beginning with the Windows 7 operating system. </p>
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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg-createresource.md">D3D11DDIARG_CREATERESOURCE</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-drawindexedinstanced.md">DrawIndexedInstanced</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_DRAWINDEXEDINSTANCEDINDIRECT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
