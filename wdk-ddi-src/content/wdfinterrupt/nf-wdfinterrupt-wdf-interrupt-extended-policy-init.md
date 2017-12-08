---
UID: NF.wdfinterrupt.WDF_INTERRUPT_EXTENDED_POLICY_INIT
title: WDF_INTERRUPT_EXTENDED_POLICY_INIT
author: windows-driver-content
description: The WDF_INTERRUPT_EXTENDED_POLICY_INIT function initializes a WDF_INTERRUPT_EXTENDED_POLICY structure.
old-location: wdf\wdf_interrupt_extended_policy_init.htm
old-project: wdf
ms.assetid: fcc1e631-c77b-483b-9b5e-ec8d643f9930
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_INTERRUPT_EXTENDED_POLICY_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 2.0
req.alt-api: WDF_INTERRUPT_EXTENDED_POLICY_INIT
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
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WDF_INTERRUPT_EXTENDED_POLICY_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_INTERRUPT_EXTENDED_POLICY_INIT</b> function initializes a <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md">WDF_INTERRUPT_EXTENDED_POLICY</a> structure.</p>


## -syntax

````
VOID WDF_INTERRUPT_EXTENDED_POLICY_INIT(
  _Out_ PWDF_INTERRUPT_EXTENDED_POLICY PolicyAndGroup
);
````


## -parameters
<dl>

### -param PolicyAndGroup [out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md">WDF_INTERRUPT_EXTENDED_POLICY</a> structure.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The <b>WDF_INTERRUPT_EXTENDED_POLICY_INIT</b> function zeros the specified <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md">WDF_INTERRUPT_EXTENDED_POLICY</a> structure and sets the structure's <b>Size</b> member. It also sets the structure's <b>Policy</b> member to <b>WdfIrqPolicyMachineDefault</b> and sets the structure's <b>Priority</b> member to <b>WdfIrqPriorityUndefined</b>.</p>

<p>For a code example that uses <b>WDF_INTERRUPT_EXTENDED_POLICY_INIT</b>, see <a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsetextendedpolicy.md">WdfInterruptSetExtendedPolicy</a>. </p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md">WDF_INTERRUPT_EXTENDED_POLICY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_EXTENDED_POLICY_INIT function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
