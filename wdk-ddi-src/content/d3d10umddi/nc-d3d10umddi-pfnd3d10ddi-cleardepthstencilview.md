---
UID: NC.d3d10umddi.PFND3D10DDI_CLEARDEPTHSTENCILVIEW
title: PFND3D10DDI_CLEARDEPTHSTENCILVIEW
author: windows-driver-content
description: The ClearDepthStencilView function clears the specified currently bound depth-stencil view.
old-location: display\cleardepthstencilview.htm
old-project: display
ms.assetid: 0474c154-1bec-4602-880c-ffdc48c738f0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClearDepthStencilView
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

# PFND3D10DDI_CLEARDEPTHSTENCILVIEW callback



## -description
<p>The <b>ClearDepthStencilView</b> function clears the specified currently bound depth-stencil view. </p>


## -prototype

````
PFND3D10DDI_CLEARDEPTHSTENCILVIEW ClearDepthStencilView;

VOID APIENTRY ClearDepthStencilView(
  _In_ D3D10DDI_HDEVICE           hDevice,
  _In_ D3D10DDI_HDEPTHSTENCILVIEW hDepthStencilView,
  _In_ UINT                       Flags,
  _In_ FLOAT                      Depth,
  _In_ UINT8                      Stencil
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>hDepthStencilView</i> [in]

<dd>
<p> A handle to the depth-stencil view to clear. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p> A value that specifies which parts of the buffer to affect. This parameter must be set to one of the following values from the D3D10_DDI_CLEAR_FLAG enumeration.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3D10_DDI_CLEAR_DEPTH (0x01L)</p>
</td>
<td>
<p>The depth value (Z) is clamped to the ZNear and ZFar range of the viewport that is currently bound to slot zero by using Microsoft Direct3D. Afterwards, Z is clamped again to the representable range of the currently bound depth-stencil view by again using Direct3D.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_DDI_CLEAR_STENCIL (0x02L)</p>
</td>
<td>
<p>The stencil value is cleared.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Depth</i> [in]

<dd>
<p> A single-precision float vector to set the depth to. </p>
</dd>

### -param <i>Stencil</i> [in]

<dd>
<p> An unsigned 8-bit integer value to set the stencil to. </p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>Floating point rules apply to the <b>ClearDepthStencilView</b> function. </p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <b>ClearDepthStencilView</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

<p>Floating point rules apply to the <b>ClearDepthStencilView</b> function. </p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <b>ClearDepthStencilView</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CLEARDEPTHSTENCILVIEW callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
