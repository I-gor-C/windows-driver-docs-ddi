---
UID : NE:pointofservicecommontypes._BarcodeSymbologyDecodeLengthType
title : _BarcodeSymbologyDecodeLengthType
author : windows-driver-content
description : The BarcodeSymbologyDecodeLengthType enum describes values for the decode length which can be set to support a range, two discrete values, or be set to any length.
old-location : pos\barcodesymbologydecodelengthtype.htm
old-project : pos
ms.assetid : 155D1C71-7935-4512-8AA2-0EB167FCBF5E
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _BarcodeSymbologyDecodeLengthType, BarcodeSymbologyDecodeLengthType
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : pointofservicecommontypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : BarcodeSymbologyDecodeLengthType
req.alt-loc : pointofservicecommontypes.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Called at PASSIVE_LEVEL.
req.typenames : BarcodeSymbologyDecodeLengthType
---

# _BarcodeSymbologyDecodeLengthType Enumeration
The <b>BarcodeSymbologyDecodeLengthType</b>   enum describes values for the decode length which can be set to support a range, two discrete values, or be set to any length.

## Syntax
````
typedef enum _BarcodeSymbologyDecodeLengthType { 
  DecodeLengthType_AnyLength  = 0,
  DecodeLengthType_Discrete   = 1,
  DecodeLengthType_Range      = 2
} BarcodeSymbologyDecodeLengthType;
````

## Constants

<table>

<tr>
<td>DecodeLengthType_AnyLength</td>
<td>Decode length can be any length.</td>
</tr>

<tr>
<td>DecodeLengthType_Discrete</td>
<td>Decode length is two discrete values</td>
</tr>

<tr>
<td>DecodeLengthType_Range</td>
<td>Decode length is is a range of values.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pointofservicecommontypes.h |