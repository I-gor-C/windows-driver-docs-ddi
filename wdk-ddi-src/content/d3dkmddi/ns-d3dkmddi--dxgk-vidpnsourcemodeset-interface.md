---
UID: NS.d3dkmddi._DXGK_VIDPNSOURCEMODESET_INTERFACE
title: DXGK_VIDPNSOURCEMODESET_INTERFACE
author: windows-driver-content
description: The DXGK_VIDPNSOURCEMODESET_INTERFACE structure contains pointers to functions that belong to the VidPn Source Mode Set interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_vidpnsourcemodeset_interface.htm
old-project: display
ms.assetid: c608643f-e791-44b8-8719-4e98e10fa7b0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_VIDPNSOURCEMODESET_INTERFACE, DXGK_VIDPNSOURCEMODESET_INTERFACE
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
req.alt-api: DXGK_VIDPNSOURCEMODESET_INTERFACE
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

# DXGK_VIDPNSOURCEMODESET_INTERFACE structure



## -description
<p>The DXGK_VIDPNSOURCEMODESET_INTERFACE structure contains pointers to functions that belong to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570558">VidPn Source Mode Set interface</a>, which is implemented by the video present network (VidPN) manager.</p>


## -syntax

````
typedef struct _DXGK_VIDPNSOURCEMODESET_INTERFACE {
  DXGKDDI_VIDPNSOURCEMODESET_GETNUMMODES           pfnGetNumModes;
  DXGKDDI_VIDPNSOURCEMODESET_ACQUIREFIRSTMODEINFO  pfnAcquireFirstModeInfo;
  DXGKDDI_VIDPNSOURCEMODESET_ACQUIRENEXTMODEINFO   pfnAcquireNextModeInfo;
  DXGKDDI_VIDPNSOURCEMODESET_ACQUIREPINNEDMODEINFO pfnAcquirePinnedModeInfo;
  DXGKDDI_VIDPNSOURCEMODESET_RELEASEMODEINFO       pfnReleaseModeInfo;
  DXGKDDI_VIDPNSOURCEMODESET_CREATENEWMODEINFO     pfnCreateNewModeInfo;
  DXGKDDI_VIDPNSOURCEMODESET_ADDMODE               pfnAddMode;
  DXGKDDI_VIDPNSOURCEMODESET_PINMODE               pfnPinMode;
} DXGK_VIDPNSOURCEMODESET_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>pfnGetNumModes</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-getnummodes.md">pfnGetNumModes</a> function.</p>
</dd>

### -field <b>pfnAcquireFirstModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-acquirefirstmodeinfo.md">pfnAcquireFirstModeInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireNextModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-acquirenextmodeinfo.md">pfnAcquireNextModeInfo</a> function.</p>
</dd>

### -field <b>pfnAcquirePinnedModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-acquirepinnedmodeinfo.md">pfnAcquirePinnedModeInfo</a> function.</p>
</dd>

### -field <b>pfnReleaseModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-releasemodeinfo.md">pfnReleaseModeInfo</a> function.</p>
</dd>

### -field <b>pfnCreateNewModeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-createnewmodeinfo.md">pfnCreateNewModeInfo</a> function.</p>
</dd>

### -field <b>pfnAddMode</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-addmode.md">pfnAddMode</a> function.</p>
</dd>

### -field <b>pfnPinMode</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-pinmode.md">pfnPinMode</a> function.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver calls the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiresourcemodeset.md">pfnAcquireSourceModeSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570556">VidPn interface</a> to obtain a handle to a VidPN source mode set object and a pointer to a DXGK_VIDPNSOURCEMODESET_INTERFACE structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the VidPN source mode set object.</p>

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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiresourcemodeset.md">pfnAcquireSourceModeSet</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561921">DXGK_MONITORSOURCEMODESET_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562082">DXGK_VIDPNTARGETMODESET_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_VIDPNSOURCEMODESET_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
