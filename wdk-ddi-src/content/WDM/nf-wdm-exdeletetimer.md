---
UID: NF.wdm.ExDeleteTimer
title: ExDeleteTimer
author: windows-driver-content
description: The ExDeleteTimer routine deletes a timer object that was previously allocated by the ExAllocateTimer routine.
old-location: kernel\exdeletetimer.htm
ms.assetid: CE0C1D49-1505-464E-90DB-2C6D30C04EC1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExDeleteTimer
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: See Remarks.
ms.keywords: ExDeleteTimer
req.iface: 
req.product: Windows 10 or later.
---

# ExDeleteTimer function



## -description
<p>The <b>ExDeleteTimer</b> routine deletes a timer object that was previously allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265179">ExAllocateTimer</a> routine.</p>


## -syntax

````
BOOLEAN ExDeleteTimer(
  _In_ PEX_TIMER              Timer,
  _In_ BOOLEAN                Cancel,
  _In_ BOOLEAN                Wait,
  _In_ PEXT_DELETE_PARAMETERS Parameters
);
````


## -parameters
<dl>

### -param <i>Timer</i> [in]

<dd>
<p>A pointer to an <a href="kernel.ex_timer">EX_TIMER</a> structure. This structure is a timer object that was previously allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265179">ExAllocateTimer</a> routine.</p>
</dd>

### -param <i>Cancel</i> [in]

<dd>
<p>Whether to cancel the timer if it is currently set. If <b>TRUE</b>, the routine cancels the timer if the timer is set. If <b>FALSE</b>, the routine does not cancel the timer if it is set. If the caller sets <i>Wait</i> to <b>TRUE</b>, <i>Cancel</i> must also be <b>TRUE</b>; otherwise, a bug check occurs.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Whether to wait for the timer to finish expiring if the timer has already started the process of expiring. If <b>TRUE</b>, the routine waits for the timer to expire. If <b>FALSE</b>, the routine does not wait. For more information, see Remarks.</p>
</dd>

### -param <i>Parameters</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/dn265194">EXT_DELETE_PARAMETERS</a> structure. The calling driver previously called the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265182">ExInitializeDeleteTimerParameters</a> routine to initialize this structure.</p>
</dd>
</dl>

## -returns
<p>This routine returns <b>TRUE</b> if <i>Cancel</i> is <b>TRUE</b> and the timer was canceled. Otherwise, the routine returns <b>FALSE</b>. For more information, see Remarks.</p>

## -remarks
<p>After your driver calls this routine, the timer object pointed to by <i>Timer</i> might no longer be valid. However, the <i>Timer</i> parameter value passed to an <a href="https://msdn.microsoft.com/library/windows/hardware/dn265190">ExTimerCallback</a> callback routine, if the driver implements this routine, is always a valid pointer to a timer object.</p>

<p>If <i>Cancel</i> is <b>TRUE</b>, a return value of <b>FALSE</b> indicates that the timer was never set, or that the timer was set but expired before it could be canceled.  If <i>Cancel</i> is <b>FALSE</b>, the routine always returns <b>FALSE</b>.</p>

<p>This routine can block if <i>Wait</i> is <b>TRUE</b>. If <b>ExDeleteTimer</b> is called from the driver's <i>ExTimerCallback</i> routine, which is called at DISPATCH_LEVEL, the <i>Wait</i> parameter in this call must be <b>FALSE</b>.</p>

<p>If <i>Wait</i> is <b>TRUE</b>, the routine must be called at IRQL &lt;= APC_LEVEL. If <i>Wait</i> is <b>FALSE</b>, the routine can be called at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265175">Deleting a System-Allocated Timer Object</a>.</p>

<p>After your driver calls this routine, the timer object pointed to by <i>Timer</i> might no longer be valid. However, the <i>Timer</i> parameter value passed to an <a href="https://msdn.microsoft.com/library/windows/hardware/dn265190">ExTimerCallback</a> callback routine, if the driver implements this routine, is always a valid pointer to a timer object.</p>

<p>If <i>Cancel</i> is <b>TRUE</b>, a return value of <b>FALSE</b> indicates that the timer was never set, or that the timer was set but expired before it could be canceled.  If <i>Cancel</i> is <b>FALSE</b>, the routine always returns <b>FALSE</b>.</p>

<p>This routine can block if <i>Wait</i> is <b>TRUE</b>. If <b>ExDeleteTimer</b> is called from the driver's <i>ExTimerCallback</i> routine, which is called at DISPATCH_LEVEL, the <i>Wait</i> parameter in this call must be <b>FALSE</b>.</p>

<p>If <i>Wait</i> is <b>TRUE</b>, the routine must be called at IRQL &lt;= APC_LEVEL. If <i>Wait</i> is <b>FALSE</b>, the routine can be called at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265175">Deleting a System-Allocated Timer Object</a>.</p>

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
<p>Available starting with Windows 8.1.</p>
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
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265190">ExTimerCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265192">ExTimerDeleteCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265179">ExAllocateTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265182">ExInitializeDeleteTimerParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265194">EXT_DELETE_PARAMETERS</a>
</dt>
<dt>
<a href="kernel.ex_timer">EX_TIMER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExDeleteTimer routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
