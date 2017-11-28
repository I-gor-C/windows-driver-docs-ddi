---
UID: NF.ks.KsFilterCreatePinFactory
title: KsFilterCreatePinFactory
author: windows-driver-content
description: The KsFilterCreatePinFactory function creates a new pin factory on the specified filter.
old-location: stream\ksfiltercreatepinfactory.htm
old-project: stream
ms.assetid: f4c8de23-dc92-41b0-82ee-2622d3942c0e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFilterCreatePinFactory
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
req.alt-api: KsFilterCreatePinFactory
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsFilterCreatePinFactory function



## -description
<p>The<b> KsFilterCreatePinFactory</b> function creates a new pin factory on the specified filter.</p>


## -syntax

````
NTSTATUS KsFilterCreatePinFactory(
  _In_        PKSFILTER           Filter,
  _In_  const KSPIN_DESCRIPTOR_EX *PinDescriptor,
  _Out_       PULONG              PinID
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure for which to create a new pin factory.</p>
</dd>

### -param <i>PinDescriptor</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a> structure that describes the pins this factory will create.</p>
</dd>

### -param <i>PinID</i> [out]

<dd>
<p>A pointer to the location containing the ID of the new factory.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterCreatePinFactory</b> returns the success or failure of the attempt to create the pin factory. Failure may occur due to invalid parameters or low memory.</p>

## -remarks
<p>Note that the filter control mutex must be held before calling this function. For more information, see <a href="NULL">Mutexes in AVStream</a>. </p>

<p>Note that the filter control mutex must be held before calling this function. For more information, see <a href="NULL">Mutexes in AVStream</a>. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562528">KsFilterCreateNode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterCreatePinFactory function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
