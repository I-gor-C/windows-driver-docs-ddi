---
UID: NF.storport.StorPortInitializeTimer
title: StorPortInitializeTimer
author: windows-driver-content
description: Creates a Storport timer context object.
old-location: storage\storportinitializetimer.htm
ms.assetid: 1F43EEDC-5DB4-4ABE-BBC6-A4A51FCAF0B6
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortInitializeTimer
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: StorPortInitializeTimer
req.iface: 
req.product: Windows 10 or later.
---

# StorPortInitializeTimer function



## -description
<p>Creates a Storport timer context object.</p>


## -syntax

````
ULONG StorPortInitializeTimer(
  _In_  PVOID HwDeviceExtension,
  _Out_ PVOID *TimerHandle
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>TimerHandle</i> [out]

<dd>
<p>A pointer to an opaque buffer that holds context information for the timer.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortInitializeTimer</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>Current IRQL &gt; DISPATCH_LEVEL.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either <i>HwDeviceExtension</i> or <i>TimerHandle</i> is NULL.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p> Insufficient resources are available to initialize the timer context.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The timer context was successfully initialized.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The number of supported timers is exceeded.</p>

<p> </p>

## -remarks
<p>Storport provides a single timer to a miniport driver by using the  <b>RequestTimerCall</b> notification type in <a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a>. If a miniport requires more than one timer, additional timers are created with <b>StorPortInitializeTimer</b>.</p>

<p>It is recommended that miniports call <b>StorPortInitializeTimer</b> in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> function to ensure that the additional timer resources are available.</p>

<p>Miniports can use this routine to set coalescing timers to create a delay period after an initial timeout.</p>

<p>Prior to Windows 8, a maximum of 4 timers can be created with <b>StorPortInitializeTimer</b>.
Starting with Windows 8, there is no maximum timers limitation.</p>

<p>Storport provides a single timer to a miniport driver by using the  <b>RequestTimerCall</b> notification type in <a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a>. If a miniport requires more than one timer, additional timers are created with <b>StorPortInitializeTimer</b>.</p>

<p>It is recommended that miniports call <b>StorPortInitializeTimer</b> in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> function to ensure that the additional timer resources are available.</p>

<p>Miniports can use this routine to set coalescing timers to create a delay period after an initial timeout.</p>

<p>Prior to Windows 8, a maximum of 4 timers can be created with <b>StorPortInitializeTimer</b>.
Starting with Windows 8, there is no maximum timers limitation.</p>

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
<p>Available in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451476">StorPortFreeTimer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451511">StorPortRequestTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortInitializeTimer routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
