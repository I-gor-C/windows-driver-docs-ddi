---
UID: NF.wdm.KeEnterCriticalRegion
title: KeEnterCriticalRegion
author: windows-driver-content
description: The KeEnterCriticalRegion routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running.
old-location: kernel\keentercriticalregion.htm
ms.assetid: 87826cc7-2710-4582-a324-365dd34e2d0d
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
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
ms.keywords: KeEnterCriticalRegion
req.iface: 
req.product: Windows 10 or later.
---

# KeEnterCriticalRegion function



## -description
<p>The <b>KeEnterCriticalRegion</b> routine temporarily disables the execution of normal kernel APCs, but does not prevent special kernel APCs from running.</p>


## -syntax

````
VOID KeEnterCriticalRegion(void);
````


## -parameters


## -returns
<p>None</p>

<p>None</p>

<p>None</p>

## -remarks
<p>A driver calls this routine to enter a critical region in which the execution of normal kernel APCs is deferred until this driver exits the critical region by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a> routine. Any caller of <b>KeEnterCriticalRegion</b> should call <b>KeLeaveCriticalRegion</b> as quickly as possible after entering a critical region.</p>

<p>Highest-level drivers can call <b>KeEnterCriticalRegion</b> while running in the context of the thread that requested the current I/O operation.</p>

<p>A thread that is inside a critical region has both user APCs and normal kernel APCs disabled, but not special kernel APCs. For more information about these APC types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564853">Types of APCs</a>.</p>

<p>Critical regions can be entered recursively and each call to <b>KeEnterCriticalRegion</b> must have a matching call to <b>KeLeaveCriticalRegion</b>.</p>

<p>A driver can use a critical region to acquire and release exclusive access to a shared resource. In this case, the <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn308551">ExReleaseResourceAndLeaveCriticalRegion</a> routines can be used instead of the <b>KeEnterCriticalRegion</b> and <b>KeLeaveCriticalRegion</b> routines. For more information, see the code example in <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a>.</p>

<p>For more information about APCs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540625">Asynchronous Procedure Calls</a>.</p>

<p>A driver calls this routine to enter a critical region in which the execution of normal kernel APCs is deferred until this driver exits the critical region by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a> routine. Any caller of <b>KeEnterCriticalRegion</b> should call <b>KeLeaveCriticalRegion</b> as quickly as possible after entering a critical region.</p>

<p>Highest-level drivers can call <b>KeEnterCriticalRegion</b> while running in the context of the thread that requested the current I/O operation.</p>

<p>A thread that is inside a critical region has both user APCs and normal kernel APCs disabled, but not special kernel APCs. For more information about these APC types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564853">Types of APCs</a>.</p>

<p>Critical regions can be entered recursively and each call to <b>KeEnterCriticalRegion</b> must have a matching call to <b>KeLeaveCriticalRegion</b>.</p>

<p>A driver can use a critical region to acquire and release exclusive access to a shared resource. In this case, the <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn308551">ExReleaseResourceAndLeaveCriticalRegion</a> routines can be used instead of the <b>KeEnterCriticalRegion</b> and <b>KeLeaveCriticalRegion</b> routines. For more information, see the code example in <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a>.</p>

<p>For more information about APCs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540625">Asynchronous Procedure Calls</a>.</p>

<p>A driver calls this routine to enter a critical region in which the execution of normal kernel APCs is deferred until this driver exits the critical region by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a> routine. Any caller of <b>KeEnterCriticalRegion</b> should call <b>KeLeaveCriticalRegion</b> as quickly as possible after entering a critical region.</p>

<p>Highest-level drivers can call <b>KeEnterCriticalRegion</b> while running in the context of the thread that requested the current I/O operation.</p>

<p>A thread that is inside a critical region has both user APCs and normal kernel APCs disabled, but not special kernel APCs. For more information about these APC types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564853">Types of APCs</a>.</p>

<p>Critical regions can be entered recursively and each call to <b>KeEnterCriticalRegion</b> must have a matching call to <b>KeLeaveCriticalRegion</b>.</p>

<p>A driver can use a critical region to acquire and release exclusive access to a shared resource. In this case, the <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn308551">ExReleaseResourceAndLeaveCriticalRegion</a> routines can be used instead of the <b>KeEnterCriticalRegion</b> and <b>KeLeaveCriticalRegion</b> routines. For more information, see the code example in <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a>.</p>

<p>For more information about APCs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540625">Asynchronous Procedure Calls</a>.</p>

<p>A driver calls this routine to enter a critical region in which the execution of normal kernel APCs is deferred until this driver exits the critical region by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a> routine. Any caller of <b>KeEnterCriticalRegion</b> should call <b>KeLeaveCriticalRegion</b> as quickly as possible after entering a critical region.</p>

<p>Highest-level drivers can call <b>KeEnterCriticalRegion</b> while running in the context of the thread that requested the current I/O operation.</p>

<p>A thread that is inside a critical region has both user APCs and normal kernel APCs disabled, but not special kernel APCs. For more information about these APC types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564853">Types of APCs</a>.</p>

<p>Critical regions can be entered recursively and each call to <b>KeEnterCriticalRegion</b> must have a matching call to <b>KeLeaveCriticalRegion</b>.</p>

<p>A driver can use a critical region to acquire and release exclusive access to a shared resource. In this case, the <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn308551">ExReleaseResourceAndLeaveCriticalRegion</a> routines can be used instead of the <b>KeEnterCriticalRegion</b> and <b>KeLeaveCriticalRegion</b> routines. For more information, see the code example in <a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a>.</p>

<p>For more information about APCs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540625">Asynchronous Procedure Calls</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543603">CriticalRegions</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547806">IrqlKeApcLte2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh466453">WithinCriticalRegion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/338E6995-0EB2-476D-B5F5-504DC8FF8609">WithinCriticalRegion(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn308550">ExEnterCriticalRegionAndAcquireResourceExclusive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn308551">ExReleaseResourceAndLeaveCriticalRegion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551938">KeAreApcsDisabled</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeEnterCriticalRegion routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
