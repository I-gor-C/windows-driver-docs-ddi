---
UID: NS.ndiswwan._NDIS_WWAN_AUTH_RESPONSE
title: NDIS_WWAN_AUTH_RESPONSE
author: windows-driver-content
description: The NDIS_WWAN_AUTH_RESPONSE structure represents a response from one of the authentication methods.
old-location: netvista\ndis_wwan_auth_response.htm
ms.assetid: 9F991E80-5155-45CE-9547-7354EE7EC4DB
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_AUTH_RESPONSE
req.alt-loc: ndiswwan.h
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
ms.keywords: NDIS_WWAN_AUTH_RESPONSE, NDIS_WWAN_AUTH_RESPONSE, *PNDIS_WWAN_AUTH_RESPONSE
req.iface: 
---

# NDIS_WWAN_AUTH_RESPONSE structure



## -description
<p>The NDIS_WWAN_AUTH_RESPONSE structure represents a response from one of the authentication methods.</p>


## -syntax

````
typedef struct _NDIS_WWAN_AUTH_RESPONSE {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_AUTH_RESPONSE AuthResponse;
} NDIS_WWAN_AUTH_RESPONSE, *PNDIS_WWAN_AUTH_RESPONSE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_AUTH_RESPONSE structure. The
     MB service sets the header with the values that are shown in the following table when it sends the data
     structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     </p>
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>NDIS_OBJECT_TYPE_DEFAULT</p>
</td>
</tr>
<tr>
<td>
<p>Revision</p>
</td>
<td>
<p>NDIS_WWAN_AUTH_RESPONSE_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_AUTH_RESPONSE)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of the response received for authentication challenge operation. The miniport driver returns one of the following WWAN_STATUS values as appropriate.</p>
<table>
<tr>
<th>WWAN_STATUS_VALUE</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_AUTH_INCORRECT_AUTN</p>
</td>
<td>
<p>If the transmitted challenge has an incorrect AUTN,  the response for the AKA and AKA' challenges will have this error code. This value applies only to the AKA and AKA' authentication methods. </p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_AUTH_SYNC_FAILURE</p>
</td>
<td>
<p> If the transmitted challenge has a synchronization failure, the response for the AKA and AKA' challenges will have this error code and will have AUTS. This value applies only to the AKA and AKA' authentication methods.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_AUTH_AMF_NOT_SET</p>
</td>
<td>
<p> If the transmitted challenge is not computed with the AMF separation bit set to 1, the response for AKA' should have this error code. This value applies only to the AKA' authentication method.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>AuthResponse</b>

<dd>
<p>A formatted <a href="https://msdn.microsoft.com/library/windows/hardware/hh464129">WWAN_AUTH_RESPONSE</a> object that represents the challenge posed by one of the authentication methods. This member (within WWAN_AUTH_RESPONSE) should be set even when <b>uStatus</b> is other than WWAN_STATUS_SUCCESS.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh439821">NDIS_STATUS_WWAN_AUTH_RESPONSE</a> NDIS status notification uses this structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464129">WWAN_AUTH_RESPONSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439821">NDIS_STATUS_WWAN_AUTH_RESPONSE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_AUTH_RESPONSE structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
