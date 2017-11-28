---
UID: NS.iscsimgt._MSiSCSI_RedirectPortalInfoClass
title: MSiSCSI_RedirectPortalInfoClass
author: windows-driver-content
description: The MSiSCSI_RedirectPortalInfoClass structure contains information about a collection of sessions for an adapter ID. It also contains the portal redirection information for each of the sessions.
old-location: storage\msiscsi_redirectportalinfoclass.htm
old-project: storage
ms.assetid: fcddf029-748b-4300-9f87-a103d961918a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MSiSCSI_RedirectPortalInfoClass, MSiSCSI_RedirectPortalInfoClass, *PMSiSCSI_RedirectPortalInfoClass
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
req.alt-api: MSiSCSI_RedirectPortalInfoClass
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

# MSiSCSI_RedirectPortalInfoClass structure



## -description
<p>The MSiSCSI_RedirectPortalInfoClass structure contains information about a collection of sessions for an adapter ID. It also contains the portal redirection information for each of the sessions.</p>


## -syntax

````
typedef struct _MSiSCSI_RedirectPortalInfoClass {
  ULONGLONG                 UniqueAdapterId;
  ULONG                     SessionCount;
  ISCSI_RedirectSessionInfo RedirectSessionList[1];
} MSiSCSI_RedirectPortalInfoClass, *PMSiSCSI_RedirectPortalInfoClass;
````


## -struct-fields
<dl>

### -field <b>UniqueAdapterId</b>

<dd>
<p>A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID).</p>
</dd>

### -field <b>SessionCount</b>

<dd>
<p>The number of sessions for which this structure contains information.</p>
</dd>

### -field <b>RedirectSessionList</b>

<dd>
<p>An array of structures that contains as many ISCSI_RedirectSessionInfo structures as specified in the connection count.</p>
</dd>
</dl>

## -remarks
<p>You must implement this class if the adapter supports target portal hopping. Otherwise, it is optional.</p>

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