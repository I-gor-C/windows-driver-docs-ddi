---
UID: NF.ntintsafe.RtlShortToULongPtr
title: RtlShortToULongPtr function
author: windows-driver-content
description: Converts a value of type SHORT to a value of type ULONG_PTR.
old-location: kernel\rtlshorttoulongptr.htm
old-project: kernel
ms.assetid: 0C279063-D5B1-4C82-8C0A-2B39E831BFB3
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlShortToULongPtr
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
req.alt-api: RtlShortToULongPtr
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

# RtlShortToULongPtr function



## -description
Converts a value of type <b>SHORT</b> to a value of type <b>ULONG_PTR</b>.


## -syntax

````
NTSTATUS RtlShortToULongPtr(
  _In_  SHORT     sOperand,
  _Out_ ULONG_PTR *pulResult
);
````


## -parameters

### -param sOperand [in]

The value to be converted.

### -param pulResult [out]

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.

## -remarks
This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.

This function uses the following alternate name:

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