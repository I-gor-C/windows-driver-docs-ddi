---
UID: NS.d3dkmddi._DXGK_VIDPNTARGETMODESET_INTERFACE
title: DXGK_VIDPNTARGETMODESET_INTERFACE
author: windows-driver-content
description: The DXGK_VIDPNTARGETMODESET_INTERFACE structure contains pointers to functions that belong to the VidPn Target Mode Set interface, which is implemented by the VidPN manager.
old-location: display\dxgk_vidpntargetmodeset_interface.htm
old-project: display
ms.assetid: 556d3134-942b-475c-adac-3087a512f481
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_VIDPNTARGETMODESET_INTERFACE, DXGK_VIDPNTARGETMODESET_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_VIDPNTARGETMODESET_INTERFACE
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

# DXGK_VIDPNTARGETMODESET_INTERFACE structure



## -description
<p>The DXGK_VIDPNTARGETMODESET_INTERFACE structure contains pointers to functions that belong to the <a href="display.vidpn_target_mode_set_interface">VidPn Target Mode Set interface</a>, which is implemented by the VidPN manager.</p>


## -syntax

````
typedef struct _DXGK_VIDPNTARGETMODESET_INTERFACE {
  DXGKDDI_VIDPNTARGETMODESET_GETNUMMODES           pfnGetNumModes;
  DXGKDDI_VIDPNTARGETMODESET_ACQUIREFIRSTMODEINFO  pfnAcquireFirstModeInfo;
  DXGKDDI_VIDPNTARGETMODESET_ACQUIRENEXTMODEINFO   pfnAcquireNextModeInfo;
  DXGKDDI_VIDPNTARGETMODESET_ACQUIREPINNEDMODEINFO pfnAcquirePinnedModeInfo;
  DXGKDDI_VIDPNTARGETMODESET_RELEASEMODEINFO       pfnReleaseModeInfo;
  DXGKDDI_VIDPNTARGETMODESET_CREATENEWMODEINFO     pfnCreateNewModeInfo;
  DXGKDDI_VIDPNTARGETMODESET_ADDMODE               pfnAddMode;
  DXGKDDI_VIDPNTARGETMODESET_PINMODE               pfnPinMode;
} DXGK_VIDPNTARGETMODESET_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>pfnGetNumModes</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-getnummodes.md">pfnGetNumModes</a> function.</p>
</dd>

### -field <b>pfnAcquireFirstModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirefirstmodeinfo.md">pfnAcquireFirstModeInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireNextModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirenextmodeinfo.md">pfnAcquireNextModeInfo</a> function.</p>
</dd>

### -field <b>pfnAcquirePinnedModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirepinnedmodeinfo.md">pfnAcquirePinnedModeInfo</a> function.</p>
</dd>

### -field <b>pfnReleaseModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-releasemodeinfo.md">pfnReleaseModeInfo</a> function.</p>
</dd>

### -field <b>pfnCreateNewModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-createnewmodeinfo.md">pfnCreateNewModeInfo</a> function.</p>
</dd>

### -field <b>pfnAddMode</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-addmode.md">pfnAddMode</a> function.</p>
</dd>

### -field <b>pfnPinMode</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntargetmodeset-pinmode.md">pfnPinMode</a> function.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver calls the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a> function of the <a href="display.vidpn_interface">VidPn interface</a> to obtain a handle to a VidPN target mode set object and a pointer to a DXGK_VIDPNTARGETMODESET_INTERFACE structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the VidPN target mode set object.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-target-mode.md">D3DKMDT_VIDPN_TARGET_MODE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-monitorsourcemodeset-interface.md">DXGK_MONITORSOURCEMODESET_INTERFACE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpnsourcemodeset-interface.md">DXGK_VIDPNSOURCEMODESET_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_VIDPNTARGETMODESET_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
