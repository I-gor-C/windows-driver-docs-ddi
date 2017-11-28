---
UID: NF.ks.KsGateTurnInputOn
title: KsGateTurnInputOn
author: windows-driver-content
description: The KsGateTurnInputOn function turns on an existing input to Gate.
old-location: stream\ksgateturninputon.htm
old-project: stream
ms.assetid: 68c914bf-a293-42b0-85aa-c9e8f2ba18ac
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGateTurnInputOn
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGateTurnInputOn
req.alt-loc: ks.h
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
---

# KsGateTurnInputOn function



## -description
<p>The<b> KsGateTurnInputOn</b> function turns on an existing input to <i>Gate</i>.</p>


## -syntax

````
void __inline KsGateTurnInputOn(
  _In_opt_ PKSGATE Gate
);
````


## -parameters
<dl>

### -param <i>Gate</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562566">KSGATE</a> structure representing the gate that currently has an input in the OFF state to transition to the ON state. May be an AND gate or an OR gate.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>It is the minidriver's responsibility to verify that the gate that the minidriver passes to <b>KsGateTurnInputOn</b> has at least one OFF input. If you call this function with an AND gate that has no inputs currently in the OFF state, the call sets the AND gate into an invalid state. If you call this function with an OR gate that has no inputs currently in the OFF state, the result is equivalent to adding another input in the ON state to <i>Gate</i>.</p>

<p>Furthermore, if turning an input on would cause <i>Gate</i> to transition from the closed state to the open state, this call instead turns on an input to whatever gate is attached to <i>Gate</i>. For more information, see <a href="NULL">Flow Control Gates in AVStream</a>. </p>

<p>It is the minidriver's responsibility to verify that the gate that the minidriver passes to <b>KsGateTurnInputOn</b> has at least one OFF input. If you call this function with an AND gate that has no inputs currently in the OFF state, the call sets the AND gate into an invalid state. If you call this function with an OR gate that has no inputs currently in the OFF state, the result is equivalent to adding another input in the ON state to <i>Gate</i>.</p>

<p>Furthermore, if turning an input on would cause <i>Gate</i> to transition from the closed state to the open state, this call instead turns on an input to whatever gate is attached to <i>Gate</i>. For more information, see <a href="NULL">Flow Control Gates in AVStream</a>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562589">KsGateTurnInputOff</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562569">KsGateAddOnInputToAnd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562570">KsGateAddOnInputToOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562567">KsGateAddOffInputToAnd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562568">KsGateAddOffInputToOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562584">KsGateRemoveOnInputFromAnd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562585">KsGateRemoveOnInputFromOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562578">KsGateRemoveOffInputFromAnd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562580">KsGateRemoveOffInputFromOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562566">KSGATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGateTurnInputOn function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
