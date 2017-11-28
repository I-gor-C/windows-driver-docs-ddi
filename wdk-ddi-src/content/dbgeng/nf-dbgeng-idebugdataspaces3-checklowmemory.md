---
UID: NF.dbgeng.IDebugDataSpaces3.CheckLowMemory
title: IDebugDataSpaces3::CheckLowMemory
author: windows-driver-content
description: The CheckLowMemory method checks for memory corruption in the low 4 GB of memory.
old-location: debugger\checklowmemory.htm
old-project: debugger
ms.assetid: b7e3bb5c-d4c7-469e-aa2d-fa9a98706c2f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces3, CheckLowMemory, IDebugDataSpaces3::CheckLowMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces.CheckLowMemory,IDebugDataSpaces2.CheckLowMemory,IDebugDataSpaces3.CheckLowMemory,IDebugDataSpaces4.CheckLowMemory
req.alt-loc: Dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IDebugDataSpaces3
---

# IDebugDataSpaces3::CheckLowMemory method



## -description
<p>The <b>CheckLowMemory</b> method checks for memory corruption in the low 4 GB of memory.</p>


## -syntax

````
HRESULT CheckLowMemory();
````


## -parameters


## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>No corruption was found.</p><dl>
<dt><b>FACILITY_NT_BIT |<i>Page</i></b></dt>
</dl><p>Corruption was found on the memory page <i>Page</i>.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>No corruption was found.</p><dl>
<dt><b>FACILITY_NT_BIT |<i>Page</i></b></dt>
</dl><p>Corruption was found on the memory page <i>Page</i>.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>No corruption was found.</p><dl>
<dt><b>FACILITY_NT_BIT |<i>Page</i></b></dt>
</dl><p>Corruption was found on the memory page <i>Page</i>.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in <a href="debugger.k#kernel_mode_debugging#kernel_mode_debugging"><i>kernel-mode debugging</i></a>, and is only useful when the <a href="debugger.k#kernel#kernel"><i>kernel</i></a> was booted using the <b>/nolowmem</b> option.</p>

<p>When the kernel is booted with the <b>/nolowmem</b> option, the kernel, drivers, operating system and applications are loaded in memory above 4 GB, while the low 4 GB of memory is filled with a unique pattern.  The <b>CheckLowMemory</b> method checks this pattern for corruption.</p>

<p>This may be used to verify that a driver behaves well when using physical addresses greater than 32 bits in length.  See <i>Physical Address Extension (PAE)</i>, <b>/pae</b>, and <b>/nolowmem</b> in the Windows Driver Kit.</p>

<p>This method is only available in <a href="debugger.k#kernel_mode_debugging#kernel_mode_debugging"><i>kernel-mode debugging</i></a>, and is only useful when the <a href="debugger.k#kernel#kernel"><i>kernel</i></a> was booted using the <b>/nolowmem</b> option.</p>

<p>When the kernel is booted with the <b>/nolowmem</b> option, the kernel, drivers, operating system and applications are loaded in memory above 4 GB, while the low 4 GB of memory is filled with a unique pattern.  The <b>CheckLowMemory</b> method checks this pattern for corruption.</p>

<p>This may be used to verify that a driver behaves well when using physical addresses greater than 32 bits in length.  See <i>Physical Address Extension (PAE)</i>, <b>/pae</b>, and <b>/nolowmem</b> in the Windows Driver Kit.</p>

<p>This method is only available in <a href="debugger.k#kernel_mode_debugging#kernel_mode_debugging"><i>kernel-mode debugging</i></a>, and is only useful when the <a href="debugger.k#kernel#kernel"><i>kernel</i></a> was booted using the <b>/nolowmem</b> option.</p>

<p>When the kernel is booted with the <b>/nolowmem</b> option, the kernel, drivers, operating system and applications are loaded in memory above 4 GB, while the low 4 GB of memory is filled with a unique pattern.  The <b>CheckLowMemory</b> method checks this pattern for corruption.</p>

<p>This may be used to verify that a driver behaves well when using physical addresses greater than 32 bits in length.  See <i>Physical Address Extension (PAE)</i>, <b>/pae</b>, and <b>/nolowmem</b> in the Windows Driver Kit.</p>

<p>This method is only available in <a href="debugger.k#kernel_mode_debugging#kernel_mode_debugging"><i>kernel-mode debugging</i></a>, and is only useful when the <a href="debugger.k#kernel#kernel"><i>kernel</i></a> was booted using the <b>/nolowmem</b> option.</p>

<p>When the kernel is booted with the <b>/nolowmem</b> option, the kernel, drivers, operating system and applications are loaded in memory above 4 GB, while the low 4 GB of memory is filled with a unique pattern.  The <b>CheckLowMemory</b> method checks this pattern for corruption.</p>

<p>This may be used to verify that a driver behaves well when using physical addresses greater than 32 bits in length.  See <i>Physical Address Extension (PAE)</i>, <b>/pae</b>, and <b>/nolowmem</b> in the Windows Driver Kit.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>