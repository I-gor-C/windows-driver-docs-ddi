---
UID: NE.wudfinterrupt._WDF_INTERRUPT_POLICY
title: _WDF_INTERRUPT_POLICY
author: windows-driver-content
description: The WDF_INTERRUPT_POLICY enumeration type identifies the affinity policies that the Plug and Play (PnP) manager can use when it assigns a device's interrupts to the processors of a multiprocessor system.
old-location: wdf\wdf_interrupt_policy_umdf.htm
old-project: wdf
ms.assetid: 92E2A992-8A0B-4E0F-B615-DC6E30E4A227
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDF_INTERRUPT_POLICY, *PWDF_INTERRUPT_POLICY, PWDF_INTERRUPT_POLICY, WDF_INTERRUPT_POLICY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfinterrupt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WDF_INTERRUPT_POLICY
req.alt-loc: Wudfinterrupt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# _WDF_INTERRUPT_POLICY enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <a href="wdf.wdf_interrupt_policy">WDF_INTERRUPT_POLICY</a> enumeration type identifies the affinity policies that the Plug and Play (PnP) manager can use when it assigns a device's interrupts to the processors of a multiprocessor system.



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

### -field WdfIrqPolicyMachineDefault

Use the system's default affinity policy.


### -field WdfIrqPolicyAllCloseProcessors

For NUMA systems, the PnP manager should assign the device's interrupts to processors that are close to the device. For non-NUMA systems, specifying <b>WdfIrqPolicyAllCloseProcessors</b> is the same as specifying <b>WdfIrqPolicyAllProcessorsInMachine</b>.


### -field WdfIrqPolicyOneCloseProcessor

For NUMA systems, the PnP manager should assign one interrupt to a processor that is close to the device. For non-NUMA systems, the PnP manager can assign the interrupt to any processor.


### -field WdfIrqPolicyAllProcessorsInMachine

The PnP manager can assign a device's interrupts to any of the system's processors.


### -field WdfIrqPolicySpecifiedProcessors

The PnP manager should assign the device's interrupts only to specified processors.


### -field WdfIrqPolicySpreadMessagesAcrossAllProcessors

The PnP manager should assign different message-based interrupts to different processors, if possible. 


## -remarks
The <a href="wdf.wdf_interrupt_policy">WDF_INTERRUPT_POLICY</a> enumeration type is used as input to the <a href="wdf.iwdfinterrupt_setpolicy">IWDFInterrupt::SetPolicy</a> method.


## -requirements
<table>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.11

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfinterrupt.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.iwdfinterrupt_setpolicy">IWDFInterrupt::SetPolicy</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_POLICY enumeration%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

