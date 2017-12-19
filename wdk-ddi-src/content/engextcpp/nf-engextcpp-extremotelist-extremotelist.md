---
UID: NF.engextcpp.ExtRemoteList.ExtRemoteList
title: ExtRemoteList::ExtRemoteList method
author: windows-driver-content
description: The ExtRemoteList class provides a wrapper around a singly-linked or doubly-linked list. The class contains methods that can be used to move both forward and backward through the list.
old-location: debugger\extremotelist.htm
old-project: Debugger
ms.assetid: d35d5186-a5ee-4a64-88e7-d3e95de32d07
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteList, ExtRemoteList::ExtRemoteList, ExtRemoteList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
---

# ExtRemoteList::ExtRemoteList method



## -description
The <b>ExtRemoteList</b> class provides a wrapper around a singly-linked or doubly-linked list.  The class contains methods that can be used to move both forward and backward through the list.

<b>ExtRemoteList</b> supports both NULL-terminated and circular lists.

<b>ExtRemoteList</b> expects that a list is lists implemented in the way that NT-based versions of Windows implements a list.  It also expects that the list uses the SINGLE_LIST_ENTRY or LIST_ENTRY structure.  In particular, <b>ExtRemoteList</b> expects the lists to have the following characteristics:

The list has a <i>head</i>.  The head represents the beginning (and, for circular and doubly-linked lists, the end) of the list and is not a list item.  The type of the head is SINGLE_LIST_ENTRY or LIST_ENTRY.

The pointer to the next item in the list points to the pointer to the following item.  In other words, the pointer to the next item points to the SINGLE_LIST_ENTRY or LIST_ENTRY structure embedded in the next item.

For doubly-linked lists, the pointer to the previous item in the list points to the pointer to the current item.  In other words, the pointer to the previous item points to the LIST_ENTRY structure embedded in the previous item.

For doubly-linked lists, the pointer to the previous item immediately follows the pointer to the next item.  This matches the layout of the LIST_ENTRY structure in memory.

For more information about the SINGLE_LIST_ENTRY and LIST_ENTRY structures and their use, see the Windows Driver Kit (WDK) documentation.

The <b>ExtRemoteList</b> class includes the following methods:


<a href="..\engextcpp\nl-engextcpp-extremotelist.md">ExtRemoteList::ExtRemoteList (ExtRemoteData)</a>



<a href="..\engextcpp\nl-engextcpp-extremotelist.md">ExtRemoteList::ExtRemoteList (ULONG64)</a>



<a href="debugger.extremotelist_starthead">StartHead</a>



<a href="debugger.extremotelist_starttail">StartTail</a>



<a href="debugger.extremotelist_hasnode">HasNode</a>



<a href="debugger.extremotelist_getnodeoffset">GetNodeOffset</a>



<a href="debugger.extremotelist_next">Next</a>



<a href="debugger.extremotelist_prev">Prev</a>




The location in the target's memory of the head of the list.

The offset of the SINGLE_LIST_ENTRY or LIST_ENTRY structures embedded within the list items.

<code>true</code> for a doubly-linked list.  <code>false</code> for a singly-linked list.

The maximum number of nodes that can be returned when iterating over the list.  The default value of <b>m_MaxIter</b> is 65536. Limiting the number of nodes that can be returned in an iteration protects against loops.

The pointer to the current item in the list.  <b>m_Node</b> is not set until an iteration is initialized using <a href="debugger.extremotelist_starthead">StartHead</a> or <a href="debugger.extremotelist_starttail">StartTail</a>.  <b>m_Node</b> is of type <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>, which describes the pointer.

The number of steps taken in the current list iteration.  For doubly-linked lists, <b>m_CurIter</b> is increased for both forward and backward steps.



## -parameters


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>
</dt>
<dt>
<a href="debugger.extremotelist_starthead">StartHead</a>
</dt>
<dt>
<a href="debugger.extremotelist_starttail">StartTail</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20ExtRemoteList class%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

