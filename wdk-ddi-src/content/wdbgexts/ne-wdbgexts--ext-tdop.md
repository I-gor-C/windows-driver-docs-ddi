---
UID: NE.wdbgexts._EXT_TDOP
title: EXT_TDOP
author: windows-driver-content
description: The EXT_TDOP enumeration is used in the Operation member of the EXT_TYPED_DATA structure to specify which suboperation the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation will perform.
old-location: debugger\ext_tdop.htm
old-project: debugger
ms.assetid: 1793aaff-b0ac-4858-8a15-56eace87a09a
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: VPCI_WRITE_BLOCK_INPUT, VPCI_WRITE_BLOCK_INPUT, *PVPCI_WRITE_BLOCK_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdbgexts.h
req.include-header: WdbgExts.h, DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EXT_TDOP
req.alt-loc: WdbgExts.h
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
req.product: Windows 10 or later.
---

# EXT_TDOP enumeration



## -description
<p>The EXT_TDOP enumeration is used in the <b>Operation</b> member of the <a href="..\wdbgexts\ns-wdbgexts--ext-typed-data.md">EXT_TYPED_DATA</a> structure to specify which suboperation the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541547">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</a>
<a href="debugger.request"> Request</a> operation will perform.</p>


## -syntax

````
typedef enum _EXT_TDOP { 
  EXT_TDOP_COPY,
  EXT_TDOP_RELEASE,
  EXT_TDOP_SET_FROM_EXPR,
   EXT_TDOP_SET_FROM_U64_EXPR,
  EXT_TDOP_GET_FIELD,
  EXT_TDOP_EVALUATE,
  EXT_TDOP_GET_TYPE_NAME,
  EXT_TDOP_OUTPUT_TYPE_NAME,
  EXT_TDOP_OUTPUT_SIMPLE_VALUE,
  EXT_TDOP_OUTPUT_FULL_VALUE,
  EXT_TDOP_HAS_FIELD,
  EXT_TDOP_GET_FIELD_OFFSET,
  EXT_TDOP_GET_ARRAY_ELEMENT,
  EXT_TDOP_GET_DEREFERENCE,
  EXT_TDOP_GET_TYPE_SIZE,
  EXT_TDOP_OUTPUT_TYPE_DEFINITION,
  EXT_TDOP_GET_POINTER_TO,
  EXT_TDOP_SET_FROM_TYPE_ID_AND_U64,
  EXT_TDOP_SET_PTR_FROM_TYPE_ID_AND_U64,
  EXT_TDOP_COUNT
} EXT_TDOP;
````


## -enum-fields
<dl>

### -field <a id="EXT_TDOP_COPY"></a><a id="ext_tdop_copy"></a><b>EXT_TDOP_COPY</b>

<dd>
<p>Makes a copy of a typed data description.</p>
</dd>

### -field <a id="EXT_TDOP_RELEASE"></a><a id="ext_tdop_release"></a><b>EXT_TDOP_RELEASE</b>

<dd>
<p>Releases a typed data description.</p>
</dd>

### -field <a id="EXT_TDOP_SET_FROM_EXPR"></a><a id="ext_tdop_set_from_expr"></a><b>EXT_TDOP_SET_FROM_EXPR</b>

<dd>
<p>Returns the value of an expression.</p>
</dd>

### -field <a id="_EXT_TDOP_SET_FROM_U64_EXPR"></a><a id="_ext_tdop_set_from_u64_expr"></a><b> EXT_TDOP_SET_FROM_U64_EXPR</b>

<dd>
<p>Returns the value of an expression. An optional address can be provided as a parameter to the expression.</p>
</dd>

### -field <a id="EXT_TDOP_GET_FIELD"></a><a id="ext_tdop_get_field"></a><b>EXT_TDOP_GET_FIELD</b>

<dd>
<p>Returns a member of a structure.</p>
</dd>

### -field <a id="EXT_TDOP_EVALUATE"></a><a id="ext_tdop_evaluate"></a><b>EXT_TDOP_EVALUATE</b>

<dd>
<p>Returns the value of an expression. An optional value can be provided as a parameter to the expression.</p>
</dd>

### -field <a id="EXT_TDOP_GET_TYPE_NAME"></a><a id="ext_tdop_get_type_name"></a><b>EXT_TDOP_GET_TYPE_NAME</b>

