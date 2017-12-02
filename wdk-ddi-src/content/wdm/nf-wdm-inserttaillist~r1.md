---
UID: NF.wdm.InsertTailList~r1
title: InsertTailList
author: windows-driver-content
description: The InsertTailList routine inserts an entry at the tail of a doubly linked list of LIST_ENTRY structures.
old-location: kernel\inserttaillist.htm
old-project: kernel
ms.assetid: 9eb470c8-ee37-497e-982e-d32b4b9b7348
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: InsertTailList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: InsertTailList
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# InsertTailList function



## -description
<p>The <b>InsertTailList</b> routine inserts an entry at the tail of a doubly linked list of <a href="kernel.list_entry">LIST_ENTRY</a> structures.</p>


## -syntax

````
VOID InsertTailList(
  _Inout_ PLIST_ENTRY ListHead,
  _Inout_ PLIST_ENTRY Entry
);
````


## -parameters
<dl>

### -param ListHead [in, out]

<dd>
<p>Pointer to the <a href="kernel.list_entry">LIST_ENTRY</a> structure that represents the head of the list.</p>
</dd>

### -param Entry [in, out]

<dd>
<p>Pointer to a <a href="kernel.list_entry">LIST_ENTRY</a> structure that represents the entry to be inserted in the list.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>InsertTailList</b> updates <i>ListHead</i>-&gt;<b>Blink</b> to point to <i>Entry</i>. It updates <i>Entry</i>-&gt;<b>Blink</b> to point to the old last entry in the list, and sets <i>Entry</i>-&gt;<b>Flink</b> to <i>ListHead</i>. The <b>Flink</b> of the previous last entry is updated to point to <i>Entry</i> as well.</p>

<p>For information about using this routine when implementing a doubly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.</p>

<p>Callers of <b>InsertTailList</b> can be running at any IRQL. If <b>InsertTailList</b> is called at IRQL &gt;= DISPATCH_LEVEL, the storage for <i>ListHead</i> and the list entries must be resident.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exinterlockedinserttaillist.md">ExInterlockedInsertTailList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-initializelisthead.md">InitializeListHead</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-insertheadlist.md">InsertHeadList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-islistempty.md">IsListEmpty</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-removeheadlist.md">RemoveHeadList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-removetaillist.md">RemoveTailList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20InsertTailList routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
