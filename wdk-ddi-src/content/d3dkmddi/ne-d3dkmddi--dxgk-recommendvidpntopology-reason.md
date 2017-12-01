---
UID: NE.d3dkmddi._DXGK_RECOMMENDVIDPNTOPOLOGY_REASON
title: DXGK_RECOMMENDVIDPNTOPOLOGY_REASON
author: windows-driver-content
description: Indicates the reason for calling the display miniport driver's DxgkDdiRecommendVidPnTopology function.
old-location: display\dxgk_recommendvidpntopology_reason.htm
old-project: display
ms.assetid: 2a67a119-863b-4cde-9308-e4862823bad1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_RECOMMENDVIDPNTOPOLOGY_REASON
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

# DXGK_RECOMMENDVIDPNTOPOLOGY_REASON enumeration



## -description
<p>The <b>DXGK_RECOMMENDVIDPNTOPOLOGY_REASON</b> enumeration indicates the reason for calling the display miniport driver's <a href="display.dxgkddirecommendvidpntopology">DxgkDdiRecommendVidPnTopology</a> function.</p>


## -syntax

````
typedef enum _DXGK_RECOMMENDVIDPNTOPOLOGY_REASON { 
  DXGK_RVT_UNINITIALIZED               = 0,
  DXGK_RVT_INITIALIZATION_NOLKG        = 1,
  DXGK_RVT_AUGMENTATION_NOLKG          = 2,
  DXGK_RVT_AUGMENTATION_LKGOVERRIDE    = 3,
  DXGK_RVT_INITIALIZATION_LKGOVERRIDE  = 4
} DXGK_RECOMMENDVIDPNTOPOLOGY_REASON;
````


## -enum-fields
<dl>

### -field <a id="DXGK_RVT_UNINITIALIZED"></a><a id="dxgk_rvt_uninitialized"></a><b>DXGK_RVT_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-recommendvidpntopology-reason.md">DXGK_RECOMMENDVIDPNTOPOLOGY_REASON</a> has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="DXGK_RVT_INITIALIZATION_NOLKG"></a><a id="dxgk_rvt_initialization_nolkg"></a><b>DXGK_RVT_INITIALIZATION_NOLKG</b>

<dd>
<p>Indicates that the call is being made during the initialization of the display adapter after an attempt to use the last known good VidPN topology failed.</p>
</dd>

### -field <a id="DXGK_RVT_AUGMENTATION_NOLKG"></a><a id="dxgk_rvt_augmentation_nolkg"></a><b>DXGK_RVT_AUGMENTATION_NOLKG</b>

<dd>
<p>
      Indicates that the call is being made during the VidPN topology augmentation by the display mode manager (DMM) after an attempt to use the last known good VidPN topology failed.
     </p>
</dd>

### -field <a id="DXGK_RVT_AUGMENTATION_LKGOVERRIDE"></a><a id="dxgk_rvt_augmentation_lkgoverride"></a><b>DXGK_RVT_AUGMENTATION_LKGOVERRIDE</b>

<dd>
<p>Indicates that the call is being made during the VidPN topology augmentation by the display mode manager (DMM), giving the display miniport driver a chance to override the last known good VidPN topology.</p>
</dd>

### -field <a id="DXGK_RVT_INITIALIZATION_LKGOVERRIDE"></a><a id="dxgk_rvt_initialization_lkgoverride"></a><b>DXGK_RVT_INITIALIZATION_LKGOVERRIDE</b>

<dd>
<p>Indicates that the call is being made during the initialization of the display adapter, giving the display miniport driver a chance to override the last known good VidPN topology.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>