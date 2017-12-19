---
UID: NF.procgrp.WdmlibProcgrpInitialize
title: WdmlibProcgrpInitialize function
author: windows-driver-content
description: The WdmlibProcgrpInitialize function initializes the Processor Group (ProcGrp) compatibility library.
old-location: kernel\wdmlibprocgrpinitialize.htm
old-project: kernel
ms.assetid: 760f7bd8-0957-4dd0-b201-64173961cbb2
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.product: Windows 10 or later.
---

# WdmlibProcgrpInitialize function



## -description
The <b>WdmlibProcgrpInitialize</b> function initializes the Processor Group (ProcGrp) compatibility library.



## -syntax

````
VOID WdmlibProcgrpInitialize(void);
````


## -parameters


## -returns
None

None

None


## -remarks
This function initializes the ProcGrp library. Call this function before calling any of the other functions in the ProcGrp library. The library implements wrapper functions that have the same names as the following processor-group <b>Ke<i>Xxx</i></b> routines in Windows 7:


<a href="kernel.kegetcurrentprocessornumberex">KeGetCurrentProcessorNumberEx</a>



<a href="kernel.kegetprocessorindexfromnumber">KeGetProcessorIndexFromNumber</a>



<a href="kernel.kegetprocessornumberfromindex">KeGetProcessorNumberFromIndex</a>



<a href="kernel.kequeryactivegroupcount">KeQueryActiveGroupCount</a>



<a href="kernel.kequeryactiveprocessorcountex">KeQueryActiveProcessorCountEx</a>



<a href="kernel.kequerygroupaffinity">KeQueryGroupAffinity</a>



<a href="kernel.kequerymaximumprocessorcount">KeQueryMaximumProcessorCount</a>



<a href="kernel.kequerymaximumprocessorcountex">KeQueryMaximumProcessorCountEx</a>



<a href="kernel.kequerymaximumgroupcount">KeQueryMaximumGroupCount</a>



<a href="kernel.kesetsystemaffinitythreadex">KeSetSystemAffinityThreadEx</a>



<a href="kernel.kesetsystemgroupaffinitythread">KeSetSystemGroupAffinityThread</a>



<a href="kernel.kereverttouseraffinitythreadex">KeRevertToUserAffinityThreadEx</a>



<a href="kernel.kereverttousergroupaffinitythread">KeRevertToUserGroupAffinityThread</a>



<a href="kernel.kesettargetprocessordpcex">KeSetTargetProcessorDpcEx</a>


For more information about the ProcGrp library, see <a href="kernel.processor_group_compatibility_library">Processor Group Compatibility Library</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Compatible with Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista, Windows Server 2003, Windows XP, and Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Procgrp.h (include Procgrp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Procgrp.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>