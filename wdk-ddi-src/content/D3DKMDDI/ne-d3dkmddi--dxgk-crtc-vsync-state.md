---
UID: NE.d3dkmddi._DXGK_CRTC_VSYNC_STATE
title: DXGK_CRTC_VSYNC_STATE
author: windows-driver-content
description: Provides additional information for DxgkDdi_ControlInterrupt2 when VSYNC is being utilized.
old-location: display\dxgk_crtc_vsync_state.htm
ms.assetid: 1A7632BB-1DA6-4D03-8A3A-6468A2E4DF71
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CRTC_VSYNC_STATE
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

# DXGK_CRTC_VSYNC_STATE enumeration



## -description
<p>Provides additional information for <a href="https://msdn.microsoft.com/0C09CAB1-3DFC-4340-8FF2-99CAF7F13156">DxgkDdi_ControlInterrupt2 </a>when VSYNC is being utilized.</p>


## -syntax

````
typedef enum _DXGK_CRTC_VSYNC_STATE { 
  DXGK_INTERRUPT_ENABLE            = 0,
  DXGK_VSYNC_DISABLE_KEEP_PHASE    = 1,
  DXGK_VSYNC_DISABLE_NO_PHASE      = 2
} DXGK_CRTC_VSYNC_STATE;
````


## -enum-fields
<dl>

### -field <a id="DXGK_INTERRUPT_ENABLE"></a><a id="dxgk_interrupt_enable"></a><b>DXGK_INTERRUPT_ENABLE</b>

<dd>
<p>Indicates that the VSYNC interrupt is enabled and will call into the interrupt callback whenever a display target enters the VBLANK state.</p>
</dd>

### -field <a id="DXGK_VSYNC_DISABLE_KEEP_PHASE__"></a><a id="dxgk_vsync_disable_keep_phase__"></a><b>DXGK_VSYNC_DISABLE_KEEP_PHASE  </b>

<dd>
<p>Indicates that the VSYNC interrupt is disabled and the display driver will ensure that any request to re-enter the VSYNC enabled state will do so in the phase of interrupts prior to disable.</p>
</dd>

### -field <a id="DXGK_VSYNC_DISABLE_NO_PHASE____"></a><a id="dxgk_vsync_disable_no_phase____"></a><b>DXGK_VSYNC_DISABLE_NO_PHASE    </b>

<dd>
<p>Indicates that the VSYNC interrupt is disabled, but that the display driver will not require re-entering the VSYNC enabled state in phase of prior interrupts.</p>
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
<p>Available in Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>