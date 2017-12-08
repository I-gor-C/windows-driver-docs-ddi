---
UID: NF.ntddk.KeEnterCriticalRegion
title: KeEnterCriticalRegion function
author: windows-driver-content
description: The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running.
old-location: kernel\keentercriticalregion.htm
old-project: kernel
ms.assetid: 87826cc7-2710-4582-a324-365dd34e2d0d
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KeEnterCriticalRegion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeEnterCriticalRegion
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CriticalRegions, IrqlKeApcLte2, WithinCriticalRegion, HwStorPortProhibitedDDIs, WithinCriticalRegion(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
---

# KeEnterCriticalRegion function



## -description
The <b>KeEnterCriticalRegion</b> routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running.


## -syntax

````
VOID KeEnterCriticalRegion(void);
````


## -parameters


## -returns
None

None

None

## -remarks
A driver calls this routine to enter a critical region in which the execution of normal kernel APCs is deferred until this driver exits the critical region by calling the <a href="kernel.keleavecriticalregion">KeLeaveCriticalRegion</a> routine. Any caller of <b>KeEnterCriticalRegion</b> should call <b>KeLeaveCriticalRegion</b> as quickly as possible after entering a critical region.

Highest-level drivers can call <b>KeEnterCriticalRegion</b> while running in the context of the thread that requested the current I/O operation.

A thread that is inside a critical region has both user APCs and normal kernel APCs disabled, but not special kernel APCs. For more information about these APC types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564853">Types of APCs</a>.

Critical regions can be entered recursively and each call to <b>KeEnterCriticalRegion</b> must have a matching call to <b>KeLeaveCriticalRegion</b>.

A driver can use a critical region to acquire and release exclusive access to a shared resource. In this case, the <a href="kernel.exentercriticalregionandacquireresourceexclusive">ExEnterCriticalRegionAndAcquireResourceExclusive</a> and <a href="kernel.exreleaseresourceandleavecriticalregion">ExReleaseResourceAndLeaveCriticalRegion</a> routines can be used instead of the <b>KeEnterCriticalRegion</b> and <b>KeLeaveCriticalRegion</b> routines. For more information, see the code example in <a href="kernel.exentercriticalregionandacquireresourceexclusive">ExEnterCriticalRegionAndAcquireResourceExclusive</a>.

For more information about APCs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540625">Asynchronous Procedure Calls</a>.

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
&lt;= APC_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.wdm_criticalregions">CriticalRegions</a>, <a href="devtest.wdm_irqlkeapclte2">IrqlKeApcLte2</a>, <a href="devtest.wdm_withincriticalregion">WithinCriticalRegion</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_withincriticalregion">WithinCriticalRegion(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exentercriticalregionandacquireresourceexclusive">ExEnterCriticalRegionAndAcquireResourceExclusive</a>
</dt>
<dt>
<a href="kernel.exreleaseresourceandleavecriticalregion">ExReleaseResourceAndLeaveCriticalRegion</a>
</dt>
<dt>
<a href="kernel.keareapcsdisabled">KeAreApcsDisabled</a>
</dt>
<dt>
<a href="kernel.keleavecriticalregion">KeLeaveCriticalRegion</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeEnterCriticalRegion routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
