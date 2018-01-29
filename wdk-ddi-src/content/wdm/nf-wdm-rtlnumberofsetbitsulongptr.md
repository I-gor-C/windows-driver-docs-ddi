---
UID : NF:wdm.RtlNumberOfSetBitsUlongPtr
title : RtlNumberOfSetBitsUlongPtr function
author : windows-driver-content
description : The RtlNumberOfSetBitsUlongPtr routine returns the number of bits in the specified ULONG_PTR integer value that are set to one.
old-location : kernel\rtlnumberofsetbitsulongptr.htm
old-project : kernel
ms.assetid : CD619018-7E6D-4B45-93C3-AD89FDFEB1E9
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.rtlnumberofsetbitsulongptr, wdm/RtlNumberOfSetBitsUlongPtr, RtlNumberOfSetBitsUlongPtr routine [Kernel-Mode Driver Architecture], RtlNumberOfSetBitsUlongPtr
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows Vista.
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
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : Any IRQL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# RtlNumberOfSetBitsUlongPtr function
The <b>RtlNumberOfSetBitsUlongPtr</b> routine returns the number of bits in the specified ULONG_PTR integer value that are set to one.

## Syntax

````
ULONG RtlNumberOfSetBitsUlongPtr(
  _In_ ULONG_PTR Target
);
````

## Parameters

`Target`

A ULONG_PTR integer value.


## Return Value

<b>RtlNumberOfSetBitsUlongPtr</b> returns a count of the bits in the <i>Target</i> parameter that are set to one.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | Any IRQL |
| **DDI compliance rules** |  |