---
UID: NS.ksmedia._KS_DVDCOPY_REGION
title: KS_DVDCOPY_REGION
author: windows-driver-content
description: The KS_DVDCOPY_REGION structure is used to describe the copy control region according to language restrictions.
old-location: stream\ks_dvdcopy_region.htm
ms.assetid: 159a8dd0-6efa-4f2c-921c-c427e1cf59ec
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_DVDCOPY_REGION
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
ms.keywords: KS_DVDCOPY_REGION, KS_DVDCOPY_REGION, *PKS_DVDCOPY_REGION
req.iface: 
---

# KS_DVDCOPY_REGION structure



## -description
<p>The KS_DVDCOPY_REGION structure is used to describe the copy control region according to language restrictions.</p>


## -syntax

````
typedef struct _KS_DVDCOPY_REGION {
  UCHAR Reserved;
  UCHAR RegionData;
  UCHAR Reserved2[2];
} KS_DVDCOPY_REGION, *PKS_DVDCOPY_REGION;
````


## -struct-fields
<dl>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>RegionData</b>

<dd>
<p>Specifies the region code for the nationality or language, as described in the following table:</p>
<table>
<tr>
<th>Numeric Code</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>North America</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Japan, European Union, Middle East, Egypt, South Africa and Greenland</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>Southeast Asia (including Hong Kong SAR)</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>Central/South America, Australia, New Zealand and the Caribbean</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p>Africa, Northwest Asia (including Korea)</p>
</td>
</tr>
<tr>
<td>
<p>6</p>
</td>
<td>
<p>China</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>The KS_DVDCOPY_REGION structure is used by the KSPROPERTY_DVDCOPY_REGION property.</p>

<p>For more information, see <a href="NULL">DVD Copyright Protection</a> and <a href="NULL">DVD Regionalization</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565146">KSPROPERTY_DVDCOPY_REGION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DVDCOPY_REGION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
