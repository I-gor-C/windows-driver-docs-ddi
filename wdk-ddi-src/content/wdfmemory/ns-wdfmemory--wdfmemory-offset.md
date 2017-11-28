---
UID: NS.wdfmemory._WDFMEMORY_OFFSET
title: WDFMEMORY_OFFSET
author: windows-driver-content
description: The WDFMEMORY_OFFSET structure identifies a subsection of a memory object's buffer.
old-location: wdf\wdfmemory_offset.htm
old-project: wdf
ms.assetid: ca891a21-e7ab-4230-bfc4-adfdb413838b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDFMEMORY_OFFSET, WDFMEMORY_OFFSET, *PWDFMEMORY_OFFSET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfmemory.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDFMEMORY_OFFSET
req.alt-loc: wdfmemory.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WDFMEMORY_OFFSET structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDFMEMORY_OFFSET</b> structure identifies a subsection of a memory object's buffer.</p>


## -syntax

````
typedef struct _WDFMEMORY_OFFSET {
  size_t BufferOffset;
  size_t BufferLength;
} WDFMEMORY_OFFSET, *PWDFMEMORY_OFFSET;
````


## -struct-fields
<dl>

### -field <b>BufferOffset</b>

<dd>
<p>A byte offset from the beginning of the memory object's buffer. This offset identifies the location of the buffer's subsection. A value of zero represents the beginning of the buffer.</p>
</dd>

### -field <b>BufferLength</b>

<dd>
<p>The length, in bytes, of the buffer's subsection. A value of zero represents the entire buffer.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDFMEMORY_OFFSET</b> structure is used as a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure and as an input parameter to various I/O target object methods.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfmemory.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDFMEMORY_OFFSET structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
