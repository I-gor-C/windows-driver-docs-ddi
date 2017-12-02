---
UID: NE.ks.VARENUM
title: VARENUM
author: windows-driver-content
description: .
old-location: stream\varenum.htm
old-project: stream
ms.assetid: 00F015F4-708F-4272-A903-56C44DC6646E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VARENUM
req.alt-loc: Ks.h
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

# VARENUM enumeration



## -description
<p></p>


## -syntax

````
enum VARENUM {
  VT_EMPTY            = 0, 
  VT_NULL             = 1, 
  VT_I2               = 2, 
  VT_I4               = 3, 
  VT_R4               = 4, 
  VT_R8               = 5, 
  VT_CY               = 6, 
  VT_DATE             = 7, 
  VT_BSTR             = 8, 
  VT_DISPATCH         = 9, 
  VT_ERROR            = 10, 
  VT_BOOL             = 11, 
  VT_VARIANT          = 12, 
  VT_UNKNOWN          = 13, 
  VT_DECIMAL          = 14, 
  VT_I1               = 16, 
  VT_UI1              = 17, 
  VT_UI2              = 18, 
  VT_UI4              = 19, 
  VT_I8               = 20, 
  VT_UI8              = 21, 
  VT_INT              = 22, 
  VT_UINT             = 23, 
  VT_VOID             = 24, 
  VT_HRESULT          = 25, 
  VT_PTR              = 26, 
  VT_SAFEARRAY        = 27, 
  VT_CARRAY           = 28, 
  VT_USERDEFINED      = 29, 
  VT_LPSTR            = 30, 
  VT_LPWSTR           = 31, 
  VT_FILETIME         = 64, 
  VT_BLOB             = 65, 
  VT_STREAM           = 66, 
  VT_STORAGE          = 67, 
  VT_STREAMED_OBJECT  = 68, 
  VT_STORED_OBJECT    = 69, 
  VT_BLOB_OBJECT      = 70, 
  VT_CF               = 71, 
  VT_CLSID            = 72, 
   VT_VECTOR          = 0x1000, 
  VT_ARRAY            = 0x2000, 
  VT_BYREF            = 0x4000, 
   VT_RESERVED        = 0x8000, 
  VT_ILLEGAL          = 0xffff, 
  VT_ILLEGALMASKED    = 0xfff, 
  VT_TYPEMASK         = 0xfff 

};
````


## -enum-fields
<dl>

### -field VT_EMPTY

<dd></dd>

### -field VT_NULL

<dd></dd>

### -field VT_I2

<dd></dd>

### -field VT_I4

<dd></dd>

### -field VT_R4

<dd></dd>

### -field VT_R8

<dd></dd>

### -field VT_CY

<dd></dd>

### -field VT_DATE

<dd></dd>

### -field VT_BSTR

<dd></dd>

### -field VT_DISPATCH

<dd></dd>

### -field VT_ERROR

<dd></dd>

### -field VT_BOOL

<dd></dd>

### -field VT_VARIANT

<dd></dd>

### -field VT_UNKNOWN

<dd></dd>

### -field VT_DECIMAL

<dd></dd>

### -field VT_I1

<dd></dd>

### -field VT_UI1

<dd></dd>

### -field VT_UI2

<dd></dd>

### -field VT_UI4

<dd></dd>

### -field VT_I8

<dd></dd>

### -field VT_UI8

<dd></dd>

### -field VT_INT

<dd></dd>

### -field VT_UINT

<dd></dd>

### -field VT_VOID

<dd></dd>

### -field VT_HRESULT

<dd></dd>

### -field VT_PTR

<dd></dd>

### -field VT_SAFEARRAY

<dd></dd>

### -field VT_CARRAY

<dd></dd>

### -field VT_USERDEFINED

<dd></dd>

### -field VT_LPSTR

<dd></dd>

### -field VT_LPWSTR

<dd></dd>

### -field VT_FILETIME

<dd></dd>

### -field VT_BLOB

<dd></dd>

### -field VT_STREAM

<dd></dd>

### -field VT_STORAGE

<dd></dd>

### -field VT_STREAMED_OBJECT

<dd></dd>

### -field VT_STORED_OBJECT

<dd></dd>

### -field VT_BLOB_OBJECT

<dd></dd>

### -field VT_CF

<dd></dd>

### -field VT_CLSID

<dd></dd>

### -field  VT_VECTOR

<dd></dd>

### -field VT_ARRAY

<dd></dd>

### -field VT_BYREF

<dd></dd>

### -field  VT_RESERVED

<dd></dd>

### -field VT_ILLEGAL

<dd></dd>

### -field VT_ILLEGALMASKED

<dd></dd>

### -field VT_TYPEMASK

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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>