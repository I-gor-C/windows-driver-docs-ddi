---
UID: NS.ksmedia.PMEDIUM_INFO
title: PMEDIUM_INFO
author: windows-driver-content
description: The MEDIUM_INFO structure describes the media loaded into an external device.
old-location: stream\medium_info.htm
old-project: stream
ms.assetid: 1dd7415d-bfbc-4dea-bac9-bc5b8531a47f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PMEDIUM_INFO, MEDIUM_INFO, *PMEDIUM_INFO
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
req.alt-api: MEDIUM_INFO
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

# PMEDIUM_INFO structure



## -description
<p>The MEDIUM_INFO structure describes the media loaded into an external device.</p>


## -syntax

````
typedef struct {
  BOOL  MediaPresent;
  ULONG MediaType;
  BOOL  RecordInhibit;
} MEDIUM_INFO, *PMEDIUM_INFO;
````


## -struct-fields
<dl>

### -field <b>MediaPresent</b>

<dd>
<p>Specifies if media is present in the external device. <b>TRUE</b> if media is loaded, <b>FALSE</b> otherwise.</p>
</dd>

### -field <b>MediaType</b>

<dd>
<p>Indicates the type of the media loaded in an external device.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_MEDIA_DVC</p>
</td>
<td>
<p>Digital video cassette. For example MiniDV</p>
</td>
</tr>
<tr>
<td>
<p>ED_MEDIA_VHS</p>
</td>
<td>
<p>VHS cassette</p>
</td>
</tr>
<tr>
<td>
<p>ED_MEDIA_HI8</p>
</td>
<td>
<p>Hi-8 cassette</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>RecordInhibit</b>

<dd>
<p>Specifies if recording is inhibited on the media. <b>TRUE</b> if recording onto the media is inhibited, <b>FALSE</b> otherwise.</p>
</dd>
</dl>

## -remarks
<p>Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.</p>

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