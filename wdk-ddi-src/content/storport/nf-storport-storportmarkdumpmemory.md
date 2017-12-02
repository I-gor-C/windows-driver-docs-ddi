---
UID: NF.storport.StorPortMarkDumpMemory
title: StorPortMarkDumpMemory
author: windows-driver-content
description: A miniport should mark memory used for the dump file or the hibernation file.
old-location: storage\storportmarkdumpmemory.htm
old-project: storage
ms.assetid: DE17FF55-A573-41FE-8979-1DB32AD5B7C0
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortMarkDumpMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortMarkDumpMemory
req.alt-loc: Storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any
req.iface: 
req.product: Windows 10 or later.
---

# StorPortMarkDumpMemory function



## -description
<p>A miniport should mark  memory used for the dump file or the hibernation file. Marked memory is retained and remains valid after a resume from hibernation operation. The memory  to mark is specified by an address and range length in a call to <b>StorPortMarkDumpMemory</b>.</p>


## -syntax

````
ULONG StorPortMarkDumpMemory(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID Address,
  _In_ PVOID Length,
  _In_ PVOID Flags
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param Address [in]

<dd>
<p>The starting address of the memory range to mark.</p>
</dd>

### -param Length [in]

<dd>
<p>The length of the marked memory range.</p>
</dd>

### -param Flags [in]

<dd>
<p>Dump memory marking flags. The <i>Flags</i> parameter must be 0 or contain only the following value.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="MARK_DUMP_MEMORY_FLAG_PHYSICAL_ADDRESS"></a><a id="mark_dump_memory_flag_physical_address"></a><dl>

### -param MARK_DUMP_MEMORY_FLAG_PHYSICAL_ADDRESS

</dl>
</td>
<td width="60%">
<p>The address provided in <i>Address</i> is a physical address and not a system virtual address.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>StorPortMarkDumpMemory</b> returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the routine set the unit attributes successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid flag value was specified in the <i>Flags</i> parameter.</p>

<p> </p>

## -remarks
<p>The <b>StorPortMarkDumpMemory</b> routine must only be called by a miniport driver in its <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> or <a href="storage.hwstorfindadapter">HwStorFindAdapter</a> routines.</p>

<p>If <i>Length</i> = 0, the entire section containing <i>Address</i> is marked.</p>

<p>Miniport drivers should call <b>StorPortMarkDumpMemory</b> to ensure that the memory used by the miniport to generate either the dump file or the hibernation file is identified. At a minimum, miniports should call <b>StorPortMarkDumpMemory</b> when the <b>DumpMode</b> member of <a href="..\strmini\ns-strmini--port-configuration-information~r1.md">PORT_CONFIGURATION_INFORMATION</a> is set to either <b>DUMP_MODE_MARK_MEMORY</b> or <b>DUMP_MODE_HIBER</b>.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any</p>
</td>
</tr>
</table>