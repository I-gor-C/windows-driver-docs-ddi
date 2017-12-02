---
UID: NF.ntifs.FsRtlInitExtraCreateParameterLookasideList
title: FsRtlInitExtraCreateParameterLookasideList
author: windows-driver-content
description: The FsRtlInitExtraCreateParameterLookasideList routine initializes a paged or nonpaged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size.
old-location: ifsk\fsrtlinitextracreateparameterlookasidelist.htm
old-project: ifsk
ms.assetid: 30ad87de-a371-415b-b77f-513369fed098
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlInitExtraCreateParameterLookasideList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The FsRtlInitExtraCreateParameterLookasideList routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlInitExtraCreateParameterLookasideList
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
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlInitExtraCreateParameterLookasideList function



## -description
<p>The <b>FsRtlInitExtraCreateParameterLookasideList</b> routine initializes a paged or nonpaged pool lookaside list used for the allocation of one or more extra create parameter context structures (ECPs) of fixed size.</p>


## -syntax

````
VOID FsRtlInitExtraCreateParameterLookasideList(
  _Inout_ PVOID                     Lookaside,
  _In_    FSRTL_ECP_LOOKASIDE_FLAGS Flags,
  _In_    SIZE_T                    Size,
  _In_    ULONG                     Tag
);
````


## -parameters
<dl>

### -param Lookaside [in, out]

<dd>
<p>Pointer to an opaque <a href="https://msdn.microsoft.com/library/windows/hardware/ff558775">PAGED_LOOKASIDE_LIST</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a> lookaside list-head structure. For a paged or nonpaged lookaside list, the list-head structure must be allocated from nonpaged pool. </p>
</dd>

### -param Flags [in]

<dd>
<p>Defines pool allocation options. If the <i>Flags</i> parameter contains the FSRTL_ECP_LOOKASIDE_FLAG_NONPAGED_POOL bit flag value, <b>FsRtlInitExtraCreateParameterLookasideList</b> initializes a lookaside list for nonpaged ECP entries of the specified size. Otherwise, <b>FsRtlInitExtraCreateParameterLookasideList</b> initializes a lookaside list for paged ECP entries of the specified size. </p>
</dd>

### -param Size [in]

<dd>
<p>Specifies the size, in bytes, for all ECP entries in the lookaside list. </p>
</dd>

### -param Tag [in]

<dd>
<p>Specifies the pool tag to use when allocating lookaside list ECP entries. For more information about pool tags, see the <i>Tag</i> parameter of <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Use this routine to initialize a paged or nonpaged pool lookaside list. Use the <a href="..\ntifs\nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist.md">FsRtlAllocateExtraCreateParameterFromLookasideList</a> routine to allocate an ECP from the lookaside list, and the <a href="..\ntifs\nf-ntifs-fsrtlfreeextracreateparameter.md">FsRtlFreeExtraCreateParameter</a> routine to return an ECP buffer to the lookaside list for recycling.</p>

<p>Use the <a href="..\ntifs\nf-ntifs-fsrtldeleteextracreateparameterlookasidelist.md">FsRtlDeleteExtraCreateParameterLookasideList</a> routine to free the lookaside list itself.</p>

<p>Drivers must free all ECPs and lookaside lists that they create before they unload.</p>

<p>For more information on using lookaside lists with drivers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

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
<p>The FsRtlInitExtraCreateParameterLookasideList routine is available starting with Windows Vista. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.ecp_list">ECP_LIST</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist.md">FsRtlAllocateExtraCreateParameterFromLookasideList</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtldeleteextracreateparameterlookasidelist.md">FsRtlDeleteExtraCreateParameterLookasideList</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlfreeextracreateparameter.md">FsRtlFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558775">PAGED_LOOKASIDE_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlInitExtraCreateParameterLookasideList routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
