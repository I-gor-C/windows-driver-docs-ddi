---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTARGETMODESET_RELEASEMODEINFO
title: DXGKDDI_VIDPNTARGETMODESET_RELEASEMODEINFO
author: windows-driver-content
description: The pfnReleaseModeInfo function releases a D3DKMDT_VIDPN_TARGET_MODE structure that the VidPN manager previously provided to the display miniport driver.
old-location: display\dxgk_vidpntargetmodeset_interface_pfnreleasemodeinfo.htm
old-project: display
ms.assetid: 0b1d0331-f0fa-40fc-a1d6-15fe3568f3cc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnReleaseModeInfo
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
req.iface: 
---

# DXGKDDI_VIDPNTARGETMODESET_RELEASEMODEINFO callback



## -description
<p>The <b>pfnReleaseModeInfo</b> function releases a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-target-mode.md">D3DKMDT_VIDPN_TARGET_MODE</a> structure that the VidPN manager previously provided to the display miniport driver.</p>


## -prototype

````
DXGKDDI_VIDPNTARGETMODESET_RELEASEMODEINFO pfnReleaseModeInfo;

NTSTATUS APIENTRY pfnReleaseModeInfo(
  _In_ const D3DKMDT_HVIDPNTARGETMODESET     hVidPnTargetModeSet,
  _In_ const D3DKMDT_VIDPN_TARGET_MODE CONST *pVidPnTargetModeInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPnTargetModeSet</i> [in]

<dd>
<p>[in] A handle to a VidPN target mode set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a> function of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpn-interface.md">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param <i>pVidPnTargetModeInfo</i> [in]

<dd>
<p>[in] A pointer to the D3DKMDT_VIDPN_TARGET_MODE structure that is to be released.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnReleaseModeInfo</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded. </p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TARGETMODESET</b></dt>
</dl><p>The handle supplied in <i>hVidPnTargetModeSet</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET_MODE</b></dt>
</dl><p>The pointer supplied in <i>pVidPnTargetModeInfo</i> was invalid.</p>

<p> </p>

## -remarks
<p>When you have finished using a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-target-mode.md">D3DKMDT_VIDPN_TARGET_MODE</a> structure that you obtained by calling any of the following functions, you must release the structure by calling <b>pfnReleaseModeInfo</b>.</p>

<p>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirefirstmodeinfo.md">pfnAcquireFirstModeInfo</a>
</p>

<p>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirenextmodeinfo.md">pfnAcquireNextModeInfo</a>
</p>

<p>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirepinnedmodeinfo.md">pfnAcquirePinnedModeInfo</a>
</p>

<p>If you obtain a D3DKMDT_VIDPN_TARGET_MODE structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-createnewmodeinfo.md">pfnCreateNewModeInfo</a> and then pass that structure to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-addmode.md">pfnAddMode</a>, you do not need to release the structure.</p>

<p>If you obtain a handle by calling <b>pfnCreateNewModeInfo</b> and then you decide not to add the new mode to a target mode set, you must release the newly created structure by calling <b>pfnReleaseModeInfo</b>.</p>

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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirefirstmodeinfo.md">pfnAcquireFirstModeInfo</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirenextmodeinfo.md">pfnAcquireNextModeInfo</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirepinnedmodeinfo.md">pfnAcquirePinnedModeInfo</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-target-mode.md">D3DKMDT_VIDPN_TARGET_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNTARGETMODESET_RELEASEMODEINFO callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
