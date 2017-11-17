---
UID: NS.acpiioct._ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX
title: ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX
author: windows-driver-content
description: This topic describes the ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX structure.
old-location: acpi\acpi_eval_input_buffer_complex_v1_ex.htm
ms.assetid: 26532FEE-6FBA-4933-BE69-A06FAC0664ED
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: acpi
req.header: acpiioct.h
req.include-header: Acpiioct.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX
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
ms.keywords: ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX, ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX, *PACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX
---

# ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX structure



## -description
<p>This topic describes the <b>ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX</b> structure.</p>


## -syntax

````
typedef struct _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX {
  ULONG                                               Signature;
  CHAR                                                MethodName[256];
  ULONG                                               Size;
  ULONG                                               ArgumentCount;
  _Field_size_(ArgumentCount) ACPI_METHOD_ARGUMENT_V1 Argument[ANYSIZE_ARRAY];
} ACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX, *PACPI_EVAL_INPUT_BUFFER_COMPLEX_V1_EX;
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

### -field <b>Size</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>Size</b>.</p>
</dd>

### -field <b>ArgumentCount</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>ArgumentCount</b>.</p>
</dd>

### -field <b>Argument[ANYSIZE_ARRAY]</b>

<dd>
<p>Defines the <b>ACPI_METHOD_ARGUMENT_V1</b> member <b>Argument[ANYSIZE_ARRAY]</b>.</p>
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