---
UID: NF.wdm.InitializeListHead
title: InitializeListHead
author: windows-driver-content
description: The InitializeListHead routine initializes a LIST_ENTRY structure that represents the head of a doubly linked list.
old-location: kernel\initializelisthead.htm
old-project: kernel
ms.assetid: 123434fd-4e83-4042-834b-1eb4cf13dd10
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: InitializeListHead
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
req.alt-api: InitializeListHead
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

# InitializeListHead function



## -description
<p>The <b>InitializeListHead</b> routine initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554296">LIST_ENTRY</a> structure that represents the head of a doubly linked list.</p>


## -syntax

````
VOID InitializeListHead(
  _Out_ PLIST_ENTRY ListHead
);
````


## -parameters
<dl>

### -param <i>ListHead</i> [out]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554296">LIST_ENTRY</a> structure that serves as the list header. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>InitializeListHead</b> routine sets the <b>Flink</b> and <b>Blink</b> members of <i>ListHead</i> to point to <i>ListHead</i>.</p>

<p>For information about using this routine when implementing a doubly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.</p>

<p>Callers of <b>InitializeListHead</b> can be running at any IRQL. If <b>InitializeListHead</b> is called at IRQL &gt;= DISPATCH_LEVEL the storage for <i>ListHead</i> must be resident.</p>

<p>The <b>InitializeListHead</b> routine sets the <b>Flink</b> and <b>Blink</b> members of <i>ListHead</i> to point to <i>ListHead</i>.</p>

<p>For information about using this routine when implementing a doubly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.</p>

<p>Callers of <b>InitializeListHead</b> can be running at any IRQL. If <b>InitializeListHead</b> is called at IRQL &gt;= DISPATCH_LEVEL the storage for <i>ListHead</i> must be resident.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545397">ExInterlockedInsertHeadList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545402">ExInterlockedInsertTailList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545427">ExInterlockedRemoveHeadList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545408">ExInterlockedPopEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545418">ExInterlockedPushEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547820">InsertHeadList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547823">InsertTailList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551789">IsListEmpty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552160">KeInitializeSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559712">PopEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559964">PushEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561029">RemoveEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561032">RemoveHeadList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561036">RemoveTailList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20InitializeListHead routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
