---
UID: NS.d3dkmddi._DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS
title: DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS
author: windows-driver-content
description: A structure containing the set of flags needed to set the VidPN source address.
old-location: display\dxgk_setvidpnsourceaddress_input_flags.htm
old-project: display
ms.assetid: FBC661AA-B028-45AF-8E3C-7C2472652BD5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS, DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS
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
req.alt-api: DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS
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

# DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS structure



## -description
<p>A structure containing the set of flags needed to set the VidPN source address.</p>


## -syntax

````
typedef struct _DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS {
  union {
    struct {
      UINT FlipStereo  :1;
      UINT FlipStereoTemporaryMono  :1;
      UINT FlipStereoPreferRight   :1;
      UINT RetryAtLowerIrql  :1;
      UINT Reserved  :28;
    };
    UINT Value;
  };
} DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS;
````


## -struct-fields
<dl>

### -field FlipStereo

<dd>
<p>Specifies whether the driver flips both left and right images of a stereo allocation.</p>
<p>If the FlipOnNextVSync member of the DXGK_PLANE_SPECIFIC_INPUT_FLAGS structure is set, the driver completes the flip to the left image on the next VSync and then completes the flip to the right image on the following VSync.</p>
<p>If the FlipImmediate member of the DXGK_PLANE_SPECIFIC_INPUT_FLAGS structure is set, the driver immediately starts to scan out from the new allocation. For example, if the driver was scanning a right image, it starts the new scan from the same relative offset in the right image of the new allocation.</p>
<div class="alert"><b>Note</b>  The FlipStereo and FlipStereoTemporaryMono members cannot both be set at the same time.</div>
<div> </div>
</dd>

### -field FlipStereoTemporaryMono

<dd>
<p>Specifies whether the driver uses the left image of a stereo allocation for the right and left portions of a stereo frame. The driver performs the same present operation as with FlipStereo, except that it scans out only from the left image to produce both images of a stereo frame.</p>
<p>This member should be set only if the driver reports support for this option in the current display mode by setting the Type member of the D3DKMDT_VIDPN_SOURCE_MODE structure to D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN.</p>
</dd>

### -field FlipStereoPreferRight 

<dd>
<p>Specifies that when the driver clones a stereo primary allocation to a mono monitor, it uses the right image.</p>
<div class="alert"><b>Note</b>  The FlipStereoTemporaryMono and FlipStereoPreferRight members cannot both be set at the same time.</div>
<div> </div>
</dd>

### -field RetryAtLowerIrql

<dd>
<p>The scheduler sets this flag if the call is made at PASSIVE_LEVEL. Hence, the driver can perform hardware changes in this call</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 28 bits (0xFFFFFFF8) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field Value

<dd></dd>
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