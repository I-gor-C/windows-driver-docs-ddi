---
UID: NF.portcls.IPinCount.PinCount
title: IPinCount::PinCount
author: windows-driver-content
description: The PinCount method queries the miniport driver for its pin count.
old-location: audio\ipincount_pincount.htm
old-project: audio
ms.assetid: 8b7a49cc-5061-475b-ac03-cbf43954c413
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IPinCount, PinCount, IPinCount::PinCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPinCount.PinCount
req.alt-loc: portcls.h
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
req.iface: IPinCount
---

# IPinCount::PinCount method



## -description
<p>The <code>PinCount</code> method queries the miniport driver for its pin count.</p>


## -syntax

````
void PinCount(
  [in]      ULONG  PinId,
  [in, out] PULONG FilterNecessary,
  [in, out] PULONG FilterCurrent,
  [in, out] PULONG FilterPossible,
  [in, out] PULONG GlobalCurrent,
  [in, out] PULONG GlobalPossible
);
````


## -parameters
<dl>

### -param <i>PinId</i> [in]

<dd>
<p>Specifies the pin ID. If a filter contains <i>n</i> pin factories, valid pin IDs range from 0 to <i>n</i>-1.</p>
</dd>

### -param <i>FilterNecessary</i> [in, out]

<dd>
<p>Specifies the minimum number of pins that the pin factory should instantiate before the filter can perform I/O operations.</p>
</dd>

### -param <i>FilterCurrent</i> [in, out]

<dd>
<p>Specifies the current number of pin instances. This number counts the pins that the pin factory has already instantiated on the filter.</p>
</dd>

### -param <i>FilterPossible</i> [in, out]

<dd>
<p>Specifies the maximum number of pins that the pin factory can instantiate on the filter. Set to KSINSTANCE_INDETERMINATE if there is no maximum.</p>
</dd>

### -param <i>GlobalCurrent</i> [in, out]

<dd>
<p>Specifies the current number of pins that the pin factory has instantiated on the driver.</p>
</dd>

### -param <i>GlobalPossible</i> [in, out]

<dd>
<p>Specifies the maximum number of pins that the pin factory can instantiate on the driver. Set to KSINSTANCE_INDETERMINATE if there is no maximum.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <code>PinCount</code> call has two purposes:</p>

<p>To let the miniport driver know the current pin counts.</p>

<p>To give the miniport driver an opportunity to alter the current pin counts.</p>

<p><i>FilterNecessary</i>, <i>FilterCurrent</i>, <i>FilterPossible</i>, <i>GlobalCurrent</i>, and <i>GlobalPossible</i> are all IN+OUT parameters that point to values in the miniport driver's filter description. During the <i>PinCount</i> call, the miniport driver can examine these values and has the option of editing the values in order to more accurately indicate how many additional pins can be created from the remaining resources.</p>

<p><i>FilterCurrent</i> and <i>FilterPossible</i> specify the per-filter values for the pin factory specified by <i>PinId</i>.</p>

<p><i>GlobalCurrent</i> and <i>GlobalPossible</i> specify the total values for the pin factory over all instances of the filter.</p>

<p>Miniport drivers typically do not need to change the <i>FilterNecessary</i> parameter, but it is included for the sake of completeness.</p>

<p>During the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a> call, the port driver calls the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536765">IMiniport::GetDescription</a> method to obtain a pointer to the filter descriptor, which includes the miniport driver's pin-descriptor array (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537721">PCPIN_DESCRIPTOR</a>). Thereafter, the port driver accesses the pin descriptors to respond to queries for pin properties.</p>

<p>If the miniport driver supports the <b>IPinCount</b> interface, the port driver calls <code>PinCount</code> to give the miniport driver an opportunity to update the pin counts before replying to a pin-property request. If the miniport driver does not support <b>IPinCount</b>, the port driver simply uses the static pin-count limits in the pin-descriptor array.</p>

<p>The port driver calls the <code>PinCount</code> method when it receives one of the following KS property requests:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565200">KSPROPERTY_PIN_GLOBALCINSTANCES</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565204">KSPROPERTY_PIN_NECESSARYINSTANCES</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565200">KSPROPERTY_PIN_GLOBALCINSTANCES</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565204">KSPROPERTY_PIN_NECESSARYINSTANCES</a>
</p>

<p>PortCls also calls the <code>PinCount</code> method each time a new stream is created.</p>

<p>Miniport drivers must not explicitly cause streams to be created or destroyed from within the <code>PinCount</code> method. Miniport drivers are not otherwise restricted in what they can do during this call.</p>

<p>The <code>PinCount</code> method is called at IRQL PASSIVE_LEVEL. The code for this method must reside in paged memory.</p>

<p>The <code>PinCount</code> call has two purposes:</p>

<p>To let the miniport driver know the current pin counts.</p>

<p>To give the miniport driver an opportunity to alter the current pin counts.</p>

<p><i>FilterNecessary</i>, <i>FilterCurrent</i>, <i>FilterPossible</i>, <i>GlobalCurrent</i>, and <i>GlobalPossible</i> are all IN+OUT parameters that point to values in the miniport driver's filter description. During the <i>PinCount</i> call, the miniport driver can examine these values and has the option of editing the values in order to more accurately indicate how many additional pins can be created from the remaining resources.</p>

<p><i>FilterCurrent</i> and <i>FilterPossible</i> specify the per-filter values for the pin factory specified by <i>PinId</i>.</p>

<p><i>GlobalCurrent</i> and <i>GlobalPossible</i> specify the total values for the pin factory over all instances of the filter.</p>

<p>Miniport drivers typically do not need to change the <i>FilterNecessary</i> parameter, but it is included for the sake of completeness.</p>

<p>During the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a> call, the port driver calls the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536765">IMiniport::GetDescription</a> method to obtain a pointer to the filter descriptor, which includes the miniport driver's pin-descriptor array (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff537721">PCPIN_DESCRIPTOR</a>). Thereafter, the port driver accesses the pin descriptors to respond to queries for pin properties.</p>

<p>If the miniport driver supports the <b>IPinCount</b> interface, the port driver calls <code>PinCount</code> to give the miniport driver an opportunity to update the pin counts before replying to a pin-property request. If the miniport driver does not support <b>IPinCount</b>, the port driver simply uses the static pin-count limits in the pin-descriptor array.</p>

<p>The port driver calls the <code>PinCount</code> method when it receives one of the following KS property requests:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565200">KSPROPERTY_PIN_GLOBALCINSTANCES</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565204">KSPROPERTY_PIN_NECESSARYINSTANCES</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565200">KSPROPERTY_PIN_GLOBALCINSTANCES</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565204">KSPROPERTY_PIN_NECESSARYINSTANCES</a>
</p>

<p>PortCls also calls the <code>PinCount</code> method each time a new stream is created.</p>

<p>Miniport drivers must not explicitly cause streams to be created or destroyed from within the <code>PinCount</code> method. Miniport drivers are not otherwise restricted in what they can do during this call.</p>

<p>The <code>PinCount</code> method is called at IRQL PASSIVE_LEVEL. The code for this method must reside in paged memory.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536832">IPinCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536765">IMiniport::GetDescription</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537721">PCPIN_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565200">KSPROPERTY_PIN_GLOBALCINSTANCES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565204">KSPROPERTY_PIN_NECESSARYINSTANCES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPinCount::PinCount method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
