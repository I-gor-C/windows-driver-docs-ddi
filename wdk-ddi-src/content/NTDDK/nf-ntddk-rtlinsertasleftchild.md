---
UID: NF.ntddk.RtlInsertAsLeftChild
title: RtlInsertAsLeftChild
author: windows-driver-content
description: The RtlInsertAsLeftChild routine inserts a splay link node into the tree as the left child of the specified node.
old-location: ifsk\rtlinsertasleftchild.htm
ms.assetid: cbb027f2-be7d-4de4-abbe-a37b7430153f
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlInsertAsLeftChild
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
ms.keywords: RtlInsertAsLeftChild
req.iface: 
---

# RtlInsertAsLeftChild function



## -description
<p>The <b>RtlInsertAsLeftChild</b> routine inserts a splay link node into the tree as the left child of the specified node. </p>


## -syntax

````
VOID RtlInsertAsLeftChild(
  _In_ PRTL_SPLAY_LINKS ParentLinks,
  _In_ PRTL_SPLAY_LINKS ChildLinks
);
````


## -parameters
<dl>

### -param <i>ParentLinks</i> [in]

<dd>
<p>Pointer to the node in the tree at which <i>ChildLinks</i> should be inserted as the left child. </p>
</dd>

### -param <i>ChildLinks</i> [in]

<dd>
<p>Pointer to the splay link node to be inserted into the tree. The node must have been initialized by calling <b>RtlInitializeSplayLinks</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Callers of <b>RtlInsertAsLeftChild</b> are must meet the following criteria:</p>

<p>The node at <i>ParentLinks</i> must have no left child. </p>

<p>A caller can determine whether the node already has a left child by calling <b>RtlLeftChild</b>. If <b>RtlLeftChild</b> returns <b>NULL</b>, <i>ParentLinks</i> is a valid parameter to <b>RtlInsertAsLeftChild</b>.</p>

<p>The node at <i>ChildLinks</i> must have no parent.</p>

<p>A caller can determine whether this node already has a parent by calling <b>RtlIsRoot</b> or <b>RtlParent</b>. If <b>RtlIsRoot</b> returns <b>TRUE</b> when called with <i>ChildLinks</i>, <i>ChildLinks</i> is a valid parameter to <b>RtlInsertAsLeftChild</b>. If <b>RtlParent</b> returns an equivalent pointer to <i>ChildLinks</i>, <i>ChildLinks</i> is a valid parameter to <b>RtlInsertAsLeftChild</b>. </p>

<p>Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlInsertAsLeftChild</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the splay link tree and <i>ChildLinks</i> node are nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL. </p>

<p>Callers of <b>RtlInsertAsLeftChild</b> are must meet the following criteria:</p>

<p>The node at <i>ParentLinks</i> must have no left child. </p>

<p>A caller can determine whether the node already has a left child by calling <b>RtlLeftChild</b>. If <b>RtlLeftChild</b> returns <b>NULL</b>, <i>ParentLinks</i> is a valid parameter to <b>RtlInsertAsLeftChild</b>.</p>

<p>The node at <i>ChildLinks</i> must have no parent.</p>

<p>A caller can determine whether this node already has a parent by calling <b>RtlIsRoot</b> or <b>RtlParent</b>. If <b>RtlIsRoot</b> returns <b>TRUE</b> when called with <i>ChildLinks</i>, <i>ChildLinks</i> is a valid parameter to <b>RtlInsertAsLeftChild</b>. If <b>RtlParent</b> returns an equivalent pointer to <i>ChildLinks</i>, <i>ChildLinks</i> is a valid parameter to <b>RtlInsertAsLeftChild</b>. </p>

<p>Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlInsertAsLeftChild</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the splay link tree and <i>ChildLinks</i> node are nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL. </p>

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
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553010">RtlInitializeSplayLinks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553022">RtlInsertAsRightChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553072">RtlIsRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553080">RtlLeftChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553165">RtlParent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553226">RtlSplay</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlInsertAsLeftChild routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
