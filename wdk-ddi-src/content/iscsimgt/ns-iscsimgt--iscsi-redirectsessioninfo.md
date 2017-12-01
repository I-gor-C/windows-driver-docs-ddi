---
UID: NS.iscsimgt._ISCSI_RedirectSessionInfo
title: ISCSI_RedirectSessionInfo
author: windows-driver-content
description: This ISCSI_RedirectSessionInfo structure contains information about an iSCSI session and its portal information resulted from iSCSI target redirection.
old-location: storage\iscsi_redirectsessioninfo.htm
old-project: storage
ms.assetid: e3980ac7-b539-4a8f-9869-14d418ebe1e7
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ISCSI_RedirectSessionInfo, ISCSI_RedirectSessionInfo, *PISCSI_RedirectSessionInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsimgt.h
req.include-header: Iscsimgt.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_RedirectSessionInfo
req.alt-loc: iscsimgt.h
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

# ISCSI_RedirectSessionInfo structure



## -description
<p>This ISCSI_RedirectSessionInfo structure contains information about an iSCSI session and its portal information resulted from iSCSI target redirection.</p>


## -syntax

````
typedef struct _ISCSI_RedirectSessionInfo {
  ULONGLONG                UniqueSessionId;
  ULONG                    TargetPortalGroupTag;
  ULONG                    ConnectionCount;
  ISCSI_RedirectPortalInfo RedirectPortalList[1];
} ISCSI_RedirectSessionInfo, *PISCSI_RedirectSessionInfo;
````


## -struct-fields
<dl>

### -field <b>UniqueSessionId</b>

<dd>
<p>A 64-bit integer that uniquely identifies the session. The <a href="storage.logintotarget">LoginToTarget</a> and <a href="storage.addconnectiontosession">AddConnectionToSession</a> methods both return this value in their UniqueSessionId parameter. Do not confuse this value with the values in the ISID and TSID members.</p>
</dd>

### -field <b>TargetPortalGroupTag</b>

<dd>
<p>Target portal group tag for this session Id.</p>
</dd>

### -field <b>ConnectionCount</b>

<dd>
<p>Number of connections for each session.</p>
</dd>

### -field <b>RedirectPortalList</b>

<dd>
<p>This provides the redirection information, and it has as many entries as the number of connections for each session.</p>
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
<dt>Iscsimgt.h (include Iscsimgt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.addconnectiontosession">AddConnectionToSession</a>
</dt>
<dt>
<a href="storage.logintotarget">LoginToTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ISCSI_RedirectSessionInfo structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
