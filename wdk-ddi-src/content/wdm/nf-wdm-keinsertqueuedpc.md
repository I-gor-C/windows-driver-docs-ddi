---
UID: NF.wdm.KeInsertQueueDpc
title: KeInsertQueueDpc function
author: windows-driver-content
description: The KeInsertQueueDpc routine queues a DPC for execution.
old-location: kernel\keinsertqueuedpc.htm
old-project: kernel
ms.assetid: f1fc6880-23d1-4154-9305-4a918efd4a1d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: KeInsertQueueDpc
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeInsertQueueDpc
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: MarkingQueuedIrps, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
req.product: Windows 10 or later.
---

# KeInsertQueueDpc function



## -description
The <b>KeInsertQueueDpc</b> routine queues a DPC for execution. 



## -syntax

````
BOOLEAN KeInsertQueueDpc(
  _Inout_  PRKDPC Dpc,
  _In_opt_ PVOID  SystemArgument1,
  _In_opt_ PVOID  SystemArgument2
);
````


## -parameters

### -param Dpc [in, out]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551882">KDPC</a> structure for the DPC object. This structure must have been initialized by either <a href="kernel.keinitializedpc">KeInitializeDpc</a> or <a href="kernel.keinitializethreadeddpc">KeInitializeThreadedDpc</a>.


### -param SystemArgument1 [in, optional]

Specifies driver-determined context data. This value is passed as the <i>SystemArgument1</i> parameter to the DPC object's <a href="kernel.customdpc">CustomDpc</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff542976">CustomThreadedDpc</a> routine. 


### -param SystemArgument2 [in, optional]

Specifies driver-determined context data. This value is passed as the <i>SystemArgument2</i> parameter to the DPC object's <a href="kernel.customdpc">CustomDpc</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff542976">CustomThreadedDpc</a> routine. 


## -returns
If the specified DPC object is not currently in a DPC queue, <b>KeInsertQueueDpc</b> queues the DPC and returns <b>TRUE</b>.


## -remarks
If the specified DPC object has already been queued, no operation is performed except to return <b>FALSE</b>. Otherwise, the DPC object is inserted in a DPC queue. For more information about DPC queues, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558754">Organization of DPC Queues</a>.

Note that a particular DPC object and the function that it represents can each be queued for execution only once at any particular time. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_markingqueuedirps">MarkingQueuedIrps</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.customdpc">CustomDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542976">CustomThreadedDpc</a>
</dt>
<dt>
<a href="kernel.keinitializedpc">KeInitializeDpc</a>
</dt>
<dt>
<a href="kernel.keremovequeuedpc">KeRemoveQueueDpc</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeInsertQueueDpc routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

