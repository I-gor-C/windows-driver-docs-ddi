---
UID: NS.ksmedia._KS_DVDCOPY_TITLEKEY
title: KS_DVDCOPY_TITLEKEY
author: windows-driver-content
description: The KS_DVDCOPY_TITLEKEY structure is used to describe the title key information for the DVD copyright protection authentication process.
old-location: stream\ks_dvdcopy_titlekey.htm
old-project: stream
ms.assetid: 8f85bc55-d05b-4075-9ae5-ba5a5516eeb4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KS_DVDCOPY_TITLEKEY, KS_DVDCOPY_TITLEKEY, *PKS_DVDCOPY_TITLEKEY
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
req.alt-api: KS_DVDCOPY_TITLEKEY
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

# KS_DVDCOPY_TITLEKEY structure



## -description
<p>The KS_DVDCOPY_TITLEKEY structure is used to describe the title key information for the DVD copyright protection authentication process.</p>


## -syntax

````
typedef struct _KS_DVDCOPY_TITLEKEY {
  ULONG KeyFlags;
  ULONG ReservedNT[2];
  UCHAR TitleKey[6];
  UCHAR Reserved[2];
} KS_DVDCOPY_TITLEKEY, *PKS_DVDCOPY_TITLEKEY;
````


## -struct-fields
<dl>

### -field <b>KeyFlags</b>

<dd>
<p>Title key flags settings that provide Copyrighted Material flag (CPM), Copy Guard Management System (CGMS) and Copyright Protection System (CP_SEC) copyright protection flags from the DVD drive. The following CGMS flags are defined:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KS_DVD_CGMS_RESERVED_MASK</p>
</td>
<td>
<p>Specifies the mask of all defined CPM, CGMS and CP_SEC flags (that is, all the other flags listed here).</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_CGMS_COPY_PROTECT_MASK</p>
</td>
<td>
<p>Specifies the mask of all defined CGMS flags.</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_CGMS_COPY_PERMITTED</p>
</td>
<td>
<p>Indicates that the content protected by CGMS can be copied.</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_CGMS_COPY_ONCE</p>
</td>
<td>
<p>Indicates that the content protected by CGMS can be copied only a single time. As part of the copy process, this flag should be cleared, and the KS_DVD_CGMS_NO_COPY flags must be set to prevent subsequent copying.</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_CGMS_NO_COPY</p>
</td>
<td>
<p>Indicates that the content protected by CGMS cannot be copied.</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_COPYRIGHT_MASK</p>
</td>
<td>
<p>Specifies the mask of all defined CPM flags (KS_DVD_NOT_COPYRIGHTED and KS_DVD_COPYRIGHTED).</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_NOT_COPYRIGHTED</p>
</td>
<td>
<p>Indicates that the content marked by CPM is not copyrighted.</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_COPYRIGHTED</p>
</td>
<td>
<p>Indicates that the content marked by CPM is copyrighted.</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_SECTOR_PROTECT_MASK</p>
</td>
<td>
<p>The mask of all defined sector protection flags.</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_SECTOR_NOT_PROTECTED</p>
</td>
<td>
<p>Indicates that the sector is not protected (encrypted).</p>
</td>
</tr>
<tr>
<td>
<p>KS_DVD_SECTOR_PROTECTED</p>
</td>
<td>
<p>Indicates that the sector is protected (encrypted).</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ReservedNT</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>TitleKey</b>

<dd>
<p>Specifies the current title key.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>The KS_DVDCOPY_TITLEKEY structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565148">KSPROPERTY_DVDCOPY_TITLE_KEY</a> property.</p>

<p>For more information, see <a href="NULL">DVD Copyright Protection</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565148">KSPROPERTY_DVDCOPY_TITLE_KEY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DVDCOPY_TITLEKEY structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
