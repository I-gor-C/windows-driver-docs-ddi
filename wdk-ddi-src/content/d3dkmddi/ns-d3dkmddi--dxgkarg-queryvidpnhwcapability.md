---
UID: NS.d3dkmddi._DXGKARG_QUERYVIDPNHWCAPABILITY
title: DXGKARG_QUERYVIDPNHWCAPABILITY
author: windows-driver-content
description: The DXGKARG_QUERYVIDPNHWCAPABILITY structure is used by the display miniport driver to describe the hardware capabilities of a functional VidPN in response to a call to the DxgkDdiQueryVidPnHWCapability function.
old-location: display\dxgkarg_queryvidpnhwcapability.htm
old-project: display
ms.assetid: b5f8073c-9989-4413-842d-e3e295cc3470
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_QUERYVIDPNHWCAPABILITY,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_QUERYVIDPNHWCAPABILITY;typedef __inout DXGKARG_QUERYVIDPNHWCAPABILITY* INOUT_PDXGKARG_QUERYVIDPNHWCAPABILITY
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

# DXGKARG_QUERYVIDPNHWCAPABILITY structure



## -description
<p>The DXGKARG_QUERYVIDPNHWCAPABILITY structure is used by the display miniport driver to describe the hardware capabilities of a functional VidPN in response to a call to the <a href="display.dxgkddiqueryvidpnhwcapability">DxgkDdiQueryVidPnHWCapability</a> function.</p>


## -syntax

````
typedef struct _DXGKARG_QUERYVIDPNHWCAPABILITY {
  D3DKMDT_HVIDPN                 hFunctionalVidPn;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID SourceId;
  D3DDDI_VIDEO_PRESENT_TARGET_ID TargetId;
  D3DKMDT_VIDPN_HW_CAPABILITY    VidPnHWCaps;
} DXGKARG_QUERYVIDPNHWCAPABILITY; typedef __inout DXGKARG_QUERYVIDPNHWCAPABILITY*  INOUT_PDXGKARG_QUERYVIDPNHWCAPABILITY;
````


## -struct-fields
<dl>

### -field <b>hFunctionalVidPn</b>

<dd>
<p>[in] A handle to a functional VidPN object for which the hardware capabilities are being queried.</p>
</dd>

### -field <b>SourceId</b>

<dd>
<p>[in] An integer that identifies a video present source on the display adapter.</p>
</dd>

### -field <b>TargetId</b>

<dd>
<p>[in] An integer that identifies a video present target on the display adapter.</p>
</dd>

### -field <b>VidPnHWCaps</b>

<dd>
<p>[out] A <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-hw-capability.md">D3DKMDT_VIDPN_HW_CAPABILITY</a> structure that describes the capabilities of the display miniport driver to perform display operations without dedicated GPU hardware support.</p>
</dd>
</dl>

## -remarks
<p>The D3DDDI_VIDEO_PRESENT_SOURCE_ID and D3DDDI_VIDEO_PRESENT_TARGET_ID data types are defined in <i>D3dukmdt.h</i>.</p>

<p>Video present source identifiers are assigned by the operating system. <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>, implemented by the display miniport driver, returns the number N of video present sources supported by the display adapter. Then the operating system assigns identifiers 0, 1, 2, ... N - 1.</p>

<p>Video present target identifiers are assigned by the display miniport driver. <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>, implemented by the display miniport driver, returns an array of <a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structures, each of which contains an identifier.</p>

<p>For more information about video present sources and targets, see <a href="https://msdn.microsoft.com/62a92f00-b1da-41c2-99af-eef8140b064e">Introduction to Video Present Networks</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-video-present-source.md">D3DKMDT_VIDEO_PRESENT_SOURCE</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-video-present-target.md">D3DKMDT_VIDEO_PRESENT_TARGET</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-hw-capability.md">D3DKMDT_VIDPN_HW_CAPABILITY</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path.md">D3DKMDT_VIDPN_PRESENT_PATH</a>
</dt>
<dt>
<a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>
</dt>
<dt>
<a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>
</dt>
<dt>
<a href="display.dxgkddiqueryvidpnhwcapability">DxgkDdiQueryVidPnHWCapability</a>
</dt>
<dt>
<a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_QUERYVIDPNHWCAPABILITY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
