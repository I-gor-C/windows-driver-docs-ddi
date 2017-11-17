---
UID: NE.wdm._IRQ_DEVICE_POLICY
title: IRQ_DEVICE_POLICY
author: windows-driver-content
description: The IRQ_DEVICE_POLICY enumeration type indicates the policy the operating system can use to assign the interrupts from a device to different processors.
old-location: kernel\irq_device_policy.htm
ms.assetid: 1a605eed-d9a1-4a2f-a095-3e790061527b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRQ_DEVICE_POLICY
req.alt-loc: Wdm.h
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
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.iface: 
req.product: Windows 10 or later.
---

# IRQ_DEVICE_POLICY enumeration



## -description
<p>The <b>IRQ_DEVICE_POLICY</b> enumeration type indicates the policy the operating system can use to assign the interrupts from a device to different processors.</p>


## -syntax

````
typedef enum _IRQ_DEVICE_POLICY { 
  IrqPolicyMachineDefault                     = 0,
  IrqPolicyAllCloseProcessors                 = 1,
  IrqPolicyOneCloseProcessor                  = 2,
  IrqPolicyAllProcessorsInMachine             = 3,
  IrqPolicySpecifiedProcessors                = 4,
  IrqPolicySpreadMessagesAcrossAllProcessors  = 5
} IRQ_DEVICE_POLICY, *PIRQ_DEVICE_POLICY;
````


## -enum-fields
<dl>

### -field <a id="IrqPolicyMachineDefault"></a><a id="irqpolicymachinedefault"></a><a id="IRQPOLICYMACHINEDEFAULT"></a><b>IrqPolicyMachineDefault</b>

<dd>
<p>The device does not require any particular assignment of interrupts to processors.</p>
</dd>

### -field <a id="IrqPolicyAllCloseProcessors"></a><a id="irqpolicyallcloseprocessors"></a><a id="IRQPOLICYALLCLOSEPROCESSORS"></a><b>IrqPolicyAllCloseProcessors</b>

<dd>
<p>The operating system should assign interrupts from the device to processors that are close to the device. On non-NUMA computers, the effect of this value is identical to that of <b>IrqPolicyAllProcessorsInMachine</b>.</p>
</dd>

### -field <a id="IrqPolicyOneCloseProcessor"></a><a id="irqpolicyonecloseprocessor"></a><a id="IRQPOLICYONECLOSEPROCESSOR"></a><b>IrqPolicyOneCloseProcessor</b>

<dd>
<p>The operating system should assign a single interrupt for the device to one processor that is close to the device. On non-NUMA computers, the operating system can assign the interrupt to any processor.</p>
</dd>

### -field <a id="IrqPolicyAllProcessorsInMachine"></a><a id="irqpolicyallprocessorsinmachine"></a><a id="IRQPOLICYALLPROCESSORSINMACHINE"></a><b>IrqPolicyAllProcessorsInMachine</b>

<dd>
<p>The operating system should assign interrupts from the device to all processors.</p>
</dd>

### -field <a id="IrqPolicySpecifiedProcessors"></a><a id="irqpolicyspecifiedprocessors"></a><a id="IRQPOLICYSPECIFIEDPROCESSORS"></a><b>IrqPolicySpecifiedProcessors</b>

<dd>
<p>The operating system should assign interrupts from the device to a specific set of processors.</p>
</dd>

### -field <a id="IrqPolicySpreadMessagesAcrossAllProcessors"></a><a id="irqpolicyspreadmessagesacrossallprocessors"></a><a id="IRQPOLICYSPREADMESSAGESACROSSALLPROCESSORS"></a><b>IrqPolicySpreadMessagesAcrossAllProcessors</b>

<dd>
<p>The operating system should assign different message-signaled interrupts to different processors, if possible. </p>
</dd>
</dl>

## -remarks
<p>The <b>Interrupt.AffinityPolicy</b> member of the <a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a> structure is an <b>IRQ_DEVICE_POLICY</b> enumeration value.</p>

<p>The <b>Interrupt.AffinityPolicy</b> member of the <a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a> structure is an <b>IRQ_DEVICE_POLICY</b> enumeration value.</p>

<p>The <b>Interrupt.AffinityPolicy</b> member of the <a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a> structure is an <b>IRQ_DEVICE_POLICY</b> enumeration value.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IRQ_DEVICE_POLICY enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
