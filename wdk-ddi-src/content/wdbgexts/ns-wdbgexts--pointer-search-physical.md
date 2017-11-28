---
UID: NS.wdbgexts._POINTER_SEARCH_PHYSICAL
title: POINTER_SEARCH_PHYSICAL
author: windows-driver-content
description: The IG_POINTER_SEARCH_PHYSICAL Ioctl operation searches the target's physical memory for pointers lying within a specified range.
old-location: debugger\ig_pointer_search_physical.htm
old-project: debugger
ms.assetid: fdb8376b-fbda-4bee-895e-a306fd0f632a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: POINTER_SEARCH_PHYSICAL, POINTER_SEARCH_PHYSICAL, *PPOINTER_SEARCH_PHYSICAL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POINTER_SEARCH_PHYSICAL
req.alt-loc: wdbgexts.h
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
req.iface: 
req.product: Windows 10 or later.
---

# POINTER_SEARCH_PHYSICAL structure



## -description
<p>The IG_POINTER_SEARCH_PHYSICAL <a href="https://msdn.microsoft.com/library/windows/hardware/ff551084">Ioctl</a> operation searches the target's physical memory for pointers lying within a specified range.  When calling <b>Ioctl</b> with <i>IoctlType</i> set to IG_POINTER_SEARCH_PHYSICAL, <i>IpvData</i> should contain an instance of the POINTER_SEARCH_PHYSICAL structure.</p>


## -syntax

````
typedef struct _POINTER_SEARCH_PHYSICAL {
  ULONG64  Offset;
  ULONG64  Length;
  ULONG64  PointerMin;
  ULONG64  PointerMax;
  ULONG    Flags;
  PULONG64 MatchOffsets;
  ULONG    MatchOffsetsSize;
  ULONG    MatchOffsetsCount;
} POINTER_SEARCH_PHYSICAL, *PPOINTER_SEARCH_PHYSICAL;
````


## -struct-fields
<dl>

### -field <b>Offset</b>

<dd>
<p>Specifies the address in the target's physical memory to start searching from.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Specifies the amount of the target's physical memory to search.</p>
</dd>

### -field <b>PointerMin</b>

<dd>
<p>Specifies the lower limit of the range of pointers to search for.</p>
</dd>

### -field <b>PointerMax</b>

<dd>
<p>Specifies the upper limit of the range of pointers to search for.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies bit flags that alter the behavior of this <b>Ioctl</b> operation.  The following flags can be included.</p>
<table>
<tr>
<th>Flag</th>
<th>Behavior when set</th>
</tr>
<tr>
<td>
<p>PTR_SEARCH_PHYS_ALL_HITS</p>
</td>
<td>
<p>Return all pointers in the specified range.  If this flag is not set, only one pointer per page is returned.</p>
</td>
</tr>
<tr>
<td>
<p>PTR_SEARCH_PHYS_PTE</p>
</td>
<td>
<p>The memory is searched for a page table entry (PTE) that matches the Page Frame Number specified in <b>PointerMin</b>.</p>
</td>
</tr>
<tr>
<td>
<p>PTR_SEARCH_PHYS_RANGE_CHECK_ONLY</p>
</td>
<td>
<p></p>
</td>
</tr>
<tr>
<td>
<p>PTR_SEARCH_NO_SYMBOL_CHECK</p>
</td>
<td>
<p>Do not check that the symbols used for the kernel are correct.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MatchOffsets</b>

<dd>
<p>Receives the addresses of all the pointers that match the search criteria.  <b>MatchOffsets</b> is an array that contains <b>MatchOffsetsSize</b> elements.</p>
</dd>

### -field <b>MatchOffsetsSize</b>

<dd>
<p>Specifies the number of entries in the array <b>MatchOffsets</b>.</p>
</dd>

### -field <b>MatchOffsetsCount</b>

<dd>
<p>Receives the number of pointers found that match the search criteria.</p>
</dd>
</dl>

## -remarks
<p>The parameters for the IG_POINTER_SEARCH_PHYSICAL <a href="https://msdn.microsoft.com/library/windows/hardware/ff551084">Ioctl</a> operation are the members of the POINTER_SEARCH_PHYSICAL structure.</p>

<p>The parameters for the IG_POINTER_SEARCH_PHYSICAL <a href="https://msdn.microsoft.com/library/windows/hardware/ff551084">Ioctl</a> operation are the members of the POINTER_SEARCH_PHYSICAL structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdbgexts.h (include Wdbgexts.h or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551084">Ioctl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20POINTER_SEARCH_PHYSICAL structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
