---
UID: NS.hidpddi._HIDP_COLLECTION_DESC
title: HIDP_COLLECTION_DESC
author: windows-driver-content
description: Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call.
old-location: hid\hidp_collection_desc.htm
old-project: hid
ms.assetid: 4B044635-1088-4CED-87C7-4385E565A54A
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HIDP_COLLECTION_DESC, HIDP_COLLECTION_DESC, *PHIDP_COLLECTION_DESC
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
req.alt-api: HIDP_COLLECTION_DESC
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

# HIDP_COLLECTION_DESC structure



## -description
<p>Contains the information of a top-level-collection. This structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt740164">HidP_GetCollectionDescription</a> call.</p>


## -syntax

````
typedef struct _HIDP_COLLECTION_DESC {
  USAGE                             UsagePage;
  USAGE                             Usage;
  UCHAR                             CollectionNumber;
  UCHAR                             Reserved[15];
  USHORT                            InputLength;
  USHORT                            OutputLength;
  USHORT                            FeatureLength;
  USHORT                            PreparsedDataLength;
  PHIDP_PREPARSED_DATA              PreparsedData;
} HIDP_COLLECTION_DESC, *PHIDP_COLLECTION_DESC;
````


## -struct-fields
<dl>

### -field <b>UsagePage</b>

<dd>
<p>Specifies the usage page of the usage ID specified by <b>Usage</b>.</p>
</dd>

### -field <b>Usage</b>

<dd>
<p>Indicates a usage ID.</p>
</dd>

### -field <b>CollectionNumber</b>

<dd>
<p>The index of the collection in the array of  <b>HIDP_COLLECTION_DESC</b> structure. This is a 1-based value.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for internal system use. Must be 0.</p>
</dd>

### -field <b>InputLength</b>

<dd>
<p>The maximum length of an input report of this collection.</p>
</dd>

### -field <b>OutputLength</b>

<dd>
<p>The maximum length of an output report of this collection.</p>
</dd>

### -field <b>FeatureLength</b>

<dd>
<p>The maximum length of a feature report of this collection.</p>
</dd>

### -field <b>PreparsedDataLength</b>

<dd>
<p>The length of the preparsed data pointed to by <i>PreparsedData</i>.</p>
</dd>

### -field <b>PreparsedData</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543586">_HIDP_PREPARSED_DATA</a> structure that contains a top-level collection's preparsed data.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDP_COLLECTION_DESC structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
