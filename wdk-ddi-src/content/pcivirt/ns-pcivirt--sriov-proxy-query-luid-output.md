---
UID: NS.pcivirt._SRIOV_PROXY_QUERY_LUID_OUTPUT
title: SRIOV_PROXY_QUERY_LUID_OUTPUT
author: windows-driver-content
description: Stores the local unique identifier of the SR_IOV device implementing the interface. This structure is the output buffer for the IOCTL_SRIOV_PROXY_QUERY_LUID request.
old-location: pci\sriov_proxy_query_luid_output.htm
old-project: PCI
ms.assetid: 8db09aa8-240d-40b6-a28c-77158aff6c39
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRIOV_PROXY_QUERY_LUID_OUTPUT, SRIOV_PROXY_QUERY_LUID_OUTPUT, *PSRIOV_PROXY_QUERY_LUID_OUTPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRIOV_PROXY_QUERY_LUID_OUTPUT
req.alt-loc: Pcivirt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# SRIOV_PROXY_QUERY_LUID_OUTPUT structure



## -description
<p>Stores the local unique
identifier of the SR_IOV device implementing the interface. This structure is the output buffer for the <a href="buses.ioctl_sriov_proxy_query_luid">IOCTL_SRIOV_PROXY_QUERY_LUID</a> request.</p>


## -syntax

````
typedef struct _SRIOV_PROXY_QUERY_LUID_OUTPUT {
  LUID  DeviceLuid;
} SRIOV_PROXY_QUERY_LUID_OUTPUT, SRIOV_PROXY_QUERY_LUID_OUTPUT;
````


## -struct-fields
<dl>

### -field DeviceLuid

<dd>
<p>Local unique
identifier of the SR_IOV device implementing the interface.</p>
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
<dt>Pcivirt.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.ioctl_sriov_proxy_query_luid">IOCTL_SRIOV_PROXY_QUERY_LUID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20SRIOV_PROXY_QUERY_LUID_OUTPUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
