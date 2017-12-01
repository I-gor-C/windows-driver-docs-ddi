---
UID: NF.procgrp.WdmlibProcgrpInitialize
title: WdmlibProcgrpInitialize
author: windows-driver-content
description: The WdmlibProcgrpInitialize function initializes the Processor Group (ProcGrp) compatibility library.
old-location: kernel\wdmlibprocgrpinitialize.htm
old-project: kernel
ms.assetid: 760f7bd8-0957-4dd0-b201-64173961cbb2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdmlibProcgrpInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: procgrp.h
req.include-header: Procgrp.h
req.target-type: Desktop
req.target-min-winverclnt: Compatible with Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista, Windows Server 2003, Windows XP, and Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WdmlibProcgrpInitialize
req.alt-loc: Procgrp.lib,Procgrp.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Procgrp.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdmlibProcgrpInitialize function



## -description
<p>The <b>WdmlibProcgrpInitialize</b> function initializes the Processor Group (ProcGrp) compatibility library.</p>


## -syntax

````
VOID WdmlibProcgrpInitialize(void);
````


## -parameters


## -returns
<p>None</p>

<p>None</p>

<p>None</p>

## -remarks
<p>This function initializes the ProcGrp library. Call this function before calling any of the other functions in the ProcGrp library. The library implements wrapper functions that have the same names as the following processor-group <b>Ke<i>Xxx</i></b> routines in Windows 7:</p>

<p>
<a href="..\ntddk\nf-ntddk-kegetcurrentprocessornumberex.md">KeGetCurrentProcessorNumberEx</a>
</p>

<p>
<a href="..\ntifs\nf-ntifs-kegetprocessorindexfromnumber.md">KeGetProcessorIndexFromNumber</a>
</p>

<p>
<a href="..\wdm\nf-wdm-kegetprocessornumberfromindex.md">KeGetProcessorNumberFromIndex</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-kequeryactivegroupcount.md">KeQueryActiveGroupCount</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-kequeryactiveprocessorcountex.md">KeQueryActiveProcessorCountEx</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-kequerygroupaffinity.md">KeQueryGroupAffinity</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-kequerymaximumprocessorcount.md">KeQueryMaximumProcessorCount</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-kequerymaximumprocessorcountex.md">KeQueryMaximumProcessorCountEx</a>
</p>

<p>
<a href="..\ntddk\nf-ntddk-kequerymaximumgroupcount.md">KeQueryMaximumGroupCount</a>
</p>

<p>
<a href="..\wdm\nf-wdm-kesetsystemaffinitythreadex.md">KeSetSystemAffinityThreadEx</a>
</p>

<p>
<a href="..\wdm\nf-wdm-kesetsystemgroupaffinitythread.md">KeSetSystemGroupAffinityThread</a>
</p>

<p>
<a href="..\wdm\nf-wdm-kereverttouseraffinitythreadex.md">KeRevertToUserAffinityThreadEx</a>
</p>

<p>
<a href="..\wdm\nf-wdm-kereverttousergroupaffinitythread.md">KeRevertToUserGroupAffinityThread</a>
</p>

<p>
<a href="..\wdm\nf-wdm-kesettargetprocessordpcex.md">KeSetTargetProcessorDpcEx</a>
</p>

<p>For more information about the ProcGrp library, see <a href="kernel.processor_group_compatibility_library">Processor Group Compatibility Library</a>. </p>

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
<p>Compatible with Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista, Windows Server 2003, Windows XP, and Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Procgrp.h (include Procgrp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Procgrp.lib</dt>
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