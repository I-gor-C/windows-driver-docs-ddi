---
UID: NF.ntddk.RtlInitializeSplayLinks
title: RtlInitializeSplayLinks
author: windows-driver-content
description: The RtlInitializeSplayLinks routine initializes a splay link node.
old-location: ifsk\rtlinitializesplaylinks.htm
ms.assetid: 34818dc0-d241-4f5f-a202-08200fbc23a3
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
req.alt-api: RtlInitializeSplayLinks
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
ms.keywords: RtlInitializeSplayLinks
req.iface: 
---

# RtlInitializeSplayLinks function



## -description
<p>The <b>RtlInitializeSplayLinks</b> routine initializes a splay link node. </p>


## -syntax

````
VOID RtlInitializeSplayLinks(
  _In_ PRTL_SPLAY_LINKS Links
);
````


## -parameters
<dl>

### -param <i>Links</i> [in]

<dd>
<p>Pointer to a caller-allocated buffer, which must be at least <b>sizeof(</b>RTL_SPLAY_LINK<b>)</b>, to contain the initialized splay link node. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Every splay link node, including the initial root node of the splay link tree, must be initialized by calling <b>RtlInitializeSplayLinks</b> before it is passed to any other <b>Rtl</b> splay link routine. The initialized splay link node structure should be considered opaque.</p>

<p>Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlInitializeSplayLinks</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the memory at <i>Links</i> is nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL. </p>

<p>Every splay link node, including the initial root node of the splay link tree, must be initialized by calling <b>RtlInitializeSplayLinks</b> before it is passed to any other <b>Rtl</b> splay link routine. The initialized splay link node structure should be considered opaque.</p>

<p>Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. </p>

<p>Callers of <b>RtlInitializeSplayLinks</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the memory at <i>Links</i> is nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545293">ExInitializeFastMutex</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552214">RtlDeleteNoSplay</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553017">RtlInsertAsLeftChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553022">RtlInsertAsRightChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553054">RtlIsLeftChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553066">RtlIsRightChild</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553186">RtlRealPredecessor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553188">RtlRealSuccessor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553200">RtlRightChild</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553226">RtlSplay</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553237">RtlSubtreePredecessor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553239">RtlSubtreeSuccessor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlInitializeSplayLinks routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
