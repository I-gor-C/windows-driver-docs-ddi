---
UID: NF.wdm.KeSynchronizeExecution
title: KeSynchronizeExecution
author: windows-driver-content
description: The KeSynchronizeExecution routine synchronizes the execution of the specified routine with the interrupt service routine (ISR) that is assigned to a set of one or more interrupt objects.
old-location: kernel\kesynchronizeexecution.htm
old-project: kernel
ms.assetid: f378a30f-7e6b-4c81-b98b-a5b40e9a1a17
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeSynchronizeExecution
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
req.alt-api: KeSynchronizeExecution
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DIRQL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# KeSynchronizeExecution function



## -description
<p>The <b>KeSynchronizeExecution</b> routine synchronizes the execution of the specified routine with the interrupt service routine (ISR) that is assigned to a set of one or more interrupt objects.</p>


## -syntax

````
BOOLEAN KeSynchronizeExecution(
  _Inout_  PKINTERRUPT           Interrupt,
  _In_     PKSYNCHRONIZE_ROUTINE SynchronizeRoutine,
  _In_opt_ PVOID                 SynchronizeContext
);
````


## -parameters
<dl>

### -param <i>Interrupt</i> [in, out]

<dd>
<p>A pointer to a set of interrupt objects. The caller obtained this pointer from the <a href="..\wdm\nf-wdm-ioconnectinterrupt.md">IoConnectInterrupt</a> or <a href="..\wdm\nf-wdm-ioconnectinterruptex.md">IoConnectInterruptEx</a> routine.</p>
</dd>

### -param <i>SynchronizeRoutine</i> [in]

<dd>
<p>Specifies a caller-supplied <a href="kernel.synchcritsection">SynchCritSection</a> routine whose execution is to be synchronized with the execution of the ISR assigned to the interrupt objects.</p>
</dd>

### -param <i>SynchronizeContext</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied context value to be passed to the <a href="kernel.synchcritsection">SynchCritSection</a> routine when it is called.</p>
</dd>
</dl>

## -returns
<p><b>KeSynchronizeExecution</b> returns <b>TRUE</b> if the operation succeeds. Otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>When this routine is called, the following occurs:</p>

<p>The IRQL is raised to the <i>SynchronizeIrql</i> value specified in the call to <a href="..\wdm\nf-wdm-ioconnectinterrupt.md">IoConnectInterrupt</a> or <a href="..\wdm\nf-wdm-ioconnectinterruptex.md">IoConnectInterruptEx</a>.</p>

<p>Access to <i>SynchronizeContext</i> is synchronized with the assigned ISR by acquiring the associated interrupt object spin lock (or system event object, in the case of an ISR that runs at PASSIVE_LEVEL).</p>

<p>The specified <a href="kernel.synchcritsection">SynchCritSection</a> routine is called with the <i>SynchronizeContext</i> value as its parameter.</p>

<p>If the ISR runs at DIRQL &gt;= DISPATCH_LEVEL, the <i>SynchCritSection</i> routine runs at the same DIRQL and must therefore run for as brief a time as possible to avoid delaying other high-priority tasks.</p>

<p>Callers of <b>KeSynchronizeExecution</b> must be running at IRQL &lt;= DIRQL; that is, at an IRQL that is less than or equal to the value of the <b>SynchronizeIrql</b> value that the caller specified when it registered its ISR with <b>IoConnectInterrupt</b> or <b>IoConnectInterruptEx</b>.</p>

<p>Starting with Windows 8, a driver can call <b>KeSynchronizeExecution</b> to synchronize execution of a <i>SynchCritSection</i> routine with an ISR that runs at IRQL = PASSIVE_LEVEL. In earlier versions of Windows, <b>KeSynchronizeExecution</b> can synchronize execution only with an ISR that runs at IRQL &gt;= DISPATCH_LEVEL. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh698277">Using Passive-Level Interrupt Service Routines</a>.</p>

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
<p>&lt;= DIRQL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioconnectinterrupt.md">IoConnectInterrupt</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioconnectinterruptex.md">IoConnectInterruptEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSynchronizeExecution routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
