---
UID: NF.ks.KsGateInitializeOr
title: KsGateInitializeOr
author: windows-driver-content
description: The KsGateInitializeOr function initializes a KSGATE structure as an OR gate and attaches it to the AND gate specified by NextAndGate.
old-location: stream\ksgateinitializeor.htm
ms.assetid: a02a3b53-03fa-49d4-835c-88623c2f4d8b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGateInitializeOr
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
ms.keywords: KsGateInitializeOr
req.iface: 
---

# KsGateInitializeOr function



## -description
<p>The<b> KsGateInitializeOr</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562566">KSGATE</a> structure as an OR gate and attaches it to the AND gate specified by <i>NextAndGate</i>.</p>


## -syntax

````
void __inline KsGateInitializeOr(
  _In_     PKSGATE OrGate,
  _In_opt_ PKSGATE NextAndGate
);
````


## -parameters
<dl>

### -param <i>OrGate</i> [in]

<dd>
<p>A pointer to the KSGATE structure to initialize as a new OR gate.</p>
</dd>

### -param <i>NextAndGate</i> [in, optional]

<dd>
<p>A pointer to an existing KSGATE structure to which <i>OrGate</i> attaches. Optional.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The next gate (following <i>OrGate</i>) must be an AND gate, whether it is specified in this call or later. If you need to connect an OR gate to another OR gate, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562573">KsGateInitialize</a>. For more information, see <a href="NULL">Flow Control Gates in AVStream</a>.</p>

<p>This function is an inline call to <b>KsGateInitialize</b>.</p>

<p>The next gate (following <i>OrGate</i>) must be an AND gate, whether it is specified in this call or later. If you need to connect an OR gate to another OR gate, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562573">KsGateInitialize</a>. For more information, see <a href="NULL">Flow Control Gates in AVStream</a>.</p>

<p>This function is an inline call to <b>KsGateInitialize</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562573">KsGateInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562574">KsGateInitializeAnd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562586">KsGateTerminateAnd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562588">KsGateTerminateOr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562566">KSGATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGateInitializeOr function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
