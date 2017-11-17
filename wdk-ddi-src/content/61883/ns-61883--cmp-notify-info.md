---
UID: NS.61883._CMP_NOTIFY_INFO
title: CMP_NOTIFY_INFO
author: windows-driver-content
description: This structure is used by the PCMP_NOTIFY_ROUTINE callback.
old-location: ieee\cmp_notify_info.htm
ms.assetid: 7451B01F-D925-4882-9E6B-EEA79F54C55B
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CMP_NOTIFY_INFO
req.alt-loc: 61883.h
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
ms.keywords: CMP_NOTIFY_INFO, CMP_NOTIFY_INFO, *PCMP_NOTIFY_INFO
---

# CMP_NOTIFY_INFO structure



## -description
<p>This structure is used by the <a href="https://msdn.microsoft.com/0576D73A-0A36-4AB7-952C-19B56FD246D8">PCMP_NOTIFY_ROUTINE</a> callback.</p>


## -syntax

````
typedef struct _CMP_NOTIFY_INFO {
  HANDLE hPlug;
  AV_PCR Pcr;
  PVOID  Context;
} CMP_NOTIFY_INFO, *PCMP_NOTIFY_INFO;
````


## -struct-fields
<dl>

### -field <b>hPlug</b>

<dd>
<p>The handle of a plug for the notification.</p>
</dd>

### -field <b>Pcr</b>

<dd>
<p>A plug control register.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A context.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CMP_NOTIFY_INFO structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
