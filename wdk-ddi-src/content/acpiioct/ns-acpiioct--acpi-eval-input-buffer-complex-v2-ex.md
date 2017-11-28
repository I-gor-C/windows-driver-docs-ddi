---
UID: NS.acpiioct._ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX
title: ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX
author: windows-driver-content
description: This topic describes the ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX structure.
old-location: acpi\acpi_eval_input_buffer_complex_v2_ex.htm
old-project: acpi
ms.assetid: 50AEF454-8E36-4348-9340-330094D2FDF8
ms.author: windowsdriverdev
ms.date: 11/16/2017
ms.keywords: ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX, ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX, *PACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX
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
req.alt-api: ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX
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

# ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX structure



## -description
<p>This topic describes the <b>ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX</b> structure.</p>


## -syntax

````
typedef struct _ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX {
  ULONG                                               Signature;
  CHAR                                                MethodName[256];
  ULONG                                               Size;
  ULONG                                               ArgumentCount;
  _Field_size_(ArgumentCount) ACPI_METHOD_ARGUMENT_V2 Argument[ANYSIZE_ARRAY];
} ACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX, *PACPI_EVAL_INPUT_BUFFER_COMPLEX_V2_EX;
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