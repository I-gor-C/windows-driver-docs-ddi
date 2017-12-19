---
UID: NF.ntifs.CcMdlWriteAbort
title: CcMdlWriteAbort function
author: windows-driver-content
description: The CcMdlWriteAbort routine frees memory descriptor lists (MDL) created by an earlier call to CcPrepareMdlWrite.
old-location: ifsk\ccmdlwriteabort.htm
old-project: ifsk
ms.assetid: 32b6fc14-dbaa-41d7-a1a7-a805b9a8795a
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: CcMdlWriteAbort
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcMdlWriteAbort
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
---

# CcMdlWriteAbort function



## -description
The <b>CcMdlWriteAbort</b> routine frees memory descriptor lists (MDL) created by an earlier call to <a href="ifsk.ccpreparemdlwrite">CcPrepareMdlWrite</a>. 



## -syntax

````
VOID CcMdlWriteAbort(
  _In_ PFILE_OBJECT FileObject,
  _In_ PMDL         MdlChain
);
````


## -parameters

### -param FileObject [in]

File object pointer that was passed to <a href="ifsk.ccpreparemdlwrite">CcPrepareMdlWrite</a>. 


### -param MdlChain [in]

Address of the MDL chain returned by <a href="ifsk.ccpreparemdlwrite">CcPrepareMdlWrite</a>. 


## -returns
None


## -remarks
File systems call <b>CcMdlWriteAbort</b> to free the memory descriptor lists (MDL) created by an earlier call to <a href="ifsk.ccpreparemdlwrite">CcPrepareMdlWrite</a> for a cached file. All physical pages that were locked down are unlocked. Any pages that were mapped are unmapped. 

File systems normally call <b>CcMdlWriteAbort</b> only in cases where, after a successful call to <a href="ifsk.ccpreparemdlwrite">CcPrepareMdlWrite</a>, it is necessary to abort or fail the subsequent MDL write operation. 

Unlike <a href="ifsk.ccmdlwritecomplete">CcMdlWriteComplete</a>, <b>CcMdlWriteAbort</b> does not cause any data to be written to the cached file. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available on Microsoft Windows XP and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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

## -see-also
<dl>
<dt>
<a href="ifsk.ccmdlwritecomplete">CcMdlWriteComplete</a>
</dt>
<dt>
<a href="ifsk.ccpreparemdlwrite">CcPrepareMdlWrite</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcMdlWriteAbort routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

