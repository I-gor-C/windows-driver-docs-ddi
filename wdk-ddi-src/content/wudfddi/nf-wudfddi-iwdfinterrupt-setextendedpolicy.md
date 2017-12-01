---
UID: NF.wudfddi.IWDFInterrupt.SetExtendedPolicy
title: IWDFInterrupt::SetExtendedPolicy
author: windows-driver-content
description: The SetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.
old-location: wdf\iwdfinterrupt_setextendedpolicy.htm
old-project: wdf
ms.assetid: 6637E939-010E-4462-92CE-50C4DB867694
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFInterrupt, SetExtendedPolicy, IWDFInterrupt::SetExtendedPolicy
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
req.alt-api: IWDFInterrupt.SetExtendedPolicy
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

# IWDFInterrupt::SetExtendedPolicy method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SetExtendedPolicy</b> method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt.
  </p>


## -syntax

````
void SetExtendedPolicy(
  [in] WDF_INTERRUPT_EXTENDED_POLICY *PolicyAndGroup
);
````


## -parameters
<dl>

### -param <i>PolicyAndGroup</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md">WDF_INTERRUPT_EXTENDED_POLICY</a> structure that the driver has previously initialized by calling <a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-extended-policy-init.md">WDF_INTERRUPT_EXTENDED_POLICY_INIT</a>.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>This method is equivalent to KMDF’s <a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsetextendedpolicy.md">WdfInterruptSetExtendedPolicy</a>. See the Remarks section of <b>WdfInterruptSetExtendedPolicy</b> for more information about this method.</p>

<p>

If a driver is running on an operating system version that is earlier than Windows 7, the framework ignores the value that the driver specifies for the processor group number when it calls <b>SetExtendedPolicy</b>.</p>

<p>For more information about handling interrupts in UMDF drivers, see <a href="wdf.accessing_hardware_and_handling_interrupts">Accessing Hardware and Handling Interrupts</a>.</p>

<p>The following code example calls <a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-extended-policy-init.md">WDF_INTERRUPT_EXTENDED_POLICY_INIT</a> to initialize a <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md">WDF_INTERRUPT_EXTENDED_POLICY</a> structure; sets values for the policy, priority, and target processor set; and calls <b>SetExtendedPolicy</b>. The example sets normal priority for the interrupt and assigns the interrupt to processor 0 in processor group 2. </p>

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
<a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md">WDF_INTERRUPT_EXTENDED_POLICY</a>
</dt>
<dt>
<a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-extended-policy-init.md">WDF_INTERRUPT_EXTENDED_POLICY_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFInterrupt::SetExtendedPolicy method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
