---
UID: NE.wdm._IRQ_PRIORITY
title: IRQ_PRIORITY
author: windows-driver-content
description: The IRQ_PRIORITY enumeration type indicates the priority the system should give to servicing a device's interrupts.
old-location: kernel\irq_priority.htm
old-project: kernel
ms.assetid: 1dee65e7-27fb-4665-82e2-d7cb3c223f87
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRQ_PRIORITY
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IRQ_PRIORITY enumeration



## -description
<p>The <b>IRQ_PRIORITY</b> enumeration type indicates the priority the system should give to servicing a device's interrupts.</p>


## -syntax

````
typedef enum _IRQ_PRIORITY { 
  IrqPriorityUndefined  = 0,
  IrqPriorityLow        = 1,
  IrqPriorityNormal     = 2,
  IrqPriorityHigh       = 3
} IRQ_PRIORITY, *PIRQ_PRIORITY;
````


## -enum-fields
<dl>

### -field <a id="IrqPriorityUndefined"></a><a id="irqpriorityundefined"></a><a id="IRQPRIORITYUNDEFINED"></a><b>IrqPriorityUndefined</b>

<dd>
<p>Specifies that the device does not require any particular priority for its interrupts.</p>
</dd>

### -field <a id="IrqPriorityLow"></a><a id="irqprioritylow"></a><a id="IRQPRIORITYLOW"></a><b>IrqPriorityLow</b>

<dd>
<p>Specifies that the device's interrupts are of low priority. This setting is appropiate for devices that can tolerate higher-than-normal latency.</p>
</dd>

### -field <a id="IrqPriorityNormal"></a><a id="irqprioritynormal"></a><a id="IRQPRIORITYNORMAL"></a><b>IrqPriorityNormal</b>

<dd>
<p>Specifies that the device's interrupts are of normal priority. </p>
</dd>

### -field <a id="IrqPriorityHigh"></a><a id="irqpriorityhigh"></a><a id="IRQPRIORITYHIGH"></a><b>IrqPriorityHigh</b>

<dd>
<p>Specifies that the device's interrupts are of high priority. This setting is appropriate for devices that require low latency. </p>
</dd>
</dl>

## -remarks
<p>The system uses <b>IRQ_PRIORITY</b> to assign IRQLs for devices. For example, it might assign a higher IRQL to a device that has an <b>IRQ_PRIORITY</b> of <b>IrqPriorityHigh</b> than it does to a device that has an <b>IRQ_PRIORITY</b> of <b>IrqPriorityLow</b>.</p>

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
<a href="..\wdm\ns-wdm--io-resource-descriptor.md">IO_RESOURCE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IRQ_PRIORITY enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
