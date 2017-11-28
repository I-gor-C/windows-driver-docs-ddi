---
UID: NC.d3d10umddi.PFND3D11DDI_ABANDONCOMMANDLIST
title: PFND3D11DDI_ABANDONCOMMANDLIST
author: windows-driver-content
description: The AbandonCommandList function abandons the command list.
old-location: display\abandoncommandlist.htm
old-project: display
ms.assetid: fc8347da-25ac-47ea-b482-61b7873ca5bc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: AbandonCommandList is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AbandonCommandList
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

# PFND3D11DDI_ABANDONCOMMANDLIST callback



## -description
<p>The <b>AbandonCommandList</b> function abandons the command list. </p>


## -prototype

````
PFND3D11DDI_ABANDONCOMMANDLIST AbandonCommandList;

VOID APIENTRY AbandonCommandList(
  _In_ D3D10DDI_HDEVICE hDevice
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set a critical error code. For more information about setting error codes, see the Remarks section.</p>

## -remarks
<p>After a deferred context is abandoned, the Direct3D runtime calls <b>AbandonCommandList</b> to abandon the command list that is associated with the deferred context. <b>AbandonCommandList</b> can apply state into whatever the driver prefers. </p>

<p>The driver is only required to implement <b>AbandonCommandList</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a> function.</p>

<p>After a deferred context is abandoned, the Direct3D runtime calls <b>AbandonCommandList</b> to abandon the command list that is associated with the deferred context. <b>AbandonCommandList</b> can apply state into whatever the driver prefers. </p>

<p>The driver is only required to implement <b>AbandonCommandList</b> if the driver supports the D3D11DDICAPS_COMMANDLISTS_BUILD_2 capability that can be returned in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure from a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a> function.</p>

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
<p>AbandonCommandList is supported beginning with the Windows 7 operating system. </p>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_ABANDONCOMMANDLIST callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
