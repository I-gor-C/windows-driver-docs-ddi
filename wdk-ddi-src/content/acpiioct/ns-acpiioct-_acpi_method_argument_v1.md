---
UID: NS:acpiioct._ACPI_METHOD_ARGUMENT_V1
title: "_ACPI_METHOD_ARGUMENT_V1"
author: windows-driver-content
description: The ACPI_METHOD_ARGUMENT structure contains the value of an input or output argument of an ACPI control method.
old-location: acpi\acpi_method_argument.htm
old-project: acpi
ms.assetid: 4038d5a5-9ce7-44cb-a6f0-3033617cfe6a
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PACPI_METHOD_ARGUMENT, *PACPI_METHOD_ARGUMENT_V1, ACPI_METHOD_ARGUMENT, ACPI_METHOD_ARGUMENT_V1, ACPI_METHOD_ARGUMENT_V1 structure [ACPI Devices], _ACPI_METHOD_ARGUMENT_V1, acpi-meth-eval-ref_a8988425-e05b-4e85-a345-31a367dec427.xml, acpi.acpi_method_argument, acpiioct/ACPI_METHOD_ARGUMENT_V1"
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
-	ACPI_METHOD_ARGUMENT_V1
product: Windows
targetos: Windows
req.typenames: ACPI_METHOD_ARGUMENT_V1, ACPI_METHOD_ARGUMENT
---

# _ACPI_METHOD_ARGUMENT_V1 structure
The ACPI_METHOD_ARGUMENT structure contains the value of an input or output argument of an ACPI control method.

## Syntax
````
typedef struct _ACPI_METHOD_ARGUMENT_V1 {
  USHORT Type;
  USHORT DataLength;
  union {
    ULONG Argument;
    UCHAR Data[ANYSIZE_ARRAY];
  };
} ACPI_METHOD_ARGUMENT_V1;
````

## Members


`Type`

The type of the method argument, as specified by one of the following:





#### ACPI_METHOD_ARGUMENT_INTEGER

<b>Argument</b> contains an integer value of type ULONG.



#### ACPI_METHOD_ARGUMENT_STRING

The <b>Data</b> array contains a NULL-terminated ASCII string, and <b>DataLength</b> supplies the number of characters in the string, including the NULL terminator.



#### ACPI_METHOD_ARGUMENT_BUFFER

The <b>Data</b> array contains custom data, and <b>DataLength</b> supplies the number of consecutive array elements that contain the custom data, beginning with the <b>Data</b>[0] element.



#### ACPI_METHOD_ARGUMENT_PACKAGE

The <b>Data</b> array contains an ACPI package descriptor and <b>DataLength</b> supplies the number of consecutive array elements that contain the package descriptor, beginning with the <b>Data</b>[0] element.

`DataLength`

The number of UCHAR elements in the <b>Data</b> array that contains the argument data.

`DUMMYUNIONNAME`



## Remarks
An ACPI_EVAL_OUTPUT_BUFFER structure includes an <b>Argument</b> array of ACPI_METHOD_ARGUMENT structures. The following IOCTLs evaluate control methods and return output arguments in an <a href="..\acpiioct\ns-acpiioct-_acpi_eval_output_buffer_v1.md">ACPI_EVAL_OUTPUT_BUFFER</a> structure:


<a href="..\acpiioct\ni-acpiioct-ioctl_acpi_async_eval_method.md">IOCTL_ACPI_ASYNC_EVAL_METHOD</a>



<a href="..\acpiioct\ni-acpiioct-ioctl_acpi_async_eval_method_ex.md">IOCTL_ACPI_ASYNC_EVAL_METHOD_EX</a>



<a href="..\acpiioct\ni-acpiioct-ioctl_acpi_eval_method.md">IOCTL_ACPI_EVAL_METHOD</a>



<a href="..\acpiioct\ni-acpiioct-ioctl_acpi_eval_method_ex.md">IOCTL_ACPI_EVAL_METHOD_EX</a>


The ACPI_METHOD_ARGUMENT structure is also used to supply an array of complex input arguments to a control method. The <a href="..\acpiioct\ns-acpiioct-_acpi_eval_input_buffer_complex_v1.md">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a> and <a href="..\acpiioct\ns-acpiioct-_acpi_eval_input_buffer_complex_v1_ex.md">ACPI_EVAL_INPUT_BUFFER_COMPLEX_EX</a> structures includes an <b>Argument</b> array of type ACPI_METHOD_ARGUMENT.

For more information about how to use ACPI_METHOD_ARGUMENT structures to supply and retrieve argument data to an ACPI control method, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/evaluating-acpi-control-methods">Evaluating ACPI Control Methods</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 2000 and later versions of Windows. Windows 2000 and later versions of Windows. |
| **Header** | acpiioct.h (include Acpiioct.h) |

## See Also

<a href="..\acpiioct\ns-acpiioct-_acpi_eval_input_buffer_complex_v1.md">ACPI_EVAL_INPUT_BUFFER_COMPLEX</a>



<a href="..\acpiioct\ns-acpiioct-_acpi_eval_input_buffer_complex_v1_ex.md">ACPI_EVAL_INPUT_BUFFER_COMPLEX_EX</a>



<a href="..\acpiioct\ns-acpiioct-_acpi_eval_output_buffer_v1.md">ACPI_EVAL_OUTPUT_BUFFER</a>