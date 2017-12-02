---
UID: NF.wudfddi.IWDFInterrupt.TryToAcquireInterruptLock
title: IWDFInterrupt::TryToAcquireInterruptLock
author: windows-driver-content
description: The TryToAcquireInterruptLock method acquires the interrupt lock if no other thread has already acquired it.
old-location: wdf\iwdfinterrupt_trytoacquireinterruptlock.htm
old-project: wdf
ms.assetid: 4A109CDF-C5DE-4BAE-AA4E-294EA5CE86C5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFInterrupt, TryToAcquireInterruptLock, IWDFInterrupt::TryToAcquireInterruptLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFInterrupt.TryToAcquireInterruptLock
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFInterrupt
req.product: Windows 10 or later.
---

# IWDFInterrupt::TryToAcquireInterruptLock method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>TryToAcquireInterruptLock</b> method acquires the interrupt lock if no other thread has already acquired it.</p>


## -syntax

````
BOOLEAN TryToAcquireInterruptLock();
````


## -parameters


## -returns
<p>The method returns TRUE if the interrupt lock was successfully acquired. Otherwise, the method returns FALSE.</p>

<p>The method returns TRUE if the interrupt lock was successfully acquired. Otherwise, the method returns FALSE.</p>

<p>The method returns TRUE if the interrupt lock was successfully acquired. Otherwise, the method returns FALSE.</p>

## -remarks
<p>Unlike <a href="wdf.iwdfinterrupt_acquireinterruptlock">IWDFInterrupt::AcquireInterruptLock</a>, <b>IWDFInterrupt::TryToAcquireInterruptLock</b> does not wait for the interrupt lock to become available if another thread is holding it.</p>

<p>When running in an arbitrary thread, such as an I/O queue callback method, drivers must call <b>IWDFInterrupt::TryToAcquireInterruptLock</b> instead of <a href="wdf.iwdfinterrupt_acquireinterruptlock">IWDFInterrupt::AcquireInterruptLock</a>. For example, the driver calls <b>IWDFInterrupt::TryToAcquireInterruptLock</b> from <a href="wdf.iqueuecallbackread_onread">IQueueCallbackRead::OnRead</a>. Doing so avoids the possibility of deadlock, as described in the Remarks section of <a href="wdf.iwdfinterrupt_acquireinterruptlock">IWDFInterrupt::AcquireInterruptLock</a>.</p>

<p>The driver must not attempt to acquire the lock recursively. If connected to the debugger, the framework introduces a breakpoint in this scenario.</p>

<p>For more information about manual interrupt locking, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.</p>

<p>For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfinterrupt.md">IWDFInterrupt</a>
</dt>
<dt>
<a href="wdf.iwdfinterrupt_acquireinterruptlock">IWDFInterrupt::AcquireInterruptLock</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterrupttrytoacquirelock.md">WdfInterruptTryToAcquireLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFInterrupt::TryToAcquireInterruptLock method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
