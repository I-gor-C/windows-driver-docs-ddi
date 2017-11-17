---
UID: NS.acpiioct._ACPI_EVAL_OUTPUT_BUFFER_V2
title: ACPI_EVAL_OUTPUT_BUFFER_V2
author: windows-driver-content
description: This topic describes the ACPI_EVAL_OUTPUT_BUFFER_V2 structure.
old-location: acpi\acpi_eval_output_buffer_v2.htm
ms.assetid: 355A600E-F207-4A3F-80AE-EA2DAE810DA3
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
req.alt-api: ACPI_EVAL_OUTPUT_BUFFER_V2
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
ms.keywords: ACPI_EVAL_OUTPUT_BUFFER_V2, ACPI_EVAL_OUTPUT_BUFFER_V2
---

# ACPI_EVAL_OUTPUT_BUFFER_V2 structure



## -description
<p>This topic describes the  <b>ACPI_EVAL_OUTPUT_BUFFER_V2</b> structure.</p>


## -syntax

````
typedef struct _ACPI_EVAL_OUTPUT_BUFFER_V2 {
  ULONG                                                                                                           Signature;
  ULONG                                                                                                           Length;
  ULONG                                                                                                           Count;
  _Field_size_bytes_(Length - FIELD_OFFSET(struct _ACPI_EVAL_OUTPUT_BUFFER_V2, Argument)) ACPI_METHOD_ARGUMENT_V2 Argument[ANYSIZE_ARRAY];
} ACPI_EVAL_OUTPUT_BUFFER_V2;
````


## -struct-fields
<dl>

### -field <b>Signature</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>Signature</b>.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>Length</b>.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>Count</b>.</p>
</dd>

### -field <b>Argument[ANYSIZE_ARRAY]</b>

<dd>
<p>Defines the <b>ACPI_METHOD_ARGUMENT_V2</b> member <b>Argument[ANYSIZE_ARRAY]</b>.</p>
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