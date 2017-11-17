---
UID: NS.61883._CIP_VALIDATE_INFO
title: CIP_VALIDATE_INFO
author: windows-driver-content
description: The CIP_VALIDATE_INFO structure contains information about the frame.
old-location: ieee\cip_validate_info.htm
ms.assetid: 98993973-91a4-456a-9343-c744408055ed
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 61883.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CIP_VALIDATE_INFO
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
ms.keywords: CIP_VALIDATE_INFO, CIP_VALIDATE_INFO, *PCIP_VALIDATE_INFO
---

# CIP_VALIDATE_INFO structure



## -description
<p>The CIP_VALIDATE_INFO structure contains information about the frame. </p>


## -syntax

````
typedef struct _CIP_VALIDATE_INFO {
  HANDLE     hConnect;
  PVOID      Context;
  CYCLE_TIME TimeStamp;
  PUCHAR     Packet;
} CIP_VALIDATE_INFO, *PCIP_VALIDATE_INFO;
````


## -struct-fields
<dl>

### -field <b>hConnect</b>

<dd>
<p>A handle to the connection.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Points to the context provided by the caller at <b>ValidateContext</b> in the input CIP_FRAME structure.</p>
</dd>

### -field <b>TimeStamp</b>

<dd>
<p>The timestamp of the current source packet.</p>
</dd>

### -field <b>Packet</b>

<dd>
<p>The packet offset for the current source packet.</p>
</dd>
</dl>

## -remarks
<p>The IEC-61883 protocol driver allocates and initializes this structure from the input CIP_FRAME structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h (include 61883.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537045">CIP_FRAME</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CIP_VALIDATE_INFO structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
