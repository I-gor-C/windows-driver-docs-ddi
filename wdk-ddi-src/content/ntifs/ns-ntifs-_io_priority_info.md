---
UID: NS.NTIFS._IO_PRIORITY_INFO
title: _IO_PRIORITY_INFO
author: windows-driver-content
description: The IO_PRIORITY_INFO structure is used to hold thread priority information.
old-location: ifsk\io_priority_info.htm
old-project: ifsk
ms.assetid: 1161b239-3ad1-4a0c-9d11-4a3a88d361b3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _IO_PRIORITY_INFO, *PIO_PRIORITY_INFO, IO_PRIORITY_INFO
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
---

# _IO_PRIORITY_INFO structure



## -description
The IO_PRIORITY_INFO structure is used to hold thread priority information.



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

### -field Size

Read-only member initialized by the <a href="ifsk.ioinitializepriorityinfo">IoInitializePriorityInfo</a> routine.


### -field ThreadPriority

Read-only member used to hold a thread's priority.


### -field PagePriority

Read-only member used to hold a thread's paging priority.


### -field IoPriority

Read-only member used to hold a thread's I/O priority.


## -remarks
The IO_PRIORITY_INFO structure is used by the <a href="ifsk.fltretrieveiopriorityinfo">FltRetrieveIoPriorityInfo</a> and <a href="ifsk.fltapplypriorityinfothread">FltApplyPriorityInfoThread</a> routines to save and set a thread's priority state.

A structure of type IO_PRIORITY_INFO must be initialized before first use by calling either the <a href="ifsk.ioinitializepriorityinfo">IoInitializePriorityInfo</a> routine or the <a href="ifsk.fltapplypriorityinfothread">FltApplyPriorityInfoThread</a> routine.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
This structure is available starting with Windows Vista.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="ifsk.fltapplypriorityinfothread">FltApplyPriorityInfoThread</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhint">FltGetIoPriorityHint</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromcallbackdata">FltGetIoPriorityHintFromCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromfileobject">FltGetIoPriorityHintFromFileObject</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromthread">FltGetIoPriorityHintFromThread</a>
</dt>
<dt>
<a href="ifsk.fltretrieveiopriorityinfo">FltRetrieveIoPriorityInfo</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintocallbackdata">FltSetIoPriorityHintIntoCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintofileobject">FltSetIoPriorityHintIntoFileObject</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintothread">FltSetIoPriorityHintIntoThread</a>
</dt>
<dt>
<a href="ifsk.ioinitializepriorityinfo">IoInitializePriorityInfo</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IO_PRIORITY_INFO structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

