---
UID: NS.ksmedia.tagKS_AMVPDIMINFO
title: tagKS_AMVPDIMINFO
author: windows-driver-content
description: The KS_AMVPDIMINFO structure is used to describe the dimensions of a video port.
old-location: stream\ks_amvpdiminfo.htm
old-project: stream
ms.assetid: 5b8126ee-ba47-4eaf-887a-764e17a20e03
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKS_AMVPDIMINFO, KS_AMVPDIMINFO, *PKS_AMVPDIMINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_AMVPDIMINFO
req.alt-loc: ksmedia.h
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

# tagKS_AMVPDIMINFO structure



## -description
<p>The KS_AMVPDIMINFO structure is used to describe the dimensions of a video port.</p>


## -syntax

````
typedef struct tagKS_AMVPDIMINFO {
  DWORD dwFieldWidth;
  DWORD dwFieldHeight;
  DWORD dwVBIWidth;
  DWORD dwVBIHeight;
  RECT  rcValidRegion;
} KS_AMVPDIMINFO, *PKS_AMVPDIMINFO;
````


## -struct-fields
<dl>

### -field dwFieldWidth

<dd>
<p>Specifies the field width.</p>
</dd>

### -field dwFieldHeight

<dd>
<p>Specifies the field height.</p>
</dd>

### -field dwVBIWidth

<dd>
<p>Specifies the VBI data width.</p>
</dd>

### -field dwVBIHeight

<dd>
<p>Specifies the VBI data height.</p>
</dd>

### -field rcValidRegion

<dd>
<p>Describes a valid rectangle for data cropping.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="stream.ks_amvpdatainfo">KS_AMVPDATAINFO</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ks_amvpdatainfo">KS_AMVPDATAINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_AMVPDIMINFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
