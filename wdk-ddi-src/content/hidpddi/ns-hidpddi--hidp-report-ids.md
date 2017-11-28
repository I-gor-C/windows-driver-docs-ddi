---
UID: NS.hidpddi._HIDP_REPORT_IDS
title: HIDP_REPORT_IDS
author: windows-driver-content
description: Contains report ID information for a top-level collection.
old-location: hid\hidp_report_ids.htm
old-project: hid
ms.assetid: C88B77C3-01CB-4E8C-83A4-EB9AFB122327
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HIDP_REPORT_IDS, HIDP_REPORT_IDS, *PHIDP_REPORT_IDS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidpddi.h
req.include-header: Hidpddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HIDP_REPORT_IDS
req.alt-loc: Hidpddi.h
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
req.iface: 
---

# HIDP_REPORT_IDS structure



## -description
<p>Contains report ID information for a top-level collection. 
</p>


## -syntax

````
typedef struct _HIDP_REPORT_IDS {
  UCHAR               ReportID;
  UCHAR               CollectionNumber;
  USHORT              InputLength;
  USHORT              OutputLength;
  USHORT              FeatureLength;
} HIDP_REPORT_IDS, *PHIDP_REPORT_IDS;
````


## -struct-fields
<dl>

### -field <b>ReportID</b>

<dd>
<p>The report ID of the top-level collection.</p>
</dd>

### -field <b>CollectionNumber</b>

<dd>
<p>The index of the collection in the array of  <a href="https://msdn.microsoft.com/library/windows/hardware/mt740161">HIDP_COLLECTION_DESC</a> structure.</p>
</dd>

### -field <b>InputLength</b>

<dd>
<p>The length of an input report of this report ID. </p>
</dd>

### -field <b>OutputLength</b>

<dd>
<p>The length of an output report of this report ID. An input report, an output report, and a feature report can use the same report.</p>
</dd>

### -field <b>FeatureLength</b>

<dd>
<p>The length of a feature report of this report ID.</p>
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
<dt>Hidpddi.h (include Hidpddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt740164">HidP_GetCollectionDescription</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDP_REPORT_IDS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
