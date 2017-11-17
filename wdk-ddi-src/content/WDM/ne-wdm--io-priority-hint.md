---
UID: NE.wdm._IO_PRIORITY_HINT
title: IO_PRIORITY_HINT
author: windows-driver-content
description: The IO_PRIORITY_HINT enumeration type specifies the priority hint for an IRP.
old-location: kernel\io_priority_hint.htm
ms.assetid: 38d19398-b34f-4934-b643-df119ebd9711
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IO_PRIORITY_HINT
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.iface: 
req.product: Windows 10 or later.
---

# IO_PRIORITY_HINT enumeration



## -description
<p>The <b>IO_PRIORITY_HINT</b> enumeration type specifies the <a href="https://msdn.microsoft.com/c34afff2-32f2-451b-ab16-ff048d5c3204">priority hint</a> for an IRP.</p>


## -syntax

````
typedef enum _IO_PRIORITY_HINT { 
  IoPriorityVeryLow   = 0,
  IoPriorityLow       = 1,
  IoPriorityNormal    = 2,
  IoPriorityHigh      = 3,
  IoPriorityCritical  = 4,
  MaxIoPriorityTypes  = 5
} IO_PRIORITY_HINT;
````


## -enum-fields
<dl>

### -field <a id="IoPriorityVeryLow"></a><a id="iopriorityverylow"></a><a id="IOPRIORITYVERYLOW"></a><b>IoPriorityVeryLow</b>

<dd>
<p>Specifies the lowest possible priority hint level. The system uses this value for background I/O operations.</p>
</dd>

### -field <a id="IoPriorityLow"></a><a id="ioprioritylow"></a><a id="IOPRIORITYLOW"></a><b>IoPriorityLow</b>

<dd>
<p>Specifies a low-priority hint level. </p>
</dd>

### -field <a id="IoPriorityNormal"></a><a id="ioprioritynormal"></a><a id="IOPRIORITYNORMAL"></a><b>IoPriorityNormal</b>

<dd>
<p>Specifies a normal-priority hint level. This value is the default setting for an IRP.</p>
</dd>

### -field <a id="IoPriorityHigh"></a><a id="iopriorityhigh"></a><a id="IOPRIORITYHIGH"></a><b>IoPriorityHigh</b>

<dd>
<p>Specifies a high-priority hint level. This value is reserved for use by the system.</p>
</dd>

### -field <a id="IoPriorityCritical"></a><a id="ioprioritycritical"></a><a id="IOPRIORITYCRITICAL"></a><b>IoPriorityCritical</b>

<dd>
<p>Specifies the highest-priority hint level. This value is reserved for use by the system.</p>
</dd>

### -field <a id="MaxIoPriorityTypes"></a><a id="maxioprioritytypes"></a><a id="MAXIOPRIORITYTYPES"></a><b>MaxIoPriorityTypes</b>

<dd>
<p>Marks the limit for priority hints. Any priority hint value must be less than <b>MaxIoPriorityTypes</b>.</p>
</dd>
</dl>

## -remarks
<p>For more information about priority hints, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565403">Using IRP Priority Hints</a>.</p>

<p>For more information about priority hints, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565403">Using IRP Priority Hints</a>.</p>

<p>For more information about priority hints, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565403">Using IRP Priority Hints</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549265">IoGetIoPriorityHint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549710">IoSetIoPriorityHint</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_PRIORITY_HINT enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
