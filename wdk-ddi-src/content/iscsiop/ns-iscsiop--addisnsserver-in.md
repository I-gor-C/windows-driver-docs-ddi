---
UID: NS.iscsiop._AddiSNSServer_IN
title: AddiSNSServer_IN
author: windows-driver-content
description: The AddiSNSServer_IN structure holds the input data for the user-mode AddISNSServer method, which is used to add a new iSNS server entry to the list of iSNS server names that the initiator maintains.
old-location: storage\addisnsserver_in.htm
old-project: storage
ms.assetid: 5d05eeeb-ab68-4770-88c1-483c56dbc116
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AddiSNSServer_IN, AddiSNSServer_IN, *PAddiSNSServer_IN
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
req.alt-api: AddiSNSServer_IN
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

# AddiSNSServer_IN structure



## -description
<p>The AddiSNSServer_IN structure holds the input data for the user-mode <b>AddISNSServer</b> method, which is used to add a new iSNS server entry to the list of iSNS server names that the initiator maintains.</p>


## -syntax

````
typedef struct _AddiSNSServer_IN {
  WCHAR iSNSServerName[223 + 1];
} AddiSNSServer_IN, *PAddiSNSServer_IN;
````


## -struct-fields
<dl>

### -field iSNSServerName

<dd>
<p>The iSNS server name to add to the list of iSNS servers that the iSCSI initiator maintains.</p>
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
<a href="..\iscsiop\ns-iscsiop--addisnsserver-out.md">AddiSNSServer_OUT</a>
</dt>
<dt>
<a href="storage.msiscsi_operations_wmi_class">MSiSCSI_Operations WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AddiSNSServer_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
