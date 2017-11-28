---
UID: NF.ntddk.RtlDelete
title: RtlDelete
author: windows-driver-content
description: The RtlDelete routine deletes the specified node from the splay link tree.
old-location: ifsk\rtldelete.htm
old-project: ifsk
ms.assetid: ca73b7cf-56c0-4e83-8804-59f73fbd4714
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlDelete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlDelete
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
req.irql: See Remarks section.
req.iface: 
---

# RtlDelete function



## -description
<p>The <b>RtlDelete</b> routine deletes the specified node from the splay link tree. </p>


## -syntax

````
PRTL_SPLAY_LINKS RtlDelete(
  _In_ PRTL_SPLAY_LINKS Links
);
````


## -parameters
<dl>

### -param <i>Links</i> [in]

<dd>
<p>Pointer to the node to be deleted. The node must have been initialized by calling <b>RtlInitializeSplayLinks</b>.</p>
</dd>
</dl>

## -returns
<p><b>RtlDelete</b> returns a pointer to the root of the splay link tree from which the given node was deleted, or it returns <b>NULL</b> if the tree is empty. </p>

## -remarks
<p><b>RtlDelete</b> rebalances the splay link tree after the node is deleted. To delete a node without rebalancing the tree, use <b>RtlDeleteNoSplay</b> instead of <b>RtlDelete</b>.</p>

<p>Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlDelete</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the splay link tree is nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL. </p>

<p><b>RtlDelete</b> rebalances the splay link tree after the node is deleted. To delete a node without rebalancing the tree, use <b>RtlDeleteNoSplay</b> instead of <b>RtlDelete</b>.</p>

<p>Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlDelete</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the splay link tree is nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL. </p>

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
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
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
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552214">RtlDeleteNoSplay</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553010">RtlInitializeSplayLinks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553017">RtlInsertAsLeftChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553022">RtlInsertAsRightChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553226">RtlSplay</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlDelete routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
