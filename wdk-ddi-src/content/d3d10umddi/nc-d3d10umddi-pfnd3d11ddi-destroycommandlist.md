---
UID: NC.d3d10umddi.PFND3D11DDI_DESTROYCOMMANDLIST
title: PFND3D11DDI_DESTROYCOMMANDLIST
author: windows-driver-content
description: The DestroyCommandList function destroys a command list.
old-location: display\destroycommandlist.htm
old-project: display
ms.assetid: 9f03c193-f017-4189-a082-908e28a2e9f7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: DestroyCommandList is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DestroyCommandList
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

# PFND3D11DDI_DESTROYCOMMANDLIST callback



## -description
<p>The <b>DestroyCommandList</b> function destroys a command list.</p>


## -prototype

````
PFND3D11DDI_DESTROYCOMMANDLIST DestroyCommandList;

VOID APIENTRY DestroyCommandList(
  _In_ D3D10DDI_HDEVICE      hDevice,
  _In_ D3D11DDI_HCOMMANDLIST hCommandList
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>hCommandList</i> [in]

<dd>
<p> A handle to the driver's private data for the command list to destroy. The Microsoft Direct3D runtime frees the memory region that it previously allocated for the command list. Therefore, the driver can no longer access this memory region. </p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>The driver is only required to implement <b>DestroyCommandList</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a> function.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>DestroyCommandList</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

<p>The driver can implement a <b>DestroyCommandList</b> function that contains a <b>switch</b> statement to process the destruction of command lists and the lightweight destruction of command lists. That is, the driver can implement one <b>DestroyCommandList</b>, and can set the <b>pfnRecycleDestroyCommandList</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a> structure to point to <b>DestroyCommandList</b> along with the <b>pfnRecycleDestroyCommandList</b> member of D3D11DDI_DEVICEFUNCS to point to <b>DestroyCommandList</b>. However, to improve performance, the driver can implement separate <b>DestroyCommandList</b> and <b>RecycleDestroyCommandList</b> functions.</p>

<p>For more information about <b>RecycleDestroyCommandList</b>, see <a href="https://msdn.microsoft.com/7bede247-680d-4fd3-a10b-6ef63f0a88ec">Optimization for Small Command Lists</a>.</p>

<p>The driver is only required to implement <b>DestroyCommandList</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a> function.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <b>DestroyCommandList</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

<p>The driver can implement a <b>DestroyCommandList</b> function that contains a <b>switch</b> statement to process the destruction of command lists and the lightweight destruction of command lists. That is, the driver can implement one <b>DestroyCommandList</b>, and can set the <b>pfnRecycleDestroyCommandList</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a> structure to point to <b>DestroyCommandList</b> along with the <b>pfnRecycleDestroyCommandList</b> member of D3D11DDI_DEVICEFUNCS to point to <b>DestroyCommandList</b>. However, to improve performance, the driver can implement separate <b>DestroyCommandList</b> and <b>RecycleDestroyCommandList</b> functions.</p>

<p>For more information about <b>RecycleDestroyCommandList</b>, see <a href="https://msdn.microsoft.com/7bede247-680d-4fd3-a10b-6ef63f0a88ec">Optimization for Small Command Lists</a>.</p>

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
<p>DestroyCommandList is supported beginning with the Windows 7 operating system. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createcommandlist.md">CreateCommandList</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_DESTROYCOMMANDLIST callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
