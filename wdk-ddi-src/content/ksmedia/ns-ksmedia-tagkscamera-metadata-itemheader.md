---
UID: NS.ksmedia.tagKSCAMERA_METADATA_ITEMHEADER
title: tagKSCAMERA_METADATA_ITEMHEADER
author: windows-driver-content
description: This structure contains the metadata header information that is filled by the camera driver.
old-location: stream\kscamera_metadata_itemheader.htm
old-project: stream
ms.assetid: B4AC04D7-9F98-41F1-A38D-927F3F3A7699
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagKSCAMERA_METADATA_ITEMHEADER, KSCAMERA_METADATA_ITEMHEADER, *PKSCAMERA_METADATA_ITEMHEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_METADATA_ITEMHEADER
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

# tagKSCAMERA_METADATA_ITEMHEADER structure



## -description
<p>This structure contains the metadata header information that is filled by the camera driver.</p>


## -syntax

````
typedef struct tagKSCAMERA_METADATA_ITEMHEADER {
  ULONG MetadataId;
  ULONG Size;
} KSCAMERA_METADATA_ITEMHEADER, *PKSCAMERA_METADATA_ITEMHEADER;
````


## -struct-fields
<dl>

### -field <b>MetadataId</b>

<dd>
<p>The identifier for the metadata item. This can be a standard identifier as defined in the <a href="..\ksmedia\ne-ksmedia-kscamera-metadataid.md">KSCAMERA_MetadataId</a> enumeration or any custom metadata identifier that starts from MetadataId_Custom_Start (0x80000000).</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Set to <b>sizeof(KSCAMERA_METADATA_ITEMHEADER)</b> + the size of the metadata payload that follows.</p>
</dd>
</dl>

## -remarks
<p>This structure along with the metadata payload that follows must be 8-byte aligned.</p>

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