---
UID: NE.d3dkmthk._D3DKMT_TDRDBGCTRLTYPE
title: D3DKMT_TDRDBGCTRLTYPE
author: windows-driver-content
description: The D3DKMT_TDRDBGCTRLTYPE enumeration type contains values that affect the behavior of the operating system's Timeout Detection and Recovery (TDR) process in a call to the OpenGL D3DKMTEscape function.
old-location: display\d3dkmt_tdrdbgctrltype.htm
ms.assetid: d3a6dfcc-e318-4fd0-85e0-5a0cc13fd00f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_TDRDBGCTRLTYPE
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
req.iface: 
---

# D3DKMT_TDRDBGCTRLTYPE enumeration



## -description
<p><b>Do not use the D3DKMT_TDRDBGCTRLTYPE enumeration; it is for testing purposes only.</b></p>
<p>The <b>D3DKMT_TDRDBGCTRLTYPE</b> enumeration type contains values that affect the behavior of the operating system's Timeout Detection and Recovery (TDR) process in a call to the OpenGL <a href="https://msdn.microsoft.com/library/windows/hardware/ff546940">D3DKMTEscape</a> function.</p>


## -syntax

````
typedef enum _D3DKMT_TDRDBGCTRLTYPE { 
  D3DKMT_TDRDBGCTRLTYPE_FORCETDR          = 0,
  D3DKMT_TDRDBGCTRLTYPE_DISABLEBREAK      = 1,
  D3DKMT_TDRDBGCTRLTYPE_ENABLEBREAK       = 2,
  D3DKMT_TDRDBGCTRLTYPE_UNCONDITIONAL     = 3,
  D3DKMT_TDRDBGCTRLTYPE_VSYNCTDR          = 4,
  D3DKMT_TDRDBGCTRLTYPE_GPUTDR            = 5,
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  D3DKMT_TDRDBGCTRLTYPE_FORCEDODTDR       = 6,
  D3DKMT_TDRDBGCTRLTYPE_FORCEDODVSYNCTDR  = 7,
  D3DKMT_TDRDBGCTRLTYPE_ENGINETDR         = 8

#endif } D3DKMT_TDRDBGCTRLTYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_FORCETDR"></a><a id="d3dkmt_tdrdbgctrltype_forcetdr"></a><b>D3DKMT_TDRDBGCTRLTYPE_FORCETDR</b>

<dd>
<p>Simulate a TDR.</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_DISABLEBREAK"></a><a id="d3dkmt_tdrdbgctrltype_disablebreak"></a><b>D3DKMT_TDRDBGCTRLTYPE_DISABLEBREAK</b>

<dd>
<p>Disable DebugBreak on timeout.</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_ENABLEBREAK"></a><a id="d3dkmt_tdrdbgctrltype_enablebreak"></a><b>D3DKMT_TDRDBGCTRLTYPE_ENABLEBREAK</b>

<dd>
<p>Enable DebugBreak on timeout.</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_UNCONDITIONAL"></a><a id="d3dkmt_tdrdbgctrltype_unconditional"></a><b>D3DKMT_TDRDBGCTRLTYPE_UNCONDITIONAL</b>

<dd>
<p>Disables all safety conditions (e.g. check for consecutive recoveries).</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_VSYNCTDR"></a><a id="d3dkmt_tdrdbgctrltype_vsynctdr"></a><b>D3DKMT_TDRDBGCTRLTYPE_VSYNCTDR</b>

<dd>
<p>Simulate a Vsync TDR.</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_GPUTDR"></a><a id="d3dkmt_tdrdbgctrltype_gputdr"></a><b>D3DKMT_TDRDBGCTRLTYPE_GPUTDR</b>

<dd>
<p>Simulate a GPU TDR.</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_FORCEDODTDR"></a><a id="d3dkmt_tdrdbgctrltype_forcedodtdr"></a><b>D3DKMT_TDRDBGCTRLTYPE_FORCEDODTDR</b>

<dd>
<p>Simulate a display-only present TDR.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_FORCEDODVSYNCTDR"></a><a id="d3dkmt_tdrdbgctrltype_forcedodvsynctdr"></a><b>D3DKMT_TDRDBGCTRLTYPE_FORCEDODVSYNCTDR</b>

<dd>
<p>Simulate a display-only VSync TDR.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3DKMT_TDRDBGCTRLTYPE_ENGINETDR"></a><a id="d3dkmt_tdrdbgctrltype_enginetdr"></a><b>D3DKMT_TDRDBGCTRLTYPE_ENGINETDR</b>

<dd>
<p>Simulate an engine TDR.</p>
<p>Supported starting with Windows 8.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547970">D3DKMT_ESCAPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546940">D3DKMTEscape</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_TDRDBGCTRLTYPE enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
