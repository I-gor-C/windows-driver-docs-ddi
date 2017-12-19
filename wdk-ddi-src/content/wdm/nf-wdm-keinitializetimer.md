---
UID: NF.wdm.KeInitializeTimer
title: KeInitializeTimer function
author: windows-driver-content
description: The KeInitializeTimer routine initializes a timer object.
old-location: kernel\keinitializetimer.htm
old-project: kernel
ms.assetid: 97140cf6-9c5a-4fdc-b7c7-10e6d28b9b1b
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: KeInitializeTimer
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
req.alt-api: KeInitializeTimer
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeDispatchLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.product: Windows 10 or later.
---

# KeInitializeTimer function



## -description
The <b>KeInitializeTimer</b> routine initializes a timer object.



## -syntax

````
VOID KeInitializeTimer(
  _Out_ PKTIMER Timer
);
````


## -parameters

### -param Timer [out]

Pointer to a timer object, for which the caller provides the storage.


## -returns
None


## -remarks
The timer object is initialized to a not-signaled state.

Storage for a timer object must be resident: in the device extension of a driver-created device object, in the controller extension of a driver-created controller object, or in nonpaged pool allocated by the caller.

<b>KeInitializeTimer</b> can only initialize a notification timer. Use <a href="kernel.keinitializetimerex">KeInitializeTimerEx</a> to initialize a notification timer or a synchronization timer.

Use <a href="kernel.kesettimer">KeSetTimer</a> or <a href="kernel.kesettimerex">KeSetTimerEx</a> to define when the timer will expire.

For more information about timer objects, see <a href="https://msdn.microsoft.com/b58487de-6e9e-45f4-acb8-9233c8718ee2">Timer Objects and DPCs</a>.

Callers of <b>KeInitializeTimer</b> should be running at IRQL = DISPATCH_LEVEL or lower. It is best to initialize timers at IRQL = PASSIVE_LEVEL.


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
&lt;= DISPATCH_LEVEL (see Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlkedispatchlte">IrqlKeDispatchLte</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.kecanceltimer">KeCancelTimer</a>
</dt>
<dt>
<a href="kernel.keinitializetimerex">KeInitializeTimerEx</a>
</dt>
<dt>
<a href="kernel.kereadstatetimer">KeReadStateTimer</a>
</dt>
<dt>
<a href="kernel.kesettimer">KeSetTimer</a>
</dt>
<dt>
<a href="kernel.kesettimerex">KeSetTimerEx</a>
</dt>
<dt>
<a href="kernel.kewaitformultipleobjects">KeWaitForMultipleObjects</a>
</dt>
<dt>
<a href="kernel.kewaitforsingleobject">KeWaitForSingleObject</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeInitializeTimer routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

