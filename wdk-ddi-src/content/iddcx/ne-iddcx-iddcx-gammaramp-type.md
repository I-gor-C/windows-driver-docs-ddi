---
UID: NE.iddcx.IDDCX_GAMMARAMP_TYPE
title: IDDCX_GAMMARAMP_TYPE
author: windows-driver-content
description: An enumeration indicating the type of gamma ramp being set.
old-location: display\iddcx_gammaramp_type.htm
old-project: display
ms.assetid: 40fa5169-e295-429c-a63d-3e4ab9c14672
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: WcsTranslateColors
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_GAMMARAMP_TYPE
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _requires_same_
req.iface: 
---

# IDDCX_GAMMARAMP_TYPE enumeration



## -description
<p>
                     An enumeration indicating the type of gamma ramp being set
                </p>


## -syntax

````
typedef enum _IDDCX_GAMMARAMP_TYPE { 
  IDDCX_GAMMARAMP_TYPE_UNINITIALIZED  = 0,
  IDDCX_GAMMARAMP_TYPE_DEFAULT        = 1,
  IDDCX_GAMMARAMP_TYPE_RGB256x3x16    = 2
} IDDCX_GAMMARAMP_TYPE;
````


## -enum-fields
<dl>

### -field IDDCX_GAMMARAMP_TYPE_UNINITIALIZED

<dd>
<p>
                        
                    Indicates that an <b>IDDCX_GAMMARAMP_TYPE</b> variable has not yet been assigned a meaningful value.</p>
</dd>

### -field IDDCX_GAMMARAMP_TYPE_DEFAULT

<dd>
<p>
                        The gamma ramp is the default ramp
                    </p>
</dd>

### -field IDDCX_GAMMARAMP_TYPE_RGB256x3x16

<dd>
<p>
                        Indicates that the gamma lookup table contains three arrays, one each for the red, green, and blue color channels. Each array has 256 16-bit values.
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>