---
UID: NS.ksmedia.PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM
title: PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM
author: windows-driver-content
description: This structure contains a custom item.
old-location: stream\kscamera_perframesetting_custom_item.htm
old-project: stream
ms.assetid: 7BB23F25-6E39-40B3-A158-5EE69370B1FD
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM, KSCAMERA_PERFRAMESETTING_CUSTOM_ITEM, *PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM
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
req.alt-api: KSCAMERA_PERFRAMESETTING_CUSTOM_ITEM
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

# PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM structure



## -description
<p>This structure contains a custom item.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Reserved;
  GUID  Id;
} KSCAMERA_PERFRAMESETTING_CUSTOM_ITEM, *PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this header and custom data that follows.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Id</b>

<dd>
<p>A GUID that identifies the custom item.</p>
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