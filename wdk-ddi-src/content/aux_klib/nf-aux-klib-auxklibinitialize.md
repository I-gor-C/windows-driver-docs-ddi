---
UID: NF.aux_klib.AuxKlibInitialize
title: AuxKlibInitialize
author: windows-driver-content
description: The AuxKlibInitialize routine initializes the Auxiliary Kernel-Mode Library.
old-location: kernel\auxklibinitialize.htm
old-project: kernel
ms.assetid: 7e15cbe1-17f7-4df7-9273-9a365d309d03
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: AuxKlibInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: aux_klib.h
req.include-header: Aux_klib.h
req.target-type: Universal
req.target-min-winverclnt: Supported starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AuxKlibInitialize
req.alt-loc: Aux_Klib.lib,Aux_Klib.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Aux_Klib.lib
req.dll: 
req.irql: 
req.iface: 
---

# AuxKlibInitialize function



## -description
<p>The <b>AuxKlibInitialize</b> routine initializes the <a href="kernel.auxiliary_kernel_mode_library_routines_and_structures">Auxiliary Kernel-Mode Library</a>.</p>


## -syntax

````
NTSTATUS AuxKlibInitialize(void);
````


## -parameters


## -returns
<p><b>AuxKlibInitialize</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the routine returns an appropriate NTSTATUS value.</p>

<p><b>AuxKlibInitialize</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the routine returns an appropriate NTSTATUS value.</p>

<p><b>AuxKlibInitialize</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the routine returns an appropriate NTSTATUS value.</p>

## -remarks
<p>Drivers that use the Auxiliary Kernel-Mode Library must call <b>AuxKlibInitialize</b> before calling any of the library's other routines.</p>

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
<p>Supported starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Aux_klib.h (include Aux_klib.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Aux_Klib.lib</dt>
</dl>
</td>
</tr>
</table>