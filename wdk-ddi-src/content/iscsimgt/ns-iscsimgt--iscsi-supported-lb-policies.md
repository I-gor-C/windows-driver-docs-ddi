---
UID: NS.iscsimgt._ISCSI_Supported_LB_Policies
title: ISCSI_Supported_LB_Policies
author: windows-driver-content
description: The ISCSI_Supported_LB_Policies structure contains information about load balancing policies for multiple connections per session (MCS).
old-location: storage\iscsi_supported_lb_policies.htm
old-project: storage
ms.assetid: 053b9f14-7319-4599-886e-3c03c717b348
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ISCSI_Supported_LB_Policies, ISCSI_Supported_LB_Policies, *PISCSI_Supported_LB_Policies
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
req.alt-api: ISCSI_Supported_LB_Policies
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

# ISCSI_Supported_LB_Policies structure



## -description
<p>The ISCSI_Supported_LB_Policies structure contains information about load balancing policies for multiple connections per session (MCS).</p>


## -syntax

````
typedef struct _ISCSI_Supported_LB_Policies {
  ULONGLONG  UniqueSessionId;
  ULONG      LoadBalancePolicy;
  ULONG      iSCSI_PathCount;
  ISCSI_Path iSCSI_Paths[1];
} ISCSI_Supported_LB_Policies, *PISCSI_Supported_LB_Policies;
````


## -struct-fields
<dl>

### -field UniqueSessionId

<dd>
<p>A 64-bit integer that uniquely identifies the session. The <a href="storage.logintotarget">LoginToTarget</a> and <a href="storage.addconnectiontosession">AddConnectionToSession</a> methods both return this value in their UniqueSessionId parameter. Do not confuse this value with the values in the ISID and TSID members.</p>
</dd>

### -field LoadBalancePolicy

<dd>
<p>This specifies the type of load balance policy that has been established on a multiconnection session.</p>
<table>
<tr>
<th>Type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>MSiSCSI_LB_FAILOVER</p>
</td>
<td>
<p>An alternate path  is used only for failover.</p>
</td>
</tr>
<tr>
<td>
<p>MSiSCSI_LB_ROUND_ROBIN</p>
</td>
<td>
<p>I/O operations are scheduled to all active paths in a round-robin fashion.</p>
</td>
</tr>
<tr>
<td>
<p>MSiSCSI_LB_ROUND_ROBIN_WITH_SUBSET</p>
</td>
<td>
<p>I/O operations are scheduled to all paths within a subset in a round-robin fashion.</p>
</td>
</tr>
<tr>
<td>
<p>MSiSCSI_LB_DYN_LEAST_QUEUE_DEPTH</p>
</td>
<td>
<p>I/O operations are balanced across a set of paths based on the least queue depth mechanism (I/O is scheduled to the path with the fewest pending I/Os in its queue).</p>
</td>
</tr>
<tr>
<td>
<p>MSiSCSI_LB_WEIGHTED_PATHS</p>
</td>
<td>
<p>I/O operations are scheduled based on the weights assigned to a path by an administrator.</p>
</td>
</tr>
<tr>
<td>
<p>MSiSCSI_LB_VENDOR_SPECIFIC</p>
</td>
<td>
<p>Vendor-specific I/O policies are in effect.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field iSCSI_PathCount

<dd>
<p>The number of paths associated with a target in the context of this session.</p>
</dd>

### -field iSCSI_Paths

<dd>
<p>Path information as shown in the <a href="..\iscsimgt\ns-iscsimgt--iscsi-path.md">ISCSI_Path</a> structure.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ISCSI_Supported_LB_Policies structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
