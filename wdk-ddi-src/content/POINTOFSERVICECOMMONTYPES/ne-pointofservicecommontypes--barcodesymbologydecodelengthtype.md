---
UID: NE.pointofservicecommontypes._BarcodeSymbologyDecodeLengthType
title: BarcodeSymbologyDecodeLengthType
author: windows-driver-content
description: The BarcodeSymbologyDecodeLengthType enum describes values for the decode length which can be set to support a range, two discrete values, or be set to any length.
old-location: pos\barcodesymbologydecodelengthtype.htm
ms.assetid: 155D1C71-7935-4512-8AA2-0EB167FCBF5E
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: pos
req.header: pointofservicecommontypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BarcodeSymbologyDecodeLengthType
req.alt-loc: pointofservicecommontypes.h
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
ms.keywords: THERMAL_COOLING_INTERFACE, THERMAL_COOLING_INTERFACE, *PTHERMAL_COOLING_INTERFACE
req.iface: 
---

# BarcodeSymbologyDecodeLengthType enumeration



## -description
<p>The <b>BarcodeSymbologyDecodeLengthType</b>   enum describes values for the decode length which can be set to support a range, two discrete values, or be set to any length.</p>


## -syntax

````
typedef enum _BarcodeSymbologyDecodeLengthType { 
  DecodeLengthType_AnyLength  = 0,
  DecodeLengthType_Discrete   = 1,
  DecodeLengthType_Range      = 2
} BarcodeSymbologyDecodeLengthType;
````


## -enum-fields
<dl>

### -field <a id="DecodeLengthType_AnyLength"></a><a id="decodelengthtype_anylength"></a><a id="DECODELENGTHTYPE_ANYLENGTH"></a><b>DecodeLengthType_AnyLength</b>

<dd>
<p>Decode length can be any length.</p>
</dd>

### -field <a id="DecodeLengthType_Discrete"></a><a id="decodelengthtype_discrete"></a><a id="DECODELENGTHTYPE_DISCRETE"></a><b>DecodeLengthType_Discrete</b>

<dd>
<p>Decode length is two discrete values</p>
</dd>

### -field <a id="DecodeLengthType_Range"></a><a id="decodelengthtype_range"></a><a id="DECODELENGTHTYPE_RANGE"></a><b>DecodeLengthType_Range</b>

<dd>
<p>Decode length is is a range of values.</p>
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
<dt>Pointofservicecommontypes.h</dt>
</dl>
</td>
</tr>
</table>