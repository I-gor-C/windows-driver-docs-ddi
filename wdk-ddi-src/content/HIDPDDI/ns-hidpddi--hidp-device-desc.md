---
UID: NS.hidpddi._HIDP_DEVICE_DESC
title: HIDP_DEVICE_DESC
author: windows-driver-content
description: Contains the device description block filled in collection descriptions as linked lists. This structure is used by HidP_GetCollectionDescription.
old-location: hid\hidp_device_desc.htm
ms.assetid: C51D645B-5DF2-4F23-904B-AB56F97520CB
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: hid
req.header: hidpddi.h
req.include-header: Hidpddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HIDP_DEVICE_DESC
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
ms.keywords: HIDP_DEVICE_DESC, HIDP_DEVICE_DESC, *PHIDP_DEVICE_DESC
req.iface: 
---

# HIDP_DEVICE_DESC structure



## -description
<p>Contains the device description block filled in
                         collection descriptions as linked lists. This structure is used by <a href="https://msdn.microsoft.com/library/windows/hardware/mt740164">HidP_GetCollectionDescription</a>.</p>


## -syntax

````
typedef struct _HIDP_DEVICE_DESC {
  PHIDP_COLLECTION_DESC     CollectionDesc;
  ULONG                     CollectionDescLength;
  PHIDP_REPORT_IDS          ReportIDs;
  ULONG                     ReportIDsLength;
  HIDP_GETCOLDESC_DBG       Dbg;
} HIDP_DEVICE_DESC, *PHIDP_DEVICE_DESC;
````


## -struct-fields
<dl>

### -field <b>CollectionDesc</b>

<dd>
<p>An array of  <a href="https://msdn.microsoft.com/library/windows/hardware/mt740161">HIDP_COLLECTION_DESC</a> structure that contains the collection descriptors.</p>
</dd>

### -field <b>CollectionDescLength</b>

<dd>
<p>The number of elements in the array of the collection descriptors.</p>
</dd>

### -field <b>ReportIDs</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt740165">HIDP_REPORT_IDS</a> structures report ID information for a report descriptor. 
</p>
</dd>

### -field <b>ReportIDsLength</b>

<dd>
<p>The number of elements in the length of the array of report IDs.</p>
</dd>

### -field <b>Dbg</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt740163">HIDP_GETCOLDESC_DBG</a> structure that contains the error code indicating the failure in parsing the report 
                                      descriptor.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDP_DEVICE_DESC structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
