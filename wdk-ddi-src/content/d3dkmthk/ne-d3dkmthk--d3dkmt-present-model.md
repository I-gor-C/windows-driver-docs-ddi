---
UID: NE.d3dkmthk._D3DKMT_PRESENT_MODEL
title: D3DKMT_PRESENT_MODEL
author: windows-driver-content
description: The D3DKMT_PRESENT_MODEL enumeration type contains values that indicate the model for a present operation.
old-location: display\d3dkmt_present_model.htm
old-project: display
ms.assetid: 4663cc8e-ce69-4454-afff-03d4a8d82dfb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_PRESENT_MODEL is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_PRESENT_MODEL
req.alt-loc: d3dkmthk.h
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

# D3DKMT_PRESENT_MODEL enumeration



## -description
<p>The D3DKMT_PRESENT_MODEL enumeration type contains values that indicate the model for a present operation. </p>


## -syntax

````
typedef enum _D3DKMT_PRESENT_MODEL { 
  D3DKMT_PM_UNINITIALIZED           = 0,
  D3DKMT_PM_REDIRECTED_GDI          = 1,
  D3DKMT_PM_REDIRECTED_FLIP         = 2,
  D3DKMT_PM_REDIRECTED_BLT          = 3,
  D3DKMT_PM_REDIRECTED_VISTABLT     = 4,
  D3DKMT_PM_SCREENCAPTUREFENCE      = 5,
  D3DKMT_PM_REDIRECTED_GDI_SYSMEM   = 6,
  D3DKMT_PM_REDIRECTED_COMPOSITION  = 7
} D3DKMT_PRESENT_MODEL;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_PM_UNINITIALIZED"></a><a id="d3dkmt_pm_uninitialized"></a><b>D3DKMT_PM_UNINITIALIZED</b>

<dd>
<p>The present-operation model is not initialized. </p>
</dd>

### -field <a id="D3DKMT_PM_REDIRECTED_GDI"></a><a id="d3dkmt_pm_redirected_gdi"></a><b>D3DKMT_PM_REDIRECTED_GDI</b>

<dd>
<p>The present-operation model is redirected GDI. </p>
</dd>

### -field <a id="D3DKMT_PM_REDIRECTED_FLIP"></a><a id="d3dkmt_pm_redirected_flip"></a><b>D3DKMT_PM_REDIRECTED_FLIP</b>

<dd>
<p>The present-operation model is redirected flip. </p>
</dd>

### -field <a id="D3DKMT_PM_REDIRECTED_BLT"></a><a id="d3dkmt_pm_redirected_blt"></a><b>D3DKMT_PM_REDIRECTED_BLT</b>

<dd>
<p>The present-operation model is redirected bit-block transfer (bitblt). </p>
</dd>

### -field <a id="D3DKMT_PM_REDIRECTED_VISTABLT"></a><a id="d3dkmt_pm_redirected_vistablt"></a><b>D3DKMT_PM_REDIRECTED_VISTABLT</b>

<dd>
<p>The present-operation model is redirected Windows Vista bitblt.</p>
</dd>

### -field <a id="D3DKMT_PM_SCREENCAPTUREFENCE"></a><a id="d3dkmt_pm_screencapturefence"></a><b>D3DKMT_PM_SCREENCAPTUREFENCE</b>

<dd>
<p>The present-operation model is screen capture through a fence. </p>
</dd>

### -field <a id="D3DKMT_PM_REDIRECTED_GDI_SYSMEM"></a><a id="d3dkmt_pm_redirected_gdi_sysmem"></a><b>D3DKMT_PM_REDIRECTED_GDI_SYSMEM</b>

<dd>
<p>The present-operation model is redirected system GDI. </p>
</dd>

### -field <a id="D3DKMT_PM_REDIRECTED_COMPOSITION"></a><a id="d3dkmt_pm_redirected_composition"></a><b>D3DKMT_PM_REDIRECTED_COMPOSITION</b>

<dd>
<p>The present-operation model is redirected composition swap chain presentation. This type of presentation is used for XAML-based apps.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DKMT_PRESENT_MODEL is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548188">D3DKMT_PRESENTHISTORYTOKEN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_PRESENT_MODEL enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
