---
UID: NS.wdm._MM_PHYSICAL_ADDRESS_LIST
title: MM_PHYSICAL_ADDRESS_LIST
author: windows-driver-content
description: The MM_PHYSICAL_ADDRESS_LIST structure specifies a range of physical addresses.
old-location: kernel\mm_physical_address_list.htm
ms.assetid: D653607A-7C37-408D-AD19-B4A8988CDACE
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MM_PHYSICAL_ADDRESS_LIST
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
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: MM_PHYSICAL_ADDRESS_LIST, MM_PHYSICAL_ADDRESS_LIST, *PMM_PHYSICAL_ADDRESS_LIST
req.iface: 
req.product: Windows 10 or later.
---

# MM_PHYSICAL_ADDRESS_LIST structure



## -description
<p>The <b>MM_PHYSICAL_ADDRESS_LIST</b> structure specifies a range of physical addresses.</p>


## -syntax

````
typedef struct _MM_PHYSICAL_ADDRESS_LIST {
  PHYSICAL_ADDRESS PhysicalAddress;
  SIZE_T           NumberOfBytes;
} MM_PHYSICAL_ADDRESS_LIST, *PMM_PHYSICAL_ADDRESS_LIST;
````


## -struct-fields
<dl>

### -field <b>PhysicalAddress</b>

<dd>
<p>The starting physical address of the range. This address must be aligned to a page boundary in physical memory.</p>
</dd>

### -field <b>NumberOfBytes</b>

<dd>
<p>The number of bytes in the range. This member must be nonzero and an integer multiple of the memory page size.</p>
</dd>
</dl>

## -remarks
<p>The first parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/jj206443">MmAllocateMdlForIoSpace</a> routine is a pointer to an array of <b>MM_PHYSICAL_ADDRESS_LIST</b> structures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj206443">MmAllocateMdlForIoSpace</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MM_PHYSICAL_ADDRESS_LIST structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
