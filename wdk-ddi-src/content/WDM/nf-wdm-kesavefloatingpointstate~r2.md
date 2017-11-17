---
UID: NF.wdm.KeSaveFloatingPointState~r2
title: KeSaveFloatingPointState
author: windows-driver-content
description: The KeSaveFloatingPointState routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations.
old-location: kernel\kesavefloatingpointstate.htm
ms.assetid: 2ab1b2dd-4848-4eb0-9836-e3be987535a6
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
req.alt-api: KeSaveFloatingPointState
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: KeSaveFloatingPointState
req.iface: 
req.product: Windows 10 or later.
---

# KeSaveFloatingPointState function



## -description
<p>The <b>KeSaveFloatingPointState</b> routine saves the nonvolatile floating-point context so the caller can carry out floating-point operations.</p>


## -syntax

````
NTSTATUS KeSaveFloatingPointState(
  _Out_ PKFLOATING_SAVE FloatSave
);
````


## -parameters
<dl>

### -param <i>FloatSave</i> [out]

<dd>
<p>Pointer to a caller-allocated resident buffer, which must be at least <b>sizeof</b>(<a href="https://msdn.microsoft.com/library/windows/hardware/ff554233">KFLOATING_SAVE</a>).</p>
</dd>
</dl>

## -returns
<p><b>KeSaveFloatingPointState</b> returns STATUS_SUCCESS if it saved the current thread's floating-point context and set up a fresh floating-point context for the caller. Otherwise, it returns one of the following error status codes.</p><dl>
<dt><b>STATUS_ILLEGAL_FLOAT_CONTEXT</b></dt>
</dl><p>The system is configured to use floating-point emulation, rather than doing floating-point operations in the processors.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>KeSaveFloatingPointState</b> could not allocate sufficient memory to save the current thread's floating-point context.</p>

<p> </p>

## -remarks
<p>A successful call to <b>KeSaveFloatingPointState</b> allows the caller to carry out floating-point operations of its own, but such a caller must restore the previous nonvolatile floating-point context as soon as its floating-point operations are done. Any routine that calls <b>KeSaveFloatingPointState</b> must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a> before that routine returns control.</p>

<p>If the call to <b>KeSaveFloatingPointState</b> is successful, the data at <i>FloatSave</i> is opaque to the caller. The caller should not release the memory that it allocated for this data until after the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a>.</p>

<p>In Windows Vista and earlier versions of Windows, a <b>KeSaveFloatingPointState</b> call and the corresponding <b>KeRestoreFloatingPointState</b> call must occur in a guarded region. That is, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552028">KeEnterGuardedRegion</a> routine must be called before <b>KeSaveFloatingPointState</b> is called, and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552967">KeLeaveGuardedRegion</a> routine must be called after <b>KeRestoreFloatingPointState</b> is called. No such requirement exists in Windows 7 and later versions of Windows.</p>

<p>For performance reasons, drivers should avoid doing any floating-point operations unless absolutely necessary. The overhead of saving and restoring the current thread's nonvolatile floating-point state degrades the performance of any driver that does floating-point operations.</p>

<p>A successful call to <b>KeSaveFloatingPointState</b> allows the caller to carry out floating-point operations of its own, but such a caller must restore the previous nonvolatile floating-point context as soon as its floating-point operations are done. Any routine that calls <b>KeSaveFloatingPointState</b> must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a> before that routine returns control.</p>

<p>If the call to <b>KeSaveFloatingPointState</b> is successful, the data at <i>FloatSave</i> is opaque to the caller. The caller should not release the memory that it allocated for this data until after the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a>.</p>

<p>In Windows Vista and earlier versions of Windows, a <b>KeSaveFloatingPointState</b> call and the corresponding <b>KeRestoreFloatingPointState</b> call must occur in a guarded region. That is, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552028">KeEnterGuardedRegion</a> routine must be called before <b>KeSaveFloatingPointState</b> is called, and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552967">KeLeaveGuardedRegion</a> routine must be called after <b>KeRestoreFloatingPointState</b> is called. No such requirement exists in Windows 7 and later versions of Windows.</p>

<p>For performance reasons, drivers should avoid doing any floating-point operations unless absolutely necessary. The overhead of saving and restoring the current thread's nonvolatile floating-point state degrades the performance of any driver that does floating-point operations.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547812">IrqlKeDispatchLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552028">KeEnterGuardedRegion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552084">KeGetCurrentThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552967">KeLeaveGuardedRegion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553185">KeRestoreFloatingPointState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559932">PsCreateSystemThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSaveFloatingPointState routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
