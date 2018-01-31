---
UID : NF:ntddk.RtlValidateCorrelationVector
title : RtlValidateCorrelationVector function
author : windows-driver-content
description : Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2).
old-location : kernel\rtlvalidatecorrelationvector.htm
old-project : kernel
ms.assetid : a73ab33b-3e8c-43d8-8547-1483bcd2af52
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlValidateCorrelationVector, ntddk/RtlValidateCorrelationVector, RtlValidateCorrelationVector function [Kernel-Mode Driver Architecture], kernel.rtlvalidatecorrelationvector
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe (kernel mode)
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# RtlValidateCorrelationVector function
Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2).
    The function specifically checks if the first 22 bytes are a valid base64 representation of a 16 byte
        buffer
         and the remaining characters match the (\.\d+)+  regular expression.

## Syntax

````
 NTSTATUS  RtlValidateCorrelationVector(
  _Inout_ PCORRELATION_VECTOR CorrelationVector
);
````

## Parameters

`Vector`

TBD


## Return Value

Returns an NTSTATUS value that indicates the success of failure of the operation. 
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The correlation vector is valid.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
The supplied correlation vector is invalid.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |