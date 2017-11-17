---
UID: NE.iddcx.IDDCX_FRAME_STATISTICS_STEP_TYPE
title: IDDCX_FRAME_STATISTICS_STEP_TYPE
author: windows-driver-content
description: Defines the type of frame processing step.
old-location: display\iddcx_frame_statistics_step_type.htm
ms.assetid: 1c58841b-fff9-4419-b001-bce150b0f7a0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_FRAME_STATISTICS_STEP_TYPE
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
ms.keywords: WcsTranslateColors
req.iface: 
---

# IDDCX_FRAME_STATISTICS_STEP_TYPE enumeration



## -description
<p>
                     Defines the type of frame processing step.
                </p>


## -syntax

````
typedef enum _IDDCX_FRAME_STATISTICS_STEP_TYPE { 
  IDDCX_FRAME_STATISTICS_STEP_TYPE_UNINITIALIZED        = 0,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_COLOR_CONVERT_START  = 0x1,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_COLOR_CONVERT_END    = 0x2,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCODE_START         = 0x3,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCODE_END           = 0x4,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCRYPT_START        = 0x5,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCRYPT_END          = 0x6,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_MUX_START            = 0x7,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_MUX_END              = 0x8,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_1     = 0x100,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_2     = 0x101,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_3     = 0x102,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_4     = 0x103,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_5     = 0x104,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_6     = 0x105,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_7     = 0x106,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_8     = 0x107,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_9     = 0x108,
  IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_10    = 0x109
} IDDCX_FRAME_STATISTICS_STEP_TYPE;
````


## -enum-fields
<dl>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_UNINITIALIZED"></a><a id="iddcx_frame_statistics_step_type_uninitialized"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_UNINITIALIZED</b>

<dd>
<p>
                        
                    Indicates that an <b>IDDCX_FRAME_STATISTICS_STEP_TYPE</b> variable has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_COLOR_CONVERT_START"></a><a id="iddcx_frame_statistics_step_type_color_convert_start"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_COLOR_CONVERT_START</b>

<dd>
<p>
                        Used to mark the start of a color convert operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_COLOR_CONVERT_END"></a><a id="iddcx_frame_statistics_step_type_color_convert_end"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_COLOR_CONVERT_END</b>

<dd>
<p>
                        Used to mark the end of a color convert operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCODE_START"></a><a id="iddcx_frame_statistics_step_type_encode_start"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCODE_START</b>

<dd>
<p>
                        Used to mark the start of a encode operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCODE_END"></a><a id="iddcx_frame_statistics_step_type_encode_end"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCODE_END</b>

<dd>
<p>
                        Used to mark the end of a encode operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCRYPT_START"></a><a id="iddcx_frame_statistics_step_type_encrypt_start"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCRYPT_START</b>

<dd>
<p>
                        Used to mark the start of a encrypt operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCRYPT_END"></a><a id="iddcx_frame_statistics_step_type_encrypt_end"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_ENCRYPT_END</b>

<dd>
<p>
                        Used to mark the end of a encrypt operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_MUX_START"></a><a id="iddcx_frame_statistics_step_type_mux_start"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_MUX_START</b>

<dd>
<p>
                        Used to mark the start of a mux'ing operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_MUX_END"></a><a id="iddcx_frame_statistics_step_type_mux_end"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_MUX_END</b>

<dd>
<p>
                        Used to mark the end of a mux'ing operation
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_1"></a><a id="iddcx_frame_statistics_step_type_driver_defined_1"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_1</b>

<dd>
<p>
                        Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_2"></a><a id="iddcx_frame_statistics_step_type_driver_defined_2"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_2</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_3"></a><a id="iddcx_frame_statistics_step_type_driver_defined_3"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_3</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_4"></a><a id="iddcx_frame_statistics_step_type_driver_defined_4"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_4</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_5"></a><a id="iddcx_frame_statistics_step_type_driver_defined_5"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_5</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_6"></a><a id="iddcx_frame_statistics_step_type_driver_defined_6"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_6</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_7"></a><a id="iddcx_frame_statistics_step_type_driver_defined_7"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_7</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_8"></a><a id="iddcx_frame_statistics_step_type_driver_defined_8"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_8</b>

<dd>
<p>Driver defined processing step
                        
                    </p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_9"></a><a id="iddcx_frame_statistics_step_type_driver_defined_9"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_9</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
</dd>

### -field <a id="IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_10"></a><a id="iddcx_frame_statistics_step_type_driver_defined_10"></a><b>IDDCX_FRAME_STATISTICS_STEP_TYPE_DRIVER_DEFINED_10</b>

<dd>
<p>
                        
                    Driver defined processing step</p>
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