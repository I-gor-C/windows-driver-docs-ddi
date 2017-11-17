---
UID: NS.ndis._NDIS_RW_LOCK_REFCOUNT
title: NDIS_RW_LOCK_REFCOUNT
author: windows-driver-content
description: The NDIS_RW_LOCK_REFCOUNT union defines attributes of a read/write lock.
old-location: netvista\ndis_rw_lock_refcount.htm
ms.assetid: 1b2c93dd-a80e-4197-bc4f-cad12f6d6c77
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Obsolete in NDIS 6.20 and later. Supported for NDIS 6.0 and NDIS 5.1 in
   Windows Vista and Windows 7. Supported for NDIS 5.1 drivers in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RW_LOCK_REFCOUNT
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
ms.keywords: NDIS_RW_LOCK_REFCOUNT, NDIS_RW_LOCK_REFCOUNT
req.iface: 
---

# NDIS_RW_LOCK_REFCOUNT structure



## -description
<p>The <b>NDIS_RW_LOCK_REFCOUNT</b> union defines attributes of a read/write lock. This union is opaque to NDIS
   drivers.
   </p>


## -syntax

````
typedef union _NDIS_RW_LOCK_REFCOUNT {
  ;      // Reserved for NDIS.
} NDIS_RW_LOCK_REFCOUNT;
````


## -struct-fields


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Obsolete in NDIS 6.20 and later. Supported for NDIS 6.0 and NDIS 5.1 in
   Windows Vista and Windows 7. Supported for NDIS 5.1 drivers in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>