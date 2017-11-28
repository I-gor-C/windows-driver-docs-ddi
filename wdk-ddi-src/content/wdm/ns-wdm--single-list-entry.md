---
UID: NS.wdm._SINGLE_LIST_ENTRY
title: SINGLE_LIST_ENTRY
author: windows-driver-content
description: A SINGLE_LIST_ENTRY structure describes an entry in a singly linked list, or serves as the header for such a list.
old-location: kernel\single_list_entry.htm
old-project: kernel
ms.assetid: 2db8ce7e-67e0-43e8-98b5-a2112db5bd5a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: SINGLE_LIST_ENTRY,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SINGLE_LIST_ENTRY
req.alt-loc: ntdef.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# SINGLE_LIST_ENTRY structure



## -description
<p>A <b>SINGLE_LIST_ENTRY</b> structure describes an entry in a singly linked list, or serves as the header for such a list.</p>


## -syntax

````
typedef struct _SINGLE_LIST_ENTRY {
  struct _SINGLE_LIST_ENTRY  *Next;
} SINGLE_LIST_ENTRY, *PSINGLE_LIST_ENTRY;
````


## -struct-fields
<dl>

### -field <b>Next</b>

<dd>
<p>For a <b>SINGLE_LIST_ENTRY</b> that serves as a list entry, the <b>Next</b> member points to the next entry in the list, or <b>NULL</b> if there is no next entry in the list. For a <b>SINGLE_LIST_ENTRY</b> that serves as the list header, the <b>Next</b> member points to the first entry in the list, or <b>NULL</b> if the list is empty.</p>
</dd>
</dl>

## -remarks
<p>If a <b>SINGLE_LIST_ENTRY</b> structure is used as a list head, initialize the <b>Next</b> member of the structure to be <b>NULL</b>.</p>

<p>A driver can access the <b>Next</b> member of a <b>SINGLE_LIST_ENTRY</b>, but (other than initializing a list head) <b>Next</b> must only be updated by the system routines supplied for this purpose.</p>

<p>For more information about how to use <b>SINGLE_LIST_ENTRY</b> structures to implement a singly linked list, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563802">Singly and Doubly Linked Lists</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdef.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545408">ExInterlockedPopEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545418">ExInterlockedPushEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559712">PopEntryList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559964">PushEntryList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20SINGLE_LIST_ENTRY structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
