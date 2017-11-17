---
UID: NL.engextcpp.ExtRemoteList
title: ExtRemoteList
author: windows-driver-content
description: The ExtRemoteList class provides a wrapper around a singly-linked or doubly-linked list. The class contains methods that can be used to move both forward and backward through the list.
old-location: debugger\extremotelist.htm
ms.assetid: d35d5186-a5ee-4a64-88e7-d3e95de32d07
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteList
req.alt-loc: engextcpp.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: ExtRemoteTypedList, SetTypeAndLink, ExtRemoteTypedList::SetTypeAndLink
req.iface: ExtRemoteTypedList
---

# ExtRemoteList interface



## -description
<p>The <b>ExtRemoteList</b> class provides a wrapper around a singly-linked or doubly-linked list.  The class contains methods that can be used to move both forward and backward through the list.</p>
<p><b>ExtRemoteList</b> supports both NULL-terminated and circular lists.</p>
<p><b>ExtRemoteList</b> expects that a list is lists implemented in the way that NT-based versions of Windows implements a list.  It also expects that the list uses the SINGLE_LIST_ENTRY or LIST_ENTRY structure.  In particular, <b>ExtRemoteList</b> expects the lists to have the following characteristics:</p>
<p>The list has a <i>head</i>.  The head represents the beginning (and, for circular and doubly-linked lists, the end) of the list and is not a list item.  The type of the head is SINGLE_LIST_ENTRY or LIST_ENTRY.</p>
<p>The pointer to the next item in the list points to the pointer to the following item.  In other words, the pointer to the next item points to the SINGLE_LIST_ENTRY or LIST_ENTRY structure embedded in the next item.</p>
<p>For doubly-linked lists, the pointer to the previous item in the list points to the pointer to the current item.  In other words, the pointer to the previous item points to the LIST_ENTRY structure embedded in the previous item.</p>
<p>For doubly-linked lists, the pointer to the previous item immediately follows the pointer to the next item.  This matches the layout of the LIST_ENTRY structure in memory.</p>
<p>For more information about the SINGLE_LIST_ENTRY and LIST_ENTRY structures and their use, see the Windows Driver Kit (WDK) documentation.</p>
<p>The <b>ExtRemoteList</b> class includes the following methods:</p>
<p>
<a href="https://msdn.microsoft.com/db670175-ad3b-4bed-b9ad-625494319256">ExtRemoteList::ExtRemoteList (ExtRemoteData)</a>
</p>
<p>
<a href="https://msdn.microsoft.com/c23487bb-c385-4633-b27c-12a49492f339">ExtRemoteList::ExtRemoteList (ULONG64)</a>
</p>
<p>
<a href="https://msdn.microsoft.com/d7d9163b-54bb-4753-96a3-f92eddbe25f5">StartHead</a>
</p>
<p>
<a href="https://msdn.microsoft.com/fe9aec87-a464-4ea9-b9ca-3dbb91bb4e3e">StartTail</a>
</p>
<p>
<a href="https://msdn.microsoft.com/412a77c8-eb10-43c5-bc45-2c61858463a7">HasNode</a>
</p>
<p>
<a href="https://msdn.microsoft.com/20c4ec7e-6dc1-4a4f-99d1-bb53213771a5">GetNodeOffset</a>
</p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn926903">Next</a>
</p>
<p>
<a href="https://msdn.microsoft.com/0dc65a1a-2188-417b-9f5c-4a3d2dc0bbb0">Prev</a>
</p>
<p></p>
<p>The location in the target's memory of the head of the list.</p>
<p>The offset of the SINGLE_LIST_ENTRY or LIST_ENTRY structures embedded within the list items.</p>
<p><code>true</code> for a doubly-linked list.  <code>false</code> for a singly-linked list.</p>
<p>The maximum number of nodes that can be returned when iterating over the list.  The default value of <b>m_MaxIter</b> is 65536. Limiting the number of nodes that can be returned in an iteration protects against loops.</p>
<p>The pointer to the current item in the list.  <b>m_Node</b> is not set until an iteration is initialized using <a href="https://msdn.microsoft.com/d7d9163b-54bb-4753-96a3-f92eddbe25f5">StartHead</a> or <a href="https://msdn.microsoft.com/fe9aec87-a464-4ea9-b9ca-3dbb91bb4e3e">StartTail</a>.  <b>m_Node</b> is of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff544008">ExtRemoteData</a>, which describes the pointer.</p>
<p>The number of steps taken in the current list iteration.  For doubly-linked lists, <b>m_CurIter</b> is increased for both forward and backward steps.</p>


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544008">ExtRemoteData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d7d9163b-54bb-4753-96a3-f92eddbe25f5">StartHead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fe9aec87-a464-4ea9-b9ca-3dbb91bb4e3e">StartTail</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20ExtRemoteList class%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
