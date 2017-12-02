---
UID: NS.d3dkmdt._D3DKMDT_WIRE_FORMAT_AND_PREFERENCE
title: D3DKMDT_WIRE_FORMAT_AND_PREFERENCE
author: windows-driver-content
description: Holds information about the preferred pixel encoding format.
old-location: display\d3dkmdt_wire_format_and_preference.htm
old-project: display
ms.assetid: 24CC6A10-6462-4681-B340-E887B679F456
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_WIRE_FORMAT_AND_PREFERENCE, D3DKMDT_WIRE_FORMAT_AND_PREFERENCE, *PD3DKMDT_WIRE_FORMAT_AND_PREFERENCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_WIRE_FORMAT_AND_PREFERENCE
req.alt-loc: d3dkmdt.h
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

# D3DKMDT_WIRE_FORMAT_AND_PREFERENCE structure



## -description
<p>Holds information about the preferred pixel encoding format.</p>


## -syntax

````
typedef union _D3DKMDT_WIRE_FORMAT_AND_PREFERENCE {
  struct {
    D3DKMDT_MODE_PREFERENCE Preference  :2;
    UINT                    Rgb  :6;
    UINT                    YCbCr444  :6;
    UINT                    YCbCr422  :6;
    UINT                    YCbCr420  :6;
    UINT                    Intensity  :6;
  };
  UINT Value;
} D3DKMDT_WIRE_FORMAT_AND_PREFERENCE, *PD3DKMDT_WIRE_FORMAT_AND_PREFERENCE;
````


## -struct-fields
<dl>

### -field Preference

<dd>
<p>Functions as it has in previous releases, but using only 2 bits.</p>
</dd>

### -field Rgb

<dd>
<p>UINT describing supported/requested pixel encoding using RGB sample format.</p>
</dd>

### -field YCbCr444

<dd>
<p>UINT describing supported/requested pixel encoding using YcbCr 4:4:4 sample format.</p>
</dd>

### -field YCbCr422

<dd>
<p>UINT describing supported/requested pixel encoding using YcbCr 4:2:2 sample format.</p>
</dd>

### -field YCbCr420

<dd>
<p>UINT describing supported/requested pixel encoding using YcbCr 4:2:0 sample format.</p>
</dd>

### -field Intensity

<dd>
<p>UINT describing supported/requested pixel encoding using intensity only.</p>
</dd>

### -field Value

<dd>
<p>UINT used to operate on the combined bit-fields.</p>
</dd>
</dl>

## -remarks
<p>The five standard color sample formats for pixel transmission are exposed separately to allow the driver to report capabilities individually but it is expected that the vast majority of display devices will not support all sample formats as input, in particular support of intensity only signals is likely restricted to monochrome displays which should therefore not support color sample formats.</p>

<p>During mode enumeration via EnumVidPnCofuncModality, the driver should set values into all five fields to indicate the pixel encodings that are supported as inputs to the display device in the current configuration.

When SetTimingsFromVidPn is called, one of these fields will indicate the pixel encoding and sample format to be applied.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>