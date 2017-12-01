---
UID: NE.wdfinterrupt._WDF_INTERRUPT_POLICY
title: WDF_INTERRUPT_POLICY
author: windows-driver-content
description: The WDF_INTERRUPT_POLICY enumeration type identifies the affinity policies that the PnP manager can use when it assigns a device's interrupts to the processors of a multiprocessor system.
old-location: wdf\wdf_interrupt_policy.htm
old-project: wdf
ms.assetid: 88f8f10d-bf1e-49bc-99c7-95a5e69c17e1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_COINSTALLER_INSTALL_OPTIONS, WDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_INTERRUPT_POLICY
req.alt-loc: wdfinterrupt.h
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

# WDF_INTERRUPT_POLICY enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_INTERRUPT_POLICY</b> enumeration type identifies the affinity policies that the PnP manager can use when it assigns a device's interrupts to the processors of a multiprocessor system.</p>


## -syntax

````
typedef enum _WDF_INTERRUPT_POLICY { 
  WdfIrqPolicyMachineDefault                     = 0,
  WdfIrqPolicyAllCloseProcessors                 = 1,
  WdfIrqPolicyOneCloseProcessor                  = 2,
  WdfIrqPolicyAllProcessorsInMachine             = 3,
  WdfIrqPolicySpecifiedProcessors                = 4,
  WdfIrqPolicySpreadMessagesAcrossAllProcessors  = 5
} WDF_INTERRUPT_POLICY, *PWDF_INTERRUPT_POLICY;
````


## -enum-fields
<dl>

### -field <a id="WdfIrqPolicyMachineDefault"></a><a id="wdfirqpolicymachinedefault"></a><a id="WDFIRQPOLICYMACHINEDEFAULT"></a><b>WdfIrqPolicyMachineDefault</b>

<dd>
<p>Use the system's default affinity policy.</p>
</dd>

### -field <a id="WdfIrqPolicyAllCloseProcessors"></a><a id="wdfirqpolicyallcloseprocessors"></a><a id="WDFIRQPOLICYALLCLOSEPROCESSORS"></a><b>WdfIrqPolicyAllCloseProcessors</b>

<dd>
<p>For NUMA systems, the PnP manager should assign the device's interrupts to processors that are close to the device. For non-NUMA systems, specifying <b>WdfIrqPolicyAllCloseProcessors</b> is the same as specifying <b>WdfIrqPolicyAllProcessorsInMachine</b>.</p>
</dd>

### -field <a id="WdfIrqPolicyOneCloseProcessor"></a><a id="wdfirqpolicyonecloseprocessor"></a><a id="WDFIRQPOLICYONECLOSEPROCESSOR"></a><b>WdfIrqPolicyOneCloseProcessor</b>

<dd>
<p>For NUMA systems, the PnP manager should assign one interrupt to a processor that is close to the device. For non-NUMA systems, the PnP manager can assign the interrupt to any processor.</p>
</dd>

### -field <a id="WdfIrqPolicyAllProcessorsInMachine"></a><a id="wdfirqpolicyallprocessorsinmachine"></a><a id="WDFIRQPOLICYALLPROCESSORSINMACHINE"></a><b>WdfIrqPolicyAllProcessorsInMachine</b>

<dd>
<p>The PnP manager can assign a device's interrupts to any of the system's processors.</p>
</dd>

### -field <a id="WdfIrqPolicySpecifiedProcessors"></a><a id="wdfirqpolicyspecifiedprocessors"></a><a id="WDFIRQPOLICYSPECIFIEDPROCESSORS"></a><b>WdfIrqPolicySpecifiedProcessors</b>

<dd>
<p>The PnP manager should assign the device's interrupts only to specified processors.</p>
</dd>

### -field <a id="WdfIrqPolicySpreadMessagesAcrossAllProcessors"></a><a id="wdfirqpolicyspreadmessagesacrossallprocessors"></a><a id="WDFIRQPOLICYSPREADMESSAGESACROSSALLPROCESSORS"></a><b>WdfIrqPolicySpreadMessagesAcrossAllProcessors</b>

<dd>
<p>The PnP manager should assign different message-based interrupts to different processors, if possible. </p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_INTERRUPT_POLICY</b> enumeration type is used as input to the <a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsetpolicy.md">WdfInterruptSetPolicy</a> method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfinterrupt.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsetpolicy.md">WdfInterruptSetPolicy</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_POLICY enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
