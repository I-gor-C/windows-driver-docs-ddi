---
UID: NE.d3dkmddi._DXGK_GLITCH_CAUSE
title: DXGK_GLITCH_CAUSE
author: windows-driver-content
description: Enumeration that describes what caused a glitch during a SetTimingsFromVidPn call.
old-location: display\dxgk_glitch_cause.htm
ms.assetid: A0356AE8-3A82-4722-9F46-8FE05646BF10
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_GLITCH_CAUSE
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

# DXGK_GLITCH_CAUSE enumeration



## -description
<p>Enumeration that describes what caused a glitch during a SetTimingsFromVidPn call.</p>


## -syntax

````
typedef enum _DXGK_GLITCH_CAUSE { 
  DXGK_GLITCH_CAUSE_DRIVER_ERROR         = 0,
  DXGK_GLITCH_CAUSE_TIMING_CHANGE        = 1,
  DXGK_GLITCH_CAUSE_PIPELINE_CHANGE      = 2,
  DXGK_GLITCH_CAUSE_MEMORY_TIMING        = 3,
  DXGK_GLITCH_CAUSE_ENCODER_RECONFIG     = 4,
  DXGK_GLITCH_CAUSE_MODIFIED_WIRE_USAGE  = 5,
  DXGK_GLITCH_CAUSE_METADATA_CHANGE      = 6,
  DXGK_GLITCH_CAUSE_NONE                 = 255
} DXGK_GLITCH_CAUSE;
````


## -enum-fields
<dl>

### -field <a id="DXGK_GLITCH_CAUSE_DRIVER_ERROR"></a><a id="dxgk_glitch_cause_driver_error"></a><b>DXGK_GLITCH_CAUSE_DRIVER_ERROR</b>

<dd>
<p>Indicates that an internal driver error caused a glitch.  </p>
</dd>

### -field <a id="DXGK_GLITCH_CAUSE_TIMING_CHANGE"></a><a id="dxgk_glitch_cause_timing_change"></a><b>DXGK_GLITCH_CAUSE_TIMING_CHANGE</b>

<dd>
<p>Indicates that the timing requested necessitated a glitch.  This cause should only be used if the OS requested a change which would always result in a glitch rather than something which could have been avoided under other circumstances.  </p>
<p>For example, this should not be used if the driver switches to a different display pipe to support an additional path, but it should be used if the OS requests a different timing to the previous one.  </p>
</dd>

### -field <a id="DXGK_GLITCH_CAUSE_PIPELINE_CHANGE"></a><a id="dxgk_glitch_cause_pipeline_change"></a><b>DXGK_GLITCH_CAUSE_PIPELINE_CHANGE</b>

<dd>
<p>Indicates that reconfiguring the display pipeline caused a glitch.  </p>
</dd>

### -field <a id="DXGK_GLITCH_CAUSE_MEMORY_TIMING"></a><a id="dxgk_glitch_cause_memory_timing"></a><b>DXGK_GLITCH_CAUSE_MEMORY_TIMING</b>

<dd>
<p>Indicates that changing graphics memory timings caused a glitch.  </p>
</dd>

### -field <a id="DXGK_GLITCH_CAUSE_ENCODER_RECONFIG"></a><a id="dxgk_glitch_cause_encoder_reconfig"></a><b>DXGK_GLITCH_CAUSE_ENCODER_RECONFIG</b>

<dd>
<p>Indicates that changing the configuration of the encoder for a target caused a glitch.  </p>
</dd>

### -field <a id="DXGK_GLITCH_CAUSE_MODIFIED_WIRE_USAGE"></a><a id="dxgk_glitch_cause_modified_wire_usage"></a><b>DXGK_GLITCH_CAUSE_MODIFIED_WIRE_USAGE</b>

<dd>
<p>Indicates that modifying the format of pixel data in the transport stream caused a glitch.  </p>
</dd>

### -field <a id="DXGK_GLITCH_CAUSE_METADATA_CHANGE"></a><a id="dxgk_glitch_cause_metadata_change"></a><b>DXGK_GLITCH_CAUSE_METADATA_CHANGE</b>

<dd>
<p>Indicates that changing the frame metadata caused a glitch.</p>
</dd>

### -field <a id="DXGK_GLITCH_CAUSE_NONE"></a><a id="dxgk_glitch_cause_none"></a><b>DXGK_GLITCH_CAUSE_NONE</b>

<dd>
<p>Indicates that there was no glitch.</p>
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