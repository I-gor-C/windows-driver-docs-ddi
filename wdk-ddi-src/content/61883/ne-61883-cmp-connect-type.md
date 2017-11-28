---
UID: NE.61883.CMP_CONNECT_TYPE
title: CMP_CONNECT_TYPE
author: windows-driver-content
description: This enumeration specifies a connection type.
old-location: ieee\cmp_connect_type.htm
old-project: IEEE
ms.assetid: 8C206071-2616-4BFB-B7CA-E872CC8D5405
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: TOPOLOGY_MAP, TOPOLOGY_MAP, *PTOPOLOGY_MAP
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CMP_CONNECT_TYPE
req.alt-loc: 61883.h
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
---

# CMP_CONNECT_TYPE enumeration



## -description
<p>This enumeration specifies a connection type. </p>


## -syntax

````
typedef enum  { 
  CMP_Broadcast     = 0,
  CMP_PointToPoint
} CMP_CONNECT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="CMP_Broadcast"></a><a id="cmp_broadcast"></a><a id="CMP_BROADCAST"></a><b>CMP_Broadcast</b>

<dd>
<p>Indicates that this is a broadcast connection.</p>
</dd>

### -field <a id="CMP_PointToPoint"></a><a id="cmp_pointtopoint"></a><a id="CMP_POINTTOPOINT"></a><b>CMP_PointToPoint</b>

<dd>
<p>Indicates that this is a point-to-point connection.</p>
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
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CMP_CONNECT_TYPE enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
