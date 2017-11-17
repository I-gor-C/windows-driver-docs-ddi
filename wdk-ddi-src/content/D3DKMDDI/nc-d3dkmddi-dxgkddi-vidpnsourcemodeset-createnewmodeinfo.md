---
UID: NC.d3dkmddi.DXGKDDI_VIDPNSOURCEMODESET_CREATENEWMODEINFO
title: DXGKDDI_VIDPNSOURCEMODESET_CREATENEWMODEINFO
author: windows-driver-content
description: The pfnCreateNewModeInfo function returns a pointer to a D3DKMDT_VIDPN_SOURCE_MODE structure that the display miniport driver populates before calling pfnAddMode.
old-location: display\dxgk_vidpnsourcemodeset_interface_pfncreatenewmodeinfo.htm
ms.assetid: b18aab68-7457-45eb-8641-0b6180cfa70e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnCreateNewModeInfo
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGKDDI_VIDPNSOURCEMODESET_CREATENEWMODEINFO callback



## -description
<p>The <b>pfnCreateNewModeInfo</b> function returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure that the display miniport driver populates before calling <a href="https://msdn.microsoft.com/754078c2-f79b-4237-a14c-96903856f3a5">pfnAddMode</a>.</p>


## -prototype

````
DXGKDDI_VIDPNSOURCEMODESET_CREATENEWMODEINFO pfnCreateNewModeInfo;

NTSTATUS APIENTRY pfnCreateNewModeInfo(
  _In_  const D3DKMDT_HVIDPNSOURCEMODESET hVidPnSourceModeSet,
  _Out_       PPD3DKMDT_VIDPN_SOURCE_MODE ppNewVidPnSourceModeInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPnSourceModeSet</i> [in]

<dd>
<p>[in] A handle to a VidPN source mode set object. The display miniport driver previously obtained this handle by calling the <a href="https://msdn.microsoft.com/cf19f468-86c1-4cc9-8945-e23f73a85c91">pfnAcquireSourceModeSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562108">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param <i>ppNewVidPnSourceModeInfo</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a D3DKMDT_VIDPN_SOURCE_MODE structure allocated by the VidPN manager.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnCreateNewModeInfo</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded. </p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_SOURCEMODESET</b></dt>
</dl><p>The handle supplied in <i>hVidPnSourceModeSet</i> was invalid.</p>

<p> </p>

## -remarks
<p>The <b>pfnCreateNewModeInfo</b> function allocates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure, sets its <b>Id</b> member to a newly generated identifier, and sets its <b>Type</b> member to <b>D3DKMDT_RMT_UNINITIALIZED</b>.</p>

<p>After you call <b>pfnCreateNewModeInfo</b> to obtain a D3DKMDT_VIDPN_SOURCE_MODE structure, you must do one, but not both, of the following:</p>

<p>Populate the structure and pass it to <a href="https://msdn.microsoft.com/754078c2-f79b-4237-a14c-96903856f3a5">pfnAddMode</a>.</p>

<p>Release the structure by calling <a href="https://msdn.microsoft.com/614283cc-90bf-44f2-bab2-1aeec5e7de01">pfnReleaseModeInfo</a>.</p>

<p>When you populate a D3DKMDT_VIDPN_SOURCE_MODE structure, you have the option of overwriting the <b>Id</b> member that was generated and set by <b>pfnCreateNewModeInfo</b>. However, if you overwrite the <b>Id</b> member of any D3DKMDT_VIDPN_SOURCE_MODE structure, you must overwrite the <b>Id</b> members of all the D3DKMDT_VIDPN_SOURCE_MODE structures you obtain from <b>pfnCreateNewModeInfo</b>. Unless you have a specific reason for overwriting the <b>Id</b> members (for example, tracking source modes with your own numbering scheme), you should leave them as set by <b>pfnCreateNewModeInfo</b>.</p>

<p>The D3DKMDT_HVIDPNSOURCEMODESET data type is defined in <i>D3dkmdt.h</i>. </p>

<p>The <b>pfnCreateNewModeInfo</b> function allocates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a> structure, sets its <b>Id</b> member to a newly generated identifier, and sets its <b>Type</b> member to <b>D3DKMDT_RMT_UNINITIALIZED</b>.</p>

<p>After you call <b>pfnCreateNewModeInfo</b> to obtain a D3DKMDT_VIDPN_SOURCE_MODE structure, you must do one, but not both, of the following:</p>

<p>Populate the structure and pass it to <a href="https://msdn.microsoft.com/754078c2-f79b-4237-a14c-96903856f3a5">pfnAddMode</a>.</p>

<p>Release the structure by calling <a href="https://msdn.microsoft.com/614283cc-90bf-44f2-bab2-1aeec5e7de01">pfnReleaseModeInfo</a>.</p>

<p>When you populate a D3DKMDT_VIDPN_SOURCE_MODE structure, you have the option of overwriting the <b>Id</b> member that was generated and set by <b>pfnCreateNewModeInfo</b>. However, if you overwrite the <b>Id</b> member of any D3DKMDT_VIDPN_SOURCE_MODE structure, you must overwrite the <b>Id</b> members of all the D3DKMDT_VIDPN_SOURCE_MODE structures you obtain from <b>pfnCreateNewModeInfo</b>. Unless you have a specific reason for overwriting the <b>Id</b> members (for example, tracking source modes with your own numbering scheme), you should leave them as set by <b>pfnCreateNewModeInfo</b>.</p>

<p>The D3DKMDT_HVIDPNSOURCEMODESET data type is defined in <i>D3dkmdt.h</i>. </p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/754078c2-f79b-4237-a14c-96903856f3a5">pfnAddMode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/614283cc-90bf-44f2-bab2-1aeec5e7de01">pfnReleaseModeInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNSOURCEMODESET_CREATENEWMODEINFO callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
