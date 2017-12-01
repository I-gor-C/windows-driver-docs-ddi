---
UID: NS.ndis._NDIS_RW_LOCK_EX~r2
title: NDIS_RW_LOCK_EX
author: windows-driver-content
description: The NDIS_RW_LOCK_EX structure defines the attributes of a read/write lock.
old-location: netvista\ndis_rw_lock_ex.htm
old-project: netvista
ms.assetid: e6454020-a5f6-4380-93eb-dd1f3e350d47
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_RW_LOCK_EX,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RW_LOCK_EX
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
req.iface: 
---

# NDIS_RW_LOCK_EX structure



## -description
<p>The <b>NDIS_RW_LOCK_EX</b> structure defines the attributes of a read/write lock. This structure is opaque to
   NDIS drivers.
   </p>


## -syntax

````
typedef struct _NDIS_RW_LOCK_EX {
  ;      // Reserved for NDIS.
} NDIS_RW_LOCK_EX, *PNDIS_RW_LOCK_EX;
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
<p>Supported in NDIS 6.20 and later.</p>
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

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--ndis-rw-lock.md">NDIS_RW_LOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RW_LOCK_EX structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
