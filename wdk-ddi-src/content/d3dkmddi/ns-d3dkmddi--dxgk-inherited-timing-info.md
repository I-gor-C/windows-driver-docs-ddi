---
UID: NS.d3dkmddi._DXGK_INHERITED_TIMING_INFO
title: DXGK_INHERITED_TIMING_INFO
author: windows-driver-content
description: Structure passed to the driver in the pPrivateDriverData argument of DxgkDdiRecommendFunctionalVidPn, which the driver should use to describe the color space and wire format which cannot be described easily in the VidPn the DDI builds.
old-location: display\dxgk_inherited_timing_info.htm
old-project: display
ms.assetid: 8A5CB3A6-970C-448D-8808-F072EE67BCA3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_INHERITED_TIMING_INFO, DXGK_INHERITED_TIMING_INFO, *PDXGK_INHERITED_TIMING_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_INHERITED_TIMING_INFO
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

# DXGK_INHERITED_TIMING_INFO structure



## -description
<p>Structure passed to the driver in the pPrivateDriverData argument of DxgkDdiRecommendFunctionalVidPn, which the driver should use to describe the color space and wire format which cannot be described easily in the VidPn the DDI builds</p>


## -syntax

````
typedef struct _DXGK_INHERITED_TIMING_INFO {
  D3DDDI_COLOR_SPACE_TYPE            OutputColorSpace;
  D3DKMDT_WIRE_FORMAT_AND_PREFERENCE SelectedWireFormat;
  union {
    struct {
      DXGK_GLITCH_CAUSE    GlitchCause;
      DXGK_GLITCH_EFFECT   GlitchEffect;
      DXGK_GLITCH_DURATION GlitchDuration;
      UINT8                Reserved;
    };
    UINT DiagnosticInfo;
  };
} DXGK_INHERITED_TIMING_INFO, *PDXGK_INHERITED_TIMING_INFO;
````


## -struct-fields
<dl>

### -field OutputColorSpace

<dd>
<p>A D3DDDI_COLOR_SPACE_TYPE value which describes the output color space currently being applied for the transported pixels.  The driver is responsible for sending appropriate metadata to ensure the display device is set up to interpret pixels correctly for this color space. </p>
</dd>

### -field SelectedWireFormat

<dd>
<p> A D3DKMDT_WIRE_FORMAT_AND_PREFERENCE value which indicates the wire format which is actually being used.  Although the target mode pinned in the VidPn returned by the call to DxgkDdiRecommendFunctionalVidPn could be required to describe exactly one wire format, that might require the driver to prepare a special target mode just for the boot case.  Instead, this field should be used to report the current wire color encoding format and bits per color channel.  Whichever format is reported in this field should also have been reported as supported in the target mode reported through DxgkDdiRecommendFunctionalVidPn.</p>
</dd>

### -field GlitchCause

<dd>
<p>A DXGK_GLITCH_CAUSE value which indicates what underlying change or changes in the display pipeline caused a user perceptible glitch.</p>
</dd>

### -field GlitchEffect

<dd>
<p>A DXGK_GLITCH_EFFECT value which indicates what the glitch looked like to a user.</p>
</dd>

### -field GlitchDuration

<dd>
<p>A DXGK_GLITCH_DURATION value which indicates approximately how long the glitch lasted.  Note, this is intended to reflect how long the underlying issue was present but the visible effect may be longer in some cases.  For example, when sync is lost long enough for a monitor to have to redetect, the display device will likely take many frames to recover.  It is the length of the underlying issue which should be reported, not the recovery time as that will vary between devices.</p>
</dd>

### -field Reserved

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field DiagnosticInfo

<dd>
<p>Set of information filled out by the driver for the boot display to describe any side-effects of the DxgkDdiStartDevice.  

</p>
<p>In many cases, glitches are inevitable so these fields attempt to understand the underlying cause and the extend of the user impact.  OEMs and customers often complain about glitches during boot so having the driver report the glitch to the OS should help to investigate such issues quickly.
</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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