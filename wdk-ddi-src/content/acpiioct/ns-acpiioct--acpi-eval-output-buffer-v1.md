---
UID: NS.acpiioct._ACPI_EVAL_OUTPUT_BUFFER_V1
title: ACPI_EVAL_OUTPUT_BUFFER_V1
author: windows-driver-content
description: This topic describes the ACPI_EVAL_OUTPUT_BUFFER_V1 structure.
old-location: acpi\acpi_eval_output_buffer_v1.htm
old-project: acpi
ms.assetid: 92BBE3B8-6B99-43CC-86E8-0D715B0E9B5E
ms.author: windowsdriverdev
ms.date: 11/16/2017
ms.keywords: ACPI_EVAL_OUTPUT_BUFFER_V1, ACPI_EVAL_OUTPUT_BUFFER_V1
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
req.alt-api: ACPI_EVAL_OUTPUT_BUFFER_V1
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

# ACPI_EVAL_OUTPUT_BUFFER_V1 structure



## -description
<p>This topic describes the  <b>ACPI_EVAL_OUTPUT_BUFFER_V1</b> structure.</p>


## -syntax

````
typedef struct _ACPI_EVAL_OUTPUT_BUFFER_V1 {
  ULONG                                                                                                           Signature;
  ULONG                                                                                                           Length;
  ULONG                                                                                                           Count;
  _Field_size_bytes_(Length - FIELD_OFFSET(struct _ACPI_EVAL_OUTPUT_BUFFER_V1, Argument)) ACPI_METHOD_ARGUMENT_V1 Argument[ANYSIZE_ARRAY];
} ACPI_EVAL_OUTPUT_BUFFER_V1;
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