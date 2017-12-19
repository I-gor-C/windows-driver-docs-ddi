---
UID: NF.ntintsafe.RtlUShortToShort
title: RtlUShortToShort function
author: windows-driver-content
description: Converts a value of type USHORT to a value of type SHORT.
old-location: kernel\rtlushorttoshort.htm
old-project: kernel
ms.assetid: 055B5605-2EBB-4B09-9C21-A8288D0DB3CD
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlUShortToShort
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntintsafe.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlUShortToShort
req.alt-loc: Ntintsafe.h
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
---

# RtlUShortToShort function



## -description
Converts a value of type <b>USHORT</b> to a value of type <b>SHORT</b>.



## -syntax

````
NTSTATUS RtlUShortToShort(
  _In_  USHORT usOperand,
  _Out_ SHORT  *psResult
);
````


## -parameters

### -param usOperand [in]

The value to be converted.


### -param psResult [out]

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## -remarks
This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntintsafe.h</dt>
</dl>
</td>
</tr>
</table>