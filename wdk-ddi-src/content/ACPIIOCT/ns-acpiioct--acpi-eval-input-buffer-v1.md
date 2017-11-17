---
UID: NS.acpiioct._ACPI_EVAL_INPUT_BUFFER_V1
title: ACPI_EVAL_INPUT_BUFFER_V1
author: windows-driver-content
description: This topic describes the ACPI_EVAL_INPUT_BUFFER_V1 structure.
old-location: acpi\acpi_eval_input_buffer_v1.htm
ms.assetid: 43892D4A-91BE-4064-AB2F-F50B38A65CA9
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
req.alt-api: ACPI_EVAL_INPUT_BUFFER_V1
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
ms.keywords: ACPI_EVAL_INPUT_BUFFER_V1, ACPI_EVAL_INPUT_BUFFER_V1, *PACPI_EVAL_INPUT_BUFFER_V1
---

# ACPI_EVAL_INPUT_BUFFER_V1 structure



## -description
<p>This topic describes the  <b>ACPI_EVAL_INPUT_BUFFER_V1</b> structure.</p>


## -syntax

````
typedef struct _ACPI_EVAL_INPUT_BUFFER_V1 {
  ULONG Signature;
  union {
    UCHAR MethodName[4];
    ULONG MethodNameAsUlong;
  } DUMMYUNIONNAME;
} ACPI_EVAL_INPUT_BUFFER_V1, *PACPI_EVAL_INPUT_BUFFER_V1;
````


## -struct-fields
<dl>

### -field <b>Signature</b>

<dd>
<p>Defines the <b>ULONG</b> member <b>Signature</b>.</p>
</dd>

### -field <b>DUMMYUNIONNAME</b>

<dd>
<p>Defines the method name member of <b>DUMMYUNIONNAME</b>.</p>
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