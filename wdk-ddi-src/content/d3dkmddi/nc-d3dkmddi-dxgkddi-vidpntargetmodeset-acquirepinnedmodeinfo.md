---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTARGETMODESET_ACQUIREPINNEDMODEINFO
title: DXGKDDI_VIDPNTARGETMODESET_ACQUIREPINNEDMODEINFO
author: windows-driver-content
description: The pfnAcquirePinnedModeInfo function returns a descriptor of the pinned mode in a specified VidPN target mode set.
old-location: display\dxgk_vidpntargetmodeset_interface_pfnacquirepinnedmodeinfo.htm
old-project: display
ms.assetid: 0a321ee2-f246-498d-b658-a01e275644be
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
req.alt-api: pfnAcquirePinnedModeInfo
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

# DXGKDDI_VIDPNTARGETMODESET_ACQUIREPINNEDMODEINFO callback



## -description
<p>The <b>pfnAcquirePinnedModeInfo</b> function returns a descriptor of the pinned mode in a specified VidPN target mode set.</p>


## -prototype

````
DXGKDDI_VIDPNTARGETMODESET_ACQUIREPINNEDMODEINFO pfnAcquirePinnedModeInfo;

NTSTATUS APIENTRY pfnAcquirePinnedModeInfo(
  _In_  const D3DKMDT_HVIDPNTARGETMODESET hVidPnTargetModeSet,
  _Out_ const D3DKMDT_VIDPN_TARGET_MODE   **ppPinnedVidPnTargetModeInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPnTargetModeSet</i> [in]

<dd>
<p>[in] A handle to a VidPN target mode set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562108">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param <i>ppPinnedVidPnTargetModeInfo</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546729">D3DKMDT_VIDPN_TARGET_MODE</a> structure. The structure contains a variety of information about the pinned mode, including its ID and video signal characteristics. If the target mode set identified by <i>hVidPnTargetModeSet</i> has no pinned mode, then this variable receives a <b>NULL</b> pointer.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnAcquirePinnedModeInfo</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded by doing one of the following:</p>

<p>Setting <i>ppPinnedVidPnTargetModeInfo</i> to the address of D3DKMDT_VIDPN_TARGET_MODE structure that describes the pinned mode.</p>

<p>Setting <i>ppPinnedVidPnTargetModeInfo</i> to <b>NULL</b> to indicate that the target mode set has no pinned mode. </p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TARGETMODESET</b></dt>
</dl><p>The handle supplied in <i>hVidPnTargetModeSet</i> was invalid.</p>

<p> </p>

## -remarks
<p>When you have finished using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546729">D3DKMDT_VIDPN_TARGET_MODE</a> structure, you must release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-releasemodeinfo.md">pfnReleaseModeInfo</a>.</p>

<p>The D3DKMDT_HVIDPNTARGETMODESET data type is defined in <i>D3dkmdt.h</i>. </p>

<p>When you have finished using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546729">D3DKMDT_VIDPN_TARGET_MODE</a> structure, you must release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-releasemodeinfo.md">pfnReleaseModeInfo</a>.</p>

<p>The D3DKMDT_HVIDPNTARGETMODESET data type is defined in <i>D3dkmdt.h</i>. </p>

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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-releasemodeinfo.md">pfnReleaseModeInfo</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-pinmode.md">pfnPinMode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546729">D3DKMDT_VIDPN_TARGET_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNTARGETMODESET_ACQUIREPINNEDMODEINFO callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
