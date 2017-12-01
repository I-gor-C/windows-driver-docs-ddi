---
UID: NF.ntddk.RtlRightChild
title: RtlRightChild
author: windows-driver-content
description: The RtlRightChild routine returns a pointer to the right child of the specified splay link node.
old-location: ifsk\rtlrightchild.htm
old-project: ifsk
ms.assetid: 1b906983-b000-449b-8e82-46ade5384168
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlRightChild
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlRightChild
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
req.iface: 
---

# RtlRightChild function



## -description
<p>The <b>RtlRightChild</b> routine returns a pointer to the right child of the specified splay link node. </p>


## -syntax

````
PRTL_SPLAY_LINKS RtlRightChild(
  _In_ PRTL_SPLAY_LINKS Links
);
````


## -parameters
<dl>

### -param <i>Links</i> [in]

<dd>
<p>Pointer to the node whose right child is to be returned. The node must have been initialized by calling <b>RtlInitializeSplayLinks</b>. </p>
</dd>
</dl>

## -returns
<p><b>RtlRightChild</b> returns a pointer to the right child of the node at <i>Links</i>, or it returns <b>NULL</b> if the specified node has no right child. </p>

## -remarks
<p><b>RtlRightChild</b> can be called repeatedly in conjunction with <b>RtlParent</b> and <b>RtlLeftChild</b> to walk a splay link tree. </p>

<p>Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlRightChild</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the tree is nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL. </p>

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
<a href="..\ntddk\nf-ntddk-rtlinitializesplaylinks.md">RtlInitializeSplayLinks</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlinsertasrightchild.md">RtlInsertAsRightChild</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlleftchild.md">RtlLeftChild</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-rtlparent.md">RtlParent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlRightChild routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
