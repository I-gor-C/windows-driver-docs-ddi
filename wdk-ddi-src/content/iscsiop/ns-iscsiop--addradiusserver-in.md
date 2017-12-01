---
UID: NS.iscsiop._AddRADIUSServer_IN
title: AddRADIUSServer_IN
author: windows-driver-content
description: The AddRADIUSServer_IN structure holds the input data for the AddRADIUSServer method, which is used to add a new RADIUS server entry to existing list.
old-location: storage\addradiusserver_in.htm
old-project: storage
ms.assetid: 7b7b9f3b-df33-4886-bd22-23429cb05ea7
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AddRADIUSServer_IN, AddRADIUSServer_IN, *PAddRADIUSServer_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AddRADIUSServer_IN
req.alt-loc: iscsiop.h
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

# AddRADIUSServer_IN structure



## -description
<p>The AddRADIUSServer_IN structure holds the input data for the <a href="storage.addradiusserver">AddRADIUSServer</a> method, which is used to add a new RADIUS server entry to existing list.</p>


## -syntax

````
typedef struct _AddRADIUSServer_IN {
  ISCSI_IP_Address RADIUSIPAddress;
} AddRADIUSServer_IN, *PAddRADIUSServer_IN;
````


## -struct-fields
<dl>

### -field <b>RADIUSIPAddress</b>

<dd>
<p>A <a href="..\iscsidef\ns-iscsidef--iscsi-ip-address.md">ISCSI_IP_Address</a> structure that contains an IP version-independent address of the RADIUS server.</p>
</dd>
</dl>

## -remarks
<p>It is optional that you implement this method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.addradiusserver">AddRADIUSServer</a>
</dt>
<dt>
<a href="..\iscsiop\ns-iscsiop--addradiusserver-out.md">AddRADIUSServer_OUT</a>
</dt>
<dt>
<a href="..\iscsidef\ns-iscsidef--iscsi-ip-address.md">ISCSI_IP_Address</a>
</dt>
<dt>
<a href="storage.msiscsi_operations_wmi_class">MSiSCSI_Operations WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AddRADIUSServer_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
