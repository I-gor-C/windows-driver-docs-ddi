---
UID: NF:ntifs.RtlRandom
title: RtlRandom function
author: windows-driver-content
description: The RtlRandom routine returns a random number that was generated from a given seed value.
old-location: ifsk\rtlrandom.htm
old-project: ifsk
ms.assetid: f3975ad7-8eb8-4f46-8024-6a1decc21c77
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RtlRandom, RtlRandom routine [Installable File System Drivers], ifsk.rtlrandom, ntifs/RtlRandom, rtlref_c9c196b4-7335-4320-ae7f-7c565b6f73e6.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later.
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
req.irql: "< DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	RtlRandom
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlRandom function
The <b>RtlRandom</b> routine returns a random number that was generated from a given seed value.

## Syntax

````
ULONG RtlRandom(
  _Inout_ PULONG Seed
);
````

## Parameters

`Seed`

Unsigned long value from which to generate a random number.


## Return Value

<b>RtlRandom</b> returns a random number in the range [0..MAXLONG-1].

## Remarks

<b>RtlRandom</b> returns values that are uniformly distributed over the range from zero to the maximum possible LONG value less 1 if it is called repeatedly with the same <i>Seed</i>.

The <b>RtlRandomEx</b> function is an improved version of the <b>RtlRandom</b> function that is twice as fast and produces better random numbers.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows 2000 and later.  |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "< DISPATCH_LEVEL" |

## See Also

<a href="..\ntifs\nf-ntifs-rtlrandomex.md">RtlRandomEx</a>