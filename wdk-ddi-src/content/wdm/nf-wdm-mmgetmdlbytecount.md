---
UID: NF.wdm.MmGetMdlByteCount
title: MmGetMdlByteCount macro
author: windows-driver-content
description: The MmGetMdlByteCount macro returns the length, in bytes, of the buffer described by the specified MDL.
old-location: kernel\mmgetmdlbytecount.htm
old-project: Benchmark
ms.assetid: a0493418-2ce2-4917-bf9f-e4dc726a3847
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: MmGetMdlByteCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmGetMdlByteCount
req.alt-loc: Wdm.h
req.ddi-compliance: MdlAfterReqCompletedIntIoctlA, MdlAfterReqCompletedIoctlA, MdlAfterReqCompletedReadA, MdlAfterReqCompletedWriteA
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level (see Remarks section)
req.product: Windows 10 or later.
---

# MmGetMdlByteCount macro



## -description
The <b>MmGetMdlByteCount</b> macro returns the length, in bytes, of the buffer described by the specified MDL.



## -syntax

````
ULONG MmGetMdlByteCount(
  [in] PMDL Mdl
);
````


## -parameters

### -param Mdl [in]

A pointer to an <a href="kernel.mdl">MDL</a> structure that describes the layout of a virtual memory buffer in physical memory. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421">Using MDLs</a>.


## -remarks
Callers of <b>MmGetMdlByteCount</b> can be running at any IRQL. Usually, callers are running at IRQL &lt;= DISPATCH_LEVEL.


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
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level (see Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_mdlafterreqcompletedintioctla">MdlAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedioctla">MdlAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedreada">MdlAfterReqCompletedReadA</a>, <a href="devtest.kmdf_mdlafterreqcompletedwritea">MdlAfterReqCompletedWriteA</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.mdl">MDL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554533">MmGetMdlByteOffset</a>
</dt>
</dl>
 

 

