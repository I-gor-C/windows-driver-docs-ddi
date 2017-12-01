---
UID: NF.ntifs.FsRtlDeleteExtraCreateParameterLookasideList
title: FsRtlDeleteExtraCreateParameterLookasideList
author: windows-driver-content
description: The FsRtlDeleteExtraCreateParameterLookasideList routine frees an extra create parameter (ECP) lookaside list.
old-location: ifsk\fsrtldeleteextracreateparameterlookasidelist.htm
old-project: ifsk
ms.assetid: 786635b4-db99-4b35-9fb5-23233997d091
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlDeleteExtraCreateParameterLookasideList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: FsRtlDeleteExtraCreateParameterLookasideList is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlDeleteExtraCreateParameterLookasideList
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

# FsRtlDeleteExtraCreateParameterLookasideList function



## -description
<p>The <b>FsRtlDeleteExtraCreateParameterLookasideList </b>routine frees an extra create parameter (ECP) lookaside list.</p>


## -syntax

````
VOID FsRtlDeleteExtraCreateParameterLookasideList(
  _Inout_ PVOID                     Lookaside,
  _In_    FSRTL_ECP_LOOKASIDE_FLAGS Flags
);
````


## -parameters
<dl>

### -param <i>Lookaside</i> [in, out]

<dd>
<p>Pointer to an opaque <a href="https://msdn.microsoft.com/library/windows/hardware/ff558775">PAGED_LOOKASIDE_LIST</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff556431">NPAGED_LOOKASIDE_LIST</a> lookaside list-head structure that represents the lookaside list to be freed.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Communicates ECP lookaside list allocation options with which the <a href="..\ntifs\nf-ntifs-fsrtlinitextracreateparameterlookasidelist.md">FsRtlInitExtraCreateParameterLookasideList</a> routine initialized the lookaside list.</p>
<p>This <i>Flags</i> parameter should be the same as the <i>Flags</i> parameter used in the call to the <a href="..\ntifs\nf-ntifs-fsrtlinitextracreateparameterlookasidelist.md">FsRtlInitExtraCreateParameterLookasideList</a> routine.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>FsRtlDeleteExtraCreateParameterLookasideList</b> routine frees the ECP lookaside list to which the <i>Lookaside</i> parameter points. However, freeing the lookaside list does not automatically free any ECP context structures allocated from the lookaside list. To free an ECP context structure allocated from a lookaside list, call the <a href="..\ntifs\nf-ntifs-fsrtlfreeextracreateparameter.md">FsRtlFreeExtraCreateParameter</a> routine.</p>

<p>Drivers must explicitly free all ECP context structures and ECP lookaside lists that they created before unloading. For more information about using lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.</p>

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
<p>FsRtlDeleteExtraCreateParameterLookasideList is available starting with Windows Vista. </p>
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
<a href="..\ntifs\nf-ntifs-fsrtlfreeextracreateparameter.md">FsRtlFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlinitextracreateparameterlookasidelist.md">FsRtlInitExtraCreateParameterLookasideList</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlDeleteExtraCreateParameterLookasideList routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
