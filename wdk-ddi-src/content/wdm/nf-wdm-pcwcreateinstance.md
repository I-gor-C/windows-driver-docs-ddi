---
UID: NF:wdm.PcwCreateInstance
title: PcwCreateInstance function
author: windows-driver-content
description: The PcwCreateInstance function creates a new instance for the specified registered counter set.
old-location: devtest\pcwcreateinstance.htm
old-project: devtest
ms.assetid: ed9bd8fa-a6e6-465a-8415-3e9c19233419
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: PcwCreateInstance, PcwCreateInstance function [Driver Development Tools], devtest.pcwcreateinstance, km_pcw_32dba149-fed7-4e86-b68c-1f3a6348cb7a.xml, wdm/PcwCreateInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
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
req.irql: "<=APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	PcwCreateInstance
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# PcwCreateInstance function
The <b>PcwCreateInstance</b> function creates a new instance for the specified registered counter set.

## Syntax

```
NTSTATUS PcwCreateInstance(
  PPCW_INSTANCE     *Instance,
  PPCW_REGISTRATION Registration,
  PCUNICODE_STRING  Name,
  ULONG             Count,
  PPCW_DATA         Data
);
```

## Parameters

`Instance`

A pointer to receive the newly created instance.

`Registration`

A pointer to the registered provider that owns this instance of the counter set.

`Name`

A pointer to the Unicode string that contains the name of the instance of the counter set.

`Count`

The number of data blocks that are associated with this instance.

`Data`

A pointer to an array of data blocks that contains the counter values of this instance.


## Return Value

This function returns one of the following values:

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
The instance was successfully created,

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER_4</b></dt>
</dl>
</td>
<td width="60%">
The number of structures, specified by <i>Count</i>, is not valid for the registered provider.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_BUFFER_SIZE</b></dt>
</dl>
</td>
<td width="60%">
A problem was detected with the size of the data buffer and the counter set,

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INTEGER_OVERFLOW</b></dt>
</dl>
</td>
<td width="60%">
The size of the structure, specified by <i>Count</i>, overflows the data buffer,

</td>
</tr>
</table>

## Remarks

Before the provider uses this function, the provider must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550323">PcwRegister</a> function to create a registration.

Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550316">PcwCloseInstance</a> function to close this instance.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<=APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550316">PcwCloseInstance</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550323">PcwRegister</a>