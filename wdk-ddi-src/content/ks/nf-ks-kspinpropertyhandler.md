---
UID: NF.ks.KsPinPropertyHandler
title: KsPinPropertyHandler
author: windows-driver-content
description: The KsPinPropertyHandler function performs standard handling of the static members of the KSPROPSETID_Pin property set. This handling does not include KSPROPERTY_PIN_CINSTANCES or KSPROPERTY_PIN_DATAINTERSECTION.
old-location: stream\kspinpropertyhandler.htm
old-project: stream
ms.assetid: b721b79b-93f3-4dc8-853d-543222464341
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinPropertyHandler
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinPropertyHandler
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
req.irql: 
req.iface: 
---

# KsPinPropertyHandler function



## -description
<p>The <b>KsPinPropertyHandler</b> function performs standard handling of the static members of<b> the </b><a href="https://msdn.microsoft.com/library/windows/hardware/ff566584">KSPROPSETID_Pin</a> property set. This handling does not include <a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff565198">KSPROPERTY_PIN_DATAINTERSECTION</a>. </p>


## -syntax

````
NTSTATUS KsPinPropertyHandler(
  _In_          PIRP             Irp,
  _In_          PKSPROPERTY      Property,
  _Inout_       PVOID            Data,
  _In_          ULONG            DescriptorsCount,
  _In_    const KSPIN_DESCRIPTOR *Descriptor
);
````


## -parameters
<dl>

### -param Irp [in]

<dd>
<p>Specifies the IRP handling the connection request.</p>
</dd>

### -param Property [in]

<dd>
<p>Specifies the specific property information.</p>
</dd>

### -param Data [in, out]

<dd>
<p>Specifies the data parameter mapped to a system address. This is the same parameter passed to a property handler through a <a href="..\ks\nf-ks-kspropertyhandler.md">KsPropertyHandler</a> callback.</p>
</dd>

### -param DescriptorsCount [in]

<dd>
<p>Specifies the number of pin descriptors being passed.</p>
</dd>

### -param Descriptor [in]

<dd>
<p>Specifies the pointer to the list of pin descriptors.</p>
</dd>
</dl>

## -returns
<p>The <b>KsPinPropertyHandler</b> function returns STATUS_SUCCESS or an error specific to the property being handled. The function fills in the IO_STATUS_BLOCK.Information field of the PIRP.IoStatus element within the IRP. It does not set the IO_STATUS_BLOCK.Status field nor complete the IRP.</p>

## -remarks
<p>Do not use the <b>KsPinPropertyHandler</b> function to define a pin property set; a pin property set can be more easily defined using the DEFINE_KSPROPERY_PINSET macro.</p>

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
</table>