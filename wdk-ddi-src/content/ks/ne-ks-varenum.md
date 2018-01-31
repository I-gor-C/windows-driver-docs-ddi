---
UID : NE:ks.VARENUM
title : VARENUM
author : windows-driver-content
description : "."
old-location : stream\varenum.htm
old-project : stream
ms.assetid : 00F015F4-708F-4272-A903-56C44DC6646E
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/VT_SAFEARRAY, ks/VT_R4, ks/VT_USERDEFINED, VT_BLOB_OBJECT, ks/VT_TYPEMASK, VT_DECIMAL, VT_BYREF, VT_DATE, VT_NULL, ks/VT_UNKNOWN, ks/VT_ERROR, ks/VT_DISPATCH, VT_UI1, ks/ VT_VECTOR, VT_BOOL, ks/VT_PTR, stream.varenum, ks/VT_NULL, VARENUM enumeration [Streaming Media Devices], ks/VT_STREAMED_OBJECT, VT_I1, ks/VT_CY, VT_DISPATCH, ks/VT_VOID, VT_UI2, VT_LPSTR, VT_CF, VT_FILETIME, ks/VT_I1, VT_UI8, VT_HRESULT, VT_UNKNOWN, VT_ILLEGAL, ks/VT_DATE, VT_VOID, VT_STREAMED_OBJECT, ks/VT_CARRAY, ks/VT_BOOL, ks/VT_ILLEGALMASKED, VT_PTR, ks/VT_UI4, VT_USERDEFINED, VT_ILLEGALMASKED, ks/VT_UI8, ks/VT_STORED_OBJECT, VT_STORED_OBJECT, VT_STREAM, VT_I2, VT_STORAGE, VT_RESERVED, VT_I8, VT_I4, VT_LPWSTR, ks/VT_ARRAY, VT_VECTOR, ks/ VT_RESERVED, ks/VT_DECIMAL, ks/VT_BLOB_OBJECT, VT_EMPTY, VT_INT, VT_ERROR, ks/VT_UINT, ks/VT_INT, ks/VT_VARIANT, ks/VT_I2, ks/VT_UI1, VT_UI4, ks/VT_I8, ks/VT_UI2, ks/VT_FILETIME, VT_CARRAY, VT_UINT, ks/VARENUM, ks/VT_ILLEGAL, VT_SAFEARRAY, VT_R8, VT_TYPEMASK, ks/VT_STORAGE, ks/VT_STREAM, ks/VT_R8, VT_CY, ks/VT_HRESULT, VT_BLOB, ks/VT_BLOB, ks/VT_CF, ks/VT_LPSTR, VT_ARRAY, VT_VARIANT, ks/VT_EMPTY, VT_CLSID, VARENUM, VT_R4, ks/VT_BSTR, ks/VT_BYREF, VT_BSTR, ks/VT_LPWSTR, ks/VT_CLSID, ks/VT_I4
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ks.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---

# VARENUM Enumeration


## Syntax
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

## Constants

<table>

<tr>
<td>VT_ARRAY</td>
<td></td>
</tr>

<tr>
<td>VT_BLOB</td>
<td></td>
</tr>

<tr>
<td>VT_BLOB_OBJECT</td>
<td></td>
</tr>

<tr>
<td>VT_BOOL</td>
<td></td>
</tr>

<tr>
<td>VT_BSTR</td>
<td></td>
</tr>

<tr>
<td>VT_BYREF</td>
<td></td>
</tr>

<tr>
<td>VT_CARRAY</td>
<td></td>
</tr>

<tr>
<td>VT_CF</td>
<td></td>
</tr>

<tr>
<td>VT_CLSID</td>
<td></td>
</tr>

<tr>
<td>VT_CY</td>
<td></td>
</tr>

<tr>
<td>VT_DATE</td>
<td></td>
</tr>

<tr>
<td>VT_DECIMAL</td>
<td></td>
</tr>

<tr>
<td>VT_DISPATCH</td>
<td></td>
</tr>

<tr>
<td>VT_EMPTY</td>
<td></td>
</tr>

<tr>
<td>VT_ERROR</td>
<td></td>
</tr>

<tr>
<td>VT_FILETIME</td>
<td></td>
</tr>

<tr>
<td>VT_HRESULT</td>
<td></td>
</tr>

<tr>
<td>VT_I1</td>
<td></td>
</tr>

<tr>
<td>VT_I2</td>
<td></td>
</tr>

<tr>
<td>VT_I4</td>
<td></td>
</tr>

<tr>
<td>VT_I8</td>
<td></td>
</tr>

<tr>
<td>VT_ILLEGAL</td>
<td></td>
</tr>

<tr>
<td>VT_ILLEGALMASKED</td>
<td></td>
</tr>

<tr>
<td>VT_INT</td>
<td></td>
</tr>

<tr>
<td>VT_LPSTR</td>
<td></td>
</tr>

<tr>
<td>VT_LPWSTR</td>
<td></td>
</tr>

<tr>
<td>VT_NULL</td>
<td></td>
</tr>

<tr>
<td>VT_PTR</td>
<td></td>
</tr>

<tr>
<td>VT_R4</td>
<td></td>
</tr>

<tr>
<td>VT_R8</td>
<td></td>
</tr>

<tr>
<td>VT_RESERVED</td>
<td></td>
</tr>

<tr>
<td>VT_SAFEARRAY</td>
<td></td>
</tr>

<tr>
<td>VT_STORAGE</td>
<td></td>
</tr>

<tr>
<td>VT_STORED_OBJECT</td>
<td></td>
</tr>

<tr>
<td>VT_STREAM</td>
<td></td>
</tr>

<tr>
<td>VT_STREAMED_OBJECT</td>
<td></td>
</tr>

<tr>
<td>VT_TYPEMASK</td>
<td></td>
</tr>

<tr>
<td>VT_UI1</td>
<td></td>
</tr>

<tr>
<td>VT_UI2</td>
<td></td>
</tr>

<tr>
<td>VT_UI4</td>
<td></td>
</tr>

<tr>
<td>VT_UI8</td>
<td></td>
</tr>

<tr>
<td>VT_UINT</td>
<td></td>
</tr>

<tr>
<td>VT_UNKNOWN</td>
<td></td>
</tr>

<tr>
<td>VT_USERDEFINED</td>
<td></td>
</tr>

<tr>
<td>VT_VARIANT</td>
<td></td>
</tr>

<tr>
<td>VT_VECTOR</td>
<td></td>
</tr>

<tr>
<td>VT_VOID</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h |