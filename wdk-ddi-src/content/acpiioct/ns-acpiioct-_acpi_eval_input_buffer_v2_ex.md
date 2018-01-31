---
UID : NS:acpiioct._ACPI_EVAL_INPUT_BUFFER_V2_EX
title : "_ACPI_EVAL_INPUT_BUFFER_V2_EX"
author : windows-driver-content
description : This topic describes the ACPI_EVAL_INPUT_BUFFER_V2_EX structure.
old-location : acpi\acpi_eval_input_buffer_v2_ex.htm
old-project : acpi
ms.assetid : 5086CA33-58B0-4F3A-9AE4-428CCE6EFB6B
ms.author : windowsdriverdev
ms.date : 12/31/2017
ms.keywords : acpiioct/ACPI_EVAL_INPUT_BUFFER_V2_EX, ACPI_EVAL_INPUT_BUFFER_V2_EX structure [ACPI Devices], acpi.acpi_eval_input_buffer_v2_ex, PACPI_EVAL_INPUT_BUFFER_V2_EX, PACPI_EVAL_INPUT_BUFFER_V2_EX structure pointer [ACPI Devices], ACPI_EVAL_INPUT_BUFFER_V2_EX, acpiioct/PACPI_EVAL_INPUT_BUFFER_V2_EX, *PACPI_EVAL_INPUT_BUFFER_V2_EX, _ACPI_EVAL_INPUT_BUFFER_V2_EX
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : acpiioct.h
req.include-header : Acpiioct.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709 and later versions.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PACPI_EVAL_INPUT_BUFFER_V2_EX, ACPI_EVAL_INPUT_BUFFER_V2_EX"
---

# _ACPI_EVAL_INPUT_BUFFER_V2_EX structure
This topic describes the  <b>ACPI_EVAL_INPUT_BUFFER_V2_EX</b> structure.

## Syntax
````
typedef struct _ACPI_EVAL_INPUT_BUFFER_V2_EX {
  ULONG                  Signature;
  _Null_terminated_ CHAR MethodName[256];
} ACPI_EVAL_INPUT_BUFFER_V2_EX, *PACPI_EVAL_INPUT_BUFFER_V2_EX;
````

## Members


`MethodName`



`Signature`

Defines the <b>ULONG</b> member <b>Signature</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | acpiioct.h (include Acpiioct.h) |