<dd>
<p>Returns the type name for typed data.</p>
</dd>

### -field <a id="EXT_TDOP_OUTPUT_TYPE_NAME"></a><a id="ext_tdop_output_type_name"></a><b>EXT_TDOP_OUTPUT_TYPE_NAME</b>

<dd>
<p>Prints the type name for typed data.</p>
</dd>

### -field <a id="EXT_TDOP_OUTPUT_SIMPLE_VALUE"></a><a id="ext_tdop_output_simple_value"></a><b>EXT_TDOP_OUTPUT_SIMPLE_VALUE</b>

<dd>
<p>Prints the value of typed data.</p>
</dd>

### -field <a id="EXT_TDOP_OUTPUT_FULL_VALUE"></a><a id="ext_tdop_output_full_value"></a><b>EXT_TDOP_OUTPUT_FULL_VALUE</b>

<dd>
<p>Prints the type and value for typed data.</p>
</dd>

### -field <a id="EXT_TDOP_HAS_FIELD"></a><a id="ext_tdop_has_field"></a><b>EXT_TDOP_HAS_FIELD</b>

<dd>
<p>Determines whether a structure contains a specified member.</p>
</dd>

### -field <a id="EXT_TDOP_GET_FIELD_OFFSET"></a><a id="ext_tdop_get_field_offset"></a><b>EXT_TDOP_GET_FIELD_OFFSET</b>

<dd>
<p>Returns the offset of a member within a structure.</p>
</dd>

### -field <a id="EXT_TDOP_GET_ARRAY_ELEMENT"></a><a id="ext_tdop_get_array_element"></a><b>EXT_TDOP_GET_ARRAY_ELEMENT</b>

<dd>
<p>Returns an element from an array.</p>
</dd>

### -field <a id="EXT_TDOP_GET_DEREFERENCE"></a><a id="ext_tdop_get_dereference"></a><b>EXT_TDOP_GET_DEREFERENCE</b>

<dd>
<p>Dereferences a pointer, returning the value it points to.</p>
</dd>

### -field <a id="EXT_TDOP_GET_TYPE_SIZE"></a><a id="ext_tdop_get_type_size"></a><b>EXT_TDOP_GET_TYPE_SIZE</b>

<dd>
<p>Returns the size of the specified typed data.</p>
</dd>

### -field <a id="EXT_TDOP_OUTPUT_TYPE_DEFINITION"></a><a id="ext_tdop_output_type_definition"></a><b>EXT_TDOP_OUTPUT_TYPE_DEFINITION</b>

<dd>
<p>Prints the definition of the type for the specified typed data.</p>
</dd>

### -field <a id="EXT_TDOP_GET_POINTER_TO"></a><a id="ext_tdop_get_pointer_to"></a><b>EXT_TDOP_GET_POINTER_TO</b>

<dd>
<p>Returns a new typed data description that represents a pointer to specified typed data.</p>
</dd>

### -field <a id="EXT_TDOP_SET_FROM_TYPE_ID_AND_U64"></a><a id="ext_tdop_set_from_type_id_and_u64"></a><b>EXT_TDOP_SET_FROM_TYPE_ID_AND_U64</b>

<dd>
<p>Creates a typed data description from a type and memory location.</p>
</dd>

### -field <a id="EXT_TDOP_SET_PTR_FROM_TYPE_ID_AND_U64"></a><a id="ext_tdop_set_ptr_from_type_id_and_u64"></a><b>EXT_TDOP_SET_PTR_FROM_TYPE_ID_AND_U64</b>

<dd>
<p>Creates a typed data description representing a pointer to a specified memory location with specified type.</p>
</dd>

### -field <a id="EXT_TDOP_COUNT"></a><a id="ext_tdop_count"></a><b>EXT_TDOP_COUNT</b>

<dd>
<p>Does not specify an operation. Instead, it represents the number of suboperations defined in the EXT_TDOP enumeration.
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
<dt>WdbgExts.h (include WdbgExts.h or DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdbgexts\ns-wdbgexts--ext-typed-data.md">EXT_TYPED_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541547">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</a>
</dt>
<dt>
<a href="debugger.request">Request</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20EXT_TDOP enumeration%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
