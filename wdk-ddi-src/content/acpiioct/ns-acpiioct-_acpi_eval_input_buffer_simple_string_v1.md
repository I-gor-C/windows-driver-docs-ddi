---
UID: NS:acpiioct._ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1
title: "_ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1"
author: windows-driver-content
description: The ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING structure is used as input to an IOCTL_ACPI_EVAL_METHOD request and to an IOCTL_ACPI_ASYNC_EVAL_METHOD request. The structure supplies the name of a control method and an input argument that is an ASCII string.
old-location: acpi\acpi_eval_input_buffer_simple_string.htm
old-project: acpi
ms.assetid: f8f5db79-d1ea-4ce8-b941-49ef7518b941
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING, *PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING, ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 structure [ACPI Devices], PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 structure pointer [ACPI Devices], _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, acpi-meth-eval-ref_e7f8f5c8-9aef-488b-b041-2dc9d2f1a280.xml, acpi.acpi_eval_input_buffer_simple_string, acpiioct/ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, acpiioct/PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: acpiioct.h
req.include-header: Acpiioct.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Acpiioct.h
api_name:
-	ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1
product:
- Windows
targetos: Windows
req.typenames: ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, *PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING, *PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING
---

# _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 structure
The ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING structure is used as input to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536148">IOCTL_ACPI_EVAL_METHOD</a> request and to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a> request. The structure supplies the name of a control method and an input argument that is an ASCII string.

## Syntax
```
typedef struct _ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1 {
  ULONG Signature;
  union {
    UCHAR MethodName[4];
    ULONG MethodNameAsUlong;
  } DUMMYUNIONNAME;
  ULONG StringLength;
  UCHAR String[ANYSIZE_ARRAY];
} *PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING, ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, *PACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_V1, ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING;
```

## Members


`Signature`

The signature of a string input buffer, which must be set to ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE.

`DUMMYUNIONNAME`



`StringLength`

The number of ASCII characters in the array of characters that is supplied by <b>String</b>.

`String`

An ASCII character string that contains the number of characters that is specified by <b>StringLength</b>. The string does not include a NULL terminator.

## Remarks
If a device supports a control method named ABCD that takes an ASCII string as input, a driver for the device can evaluate the method by sending an IOCTL_ACPI_EVAL_METHOD request or an IOCTL_ACPI_ASYNC_EVAL_METHOD request to the device and setting the members of the input ACPI_EVAL_INPUT_BUFFER structure as follows:

<ul>
<li>
Set <b>Signature</b> to ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_SIGNATURE.

</li>
<li>
Set <b>MethodName</b> to 'ABCD' or <b>MethodNameAsUlong</b> to (ULONG)('DCBA').

</li>
<li>
Set <b>StringLength</b> to the number of characters that is supplied by <b>String</b>.

</li>
<li>
Set <b>String</b> to the input string.

</li>
</ul>
For more information about how to use this structure, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods">Evaluating ACPI Control Methods</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 2000 and later versions of Windows. Windows 2000 and later versions of Windows. |
| **Header** | acpiioct.h (include Acpiioct.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536145">IOCTL_ACPI_ASYNC_EVAL_METHOD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536148">IOCTL_ACPI_EVAL_METHOD</a>