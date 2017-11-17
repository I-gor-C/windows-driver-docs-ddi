---
UID: NS.61883._CIP_ATTACH_FRAME
title: CIP_ATTACH_FRAME
author: windows-driver-content
description: This structure is used in an attach frame request.
old-location: ieee\cip_attach_frame.htm
ms.assetid: F7E283BB-B714-4CD4-AFF4-EFB62D82791D
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
req.alt-api: CIP_ATTACH_FRAME
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
ms.keywords: CIP_ATTACH_FRAME, CIP_ATTACH_FRAME, *PCIP_ATTACH_FRAME
---

# CIP_ATTACH_FRAME structure



## -description
<p>This structure is used in an attach frame request.</p>


## -syntax

````
typedef struct _CIP_ATTACH_FRAME {
  HANDLE     hConnect;
  ULONG      FrameLength;
  ULONG      SourceLength;
  PCIP_FRAME Frame;
} CIP_ATTACH_FRAME, *PCIP_ATTACH_FRAME;
````


## -struct-fields
<dl>

### -field <b><b>hConnect</b></b>

<dd>
<p>A handle to the connection.</p>
</dd>

### -field <b><b>FrameLength</b></b>

<dd>
<p>The length of the frame in bytes. The total frame length must be evenly divisible by the value in <b>SourceLength</b>.</p>
</dd>

### -field <b><b>SourceLength</b></b>

<dd>
<p>The length of the source packets, in bytes. The source length must be evenly divisible into the frame length.</p>
</dd>

### -field <b><b>Frame</b></b>

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537045">CIP_FRAME</a> structure that contains information about the frame and a data buffer to be sent or filled.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CIP_ATTACH_FRAME structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
