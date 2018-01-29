---
UID : NF:ntddk.RtlRunOnceBeginInitialize
title : RtlRunOnceBeginInitialize function
author : windows-driver-content
description : The RtlRunOnceBeginInitialize routine begins a one-time initialization.
old-location : kernel\rtlrunoncebegininitialize.htm
old-project : kernel
ms.assetid : ed96b2ec-95ea-47a6-a3b0-f4d018e0c8e2
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.rtlrunoncebegininitialize, RtlRunOnceBeginInitialize, ntddk/RtlRunOnceBeginInitialize, RtlRunOnceBeginInitialize routine [Kernel-Mode Driver Architecture], k109_f7299ad8-4567-4ad8-a13c-2329a12af6ea.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Universal
req.target-min-winverclnt : Available in Windows Vista and later versions of Windows.
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
req.irql : "<= APC_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PWHEA_RAW_DATA_FORMAT, WHEA_RAW_DATA_FORMAT"
---


# RtlRunOnceBeginInitialize function
The <b>RtlRunOnceBeginInitialize</b> routine begins a one-time initialization.

## Syntax

````
NTSTATUS RtlRunOnceBeginInitialize(
  _Inout_ PRTL_RUN_ONCE RunOnce,
  _In_    ULONG         Flags,
  _Out_   PVOID         *Context
);
````

## Parameters

`RunOnce`

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a> one-time initialization structure.

`Flags`

Drivers can optionally specify one or more of the following flags:

`Context`

Specifies a pointer to a PVOID variable that receives the initialized data. The value of *<i>Context</i> is valid only when the routine returns STATUS_SUCCESS.


## Return Value

<b>RtlRunOnceBeginInitialize</b> returns one of the following NTSTATUS values:
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
The one-time initialization has already completed. The initialized data is stored in the memory location that <i>Context</i> points to.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_PENDING</b></dt>
</dl>
</td>
<td width="60%">
The caller has successfully begun one-time initialization. The caller now performs the driver-specific initialization steps and then calls <a href="..\ntddk\nf-ntddk-rtlrunoncecomplete.md">RtlRunOnceComplete</a> to complete the initialization. 

</td>
</tr>
</table>

## Remarks

Drivers can alternatively perform one-time initialization by calling <a href="..\ntddk\nf-ntddk-rtlrunonceexecuteonce.md">RtlRunOnceExecuteOnce</a> and supplying a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563635">RunOnceInitialization</a> routine.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563635">RunOnceInitialization</a>

<a href="..\ntddk\nf-ntddk-rtlrunoncecomplete.md">RtlRunOnceComplete</a>

<a href="..\ntddk\nf-ntddk-rtlrunonceinitialize.md">RtlRunOnceInitialize</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563626">RTL_RUN_ONCE</a>

<a href="..\ntddk\nf-ntddk-rtlrunonceexecuteonce.md">RtlRunOnceExecuteOnce</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlRunOnceBeginInitialize routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>