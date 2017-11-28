---
UID: NS.acpiioct._ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX~r1
title: ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX
author: windows-driver-content
description: This topic describes the ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX structure.
old-location: acpi\acpi_eval_input_buffer_simple_integer_v1_ex.htm
old-project: acpi
ms.assetid: 96F3CEE7-6B57-41E0-90CA-10C144BA3D1D
ms.author: windowsdriverdev
ms.date: 11/16/2017
ms.keywords: ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: acpiioct.h
req.include-header: Acpiioct.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX
req.alt-loc: Acpiioct.h
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

# ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX structure



## -description
<p>This topic describes the <b>ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX</b> structure.</p>


## -syntax

````
typedef struct _ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX {
  ULONG                  Signature;
  _Null_terminated_ CHAR MethodName[256];
  ULONG64                IntegerArgument;
} ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX, *PACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_V1_EX;
````


## -struct-fields
<dl>

### -field <b>Signature</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>Signature</b>.</p>
</dd>

### -field <b>MethodName[256]</b>

<dd>
<p>NULL terminated name string.</p>
</dd>

### -field <b>IntegerArgument</b>

<dd>
<p>Defines the <b>ULONG64</b> member <b>IntegerArgument</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1709 and later versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Acpiioct.h (include Acpiioct.h)</dt>
</dl>
</td>
</tr>
</table>