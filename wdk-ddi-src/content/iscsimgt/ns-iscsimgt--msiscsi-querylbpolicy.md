---
UID: NS.iscsimgt._MSiSCSI_QueryLBPolicy
title: MSiSCSI_QueryLBPolicy
author: windows-driver-content
description: This MSiSCSI_QueryLBPolicy method returns the MCS load balancing policy for each information if any that has been set across different iSCSI session.
old-location: storage\msiscsi_querylbpolicy.htm
old-project: storage
ms.assetid: da45810a-12f2-4242-8428-a1717ecf8af3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MSiSCSI_QueryLBPolicy, MSiSCSI_QueryLBPolicy, *PMSiSCSI_QueryLBPolicy
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
req.alt-api: MSiSCSI_QueryLBPolicy
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

# MSiSCSI_QueryLBPolicy structure



## -description
<p>This MSiSCSI_QueryLBPolicy method returns the MCS load balancing policy for each information if any that has been set across different iSCSI session.</p>


## -syntax

````
typedef struct _MSiSCSI_QueryLBPolicy {
  ULONGLONG                   UniqueAdapterId;
  ULONG                       Reserved;
  ULONG                       SessionCount;
  ISCSI_Supported_LB_Policies LoadBalancePolicies[1];
} MSiSCSI_QueryLBPolicy, *PMSiSCSI_QueryLBPolicy;
````


## -struct-fields
<dl>

### -field <b>UniqueAdapterId</b>

<dd>
<p>This is a unique connection identifier that the initiator uses to identify a connection. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff561599">LoginToTarget</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550121">AddConnectionToSession</a> methods both return this value in the UniqueConnectionId parameter.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for Microsoft use only.</p>
</dd>

### -field <b>SessionCount</b>

<dd>
<p>This specifies the number of active sessions for this adapater ID.</p>
</dd>

### -field <b>LoadBalancePolicies</b>

<dd>
<p>This is an enumeration that contains information required to set the load balance policy. For more information about how to set the load balance policy, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561570">ISCSI_Supported_LB_Policies</a>. There will be as many of these structures as the number of sessions available for this adapter.</p>
</dd>
</dl>

## -remarks
<p>You must implement this class only if the adapter supports MCS. Otherwise, it is optional.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550121">AddConnectionToSession</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561570">ISCSI_Supported_LB_Policies</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561599">LoginToTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSiSCSI_QueryLBPolicy structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
