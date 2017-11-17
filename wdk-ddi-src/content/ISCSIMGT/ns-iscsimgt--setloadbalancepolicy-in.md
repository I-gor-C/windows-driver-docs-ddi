---
UID: NS.iscsimgt._SetLoadBalancePolicy_IN
title: SetLoadBalancePolicy_IN
author: windows-driver-content
description: The SetLoadBalancePolicy_IN structure holds the input data for the SetLoadBalance method.
old-location: storage\setloadbalancepolicy_in.htm
ms.assetid: e1895fed-a006-45f6-a38a-1767202cbf4f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsimgt.h
req.include-header: Iscsimgt.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetLoadBalancePolicy_IN
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
ms.keywords: SetLoadBalancePolicy_IN, SetLoadBalancePolicy_IN, *PSetLoadBalancePolicy_IN
req.iface: 
---

# SetLoadBalancePolicy_IN structure



## -description
<p>The SetLoadBalancePolicy_IN structure holds the input data for the SetLoadBalance method.</p>


## -syntax

````
typedef struct _SetLoadBalancePolicy_IN {
  ISCSI_Supported_LB_Policies LoadBalancePolicies;
} SetLoadBalancePolicy_IN, *PSetLoadBalancePolicy_IN;
````


## -struct-fields
<dl>

### -field <b>LoadBalancePolicies</b>

<dd>
<p>A structure that contains the information that is required for setting the load balance policy.</p>
</dd>
</dl>

## -remarks
<p>You must implement this class.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563062">MSiSCSI_LB_Operations WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20SetLoadBalancePolicy_IN structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
