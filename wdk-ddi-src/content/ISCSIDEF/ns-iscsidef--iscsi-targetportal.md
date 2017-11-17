---
UID: NS.iscsidef._ISCSI_TargetPortal
title: ISCSI_TargetPortal
author: windows-driver-content
description: The ISCSI_TargetPortal structure provides a definition of a target portal.
old-location: storage\iscsi_targetportal.htm
ms.assetid: 1adb1dbf-3ec4-4e32-bfe8-cfcf992f67ca
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsidef.h
req.include-header: Iscsidef.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_TargetPortal
req.alt-loc: iscsidef.h
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
ms.keywords: ISCSI_TargetPortal, ISCSI_TargetPortal, *PISCSI_TargetPortal
req.iface: 
---

# ISCSI_TargetPortal structure



## -description
<p>The ISCSI_TargetPortal structure provides a definition of a target portal. </p>


## -syntax

````
typedef struct _ISCSI_TargetPortal {
  ISCSI_IP_Address Address;
  ULONG            Reserved;
  USHORT           Socket;
} ISCSI_TargetPortal, *PISCSI_TargetPortal;
````


## -struct-fields
<dl>

### -field <b>Address</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561536">ISCSI_IP_Address</a> structure that indicates the IP address of the portal. The ISCSI_IP_Address structure provides a way to define an IP address that is independent of the version of the IP protocol that the initiator and the target use.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for Microsoft use only. </p>
</dd>

### -field <b>Socket</b>

<dd>
<p>Socket number associated with the target.</p>
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
<dt>Iscsidef.h (include Iscsidef.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561536">ISCSI_IP_Address</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561577">ISCSI_TargetPortal WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20ISCSI_TargetPortal structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
