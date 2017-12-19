---
UID: NS.NDIS._NDIS_RW_LOCK
title: _NDIS_RW_LOCK
author: windows-driver-content
description: The NDIS_RW_LOCK structure defines the attributes of a read/write lock.
old-location: netvista\ndis_rw_lock.htm
old-project: NetVista
ms.assetid: b44e62ec-d36a-46df-846c-3f1cf6cef003
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _NDIS_RW_LOCK, *PNDIS_RW_LOCK, PNDIS_RW_LOCK, NDIS_RW_LOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use NDIS_RW_LOCK_EX instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RW_LOCK
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
---

# _NDIS_RW_LOCK structure



## -description
The <b>NDIS_RW_LOCK</b> structure defines the attributes of a read/write lock. This structure is opaque to
   NDIS drivers.



## -syntax

````
typedef struct _NDIS_RW_LOCK {
  ;      // Reserved for NDIS.
} NDIS_RW_LOCK, *PNDIS_RW_LOCK;
````


## -struct-fields


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use <a href="netvista.ndis_rw_lock_ex">NDIS_RW_LOCK_EX</a> instead.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_rw_lock_ex">NDIS_RW_LOCK_EX</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_RW_LOCK structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

