---
UID: NC.pepfx.PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK
title: PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK
author: windows-driver-content
description: An EnumerateInterruptSource callback routine supplies a platform extension plug-in (PEP) with information about an interrupt source.
old-location: kernel\enumerateinterruptsource.htm
old-project: kernel
ms.assetid: 1E6841D8-88A0-4EDB-89EF-3878AF8B0072
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: VPCI_PNP_ID, VPCI_PNP_ID, *PVPCI_PNP_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EnumerateInterruptSource
req.alt-loc: pepfx.h
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
req.iface: 
---

# PPO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK callback



## -description
<p>An <i>EnumerateInterruptSource</i> callback routine supplies a platform extension plug-in (PEP) with information about an interrupt source.</p>


## -prototype

````
PO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK EnumerateInterruptSource;

BOOLEAN EnumerateInterruptSource(
  _In_ PVOID                               CallbackContext,
  _In_ PPEP_UNMASKED_INTERRUPT_INFORMATION InterruptInformation
)
{ ... }
````


## -parameters
<dl>

### -param <i>CallbackContext</i> [in]

<dd>
<p>A pointer to a callback context. The PEP specified this pointer value as a parameter in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186633">EnumerateUnmaskedInterrupts</a> call that initiated the enumeration of interrupt sources.</p>
</dd>

### -param <i>InterruptInformation</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186857">PEP_UNMASKED_INTERRUPT_INFORMATION</a> structure that contains information about the interrupt source.</p>
</dd>
</dl>

## -returns
<p>If the <i>EnumerateInterruptSource</i> callback routine returns TRUE, <b>EnumerateUnmaskedInterrupts</b> will continue to call the <i>EnumerateInterruptSource</i> callback routine while more interrupts are available to be enumerated. If the <i>EnumerateInterruptSource</i> callback routine returns FALSE, <b>EnumerateUnmaskedInterrupts</b> returns without enumerating any more interrupts.</p>

## -remarks
<p>This callback routine is implemented by a PEP, and is called by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The <i>Callback</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186633">EnumerateUnmaskedInterrupts</a> routine is a pointer to an <i>EnumerateInterruptSource</i> callback routine.</p>

<p>After a PEP calls <b>EnumerateUnmaskedInterrupts</b> to enumerate the unmasked interrupt sources, PoFx calls the PEP's <i>EnumerateInterruptSource</i> callback routine once for each unmasked interrupt source. <b>EnumerateUnmaskedInterrupts</b> returns only after the last call to the <i>EnumerateInterruptSource</i> callback routine completes.</p>

<p>An <i>EnumerateInterruptSource</i> callback routine is called at the same IRQL as the PEP's call to <b>EnumerateUnmaskedInterrupts</b> that initiates the enumeration callbacks.</p>

<p>This callback routine is implemented by a PEP, and is called by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The <i>Callback</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186633">EnumerateUnmaskedInterrupts</a> routine is a pointer to an <i>EnumerateInterruptSource</i> callback routine.</p>

<p>After a PEP calls <b>EnumerateUnmaskedInterrupts</b> to enumerate the unmasked interrupt sources, PoFx calls the PEP's <i>EnumerateInterruptSource</i> callback routine once for each unmasked interrupt source. <b>EnumerateUnmaskedInterrupts</b> returns only after the last call to the <i>EnumerateInterruptSource</i> callback routine completes.</p>

<p>An <i>EnumerateInterruptSource</i> callback routine is called at the same IRQL as the PEP's call to <b>EnumerateUnmaskedInterrupts</b> that initiates the enumeration callbacks.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186633">EnumerateUnmaskedInterrupts</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186857">PEP_UNMASKED_INTERRUPT_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PO_ENUMERATE_INTERRUPT_SOURCE_CALLBACK routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
