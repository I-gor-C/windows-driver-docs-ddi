---
UID: NF.gpioclx.GPIO_CLX_AcquireInterruptLock
title: GPIO_CLX_AcquireInterruptLock
author: windows-driver-content
description: The GPIO_CLX_AcquireInterruptLock method acquires an interrupt lock on a bank of pins in the general-purpose I/O (GPIO) controller.
old-location: gpio\gpio_clx_acquireinterruptlock.htm
ms.assetid: E0332415-1028-489B-AA81-DF8AEE0A28E8
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: GPIO
req.header: gpioclx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GPIO_CLX_AcquireInterruptLock
req.alt-loc: Gpioclx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks.
ms.keywords: GPIO_CLX_AcquireInterruptLock
req.iface: 
---

# GPIO_CLX_AcquireInterruptLock function



## -description
<p>The <b>GPIO_CLX_AcquireInterruptLock</b> method acquires an interrupt lock on a bank of pins in the general-purpose I/O (GPIO) controller.</p>


## -syntax

````
VOID GPIO_CLX_AcquireInterruptLock(
  [in] PVOID   Context,
  [in] BANK_ID BankId
);
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to the GPIO controller driver's <a href="https://msdn.microsoft.com/4BE99C71-9BA6-44E3-A54F-DE8C3440A474">device context</a>. The GPIO framework extension (GpioClx) passes this pointer value as a parameter to the callback functions that are implemented by the GPIO controller driver.</p>
</dd>

### -param <i>BankId</i> [in]

<dd>
<p>The identifier for this bank of GPIO pins. If N is the number of banks in the GPIO controller, <b>BankId</b> is an integer in the range 0 to N–1.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A GPIO controller driver thread calls this method to synchronize to the interrupt service routine (ISR) in GpioClx. While the caller holds the interrupt lock, the ISR cannot call driver-implemented callback functions to access GPIO registers in the specified bank. A GPIO controller driver should call this method before it tries to access GPIO registers that might be accessed by the GpioClx ISR.</p>

<p>The GpioClx ISR calls driver-implemented callback functions to access interrupt status and enable registers in the GPIO controller. Depending on the capabilities of the GPIO controller, the ISR is called either at DIRQL or at PASSIVE_LEVEL. For more information, see <a href="NULL">Interrupt-Related Callbacks</a>.</p>

<p>If the GpioClx ISR accesses these interrupt registers at DIRQL, <b>GPIO_CLX_AcquireInterruptLock</b> raises the calling thread's IRQL to the DIRQL at which the ISR runs. If the ISR runs at PASSIVE_LEVEL, this method does not change the calling thread's IRQL.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh439494">GPIO_CLX_ReleaseInterruptLock</a> method releases an interrupt lock that was acquired in a previous call to <b>GPIO_CLX_AcquireInterruptLock</b>. The <b>BankId</b> parameter specifies the bank that is affected by the lock. To release a lock on a bank, the <b>BankId</b> parameter of the <b>GPIO_CLX_ReleaseInterruptLock</b> call must match the <b>BankId</b> parameter of the <b>GPIO_CLX_AcquireInterruptLock</b> call that acquired the lock. If the <b>GPIO_CLX_AcquireInterruptLock</b> call raised the calling thread's IRQL, <b>GPIO_CLX_ReleaseInterruptLock</b> restores this thread's original IRQL.</p>

<p>The GPIO controller driver can independently acquire and release interrupt locks on the various banks in the GPIO controller. However, it is a fatal error for the driver to try to acquire a lock on a particular bank if the driver already holds a lock on this bank.</p>

<p>If the <i>Context</i> parameter is NULL or points to an invalid GPIO device context, this method causes a bug check in debug builds of GpioClx.</p>

<p>A GPIO controller driver thread calls this method to synchronize to the interrupt service routine (ISR) in GpioClx. While the caller holds the interrupt lock, the ISR cannot call driver-implemented callback functions to access GPIO registers in the specified bank. A GPIO controller driver should call this method before it tries to access GPIO registers that might be accessed by the GpioClx ISR.</p>

<p>The GpioClx ISR calls driver-implemented callback functions to access interrupt status and enable registers in the GPIO controller. Depending on the capabilities of the GPIO controller, the ISR is called either at DIRQL or at PASSIVE_LEVEL. For more information, see <a href="NULL">Interrupt-Related Callbacks</a>.</p>

<p>If the GpioClx ISR accesses these interrupt registers at DIRQL, <b>GPIO_CLX_AcquireInterruptLock</b> raises the calling thread's IRQL to the DIRQL at which the ISR runs. If the ISR runs at PASSIVE_LEVEL, this method does not change the calling thread's IRQL.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh439494">GPIO_CLX_ReleaseInterruptLock</a> method releases an interrupt lock that was acquired in a previous call to <b>GPIO_CLX_AcquireInterruptLock</b>. The <b>BankId</b> parameter specifies the bank that is affected by the lock. To release a lock on a bank, the <b>BankId</b> parameter of the <b>GPIO_CLX_ReleaseInterruptLock</b> call must match the <b>BankId</b> parameter of the <b>GPIO_CLX_AcquireInterruptLock</b> call that acquired the lock. If the <b>GPIO_CLX_AcquireInterruptLock</b> call raised the calling thread's IRQL, <b>GPIO_CLX_ReleaseInterruptLock</b> restores this thread's original IRQL.</p>

<p>The GPIO controller driver can independently acquire and release interrupt locks on the various banks in the GPIO controller. However, it is a fatal error for the driver to try to acquire a lock on a particular bank if the driver already holds a lock on this bank.</p>

<p>If the <i>Context</i> parameter is NULL or points to an invalid GPIO device context, this method causes a bug check in debug builds of GpioClx.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gpioclx.h</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439494">GPIO_CLX_ReleaseInterruptLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20GPIO_CLX_AcquireInterruptLock method%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
