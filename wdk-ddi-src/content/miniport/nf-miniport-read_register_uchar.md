---
UID: NF:miniport.READ_REGISTER_UCHAR
title: READ_REGISTER_UCHAR function
author: windows-driver-content
description: The READ_REGISTER_UCHAR routine reads a byte from the specified register address.
old-location: kernel\read_register_uchar.htm
old-project: kernel
ms.assetid: 49f9d7d7-c774-4ba5-a9f3-6d605a3de674
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: READ_REGISTER_UCHAR, wdm/READ_REGISTER_UCHAR, kernel.read_register_uchar, k103_b7970afc-0b18-49c4-b873-a9fd689c0c97.xml, READ_REGISTER_UCHAR routine [Kernel-Mode Driver Architecture]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: miniport.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Ioaccess.h, Miniport.h, Wudfwdm.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level (see Remarks section)
topictype:
-	APIRef
-	kbSyntax
apitype:
-	DllExport
apilocation:
-	NtosKrnl.exe
apiname:
-	READ_REGISTER_UCHAR
product: Windows
targetos: Windows
req.typenames: MEMORY_CACHING_TYPE
---


# READ_REGISTER_UCHAR function
The <b>READ_REGISTER_UCHAR</b> routine reads a byte from the specified register address.

## Syntax

````
UCHAR READ_REGISTER_UCHAR(
  _In_ PUCHAR Register
);
````

## Parameters

`Register`




## Return Value

<b>READ_REGISTER_UCHAR</b> returns the byte read from the specified register address.

## Remarks

Callers of <b>READ_REGISTER_UCHAR</b> can be running at any IRQL, assuming the <i>Register</i> is resident, mapped device memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | miniport.h (include Wdm.h, Ntddk.h, Ntifs.h, Ioaccess.h, Miniport.h, Wudfwdm.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level (see Remarks section) |