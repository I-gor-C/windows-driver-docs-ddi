---
UID : NE:d3dkmddi._DXGK_CRTC_VSYNC_STATE
title : _DXGK_CRTC_VSYNC_STATE
author : windows-driver-content
description : Provides additional information for DxgkDdi_ControlInterrupt2 when VSYNC is being utilized.
old-location : display\dxgk_crtc_vsync_state.htm
old-project : display
ms.assetid : 1A7632BB-1DA6-4D03-8A3A-6468A2E4DF71
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_CRTC_VSYNC_STATE, DXGK_CRTC_VSYNC_STATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 10.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_CRTC_VSYNC_STATE
req.alt-loc : d3dkmddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : DXGK_CRTC_VSYNC_STATE
---

# _DXGK_CRTC_VSYNC_STATE Enumeration
Provides additional information for <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_controlinterrupt2.md">DxgkDdi_ControlInterrupt2 </a>when VSYNC is being utilized.

## Syntax
````
typedef enum _DXGK_CRTC_VSYNC_STATE { 
  DXGK_INTERRUPT_ENABLE            = 0,
  DXGK_VSYNC_DISABLE_KEEP_PHASE    = 1,
  DXGK_VSYNC_DISABLE_NO_PHASE      = 2
} DXGK_CRTC_VSYNC_STATE;
````

## Constants

<table>

<tr>
<td>DXGK_VSYNC_DISABLE_KEEP_PHASE</td>
<td>Indicates that the VSYNC interrupt is disabled and the display driver will ensure that any request to re-enter the VSYNC enabled state will do so in the phase of interrupts prior to disable.</td>
</tr>

<tr>
<td>DXGK_VSYNC_DISABLE_NO_PHASE</td>
<td>Indicates that the VSYNC interrupt is disabled, but that the display driver will not require re-entering the VSYNC enabled state in phase of prior interrupts.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |