---
UID: NS.ntifs._IO_PRIORITY_INFO
title: IO_PRIORITY_INFO
author: windows-driver-content
description: The IO_PRIORITY_INFO structure is used to hold thread priority information.
old-location: ifsk\io_priority_info.htm
old-project: ifsk
ms.assetid: 1161b239-3ad1-4a0c-9d11-4a3a88d361b3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IO_PRIORITY_INFO, IO_PRIORITY_INFO, *PIO_PRIORITY_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IO_PRIORITY_INFO
req.alt-loc: ntifs.h
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
---

# IO_PRIORITY_INFO structure



## -description
<p>The IO_PRIORITY_INFO structure is used to hold thread priority information.</p>


## -syntax

````
typedef struct _IO_PRIORITY_INFO {
  ULONG            Size;
  ULONG            ThreadPriority;
  ULONG            PagePriority;
  IO_PRIORITY_HINT IoPriority;
} IO_PRIORITY_INFO, *PIO_PRIORITY_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Read-only member initialized by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548424">IoInitializePriorityInfo</a> routine.</p>
</dd>

### -field <b>ThreadPriority</b>

<dd>
<p>Read-only member used to hold a thread's priority.</p>
</dd>

### -field <b>PagePriority</b>

<dd>
<p>Read-only member used to hold a thread's paging priority.</p>
</dd>

### -field <b>IoPriority</b>

<dd>
<p>Read-only member used to hold a thread's I/O priority.</p>
</dd>
</dl>

## -remarks
<p>The IO_PRIORITY_INFO structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544354">FltRetrieveIoPriorityInfo</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff541766">FltApplyPriorityInfoThread</a> routines to save and set a thread's priority state.</p>

<p>A structure of type IO_PRIORITY_INFO must be initialized before first use by calling either the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548424">IoInitializePriorityInfo</a> routine or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541766">FltApplyPriorityInfoThread</a> routine.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541766">FltApplyPriorityInfoThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543065">FltGetIoPriorityHint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543068">FltGetIoPriorityHintFromCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543074">FltGetIoPriorityHintFromFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543080">FltGetIoPriorityHintFromThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544354">FltRetrieveIoPriorityInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544526">FltSetIoPriorityHintIntoCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544530">FltSetIoPriorityHintIntoFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544534">FltSetIoPriorityHintIntoThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548424">IoInitializePriorityInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IO_PRIORITY_INFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
