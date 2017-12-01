---
UID: NF.ks.KsPinAttachAndGate
title: KsPinAttachAndGate
author: windows-driver-content
description: The KsPinAttachAndGate function connects Pin as an input to a previously initialized AND gate, and connects AndGate as an input to the relevant filter's AND gate.
old-location: stream\kspinattachandgate.htm
old-project: stream
ms.assetid: 63081b07-add8-49fc-b12d-6aa5c43356ce
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinAttachAndGate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinAttachAndGate
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL (See Remarks section)
req.iface: 
---

# KsPinAttachAndGate function



## -description
<p>The<b> KsPinAttachAndGate</b> function connects <i>Pin</i> as an input to a previously initialized AND gate, and connects <i>AndGate</i> as an input to the relevant filter's AND gate.</p>


## -syntax

````
void KsPinAttachAndGate(
  _In_     PKSPIN  Pin,
  _In_opt_ PKSGATE AndGate
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="..\ks\ns-ks--kspin.md">KSPIN</a> structure to use an input to the AND gate.</p>
</dd>

### -param <i>AndGate</i> [in, optional]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--ksgate.md">KSGATE</a> structure that is the previously initialized AND gate to connect to the relevant filter's AND gate. If this optional parameter is <b>NULL</b>, any <b>KSGATE</b> currently attached to the pin is detached.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>To insert the gate, first call <a href="..\ks\nf-ks-ksgateinitializeand.md">KsGateInitializeAnd</a>. Then call <b>KsPinAttachAndGate</b>. For more information, see <a href="NULL">Flow Control Gates in AVStream</a>.</p>

<p><b>KsPinAttachAndGate </b>must be called at IRQL = PASSIVE_LEVEL before the pin in question leaves KSSTATE_STOP.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\nf-ks-kspinattachorgate.md">KsPinAttachOrGate</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgateinitializeand.md">KsGateInitializeAnd</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksgate.md">KSGATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinAttachAndGate function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
