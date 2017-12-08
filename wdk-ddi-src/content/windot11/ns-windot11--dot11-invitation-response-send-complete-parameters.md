---
UID: NS.windot11._DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS
title: DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS
author: windows-driver-content
description: The parameters for an invitation response send completion are specified in a DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS structure. This structure is sent with an NDIS_STATUS_DOT11_WFD_INVITATION_RESPONSE_SEND_COMPLETE indication.
old-location: netvista\dot11_invitation_response_send_complete_parameters.htm
old-project: netvista
ms.assetid: EE537A6E-6722-4829-986A-37D41B149E37
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS
req.alt-loc: Windot11.h
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
req.product: Windows 10 or later.
---

# DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS structure



## -description

## -syntax

````
typedef struct _DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS {
  NDIS_OBJECT_HEADER  Header;
  DOT11_MAC_ADDRESS   ReceiverDeviceAddress;
  DOT11_DIALOG_TOKEN  DialogToken;
  NDIS_STATUS         Status;
  ULONG               uIEsOffset;
  ULONG               uIEsLength;
} DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS, *PDOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the <b>DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS</b> structure. The required settings for the members of <b>Header</b> are the following.</p>
<table>
<tr>
<th>Member</th>
<th>Setting</th>
</tr>
<tr>
<td><b>Type</b></td>
<td>NDIS_OBJECT_TYPE_DEFAULT</td>
</tr>
<tr>
<td><b>Revision</b></td>
<td>DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS_REVISION_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field ReceiverDeviceAddress

<dd>
<p>The address of the device that the invitation response was sent to. This must match the <b>ReceiverDeviceAddress</b> member of <a href="..\windot11\ns-windot11--dot11-send-invitation-response-parameters.md">DOT11_SEND_INVITATION_RESPONSE_PARAMETERS</a> sent with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451807">OID_DOT11_WFD_SEND_INVITATION_RESPONSE</a> request.</p>
</dd>

### -field DialogToken

<dd>
<p>The dialog token from the invitation response packet. This must match the dialog token sent with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451807">OID_DOT11_WFD_SEND_INVITATION_RESPONSE</a> request.</p>
</dd>

### -field Status

<dd>
<p>The status of the response send attempt. Set to <b>NDIS_STATUS_SUCCESS</b> if the packet was successfully transmitted.</p>
</dd>

### -field uIEsOffset

<dd>
<p>The offset, in bytes,  of the array of additional information elements (IEs) that were included in the invitation response packet. This offset is from the start of the buffer that contains this structure.</p>
</dd>

### -field uIEsLength

<dd>
<p>The length, in bytes, of the array of IEs provided at <b>uIEsOffset</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with   Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\windot11\ns-windot11--dot11-invitation-response-send-complete-parameters.md">DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439781">NDIS_STATUS_DOT11_WFD_INVITATION_RESPONSE_SEND_COMPLETE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451807">OID_DOT11_WFD_SEND_INVITATION_RESPONSE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_INVITATION_RESPONSE_SEND_COMPLETE_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
