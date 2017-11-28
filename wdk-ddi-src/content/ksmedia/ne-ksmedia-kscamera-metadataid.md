---
UID: NE.ksmedia.KSCAMERA_MetadataId
title: KSCAMERA_MetadataId
author: windows-driver-content
description: This enumeration contains identifiers for a metadata item.
old-location: stream\kscamera_metadataid.htm
old-project: stream
ms.assetid: 1CD1D065-9A96-42D5-807E-B439B4273920
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_MetadataId
req.alt-loc: Ksmedia.h
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

# KSCAMERA_MetadataId enumeration



## -description
<p>This enumeration contains identifiers for a metadata item.</p>


## -syntax

````
typedef enum  { 
  MetadataId_Standard_Start     = 1,
  MetadataId_PhotoConfirmation  = MetadataId_Standard_Start,
  MetadataId_Standard_End       = MetadataId_PhotoConfirmation,
  MetadataId_Custom_Start       = 0x80000000
} KSCAMERA_MetadataId;
````


## -enum-fields
<dl>

### -field <a id="MetadataId_Standard_Start"></a><a id="metadataid_standard_start"></a><a id="METADATAID_STANDARD_START"></a><b>MetadataId_Standard_Start</b>

<dd>
<p>This represent the standard start metadata ID.</p>
</dd>

### -field <a id="MetadataId_PhotoConfirmation"></a><a id="metadataid_photoconfirmation"></a><a id="METADATAID_PHOTOCONFIRMATION"></a><b>MetadataId_PhotoConfirmation</b>

<dd>
<p>This represents the photo confirmation metadata ID</p>
</dd>

### -field <a id="MetadataId_Standard_End"></a><a id="metadataid_standard_end"></a><a id="METADATAID_STANDARD_END"></a><b>MetadataId_Standard_End</b>

<dd>
<p>This represent the standard end  metadata ID.</p>
</dd>

### -field <a id="MetadataId_Custom_Start"></a><a id="metadataid_custom_start"></a><a id="METADATAID_CUSTOM_START"></a><b>MetadataId_Custom_Start</b>

<dd>
<p>This represents the lowest acceptable custom metadata ID.</p>
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
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>