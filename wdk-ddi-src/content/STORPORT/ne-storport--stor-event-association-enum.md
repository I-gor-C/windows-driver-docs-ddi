---
UID: NE.storport._STOR_EVENT_ASSOCIATION_ENUM
title: STOR_EVENT_ASSOCIATION_ENUM
author: windows-driver-content
description: The STOR_EVENT_ASSOCIATION_ENUM enumerator specifies the type of device that is associated with an event.
old-location: storage\stor_event_association_enum.htm
ms.assetid: 2e0672b6-e692-43c8-8a20-7947c854c4c9
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STOR_EVENT_ASSOCIATION_ENUM
req.alt-loc: storport.h
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
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
req.iface: 
req.product: Windows 10 or later.
---

# STOR_EVENT_ASSOCIATION_ENUM enumeration



## -description
<p>The STOR_EVENT_ASSOCIATION_ENUM enumerator specifies the type of device that is associated with an event.</p>


## -syntax

````
typedef enum _STOR_EVENT_ASSOCIATION_ENUM { 
  StorEventAdapterAssociation  = 0,
  StorEventLunAssociation      = 1,
  StorEventTargetAssociation   = 2,
  StorEventInvalidAssociation  = 3
} STOR_EVENT_ASSOCIATION_ENUM;
````


## -enum-fields
<dl>

### -field <a id="StorEventAdapterAssociation"></a><a id="storeventadapterassociation"></a><a id="STOREVENTADAPTERASSOCIATION"></a><b>StorEventAdapterAssociation</b>

<dd>
<p>The event is associated with the adapter.</p>
</dd>

### -field <a id="StorEventLunAssociation"></a><a id="storeventlunassociation"></a><a id="STOREVENTLUNASSOCIATION"></a><b>StorEventLunAssociation</b>

<dd>
<p>The event is associated with the LUN.</p>
</dd>

### -field <a id="StorEventTargetAssociation"></a><a id="storeventtargetassociation"></a><a id="STOREVENTTARGETASSOCIATION"></a><b>StorEventTargetAssociation</b>

<dd>
<p>The event is associated with the target.</p>
</dd>

### -field <a id="StorEventInvalidAssociation"></a><a id="storeventinvalidassociation"></a><a id="STOREVENTINVALIDASSOCIATION"></a><b>StorEventInvalidAssociation</b>

<dd>
<p>Marks end of valid enumeration range</p>
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
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>