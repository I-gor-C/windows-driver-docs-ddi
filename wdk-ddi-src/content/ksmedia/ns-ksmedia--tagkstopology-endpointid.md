---
UID: NS.ksmedia._tagKSTOPOLOGY_ENDPOINTID
title: tagKSTOPOLOGY_ENDPOINTID
author: windows-driver-content
description: The KSTOPOLOGY_ENDPOINTID structure specifies the name and the pin ID of a topology endpoint.
old-location: audio\kstopology_endpointid.htm
ms.assetid: A84BE3D6-7D2A-4123-979B-F6E1CA8C8B23
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSTOPOLOGY_ENDPOINTID
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
ms.keywords: tagKSTOPOLOGY_ENDPOINTID, KSTOPOLOGY_ENDPOINTID, *PKSTOPOLOGY_ENDPOINTID
req.iface: 
---

# tagKSTOPOLOGY_ENDPOINTID structure



## -description
<p>The <b>KSTOPOLOGY_ENDPOINTID</b> structure specifies the name and the pin ID of a topology endpoint.</p>


## -syntax

````
typedef struct _tagKSTOPOLOGY_ENDPOINTID {
  WCHAR TopologyName[MAX_PATH];
  ULONG PinId;
} KSTOPOLOGY_ENDPOINTID, *PKSTOPOLOGY_ENDPOINTID;
````


## -struct-fields
<dl>

### -field <b>TopologyName</b>

<dd>
<p>The name of the topology endpoint.</p>
</dd>

### -field <b>PinId</b>

<dd>
<p>The pin ID of the topology endpoint.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10 Mobile</p>
</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169887">KSTOPOLOGY_ENDPOINTIDPAIR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSTOPOLOGY_ENDPOINTID structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
