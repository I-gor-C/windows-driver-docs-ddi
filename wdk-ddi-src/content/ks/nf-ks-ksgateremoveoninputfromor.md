---
UID: NF.ks.KsGateRemoveOnInputFromOr
title: KsGateRemoveOnInputFromOr
author: windows-driver-content
description: The KsGateRemoveOnInputFromOr function removes an existing input that is in the ON state from an OR gate.
old-location: stream\ksgateremoveoninputfromor.htm
old-project: stream
ms.assetid: e7226684-afbf-46e1-aeb2-6b0c60c12680
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGateRemoveOnInputFromOr
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
req.alt-api: KsGateRemoveOnInputFromOr
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

# KsGateRemoveOnInputFromOr function



## -description
<p>The<b> KsGateRemoveOnInputFromOr </b>function removes an existing input that is in the ON state from an OR gate.</p>


## -syntax

````
void __inline KsGateRemoveOnInputFromOr(
  _In_ PKSGATE OrGate
);
````


## -parameters
<dl>

### -param <i>OrGate</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562566">KSGATE</a> structure representing the OR gate from which to remove an ON input.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Removing the last ON input from a given OR gate results in the gate closing and the transition being propagated to any gates connected to <i>OrGate</i>. For more information, see <a href="NULL">Flow Control Gates in AVStream</a>.</p>

<p><b>KsGateRemoveOnInputFromOr</b> should only be used on gates that were specifically created as AND gates; AVStream does not verify that the given gate is an AND gate.</p>

<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562589">KsGateTurnInputOff</a>. If conceptually removing an existing input to a gate, a minidriver should call <b>KsGateRemoveOnInputFromOr</b> rather than <b>KsGateTurnInputOff</b>.</p>

<p>Removing the last ON input from a given OR gate results in the gate closing and the transition being propagated to any gates connected to <i>OrGate</i>. For more information, see <a href="NULL">Flow Control Gates in AVStream</a>.</p>

<p><b>KsGateRemoveOnInputFromOr</b> should only be used on gates that were specifically created as AND gates; AVStream does not verify that the given gate is an AND gate.</p>

<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562589">KsGateTurnInputOff</a>. If conceptually removing an existing input to a gate, a minidriver should call <b>KsGateRemoveOnInputFromOr</b> rather than <b>KsGateTurnInputOff</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562570">KsGateAddOnInputToOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562568">KsGateAddOffInputToOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562580">KsGateRemoveOffInputFromOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562591">KsGateTurnInputOn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562589">KsGateTurnInputOff</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGateRemoveOnInputFromOr function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
