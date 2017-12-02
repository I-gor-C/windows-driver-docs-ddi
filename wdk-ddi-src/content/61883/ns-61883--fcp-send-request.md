---
UID: NS.61883._FCP_SEND_REQUEST
title: FCP_SEND_REQUEST
author: windows-driver-content
description: This structure is used for a send request.
old-location: ieee\fcp_send_request.htm
old-project: IEEE
ms.assetid: 82F36729-57E0-49AB-8C2D-BCBA6EED33EE
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: FCP_SEND_REQUEST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FCP_SEND_REQUEST
req.alt-loc: 61883.h
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
---

# FCP_SEND_REQUEST structure



## -description
<p>This structure is used for a send request. The  request sends an FCP request to the device. If the protocol driver is being used to represent a virtual device on the machine, the client driver must specify the <b>NodeAddress</b> member of FCP_SEND_REQUEST structure. This information is required in order to route the request to the proper node on the 1394 bus. If the protocol driver is being used to control a physical device, the 1394 bus driver determines the node address dynamically, and <b>NodeAddress</b> is not used.</p>


## -syntax

````
typedef struct _FCP_SEND_REQUEST {
  NODE_ADDRESS NodeAddress;
  ULONG        Length;
  PFCP_FRAME   Frame;
} FCP_SEND_REQUEST, *PFCP_SEND_REQUEST;
````


## -struct-fields
<dl>

### -field NodeAddress

<dd>
<p>On input, if the protocol driver is being used to control a virtual device, <b>NodeAddress</b> must contain the node address of the device to which this request is being sent so the protocol driver can route the request to the correct device. If the protocol driver is being used to control a physical device, <b>NodeAddress</b> is not used.</p>
</dd>

### -field Length

<dd>
<p>On input, the length of the Frame payload in bytes, including the FCP header.</p>
</dd>

### -field Frame

<dd>
<p>On input, a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff537113">FCP_FRAME</a> structure that contains the FCP request to send to the device.</p>
</dd>
</dl>

## -remarks
<p>If successful, the IEC-61883 protocol driver sets <b>Irp-&gt;IoStatus.Status </b>to STATUS_SUCCESS. </p>

<p>If an incorrect parameter is passed in, the protocol driver sets <b>Irp-&gt;IoStatus.Status </b>to STATUS_INVALID_PARAMETER.</p>

<p>If the protocol driver is unable to allocate resources, it sets <b>Irp-&gt;IoStatus.Status </b>to STATUS_INSUFFICIENT_RESOURCES.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20FCP_SEND_REQUEST structure%20 RELEASE:%20(11/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
