---
UID: NE.ks.VARENUM
title: VARENUM
author: windows-driver-content
description: TBD.
old-location: stream\varenum.htm
ms.assetid: 00F015F4-708F-4272-A903-56C44DC6646E
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VARENUM
req.alt-loc: 
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
ms.keywords: MIDL_IKeywordDetectorOemAdapter_0003, KEYWORDSELECTOR
req.iface: IKeywordDetectorOemAdapter
---

# VARENUM enumeration



## -description
<p>TBD</p>


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

### -field <a id="VT_EMPTY"></a><a id="vt_empty"></a><b>VT_EMPTY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_NULL"></a><a id="vt_null"></a><b>VT_NULL</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_I2"></a><a id="vt_i2"></a><b>VT_I2</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_I4"></a><a id="vt_i4"></a><b>VT_I4</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_R4"></a><a id="vt_r4"></a><b>VT_R4</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_R8"></a><a id="vt_r8"></a><b>VT_R8</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_CY"></a><a id="vt_cy"></a><b>VT_CY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_DATE"></a><a id="vt_date"></a><b>VT_DATE</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_BSTR"></a><a id="vt_bstr"></a><b>VT_BSTR</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_DISPATCH"></a><a id="vt_dispatch"></a><b>VT_DISPATCH</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_ERROR"></a><a id="vt_error"></a><b>VT_ERROR</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_BOOL"></a><a id="vt_bool"></a><b>VT_BOOL</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_VARIANT"></a><a id="vt_variant"></a><b>VT_VARIANT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_UNKNOWN"></a><a id="vt_unknown"></a><b>VT_UNKNOWN</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_DECIMAL"></a><a id="vt_decimal"></a><b>VT_DECIMAL</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_I1"></a><a id="vt_i1"></a><b>VT_I1</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_UI1"></a><a id="vt_ui1"></a><b>VT_UI1</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_UI2"></a><a id="vt_ui2"></a><b>VT_UI2</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_UI4"></a><a id="vt_ui4"></a><b>VT_UI4</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_I8"></a><a id="vt_i8"></a><b>VT_I8</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_UI8"></a><a id="vt_ui8"></a><b>VT_UI8</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_INT"></a><a id="vt_int"></a><b>VT_INT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_UINT"></a><a id="vt_uint"></a><b>VT_UINT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_VOID"></a><a id="vt_void"></a><b>VT_VOID</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_HRESULT"></a><a id="vt_hresult"></a><b>VT_HRESULT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_PTR"></a><a id="vt_ptr"></a><b>VT_PTR</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_SAFEARRAY"></a><a id="vt_safearray"></a><b>VT_SAFEARRAY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_CARRAY"></a><a id="vt_carray"></a><b>VT_CARRAY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_USERDEFINED"></a><a id="vt_userdefined"></a><b>VT_USERDEFINED</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_LPSTR"></a><a id="vt_lpstr"></a><b>VT_LPSTR</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_LPWSTR"></a><a id="vt_lpwstr"></a><b>VT_LPWSTR</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_FILETIME"></a><a id="vt_filetime"></a><b>VT_FILETIME</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_BLOB"></a><a id="vt_blob"></a><b>VT_BLOB</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_STREAM"></a><a id="vt_stream"></a><b>VT_STREAM</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_STORAGE"></a><a id="vt_storage"></a><b>VT_STORAGE</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_STREAMED_OBJECT"></a><a id="vt_streamed_object"></a><b>VT_STREAMED_OBJECT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_STORED_OBJECT"></a><a id="vt_stored_object"></a><b>VT_STORED_OBJECT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_BLOB_OBJECT"></a><a id="vt_blob_object"></a><b>VT_BLOB_OBJECT</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_CF"></a><a id="vt_cf"></a><b>VT_CF</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_CLSID"></a><a id="vt_clsid"></a><b>VT_CLSID</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="_VT_VECTOR"></a><a id="_vt_vector"></a><b> VT_VECTOR</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_ARRAY"></a><a id="vt_array"></a><b>VT_ARRAY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_BYREF"></a><a id="vt_byref"></a><b>VT_BYREF</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="_VT_RESERVED"></a><a id="_vt_reserved"></a><b> VT_RESERVED</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_ILLEGAL"></a><a id="vt_illegal"></a><b>VT_ILLEGAL</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_ILLEGALMASKED"></a><a id="vt_illegalmasked"></a><b>VT_ILLEGALMASKED</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="VT_TYPEMASK"></a><a id="vt_typemask"></a><b>VT_TYPEMASK</b>

<dd>
<p>TBD</p>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>