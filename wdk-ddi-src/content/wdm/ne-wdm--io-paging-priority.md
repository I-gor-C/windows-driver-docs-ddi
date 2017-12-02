---
UID: NE.wdm._IO_PAGING_PRIORITY
title: IO_PAGING_PRIORITY
author: windows-driver-content
description: The IO_PAGING_PRIORITY enumeration describes the priority value for a paging I/O IRP.
old-location: kernel\io_paging_priority.htm
old-project: kernel
ms.assetid: c96d1c81-429f-46de-b56c-6424734ccd7a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IO_PAGING_PRIORITY
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IO_PAGING_PRIORITY enumeration



## -description
<p>The <b>IO_PAGING_PRIORITY</b> enumeration describes the priority value for a paging I/O IRP.</p>


## -syntax

````
typedef enum _IO_PAGING_PRIORITY { 
  IoPagingPriorityInvalid    = 0,
  IoPagingPriorityNormal     = 1,
  IoPagingPriorityHigh       = 2,
  IoPagingPriorityReserved1  = 3,
  IoPagingPriorityReserved2  = 4
} IO_PAGING_PRIORITY;
````


## -enum-fields
<dl>

### -field IoPagingPriorityInvalid

<dd>
<p>The IRP is not a paging I/O IRP.</p>
</dd>

### -field IoPagingPriorityNormal

<dd>
<p>The associated IRP has a normal priority level for paging I/O. </p>
</dd>

### -field IoPagingPriorityHigh

<dd>
<p>The associated IRP has a high priority level for paging I/O. </p>
</dd>

### -field IoPagingPriorityReserved1

<dd>
<p>Reserved for system use.</p>
</dd>

### -field IoPagingPriorityReserved2

<dd>
<p>Reserved for system use. </p>
</dd>
</dl>

## -remarks
<p>The <a href="..\ntddk\nf-ntddk-iogetpagingiopriority.md">IoGetPagingIoPriority</a> routine returns an <b>IO_PAGING_PRIORITY</b> value to indicate the priority value of a paging I/O IRP. </p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-iogetpagingiopriority.md">IoGetPagingIoPriority</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_PAGING_PRIORITY enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
