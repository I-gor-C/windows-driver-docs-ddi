---
UID: NF.ks.KsTopologyPropertyHandler
title: KsTopologyPropertyHandler
author: windows-driver-content
description: The KsTopologyPropertyHandler function performs standard handling of the static members of the KSPROPSETID_Topology Property Set. The function uses the KSTOPOLOGY structure, which describes the set of information that is returned by this property set.
old-location: stream\kstopologypropertyhandler.htm
ms.assetid: fe033614-b1a0-490b-b45b-a8d8de650dbf
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsTopologyPropertyHandler
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
ms.keywords: KsTopologyPropertyHandler
req.iface: 
---

# KsTopologyPropertyHandler function



## -description
<p>The <b>KsTopologyPropertyHandler</b> function performs standard handling of the static members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566598">KSPROPSETID_Topology</a> Property Set. The function uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567146">KSTOPOLOGY</a> structure, which describes the set of information that is returned by this property set.</p>


## -syntax

````
NTSTATUS KsTopologyPropertyHandler(
  _In_          PIRP        Irp,
  _In_          PKSPROPERTY Property,
  _Inout_       PVOID       Data,
  _In_    const KSTOPOLOGY  *Topology
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP handling the property request.</p>
</dd>

### -param <i>Property</i> [in]

<dd>
<p>Specifies the specific property being queried.</p>
</dd>

### -param <i>Data</i> [in, out]

<dd>
<p>Specifies the topology property-specific data.</p>
</dd>

### -param <i>Topology</i> [in]

<dd>
<p>Points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567146">KSTOPOLOGY</a> structure containing the topology information.</p>
</dd>
</dl>

## -returns
<p>The <b>KsTopologyPropertyHandler</b> function returns STATUS_SUCCESS if successful, or it returns an error specific to the property being handled. The function always fills in the IO_STATUS_BLOCK.Information field of the PIRP.IoStatus element within the IRP. It does not set the IO_STATUS_BLOCK.Status field, nor does it complete the IRP. </p>

## -remarks


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